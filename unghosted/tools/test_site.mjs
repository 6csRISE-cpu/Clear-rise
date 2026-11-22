// Automated site checks (no network needed): every page loads without JS errors, internal links resolve,
// no horizontal scroll on a phone, buy buttons are disabled with empty config and wire up correctly when
// links are filled in, calculator math is right, support-email fallback points at the support form.
// Usage: node tools/test_site.mjs  → exits 1 on any failure; writes results to ops/qa/site-results.json
import { createRequire } from 'module'; import { fileURLToPath, pathToFileURL } from 'url';
import { join, dirname, relative } from 'path'; import { readdirSync, statSync, existsSync, mkdirSync, writeFileSync, readFileSync } from 'fs';
const require = createRequire(import.meta.url); const { chromium } = require('playwright');
const root = join(dirname(fileURLToPath(import.meta.url)), '..'); const site = join(root, 'site');
const pages = []; (function walk(d) { for (const f of readdirSync(d)) { const p = join(d, f); if (statSync(p).isDirectory()) walk(p); else if (f.endsWith('.html')) pages.push(p); } })(site);
const results = []; const ok = (name, pass, detail = '') => { results.push({ name, pass, detail }); if (!pass) console.log('FAIL', name, detail); };

const b = await chromium.launch();
// Block all external requests (fonts, analytics) so tests are deterministic offline.
const ctx = await b.newContext(); await ctx.route(/^https?:\/\//, r => r.abort());
for (const p of pages) {
  const rel = relative(site, p); const pg = await ctx.newPage(); const errs = [];
  pg.on('pageerror', e => errs.push(String(e)));
  await pg.setViewportSize({ width: 390, height: 844 });
  await pg.goto(pathToFileURL(p).href);
  ok(`${rel}: no JS errors`, errs.length === 0, errs.join(' | '));
  const sw = await pg.evaluate(() => document.documentElement.scrollWidth);
  ok(`${rel}: no horizontal scroll at 390px`, sw <= 390, `scrollWidth=${sw}`);
  const hrefs = await pg.evaluate(() => [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')));
  for (const h of hrefs) {
    if (/^(https?:|mailto:|#)/.test(h) || h === '/') continue;
    let t = join(dirname(p), h.split('#')[0]); if (h.endsWith('/')) t = join(t, 'index.html');
    ok(`${rel}: link ${h}`, existsSync(t));
  }
  const title = await pg.title(); ok(`${rel}: has title`, title.length > 5, title);
  ok(`${rel}: no old brand`, !/clearrise/i.test(await pg.content()));
  await pg.close();
}

// Buy buttons: disabled when config links are empty
const home = pathToFileURL(join(site, 'index.html')).href;
let pg = await ctx.newPage(); await pg.goto(home);
const disabled = await pg.evaluate(() => [...document.querySelectorAll('[data-link]')].filter(a => ['starter','system','pro','club','free'].includes(a.dataset.link)).map(a => ({ l: a.dataset.link, href: a.getAttribute('href'), dis: a.getAttribute('aria-disabled') })));
ok('buy buttons disabled while links are empty', disabled.length >= 5 && disabled.every(x => x.dis === 'true' && x.href === null), JSON.stringify(disabled));
// Calculator: recompute from the page's own slider values and compare with what it displays
const calc = await pg.evaluate(() => {
  const v = id => +document.getElementById(id).value;
  return { calls: v('calls'), missed: v('missed'), book: v('book'), job: v('job'), quotes: v('quotes'), quote: v('quote'),
           risk: document.getElementById('r-risk').textContent, rec2: document.getElementById('r-rec2').textContent };
});
const money = n => '$' + Math.round(n).toLocaleString('en-US');
const exp = calc.calls * 4.33 * calc.missed / 100 * calc.book / 100 * calc.job;
ok('calculator: revenue at risk', calc.risk === money(exp), `${calc.risk} vs ${money(exp)}`);
ok('calculator: quote follow-up recovery', calc.rec2 === money(calc.quotes * 0.05 * calc.quote), calc.rec2);
await pg.close();

// Buy buttons: wired when config links are filled (simulate a filled config)
const cfg = readFileSync(join(site, 'config.js'), 'utf8').replace(/(free|starter|system|pro|club):\s*"",/g, (m, k) => `${k}: "https://payhip.com/b/TEST-${k}",`);
pg = await ctx.newPage(); await pg.route('**/config.js', r => r.fulfill({ body: cfg, contentType: 'application/javascript' }));
await pg.goto(home);
const wired = await pg.evaluate(() => [...document.querySelectorAll('[data-link]')].filter(a => ['starter','system','pro','club','free'].includes(a.dataset.link)).map(a => ({ l: a.dataset.link, href: a.getAttribute('href') })));
ok('buy buttons wire to Payhip links once configured', wired.every(x => x.href === `https://payhip.com/b/TEST-${x.l}`), JSON.stringify(wired));
await pg.close();

pg = await ctx.newPage(); await pg.goto(pathToFileURL(join(site, 'support.html')).href);
const mail = await pg.evaluate(() => [...document.querySelectorAll('[data-mail]')].map(a => a.getAttribute('href')));
ok('support page: contact links go to the live support form', mail.length > 0 && mail.every(h => h === 'https://tally.so/r/db9DvD'), JSON.stringify(mail));
await pg.close();
pg = await ctx.newPage(); await pg.goto(pathToFileURL(join(site, 'partners.html')).href);
const apply = await pg.evaluate(() => [...document.querySelectorAll('a')].some(a => a.href === 'https://tally.so/r/KpVJZX'));
ok('partners page: apply button goes to the live partner form', apply);
await pg.close(); await b.close();

const failed = results.filter(r => !r.pass);
mkdirSync(join(root, 'ops', 'qa'), { recursive: true });
writeFileSync(join(root, 'ops', 'qa', 'site-results.json'), JSON.stringify({ ran: new Date().toISOString(), total: results.length, failed: failed.length, results }, null, 1));
console.log(`site checks: ${results.length - failed.length}/${results.length} passed`);
process.exit(failed.length ? 1 : 0);
