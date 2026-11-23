# Unghosted Launch Readiness Checklist (v3)

*Audit date: November 22, 2026. Legend: ✅ done **and verified** (evidence given) · 🟡 built but **not verified** · 🔴 not started / blocked · 👤 owner-only.*

**Bottom line:** the product, website and compliance material are built, and automated checks pass. The business **cannot take a payment yet**, and nothing about checkout, email delivery, renewals or refunds has been tested, because those accounts don't exist yet. Nothing below is marked done without evidence.

---

## A. Launch blockers, in priority order

| # | Blocker | Owner-only? | Status | Next action |
|---|---|---|---|---|
| 1 | **Hosting with clear commercial-use terms.** The current preview runs on Vercel Hobby, which Vercel's terms limit to personal/non-commercial use. | 👤 | 🔴 | Choose: Vercel Pro (~$20/mo, no migration) **or** another host after reading its current terms (Cloudflare Pages Free has no explicit ban I found, but describes Free as "for personal or hobby projects"). **Don't take payments on Hobby.** |
| 2 | **Payment accounts:** Payhip + Stripe and/or PayPal in your name | 👤 | 🟡 **Owner-reported done (Nov 23, 2026): Payhip + PayPal.** Not yet verified by a test purchase | Create the 6 products from `ops/PAYHIP-LISTINGS.md`, send the product links, then run test B1 |
| 3 | **Attorney review** of *The Texting Rules* and template labels | 👤 | 🔴 | Send `ops/COMPLIANCE-REVIEW-PACKET.md`; get a flat-fee quote |
| 4 | **Email platform:** MailerLite account + Payhip connection + automations loaded | 👤 (account) | 🔴 | `ops/OWNER-SETUP.md` Step 3. Sequences are written, not loaded |
| 5 | **Legal details:** legal name/entity, mailing address, state | 👤 | 🔴 | Send to Claude; currently placeholders in `site/config.js` |
| 6 | **End-to-end journey test** (30 tests) on live accounts | 👤 + Claude | 🔴 Blocked by 2 and 4 | `ops/E2E-TEST-PLAN.md` |
| 7 | **Domain** in your name (optional but recommended) | 👤 | 🔴 | e.g. unghostedhq.com (~$12/yr); availability checked Nov 22, 2026 |

**Buy buttons stay disabled ("Opening soon") until blockers 1–6 are cleared.** One switch controls them: `sellingEnabled` in `site/config.js` (currently `false`). Product links are saved as they arrive.

---

## B. Customer journey: verification status

| Step | Status | Evidence / what's missing |
|---|---|---|
| 1. Website visit | ✅ Preview live | https://unghostedhq.vercel.app serves the site (HTTP 200 confirmed via Vercel on Nov 22). Automated: 248/248 site checks (`ops/qa/site-results.json`) |
| 2. Free-guide download | 🟡 Linked, not yet tested | Payhip product created by owner: https://payhip.com/b/9QTX8 (Nov 23, 2026). Site buttons point to it (site check "button 'free' points at configured link"). Payhip page not opened from this environment (network blocks payhip.com). **Needs test A1/A2** |
| 3. Email capture | 🔴 | Needs Payhip + MailerLite (test A1, A3) |
| 4. Welcome sequence | 🔴 | Written in `marketing/emails/email-sequences.md`, not loaded (test A4–A6) |
| 5. Product purchase | 🟡 Product created, not tested | Ghost-Proof Kit: https://payhip.com/b/6D8Lo · Unghosted System: https://payhip.com/b/Sj7qd · Pro Bundle: https://payhip.com/b/7Dl5m (owner, Nov 23, 2026). Saved in `site/config.js`; button intentionally **off** (`sellingEnabled: false`) until hosting with commercial terms + tests B1–B5 pass |
| 6. Payment confirmation | 🔴 | Test B1 |
| 7. Product delivery | 🟡 Files verified, delivery not | Every ZIP has exactly the right files: 63/63 package checks. Payhip delivery is untested (B2, D1) |
| 8. Upgrade offer | 🔴 | Coupons UPGRADE27/PRO67 and upsells are designed, not created (C1–C4) |
| 9. Subscription purchase | 🔴 | Ghost Club product not created (E1); renewal needs a real billing cycle (E2) |
| 10. Cancellation & refund | 🔴 | Tests B5, E3 |
| Support | ✅ Form published · 🟡 response flow | Support form published via the Tally API (https://tally.so/r/db9DvD). Owner notification + reply not yet tested (H1–H3) |
| Partner intake | ✅ Form published · 🟡 flow | https://tally.so/r/KpVJZX published; intake → review copy not tested (I1) |

---

## C. Completed and verified

| Item | Evidence |
|---|---|
| Product files: Free guide, Kit ($27), System ($67), Pro ($127), Partner License ($297), 3 Ghost Club packs | `products/dist/pkg/`; `python3 tools/test_packages.py` → 63/63 (exact file lists, PDFs render, spreadsheets open, no old branding) |
| Multi-trade positioning restored (HVAC, plumbing, electrical, cleaning, lawn, pest + general) | Kit Part 3 "Trade Playbooks"; site hero; screenshot check at 1280px and 390px |
| Pricing structure: Kit = easy first buy, **System = primary (featured)**, Pro = teams; Ghost Club offered post-purchase only | `site/index.html` pricing section; FAQ; onboarding emails B2-4/B3-3 |
| *The Texting Rules* (4 message types) included in every paid product | `products/dist/pdf/00-texting-rules.pdf` (11 pages); in every paid ZIP (package checks) |
| Every template labeled with a message type | CSV `message_type`: Pro 92 templates = 20 Reply, 34 Service, 35 Marketing, 3 Live call; 0 untyped (package checks) |
| Review requests comply with Google's selective-solicitation and incentive rules | Neutral wording in System Campaign 4, playbook, guide, emails, community answers; "if you're happy" removed (grep shows it remains only as a prohibition) |
| Partner & Affiliate Terms with FTC disclosure rules | `site/legal/affiliates.html`; every Partner Drop includes a disclosure line |
| Website pages, links, mobile layout, buy-button wiring, calculator math | `node tools/test_site.mjs` → 248/248 |
| Financial model with actual-vs-assumption split | `ops/FINANCIALS.md` (actuals: $0 / 0 sales); `ops/Unghosted-Financial-Model.xlsx` recalculated without errors |

## D. Incomplete or unverified (not owner-only)

| Item | Status | Note |
|---|---|---|
| Attorney-reviewed compliance content | 🟡 Written | Not approved; may change after review |
| Owner dashboard populated | 🟡 Template ready | No actual data yet |
| Partner outreach started | 🔴 | First 20 researched prospects arrive with the Dec 20 scheduled run; owner/VA sends |
| Live site matches latest repo | 🟡 | Redeployed with this version as a **non-selling preview** (see E) |
| Search Console / analytics | 🔴 | Needs owner accounts |

---

## E. Owner control: who owns what

| Asset | Where it lives now | Owner | Evidence | Action needed |
|---|---|---|---|---|
| Source code & content | GitHub repo `6csRISE-cpu/Clear-rise` | ✅ You | Your GitHub organization/account | Merge the branch to `main` when ready |
| Website hosting (preview) | Vercel project `unghosted`, team "Big Hands" | ✅ You | Created through your connected Vercel account | Decide paid plan or another host before selling |
| Free domain alias | unghostedhq.vercel.app | ✅ Your Vercel project | Assigned in your team | Replace with your own domain later |
| Custom domain | Not purchased | — | — | 👤 Buy in **your** name, with your email and card |
| Support / feedback / partner forms | Tally "My workspace" | ✅ You | Created in your Tally workspace | Confirm notifications go to your inbox |
| Monthly content task | Your claude.ai scheduled tasks ("Unghosted monthly content") | ✅ You | Created under your account | Pause/delete anytime |
| Payment accounts (Payhip, Stripe, PayPal) | Not created | — | — | 👤 Create with **your** identity and bank; payouts to **your** account |
| Customer database | Will live in Payhip + MailerLite | — | — | 👤 Create both under your email; export customers monthly as a backup |
| Email marketing (MailerLite) | Not created | — | — | 👤 Your account, your domain authentication |
| Brand assets (logo, ghost mark, PDFs, pins, share image) | In the repo | ✅ You | `site/assets/`, `marketing/pinterest/`, `products/dist/` | Fonts are Inter + JetBrains Mono (SIL Open Font License, free for commercial use) |
| Revenue & payouts | Not flowing | — | — | 👤 Only your Stripe/PayPal accounts should receive payouts |

**No account, domain or payment destination is held by Claude or any third party.** Every future account should be created with your email, your card and two-factor login.

---

## F. Risks requiring attention

| Risk | Severity | Mitigation |
|---|---|---|
| Selling on a non-commercial hosting plan | High | Blocker 1. Don't connect payments until resolved |
| Texting guidance inaccurate in some states | High | Attorney review (Blocker 3); conservative rules; labels on every template |
| No validated demand yet | High | 90-day validation plan (`marketing/ACQUISITION-PLAN.md`); judge by sales, not projections |
| Partners don't engage | Medium | Measurable recruitment funnel; rewrite outreach by week 4 if fewer than 2 active |
| Broad market dilutes the message | Medium | One promise across trades + trade playbooks; let sales data show which trades to emphasize |
| FCC opt-out rules changing (FCC 26-67, reported effective Nov 25, 2026) | Medium | Guide uses "honor everything, immediately, everywhere"; flagged for counsel |
| Trademark conflict on "Unghosted" | Low–Medium | Quick search only; consider a formal search before spending on the brand |
| Refund abuse | Low | 30-day policy with a fair-use clause; watch the refund rate on the dashboard |

## G. Expected costs to launch

| Item | One-time | Monthly |
|---|---|---|
| Domain | — | ~$1 (≈$12/yr) |
| Hosting with commercial terms | — | $0–$20 (decision) |
| Payhip / Tally / Zapier / MailerLite (start) | — | $0 |
| Attorney review | Flat-fee quote needed | — |
| E2E test purchase + refund fees | ~$1–2 | — |
| Per sale | — | ~5% Payhip + ~2.9% + $0.30 processing; 30% commission on partner sales |

**No financial commitments have been made on your behalf.** Nothing has been purchased, subscribed to or signed.
