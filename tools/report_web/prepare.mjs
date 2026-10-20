// AST-position edits preserve canonical prose, code and diagram source bytes.
import fs from "node:fs"
import path from "node:path"
import crypto from "node:crypto"
import { unified } from "unified"
import remarkParse from "remark-parse"
import remarkGfm from "remark-gfm"
import { visit } from "unist-util-visit"
import { toString } from "mdast-util-to-string"
import Slugger from "github-slugger"

const [input, destination] = process.argv.slice(2)
const data = JSON.parse(fs.readFileSync(input, "utf8"))
const parser = unified().use(remarkParse).use(remarkGfm)
const sources = new Map(data.pages.map(p => [p.source, p]))
const assets = new Set(data.assets)
const sourceBase = `https://github.com/${data.repository}/blob/${data.source_commit}/`
const edits = []
const graph = []
const hash = bytes => crypto.createHash("sha256").update(bytes).digest("hex")
const route = slug => data.mount + (slug === "index" ? "" : slug.endsWith("/index") ? slug.slice(0, -5) : slug)
const safe = relative => {
  if (relative.startsWith("/") || relative.split("/").some(p => p === ".." || !p)) throw new Error(`Unsafe source: ${relative}`)
  let current = data.root
  for (const part of relative.split("/")) {
    current = path.join(current, part)
    if (fs.lstatSync(current).isSymbolicLink()) throw new Error(`Symlink source: ${relative}`)
  }
  return current
}

for (const page of data.pages) {
  const tree = parser.parse(page.body)
  const slugger = new Slugger()
  page.headings = []
  visit(tree, "heading", node => {
    const text = toString(node)
    page.headings.push({ id: slugger.slug(text), depth: node.depth, text })
  })
  page.title = page.headings.find(h => h.depth === 1)?.text || path.basename(page.source)
}

for (const page of data.pages) {
  const tree = parser.parse(page.body)
  const replacements = []
  const referencedImages = new Set()
  visit(tree, "imageReference", node => referencedImages.add(node.identifier.toLowerCase()))
  visit(tree, node => {
    if (node.type === "html" && !/^<!--(?:[^-]|-(?!->))*-->$/s.test(node.value.trim())) {
      // Reviewed text markup only. Code-fenced Mermaid is not raw HTML.
      if (/<\s*\/?\s*(?!br\b|b\b|strong\b|em\b|sub\b|sup\b|span\b|details\b|summary\b)[a-z]/i.test(node.value)
          || /\bon\w+\s*=|javascript:|\bstyle\s*=/i.test(node.value)) throw new Error(`Unsupported active HTML in ${page.source}`)
    }
    if (node.type === "code" && node.lang === "mermaid" && /^\s*(click\s|%%\{)/m.test(node.value)) throw new Error(`Active Mermaid directives need review: ${page.source}`)
    if (!["link", "image", "definition"].includes(node.type)) return
    const original = node.url
    const isImage = node.type === "image" || (node.type === "definition" && referencedImages.has(node.identifier.toLowerCase()))
    if (/^(https?:|mailto:|tel:)/i.test(original)) {
      if (isImage) throw new Error(`External images need an explicit asset contract: ${original}`)
      return
    }
    if (/^[a-z][a-z\d+.-]*:|^\/\//i.test(original)) throw new Error(`Unsupported URL scheme: ${original}`)
    const parsed = new URL(original, "https://source.invalid/" + page.source)
    if (parsed.search) throw new Error(`Local query needs an explicit mapping: ${original}`)
    let target = decodeURIComponent(parsed.pathname).replace(/^\//, "")
    const fragment = decodeURIComponent(parsed.hash.slice(1))
    if (target.includes("\\") || /%[0-9a-f]{2}/i.test(target)) throw new Error(`Ambiguous source URL: ${original}`)
    const included = sources.get(target)
    let rewritten
    let kind
    if (included && !isImage) {
      if (fragment && !included.headings.some(h => h.id === fragment)) throw new Error(`Missing source anchor: ${page.source} -> ${target}#${fragment}`)
      rewritten = route(included.slug) + parsed.hash
      kind = "page"
    } else if (assets.has(target)) {
      const bytes = fs.readFileSync(safe(target))
      const output = `media/${hash(bytes)}${path.extname(target).toLowerCase()}`
      fs.mkdirSync(path.join(destination, "media"), { recursive: true })
      fs.writeFileSync(path.join(destination, output), bytes)
      rewritten = data.mount + output
      kind = "asset"
    } else {
      safe(target) // Missing relative references are errors, never invented fallback URLs.
      if (isImage || !fs.statSync(safe(target)).isFile()) throw new Error(`Unlisted asset or directory: ${target}`)
      rewritten = sourceBase + target.split("/").map(encodeURIComponent).join("/") + parsed.hash
      kind = "source-fallback"
    }
    const raw = page.body.slice(node.position.start.offset, node.position.end.offset)
    const offset = node.type === "definition" ? raw.indexOf(":") + 1 : raw.lastIndexOf("](") + 2
    const before = raw.slice(0, offset)
    const after = raw.slice(offset)
    const at = after.indexOf(original)
    if (at < 0) throw new Error(`Unsupported URL spelling in ${page.source}: ${original}`)
    replacements.push({ start: node.position.start.offset + offset + at, end: node.position.start.offset + offset + at + original.length, text: rewritten })
    graph.push({ source: page.source, target, fragment, kind, url: rewritten })
  })
  let body = page.body
  for (const edit of replacements.sort((a, b) => b.start - a.start)) body = body.slice(0, edit.start) + edit.text + body.slice(edit.end)
  const metadata = { ...page.metadata, title: page.title, group: page.group, order: data.pages.indexOf(page), route: route(page.slug),
    canonical_url: data.canonical_base + route(page.slug).slice(data.mount.length),
    preview: data.mode === "preview", source_url: sourceBase + page.source,
    source_commit: data.source_commit, source_modified: page.modified }
  const header = "---\n" + Object.entries(metadata).map(([k, v]) => `${k}: ${JSON.stringify(v)}\n`).join("") + "---\n\n"
  const output = path.join(destination, page.slug + ".md")
  fs.mkdirSync(path.dirname(output), { recursive: true })
  fs.writeFileSync(output, header + body)
  edits.push({ ...page, body: undefined, headings: page.headings, title: page.title, route: route(page.slug) })
}
fs.writeFileSync(input, JSON.stringify({ ...data, pages: edits, links: graph }, null, 2) + "\n")
