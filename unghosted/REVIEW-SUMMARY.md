# Unghosted: Full Review Summary

*Prepared November 22, 2026. Everything below is in the repo `6csRISE-cpu/Clear-rise`, branch `claude/autonomous-digital-business-qdjpdr`, folder `unghosted/`.*

**One-line status:** the business is fully built and the website is live on a free domain. It can't take money yet: the owner still has to create the payment accounts (Payhip + Stripe/PayPal), which require the owner's identity and bank verification.

---

## 1. The business

| | |
|---|---|
| **Name** | **Unghosted** (renamed from ClearRise at the owner's request: trendier, rawer) |
| **Tagline** | "Your customers are ghosting you. Let's unf\*ck that." |
| **Live site (free)** | **https://unghostedhq.vercel.app** |
| **What it sells** | Ready-to-send text, email and phone templates, plus a tracker, that help small home-service businesses win back missed calls, close quiet quotes, rebook past customers, save cancellations, get Google reviews and start maintenance plans |
| **Who buys** | Owners of small HVAC, plumbing, electrical, cleaning, lawn/landscaping and pest-control businesses (1–15 staff) |
| **Model** | Digital downloads + monthly subscription. Instant automated delivery, about 80% net margin, no owner face or identity in the brand |

### Why this opportunity was chosen
- **Real, measured pain:** call-tracking studies find 14–27% of calls to home-service businesses go unanswered (Invoca 2024; CallRail 2025), and quotes often die to silence.
- **Buyers with money and a clear payoff:** one recovered job ($150–$5,000) pays for any product many times over.
- **Gap in the market:** free templates exist but are scattered across software-vendor blogs. Unghosted is a complete, trade-specific system with timing, consent guidance, a tracker and seasonal campaigns.
- **Low cost, low complexity, scalable:** fully digital, no inventory, expands to more trades and to agency licenses.
- **Rejected:** Etsy printables (race to the bottom), courses/coaching (needs the owner's face and time), SaaS (expensive to build and support), affiliate blogs (tiny commissions, slow).

### Brand identity
- **Voice:** blunt, raw and funny on the website, emails and social ("Copy. Paste. Get paid.", "No forms. No BS.", "Built for people who fix things, not people who 'circle back'"). Swearing is censored (unf\*ck) so spam filters, ad platforms and Facebook groups don't block the brand.
- **The templates customers send to homeowners stay polite and professional,** because they go out under the customer's name.
- **Look:** neo-brutalist. Bone background, black ink, acid-lime highlights, chunky Inter Black type, hard-shadow buttons and cards, a ghost logo with lime eyes.

---

## 2. Products and pricing (all finished)

| Product | Price | What's inside | File for Payhip |
|---|---|---|---|
| **5 Texts That Win Back Missed Calls** | Free | 4-page guide; collects email addresses | `Unghosted-5-Texts-Free-Guide.pdf` |
| **Ghost-Proof Kit** | $27 | 7 missed-call texts, voicemail script, 5-touch quote follow-up, phone scripts, texting-consent guide, tracker | `Unghosted-Ghost-Proof-Kit.zip` |
| **Unghosted System** ★ most popular | $67 | Kit + rebooking (12 trades), cancellation/no-show recovery, review engine, referral loop, maintenance-plan builder, 10 AI prompts, 30-day rollout, scorecard | `Unghosted-System.zip` |
| **Pro Bundle** | $127 | System + 6 trade packs with 12-month calendars, staff scripts and training, software cheat sheet, Google Business Profile checklist, 90-day plan, bonus Ghost Club pack | `Unghosted-Pro-Bundle.zip` |
| **Ghost Club** | $19/mo or $159/yr | A new seasonal campaign pack every month. Dec 2026, Jan 2027 and Feb 2027 are already written | `Unghosted-Ghost-Club-*.zip` |

**Every paid product includes:** branded PDFs, editable Word versions, a tracker spreadsheet whose scorecard calculates itself (Excel or Google Sheets), and a CSV of every template (105 in total) for bulk import into texting apps.

**Guarantee:** 30-day money-back on everything.

**Upgrade path:** code `UPGRADE27` (Kit → System), code `PRO67` (System → Pro), checkout upsells and onboarding emails.

---

## 3. What's live and verified

| Item | Status |
|---|---|
| Website at **unghostedhq.vercel.app**: sales page, lost-revenue calculator, pricing, FAQ, guarantee | ✅ Live. Served HTTP 200 with the new brand; production is public |
| 6 SEO guides, guides index, sitemap, robots.txt | ✅ Live |
| Support page, Terms, Privacy, Refund policy | ✅ Live (legal name and address are placeholders until the owner provides them) |
| Phone and desktop layout | ✅ Checked at 390px and 1280px, no sideways scrolling, no broken links |
| Support form | ✅ Published: https://tally.so/r/db9DvD |
| Feedback survey | ✅ Published: https://tally.so/r/Yj4Mkz |
| Product PDFs | ✅ 8 PDFs rendered and visually checked |
| Spreadsheet formulas (tracker, financial model, dashboard) | ✅ Recalculated with test data, no errors |
| Monthly content automation | ✅ Scheduled task "Unghosted monthly content" runs on the 20th of each month (first run Dec 20, 2026): writes the next Ghost Club pack and 2 new SEO guides, rebuilds, commits, redeploys |

**Buy buttons** show "Opening soon" until Payhip links are added. One paste per product in `site/config.js`.

---

## 4. What needs the owner (about 2 hours, once)

Full step-by-step instructions: `ops/OWNER-SETUP.md`

| # | Action | Why only the owner can do it | Cost |
|---|---|---|---|
| 1 | **Create a Payhip account and connect Stripe and/or PayPal.** Upload the 6 product files (listing text ready in `ops/PAYHIP-LISTINGS.md`), create the 2 coupons, turn on abandoned-cart emails and affiliates (30%), make a test purchase | Identity and bank verification | $0/mo + 5% per sale + card fees |
| 2 | **Send Claude the Payhip product links** | Links only exist after step 1 | — |
| 3 | **Create a MailerLite account**, connect it to Payhip, add 5 groups; paste in the written email sequences (or give Claude/a VA access) | Account ownership | $0 to start |
| 4 | **Send Claude** your legal name or business entity, a mailing address (PO box is fine) and your state | Legal pages and email law (CAN-SPAM) | — |
| 5 | **Before selling, move hosting** to free Cloudflare Pages (commercial use allowed) *or* upgrade Vercel. Vercel's free plan is non-commercial | Account ownership | $0 |
| 6 | *Optional:* buy **unghostedhq.com** (available, ~$12/yr) and set up `support@unghostedhq.com` forwarding | Purchase | ~$12/yr |
| 7 | *Optional:* submit the sitemap to Google Search Console; create YouTube/TikTok/Instagram accounts for short videos | Account ownership | $0 |

---

## 5. Marketing system (all written; no paid ads at launch)

| Rank | Channel | What's ready | Owner time |
|---|---|---|---|
| 1 | **Google search** | 6 guides live + 24 queued topics; 2 new guides/month written automatically | 0 |
| 2 | **Affiliates and partners** | 30% commission program design, outreach + follow-up emails, prospect sheet | 0 (a VA can send outreach) |
| 3 | **Faceless short video** | 12 scripts (TikTok, YouTube Shorts, Reels) | 0 if outsourced |
| 4 | **Communities** | Answer bank for trade Facebook groups and Reddit (value-first, no spam) | Optional, 15 min/week |
| 5 | **Email** | 7 automated sequences: free-guide nurture (7 emails), Kit/System/Pro onboarding with upgrade offers, abandoned cart, Ghost Club welcome/monthly/renewal/cancellation, day-21 feedback, plus a weekly newsletter format with 12 topics | 0 once set up |
| 6 | **Pinterest** | 12 branded pins + upload CSV | 0 |

Plus a 90-day launch and publishing calendar: `marketing/CONTENT-CALENDAR.md`.

**Rules we follow:** no fake testimonials or reviews, no invented results, no incentivized reviews, no spam, texting-consent rules respected.

---

## 6. How the automation fits together

Visitor → website → Payhip (checkout, tax, instant delivery, upsells, coupons, abandoned cart, affiliates, subscription billing) → MailerLite (all email sequences) → Tally (support and feedback) → monthly Owner Dashboard.

**Fully automatic once set up:** checkout, delivery, VAT, lead capture, all emails, upsells, abandoned cart, subscription billing and renewals, feedback collection, self-serve FAQ, affiliate tracking, monthly content creation.

**Still human (about 1.5 hours/month):** answer support and approve refunds (~15 min/week), upload the monthly Ghost Club pack to Payhip and send the broadcast (10 min; Claude can do this if the accounts are connected), pay affiliates by PayPal (10 min), fill in the dashboard (10 min, or ask Claude).

---

## 7. Money

**Fixed costs at launch: about $1/month** (only a domain, if you buy one). Payhip takes 5% per sale, plus about 2.9% + $0.30 card fees.

**Per average order** ($65): about **$52 net** after fees, refunds and affiliate commissions (≈80% margin). **Break-even:** the first sale.

| 12-month scenario *(estimates, not promises)* | Conservative | Base | Strong (upper bound) |
|---|---|---|---|
| Orders at month 12 | 13/mo | 64/mo | 320/mo |
| Ghost Club members at month 12 | 3 | 20 | 132 |
| **Year-1 gross revenue** | ≈ $5,000 | ≈ $22,700 | ≈ $102,000 |
| **Year-1 net profit** | ≈ $4,000 | ≈ $17,900 | ≈ $80,500 |

**Targets (Base assumptions):** $1K/month net ≈ 20 orders ≈ 1,300 visitors · $3K ≈ 58 orders ≈ 3,900 visitors · $5K ≈ 97 orders ≈ 6,500 visitors.

Files: `ops/Unghosted-Financial-Model.xlsx` (change any blue cell and it all recalculates) and `ops/FINANCIALS.md`.

---

## 8. Owner dashboard and maintenance

- **Dashboard:** `ops/Owner-Dashboard.xlsx`. Enter 15 numbers monthly; 11 KPIs turn green or orange against targets (net profit, orders, average order value, conversion rates, refund rate, club members, churn, recurring revenue, email open rate, support tickets). Rule: fix the single worst orange number each month.
- **Maintenance:** `ops/MAINTENANCE.md`: weekly (15 min), monthly (45 min), quarterly (1 hr), plus decision triggers (e.g. switch to Payhip Plus above $1,000/month in sales; add a trade pack when 3+ customers ask).
- **Support replies:** `ops/SUPPORT-MACROS.md` (downloads, refunds, cancellations, setup help, licensing, affiliates).

---

## 9. Honest notes and risks

- **Nothing has sold yet.** No market validation exists until real traffic and purchases. The first 90 days of data matter more than any projection.
- **Hosting:** the free Vercel site is fine for preview and review, but its free plan doesn't allow commercial use. Move to Cloudflare Pages (free) before taking payments.
- **Name:** no existing "Unghosted" brand turned up in a search (the closest is an unrelated dating app called "Ghosted"). This isn't a formal trademark search; worth one before significant spending.
- **The edgy voice** may turn off a few conservative buyers. The site copy can be dialed up or down at any time without touching the products.
- **Compliance:** templates include texting-consent and review-policy guidance, but it's practical guidance, not legal advice. Legal pages need the owner's real details before launch.
- **Taxes:** Payhip handles EU/UK VAT. U.S. state sales tax only matters past state thresholds; check with an accountant once sales are steady.

---

## 10. Where everything lives

| Path | Contents |
|---|---|
| `unghosted/products/dist/pkg/` | **Upload-ready product files** |
| `unghosted/products/src/` | Product content source (Markdown) |
| `unghosted/site/` | The website; `site/config.js` holds every link |
| `unghosted/marketing/` | Acquisition plan, emails, SEO articles, pins, video scripts, community answers, partner kit, calendar |
| `unghosted/ops/` | Owner setup, Payhip listings, launch checklist, automation map, financials, dashboard, maintenance, support replies |
| `unghosted/tools/` | Scripts that rebuild PDFs, the site, pins and the spreadsheets |

**Accounts and tools Claude set up for you:** Vercel project `unghosted` (team Big Hands) with free domain unghostedhq.vercel.app · Tally forms "Unghosted Support" and "Unghosted: 30-Second Feedback" · scheduled task "Unghosted monthly content" (delete it any time from your scheduled tasks if you don't want it).
