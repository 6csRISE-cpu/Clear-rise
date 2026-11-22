// Generate the social share image (site/assets/og.png). With --shots, also screenshot pages for QA.
import { createRequire } from 'module'; import { fileURLToPath, pathToFileURL } from 'url'; import { join, dirname } from 'path';
const require = createRequire(import.meta.url); const { chromium } = require('playwright');
const site = join(dirname(fileURLToPath(import.meta.url)), '..', 'site');
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
await p.setContent(`<html><body style="margin:0;font-family:Inter;background:linear-gradient(150deg,#0F2A3D,#173E57 65%,#1F6F80);color:#fff;width:1200px;height:630px;display:flex;flex-direction:column;justify-content:space-between;padding:70px 80px;box-sizing:border-box">
<div style="display:flex;align-items:center;gap:14px;font-weight:800;letter-spacing:.16em;font-size:26px"><span style="width:30px;height:30px;border-radius:50%;background:#E8962E;box-shadow:0 0 0 8px rgba(232,150,46,.25)"></span>CLEARRISE</div>
<div><div style="font-size:76px;font-weight:800;line-height:1.02;letter-spacing:-.02em">Win back the jobs<br>you're already losing.</div>
<div style="font-size:30px;color:#C9D6DF;margin-top:22px">Missed-call, quote follow-up, rebooking & review templates for home-service businesses</div></div>
<div style="font-size:24px;color:#E8962E;font-weight:700">clearrisetools.com</div></body></html>`);
await p.screenshot({ path: join(site, 'assets', 'og.png') });
const out = process.argv[3];
if (process.argv[2] === '--shots') {
  for (const [name, path, w] of [['home-desktop','index.html',1280],['home-mobile','index.html',390],['article-mobile','guides/missed-call-text-back-templates.html',390]]) {
    const q = await b.newPage({ viewport: { width: w, height: 900 } });
    await q.goto(pathToFileURL(join(site, path)).href); await q.waitForTimeout(300);
    const sw = await q.evaluate(() => document.documentElement.scrollWidth);
    console.log(name, 'scrollWidth', sw, 'viewport', w);
    await q.screenshot({ path: join(out, name + '.png'), fullPage: true });
  }
}
await b.close();
