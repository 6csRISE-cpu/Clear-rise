# Unghosted: Review Summary (v3)

*Updated November 22, 2026. Repo `6csRISE-cpu/Clear-rise`, branch `claude/autonomous-digital-business-qdjpdr`, folder `unghosted/`. The detailed, evidence-backed checklist is `ops/LAUNCH-CHECKLIST.md`.*

**Status:** built, with a non-selling preview at https://unghostedhq.netlify.app. **Not ready to take money:** hosting terms, payment accounts, attorney review, email setup and the end-to-end tests are still open. Actual results so far: **0 sales, $0 revenue, $0 spent.**

## What changed in v3
| Decision | Result |
|---|---|
| **Many businesses, not one niche** (owner's call) | Back to all home-service trades under one promise: **"Stop losing jobs because you didn't follow up."** The Kit's playbook now covers HVAC & plumbing, electrical, cleaning, lawn care, pest control, plus guidance for every other trade |
| **Pricing structure** | Kit $27 = easy first buy · **System $67 = primary, featured** · Pro $127 = established businesses with staff · Ghost Club $19/mo offered **after** purchase (removed from the homepage pricing) |
| **Partners stay the lead channel** | Broadened to consultants, bookkeepers, agencies and VAs across all trades; measurable recruitment funnel; 90-day validation plan |
| **Hosting** | The current preview is on Vercel Hobby (non-commercial). Selling waits until you choose a plan or host with clear commercial terms |
| **Owner control** | Full inventory added: every existing asset (repo, Vercel project, Tally forms, scheduled task) is in your accounts. Payment, email and domain accounts must be created in your name |
| **Financials** | Rebuilt with actuals (all zero) clearly separated from assumptions, including direct vs. partner unit economics, hosting cost and CAC |
| **Done-for-you setup ($149–$249)** | Noted as a *later* option if buyers ask for implementation help. Not built |

## Kept from v2 (still in place)
- *The Texting Rules* with 4 message types (Reply / Service / Marketing / Automated) in every paid product, and every template labeled. Awaits attorney review (launch gate).
- Google-compliant review requests; Partner & Affiliate Terms with FTC disclosure rules.
- Automated checks: **248/248 site, 63/63 package**. E2E test plan (30 tests) for the live accounts.

## Products
| Product | Price | Role |
|---|---|---|
| 5 Texts That Win Back Missed Calls | Free | Email capture |
| Ghost-Proof Kit | $27 | Easy first purchase: missed calls, quote follow-up, trade playbooks, Texting Rules, tracker |
| **Unghosted System** | **$67** | **Primary product:** + rebooking, cancellations, reviews, referrals, maintenance plans |
| Pro Bundle | $127 | Teams: + 12-month calendars, staff scripts, training, Google Business Profile checklist, 90-day plan |
| Ghost Club | $19/mo or $159/yr | Offered after purchase |
| Partner License | $297 | Agencies/VAs implementing for up to 10 clients |

## Money (assumptions; see `ops/FINANCIALS.md`)
- **Per order:** ≈ $48.90 net on a $65 average (direct ≈ $56.30, partner-referred ≈ $37.80).
- **Fixed:** $1–$51/month depending on hosting and email tier.
- **Year 1:** Conservative ≈ $3.8K net · Base ≈ $16.8K · Strong ≈ $74K (ceiling).
- **The 90-day goal is evidence:** 25+ sales, 3+ active partners, refund rate under 10%. Not the projection.

## Your actions (owner-only)
1. Choose hosting with commercial terms (Vercel Pro ~$20/mo, or another host after reading its terms).
2. Create Payhip + Stripe/PayPal in your name.
3. Get an attorney to review *The Texting Rules* (flat-fee quote).
4. Create MailerLite in your name; connect Payhip.
5. Send Claude your legal name, mailing address and state.
6. Run the E2E tests with Claude (`ops/E2E-TEST-PLAN.md`).
7. Optional: buy your own domain; start partner outreach (or hire a VA).

## Where things are
`ops/LAUNCH-CHECKLIST.md` (blockers, evidence, owner control, risks, costs) · `ops/FINANCIALS.md` · `ops/E2E-TEST-PLAN.md` · `ops/COMPLIANCE-REVIEW-PACKET.md` · `marketing/ACQUISITION-PLAN.md` (partner-led, 90-day plan) · `marketing/partners/` · `products/dist/pkg/` (upload-ready files) · `site/` · `tools/` (build + tests)
