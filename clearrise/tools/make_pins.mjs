// Generate 12 Pinterest pin images (1000x1500) + pins.csv for bulk upload/scheduling.
import { createRequire } from 'module'; import { fileURLToPath } from 'url'; import { join, dirname } from 'path'; import { writeFileSync } from 'fs';
const require = createRequire(import.meta.url); const { chromium } = require('playwright');
const out = join(dirname(fileURLToPath(import.meta.url)), '..', 'marketing', 'pinterest');
const S = 'https://clearrisetools.com/guides/';
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
const themes = [['#0F2A3D','#1F6F80','#fff'],['#FBF8F3','#F3E3C8','#0F2A3D']];
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1000, height: 1500 } });
const rows = [['file','title','description','link']];
for (const [i, [t, s, slug]] of pins.entries()) {
  const [c1, c2, fg] = themes[i % 2];
  await p.setContent(`<html><body style="margin:0;width:1000px;height:1500px;font-family:Inter;background:linear-gradient(165deg,${c1},${c2});color:${fg};display:flex;flex-direction:column;justify-content:space-between;padding:90px 80px;box-sizing:border-box">
  <div style="display:flex;align-items:center;gap:14px;font-weight:800;letter-spacing:.16em;font-size:30px"><span style="width:34px;height:34px;border-radius:50%;background:#E8962E"></span>CLEARRISE</div>
  <div><div style="font-size:30px;font-weight:700;color:#E8962E;letter-spacing:.08em;text-transform:uppercase;margin-bottom:26px">Free guide</div>
  <div style="font-size:96px;font-weight:800;line-height:1.02;letter-spacing:-.02em">${t}</div>
  <div style="font-size:44px;margin-top:30px;opacity:.85">${s}</div></div>
  <div style="background:#E8962E;color:#1D1205;font-weight:800;font-size:36px;padding:26px 34px;border-radius:18px;align-self:flex-start">Copy-and-paste templates →</div></body></html>`);
  const file = `pin-${String(i+1).padStart(2,'0')}.png`;
  await p.screenshot({ path: join(out, file) });
  rows.push([file, t.replace(/"/g,''), `${t} ${s}. Free copy-and-paste templates for home-service business owners. #smallbusiness #contractor #hvac #plumbing #cleaningbusiness`, S + slug + '.html']);
}
writeFileSync(join(out, 'pins.csv'), rows.map(r => r.map(x => `"${String(x).replace(/"/g,'""')}"`).join(',')).join('\n') + '\n');
await b.close(); console.log('pins', pins.length);
