// Generate 12 Pinterest pin images (1000x1500) + pins.csv for bulk upload/scheduling.
import { createRequire } from 'module'; import { fileURLToPath } from 'url'; import { join, dirname } from 'path'; import { writeFileSync } from 'fs';
const require = createRequire(import.meta.url); const { chromium } = require('playwright');
const out = join(dirname(fileURLToPath(import.meta.url)), '..', 'marketing', 'pinterest');
const S = 'https://unghostedhq.netlify.app/guides/';
const pins = [
  ['7 Missed Call Text Templates', 'for plumbers, HVAC & cleaners', 'missed-call-text-back-templates'],
  ['The Text That Revives "Dead" Quotes', 'copy & paste for contractors', 'quote-follow-up-templates'],
  ['How to Follow Up on a Quote', 'without being pushy: 5 templates', 'quote-follow-up-templates'],
  ['Get More Google Reviews', 'the rules-safe system for home services', 'get-more-google-reviews-home-service'],
  ['When to Rebook Past Customers', 'intervals for 12 trades', 'customer-rebooking-reminders'],
  ['How to Price a Maintenance Plan', 'HVAC · plumbing · pest · lawn', 'maintenance-plan-pricing'],
  ['A Referral Program That Gets Used', 'for small service businesses', 'referral-program-for-contractors'],
  ['Stop Losing Jobs to Missed Calls', '5 texts to set up today', 'missed-call-text-back-templates'],
  ['Slow Season? Text Your Old Customers', 'rebooking templates inside', 'customer-rebooking-reminders'],
  ['"Just Checking In" Doesn\'t Work', 'say this instead', 'quote-follow-up-templates'],
  ['One Sentence = More 5-Star Reviews', 'for plumbers, HVAC & cleaners', 'get-more-google-reviews-home-service'],
  ['Turn Customers Into Monthly Revenue', 'maintenance plan pricing guide', 'maintenance-plan-pricing'],
];
const themes = [['#111111','#111111','#fff'],['#F3EFE6','#F3EFE6','#111111']];
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1000, height: 1500 } });
const rows = [['file','title','description','link']];
for (const [i, [t, s, slug]] of pins.entries()) {
  const [c1, c2, fg] = themes[i % 2];
  await p.setContent(`<html><body style="margin:0;width:1000px;height:1500px;font-family:Inter;background:${c1};color:${fg};display:flex;flex-direction:column;justify-content:space-between;padding:84px 76px;box-sizing:border-box;position:relative;overflow:hidden"><div style="position:absolute;right:-110px;top:930px;opacity:${i%2?0.35:0.95};transform:rotate(12deg)"><svg width="440" height="440" viewBox="0 0 24 24"><path d="M12 2C7.6 2 4 5.6 4 10v11.2c0 .7.8 1 1.3.5l1.9-1.9 1.9 1.9c.4.4 1 .4 1.4 0L12 20l1.5 1.7c.4.4 1 .4 1.4 0l1.9-1.9 1.9 1.9c.5.5 1.3.2 1.3-.5V10c0-4.4-3.6-8-8-8z" fill="#D7FF3A"/><circle cx="9.2" cy="10" r="1.7" fill="#111"/><circle cx="14.8" cy="10" r="1.7" fill="#111"/></svg></div><div style="display:flex;align-items:center;gap:12px;font-weight:900;letter-spacing:-.03em;font-size:46px;position:relative"><svg width="54" height="54" viewBox="0 0 24 24"><path d="M12 2C7.6 2 4 5.6 4 10v11.2c0 .7.8 1 1.3.5l1.9-1.9 1.9 1.9c.4.4 1 .4 1.4 0L12 20l1.5 1.7c.4.4 1 .4 1.4 0l1.9-1.9 1.9 1.9c.5.5 1.3.2 1.3-.5V10c0-4.4-3.6-8-8-8z" fill="${fg}"/><circle cx="9.2" cy="10" r="1.7" fill="#D7FF3A"/><circle cx="14.8" cy="10" r="1.7" fill="#D7FF3A"/></svg>unghosted</div><div style="position:relative"><div style="display:inline-block;font-family:JetBrains Mono,monospace;font-size:28px;font-weight:700;background:#D7FF3A;color:#111;padding:6px 14px;border-radius:6px;margin-bottom:30px">FREE TEMPLATES</div><div style="font-size:104px;font-weight:900;line-height:.98;letter-spacing:-.04em">${t}</div><div style="font-size:44px;margin-top:30px;opacity:.85;font-weight:600">${s}</div></div><div style="position:relative;background:#D7FF3A;color:#111;font-weight:900;font-size:38px;padding:26px 34px;border:4px solid #111;box-shadow:8px 8px 0 ${i%2?"#111":"#fff"};border-radius:14px;align-self:flex-start">Copy. Paste. Get paid. →</div></body></html>`);
  const file = `pin-${String(i+1).padStart(2,'0')}.png`;
  await p.screenshot({ path: join(out, file) });
  rows.push([file, t.replace(/"/g,''), `${t} ${s}. Free copy-and-paste templates for home-service business owners. #smallbusiness #contractor #hvac #plumbing #cleaningbusiness`, S + slug + '.html']);
}
writeFileSync(join(out, 'pins.csv'), rows.map(r => r.map(x => `"${String(x).replace(/"/g,'""')}"`).join(',')).join('\n') + '\n');
await b.close(); console.log('pins', pins.length);
