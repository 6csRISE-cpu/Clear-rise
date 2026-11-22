// Generate the social share image (site/assets/og.png). With --shots, also screenshot pages for QA.
import { createRequire } from 'module'; import { fileURLToPath, pathToFileURL } from 'url'; import { join, dirname } from 'path';
const require = createRequire(import.meta.url); const { chromium } = require('playwright');
const site = join(dirname(fileURLToPath(import.meta.url)), '..', 'site');
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
await p.setContent(`<html><body style="margin:0;font-family:Inter;background:#111;color:#fff;width:1200px;height:630px;display:flex;flex-direction:column;justify-content:space-between;padding:64px 76px;box-sizing:border-box;position:relative;overflow:hidden"><div style="position:absolute;right:-60px;bottom:-90px;opacity:.95;transform:rotate(-10deg)"><svg width="460" height="460" viewBox="0 0 24 24"><path d="M12 2C7.6 2 4 5.6 4 10v11.2c0 .7.8 1 1.3.5l1.9-1.9 1.9 1.9c.4.4 1 .4 1.4 0L12 20l1.5 1.7c.4.4 1 .4 1.4 0l1.9-1.9 1.9 1.9c.5.5 1.3.2 1.3-.5V10c0-4.4-3.6-8-8-8z" fill="#D7FF3A"/><circle cx="9.2" cy="10" r="1.7" fill="#111"/><circle cx="14.8" cy="10" r="1.7" fill="#111"/></svg></div><div style="display:flex;align-items:center;gap:10px;font-weight:900;letter-spacing:-.03em;font-size:40px"><svg width="46" height="46" viewBox="0 0 24 24"><path d="M12 2C7.6 2 4 5.6 4 10v11.2c0 .7.8 1 1.3.5l1.9-1.9 1.9 1.9c.4.4 1 .4 1.4 0L12 20l1.5 1.7c.4.4 1 .4 1.4 0l1.9-1.9 1.9 1.9c.5.5 1.3.2 1.3-.5V10c0-4.4-3.6-8-8-8z" fill="#fff"/><circle cx="9.2" cy="10" r="1.7" fill="#D7FF3A"/><circle cx="14.8" cy="10" r="1.7" fill="#D7FF3A"/></svg>unghosted</div><div style="position:relative"><div style="font-size:84px;font-weight:900;line-height:.98;letter-spacing:-.04em;max-width:820px">Your customers are ghosting you.</div><div style="display:inline-block;margin-top:18px;background:#D7FF3A;color:#111;font-size:52px;font-weight:900;letter-spacing:-.03em;padding:2px 14px">Let&#39;s unf*ck that.</div></div><div style="font-family:JetBrains Mono,monospace;font-size:22px;color:#D7FF3A;font-weight:700">missed calls · dead quotes · no-shows → booked jobs</div></body></html>`);
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
