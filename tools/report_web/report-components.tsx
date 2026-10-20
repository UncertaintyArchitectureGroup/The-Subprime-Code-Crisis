import { QuartzComponent } from "./quartz/components/types"
import { CSSResourceToStyleElement, JSResourceToScriptElement } from "./quartz/util/resources"

export const ReportHead: QuartzComponent = ({ fileData, externalResources }) => (
  <head>
    <meta charSet="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{fileData.frontmatter?.title} · Subprime</title>
    <meta name="description" content="An independent research synthesis on AI-assisted software delivery risk." />
    <meta name="robots" content={fileData.frontmatter?.preview ? "noindex, nofollow" : "index, follow"} />
    <link rel="canonical" href={String(fileData.frontmatter?.canonical_url)} />
    {externalResources.css.map(r => CSSResourceToStyleElement(r, true))}
    {externalResources.js.filter(r => r.loadTime === "beforeDOMReady").map(r => JSResourceToScriptElement(r, true))}
    {externalResources.additionalHead.map(r => typeof r === "function" ? r(fileData) : r)}
  </head>
)

export const ReportHeader: QuartzComponent = () => (
  <>
    <a class="skip-link" href="#report-content">Skip to content</a>
    <nav class="report-header" aria-label="Publication">
      <a href="/subprime/" class="report-brand">Subprime Code Crisis</a>
      <a href="https://vitaliioborskyi.ai/">Vitalii Oborskyi ↗</a>
      <button type="button" id="subprime-theme" hidden>Change theme</button>
    </nav>
  </>
)

export const ReportContents: QuartzComponent = ({ allFiles, fileData }) => (
  <details class="report-contents-panel"><summary>Contents & search</summary>
  <nav class="report-contents" id="report-navigation" aria-label="Report contents">
    <a href="/subprime/" class="contents-label">READ THE REPORT</a>
    <ul>{allFiles.filter(f => f.frontmatter?.group === "Report").sort((a, b) => Number(a.frontmatter?.order) - Number(b.frontmatter?.order)).map(f => (
      <li><a href={String(f.frontmatter?.route)} aria-current={f.slug === fileData.slug ? "page" : undefined}>{f.frontmatter?.title}</a>
        {f.toc?.filter(t => t.text.startsWith("Chapter ")).map(t => <a class="chapter-link" href={`${f.frontmatter?.route}#${t.slug}`}>{t.text}</a>)}
      </li>
    ))}</ul>
    <ul class="support-links">
      <li><a href="/subprime/evidence/">Evidence library</a></li>
      <li><a href="/subprime/evidence/sources">Source registry</a></li>
      <li><a href="/subprime/protocols/">Operational protocols</a></li>
      <li><a href="/subprime/scope">Scope & boundaries</a></li>
      <li><a href="/subprime/references">References</a></li>
    </ul>
    <details class="report-search"><summary>Search this edition</summary>
      <form role="search"><label for="subprime-query">Words or source ID</label><input id="subprime-query" type="search" /><button type="submit">Search</button></form>
      <p id="subprime-search-status" role="status"></p><ul id="subprime-search-results"></ul>
      <noscript>Search needs JavaScript. Use the contents or your browser's Find command.</noscript>
    </details>
    {!!fileData.toc?.length && <details class="page-contents" open><summary>On this page</summary><ul>{fileData.toc.filter(t => t.depth > 0).map(t => <li><a href={`#${t.slug}`}>{t.text}</a></li>)}</ul></details>}
  </nav>
  </details>
)

export const ReportMeta: QuartzComponent = ({ fileData }) => {
  const f = fileData.frontmatter!
  return <section class="report-meta" id="report-content" tabIndex={-1} aria-label="Source edition">
    {f.preview && <p class="preview-label">REVIEW PREVIEW · not a published edition</p>}
    <p>Living research synthesis · <a href={String(f.source_url)}>Canonical source</a> · source <code>{String(f.source_commit).slice(0, 8)}</code></p>
    <details><summary>Source and review context</summary>
      <p>Source modified: {String(f.source_modified || "unknown (history unavailable)")}. Publication date: not assigned.</p>
      {f.evidence_review && <dl>
        <dt>Source IDs</dt><dd>{(f.source_ids as string[]).join(", ")}</dd>
        <dt>Evidence review</dt><dd>{String(f.evidence_review)}</dd>
        <dt>Integration audit</dt><dd>{String(f.integration_audit)}</dd>
        <dt>Last verified</dt><dd>{String(f.last_verified)}</dd>
      </dl>}
      <p>Rendering does not verify the research. See the <a href="/subprime/evidence/sources">canonical source states</a> and limitations in the source text.</p>
    </details>
  </section>
}

export const ReportFooter: QuartzComponent = ({ fileData, allFiles }) => {
  const parts = allFiles.filter(f => f.frontmatter?.group === "Report").sort((a, b) => Number(a.frontmatter?.order) - Number(b.frontmatter?.order))
  const index = parts.findIndex(f => f.slug === fileData.slug)
  return <footer class="report-footer">
    {index >= 0 && <nav aria-label="Report sequence">{index > 0 && <a href={String(parts[index - 1].frontmatter?.route)}>← Previous part</a>}{index < parts.length - 1 ? <a href={String(parts[index + 1].frontmatter?.route)}>Next part →</a> : <a href="/subprime/protocols/">Operational protocols →</a>}</nav>}
    <p>Vitalii Oborskyi & contributors · <a href="/subprime/license">CC BY-SA 4.0</a>. Attributed third-party material retains its own rights. <a href="/subprime/notices/README.txt">Runtime notices</a>.</p>
    <p><a href={String(fileData.frontmatter?.source_url)}>Source & history</a> · <a href="https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues">Corrections & discussion</a> · <a href="https://vitaliioborskyi.ai/">Author website</a></p>
  </footer>
}

ReportHeader.beforeDOMLoaded = `try {const t=localStorage.getItem('subprime.theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('saved-theme',t)}catch{}`
ReportContents.afterDOMLoaded = `
document.querySelector('.report-contents-panel').open=matchMedia('(min-width: 1001px)').matches;
const button=document.getElementById('subprime-theme');
button.hidden=false;
button.addEventListener('click',()=>{const root=document.documentElement;const current=root.getAttribute('saved-theme')|| (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');const next=current==='dark'?'light':'dark';root.setAttribute('saved-theme',next);try{localStorage.setItem('subprime.theme',next)}catch{};button.textContent=next==='dark'?'Light theme':'Dark theme'});
document.querySelector('.report-search form').addEventListener('submit',async event=>{event.preventDefault();const q=document.getElementById('subprime-query').value.trim().toLowerCase();const list=document.getElementById('subprime-search-results');list.replaceChildren();const status=document.getElementById('subprime-search-status');if(!q){status.textContent='Enter a word or source ID.';return}try{const data=await fetchData;let count=0;for(const [slug,page] of Object.entries(data)){if((page.title+' '+page.content).toLowerCase().includes(q)){const li=document.createElement('li');const a=document.createElement('a');a.textContent=page.title;a.href='/subprime/'+(slug==='index'?'':slug.endsWith('/index')?slug.slice(0,-5):slug);li.append(a);list.append(li);if(++count===12)break}}status.textContent=count?count+' matching pages':'No matching pages.'}catch{status.textContent='Search is unavailable. Use the contents or reload this edition.'}});
`
