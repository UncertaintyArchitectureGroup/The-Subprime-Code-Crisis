// Adapted transport boundary: Quartz HTML -> isolated Chromium -> new PDF.
// No source overwrite, external network, deployment or evidence-state mutation.
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, realpath, lstat, rename, unlink } from 'node:fs/promises';
import path from 'node:path';
import { randomUUID } from 'node:crypto';

const [siteArg, slug, outputArg] = process.argv.slice(2);
if (!siteArg || !outputArg || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug ?? '')) {
  throw new Error('Usage: export-pdf.mjs <site> <slug> <output.pdf>');
}
const site = await realpath(siteArg);
const output = path.resolve(outputArg);
if (!output.endsWith('.pdf')) throw new Error('Output must end in .pdf');
const parent = await realpath(path.dirname(output));
if (parent !== path.dirname(output)) throw new Error('Output parent must not be a symlink');
try {
  const info = await lstat(output);
  if (!info.isFile() || info.isSymbolicLink() || info.nlink > 1) {
    throw new Error('Output must not be a symlink, hard link or special file');
  }
} catch (error) {
  if (error.code !== 'ENOENT') throw error;
}
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2', '.json': 'application/json' };
const server = createServer(async (request, response) => {
  try {
    const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
    let candidate = path.resolve(site, '.' + pathname);
    if (pathname === '/') candidate = path.join(site, 'index.html');
    const actual = await realpath(candidate);
    if (!actual.startsWith(site + path.sep)) throw new Error('Outside site');
    response.setHeader('Content-Type', types[path.extname(actual)] ?? 'application/octet-stream');
    response.end(await readFile(actual));
  } catch {
    response.writeHead(404).end();
  }
});
await new Promise((resolve, reject) => {
  server.once('error', reject);
  server.listen(0, '127.0.0.1', resolve);
});
const origin = `http://127.0.0.1:${server.address().port}`;
const temporary = output + '.' + randomUUID() + '.tmp';
let browser;
try {
  browser = await chromium.launch();
  const page = await browser.newPage();
  await page.route('**/*', route => {
    const url = route.request().url();
    return url.startsWith(origin + '/') || url.startsWith('data:')
      ? route.continue() : route.abort();
  });
  const response = await page.goto(`${origin}/${slug}.html`, { waitUntil: 'networkidle' });
  if (!response?.ok()) throw new Error('Quartz article page did not load');
  await page.waitForSelector('article');
  await page.evaluate(async () => {
    await document.fonts.ready;
    const article = document.querySelector('article');
    if (!article?.innerText.trim()) throw new Error('Empty article');
    const copy = article.cloneNode(true);
    document.body.replaceChildren(copy);
    document.body.className = 'publication';
    document.documentElement.setAttribute('saved-theme', 'light');
    // Quartz's upstream theme includes UA-specific print margin boxes. Use a
    // self-contained PDF stylesheet so branding and pagination cannot leak.
    for (const stylesheet of document.querySelectorAll('link[rel="stylesheet"], style')) {
      stylesheet.remove();
    }
    for (const link of document.querySelectorAll('a[href]')) {
      // Keep internal heading links meaningful in the PDF.
      if (link.getAttribute('href').startsWith('#')) continue;
      if (link.href.startsWith(location.origin)) link.removeAttribute('href');
    }
  });
  await page.addStyleTag({ content: `
    @page { size: A4; margin: 20mm 18mm 22mm; }
    html, body.publication { background: white !important; color: #111 !important; }
    body.publication { margin: 0 !important; padding: 0 !important; width: auto !important; }
    article { width: auto !important; max-width: none !important; margin: 0 !important;
      font: 11pt/1.5 Arial, sans-serif; color: #111 !important; }
    h1 { font-size: 25pt; line-height: 1.15; } h2 { font-size: 16pt; } h3 { font-size: 12pt; }
    h1, h2, h3 { break-after: avoid; color: #111 !important; }
    h1 { margin: 0 0 14pt; } h2, h3 { margin: 18pt 0 8pt; }
    p { margin: 0 0 10pt; } li { margin: 0 0 5pt; }
    blockquote { margin: 12pt 0; padding: 0 0 0 10pt; border-left: 2pt solid #444; }
    code { font-family: monospace; } table { border-collapse: collapse; }
    td, th { padding: 5pt; border: 0.5pt solid #888; text-align: left; }
    a { color: #111; }
    p, li { orphans: 3; widows: 3; } pre, blockquote, tr { break-inside: avoid; }
    pre { white-space: pre-wrap; overflow-wrap: anywhere; font-size: 9pt; }
    table { width: 100%; table-layout: fixed; font-size: 9pt; }
    td, th { overflow-wrap: anywhere; } a { overflow-wrap: anywhere; }
    .anchor, .clipboard-button { display: none !important; }
  ` });
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: temporary, format: 'A4', printBackground: true,
    preferCSSPageSize: true, displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font:9px Arial;width:100%;text-align:center">The Subprime Code Crisis · <span class="pageNumber"></span> / <span class="totalPages"></span></div>' });
  const bytes = await readFile(temporary);
  if (bytes.length < 1024 || bytes.subarray(0, 5).toString() !== '%PDF-'
      || !bytes.subarray(-2048).includes(Buffer.from('%%EOF'))) throw new Error('Incomplete PDF');
  await rename(temporary, output);
  console.log(output);
} finally {
  await browser?.close();
  await new Promise(resolve => server.close(resolve));
  await unlink(temporary).catch(error => { if (error.code !== 'ENOENT') throw error; });
}
