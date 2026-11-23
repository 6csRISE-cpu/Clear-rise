// Render products/dist/html/*.html to products/dist/pdf/*.pdf with the preinstalled Chromium.
import { createRequire } from 'module';
import { readdirSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath, pathToFileURL } from 'url';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const dist = join(dirname(fileURLToPath(import.meta.url)), '..', 'products', 'dist');
mkdirSync(join(dist, 'pdf'), { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage();
for (const f of readdirSync(join(dist, 'html')).filter(f => f.endsWith('.html'))) {
  await page.goto(pathToFileURL(join(dist, 'html', f)).href, { waitUntil: 'load' });
  await page.pdf({
    path: join(dist, 'pdf', f.replace('.html', '.pdf')),
    format: 'Letter', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-family:Inter,sans-serif;font-size:7.5pt;color:#7A8B96;width:100%;padding:0 0.8in;display:flex;justify-content:space-between"><span>Unghosted · unghostedhq.netlify.app</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: '0.7in', bottom: '0.75in', left: '0.8in', right: '0.8in' },
  });
  console.log('pdf', f);
}
await browser.close();
