// Real AST regression cases run only after the pinned engine is installed.
import fs from "node:fs"
import os from "node:os"
import path from "node:path"
import { execFileSync } from "node:child_process"
import assert from "node:assert/strict"

const manifest = JSON.parse(fs.readFileSync(new URL("./publication.json", import.meta.url)))
const engine = process.env.SUBPRIME_QUARTZ_ENGINE || path.join(os.homedir(), ".cache/subprime-quartz", manifest.engine.commit)
const script = path.join(engine, "prepare.mjs")
assert.equal(fs.readFileSync(script, "utf8"), fs.readFileSync(new URL("./prepare.mjs", import.meta.url), "utf8"), "AST checks require the current installed adapter")
const cases = [
  { name: "unlisted reference image", body: "# A\n\n![image][img]\n\n[img]: assets/picture.png\n", error: /Unlisted asset/ },
  { name: "unlisted inline image", body: "# A\n\n![image](assets/picture.png)\n", error: /Unlisted asset/ },
  { name: "listed reference image", body: "# A\n\n![image][img]\n\n[img]: assets/picture.png\n", listed: true, expected: /\[img\]: \/subprime\/media\/[a-f0-9]{64}\.png/ },
  { name: "active HTML", body: "# A\n\n<script>alert(1)</script>\n", error: /Unsupported active HTML/ },
  { name: "missing local heading", body: "# A\n\n[Jump](#missing)\n", error: /Missing source anchor/ },
  { name: "code and diagram preservation", body: '# A\n\n```md\n![image](assets/picture.png)\n```\n\n```mermaid\nA[Label<br/>detail] --> B\n```\n', expected: /```mermaid\nA\[Label<br\/>detail\] --> B\n```/ },
]
for (const test of cases) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "subprime-projection-test-"))
  try {
    fs.mkdirSync(path.join(root, "assets"))
    fs.mkdirSync(path.join(root, "content"))
    fs.writeFileSync(path.join(root, "assets/picture.png"), Buffer.from("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aRuoAAAAASUVORK5CYII=", "base64"))
    const original = path.join(root, "README.md")
    fs.writeFileSync(original, test.body)
    const request = path.join(root, "request.json")
    fs.writeFileSync(request, JSON.stringify({ root, repository: manifest.repository, source_commit: "1".repeat(40), canonical_base: manifest.canonical_base, mount: manifest.mount, mode: "preview", assets: test.listed ? ["assets/picture.png"] : [], pages: [{ source: "README.md", slug: "index", group: "Start", body: test.body, metadata: {}, modified: null }] }))
    let error
    try { execFileSync(process.execPath, [script, request, path.join(root, "content")], { encoding: "utf8", stdio: "pipe" }) } catch (caught) { error = caught }
    if (test.error) {
      assert.ok(error, `${test.name} must fail`)
      assert.match(error.stderr, test.error)
    } else {
      if (error) throw error
      assert.match(fs.readFileSync(path.join(root, "content/index.md"), "utf8"), test.expected)
    }
    assert.equal(fs.readFileSync(original, "utf8"), test.body, "canonical source mutated")
    console.log(`PASS ${test.name}`)
  } finally { fs.rmSync(root, { recursive: true, force: true }) }
}
