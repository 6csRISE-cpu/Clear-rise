# Unghosted: Revenue Recovery for Home-Service Businesses

**What it is:** a digital-product business that sells ready-to-send follow-up texts, emails and phone scripts, plus a tracker, to **home-service businesses** (HVAC, plumbing, electrical, cleaning, lawn care, pest control, roofing and more). **Promise:** *Stop losing jobs because you didn't follow up.* **Pricing:** Kit $27 (easy first buy) → **System $67 (primary product)** → Pro $127 (teams); Ghost Club $19/mo offered after purchase. **Acquisition:** partner-led (consultants, contractor bookkeepers, agencies, VAs), SEO in the background. **Compliance:** every template labeled by message type; *The Texting Rules* awaits attorney review before launch.

**Status:** fully built; site live at https://unghostedhq.netlify.app; not yet selling. Full review: [`REVIEW-SUMMARY.md`](REVIEW-SUMMARY.md). It's waiting on the owner account steps in [`ops/OWNER-SETUP.md`](ops/OWNER-SETUP.md) (about 2 hours). See [`ops/LAUNCH-CHECKLIST.md`](ops/LAUNCH-CHECKLIST.md) for exactly what's verified.

## Why this opportunity
- **Proven pain, measurable money:** call-tracking studies find 14–27% of calls to home-service businesses go unanswered, and quotes commonly die to silence. Owners already pay $50–$300+/month for software that partly solves this.
- **Buyers with budget:** these are business owners, so one recovered job ($150–$5,000) pays for any product many times over.
- **Free alternatives exist but are scattered:** vendor blog posts with a few templates. Unghosted wins on being a *complete, trade-specific system* with timing, consent guidance, a tracker and seasonal campaigns.
- **Digital, automated, ~80% net margin**, no owner face or identity needed, and it expands to new trades (roofing, pool, garage doors), new channels (agency licenses) and new products without rebuilding.
- Rejected alternatives: generic printables/Etsy (race to the bottom), course/coaching (needs the owner's face and time), SaaS (build and support costs), affiliate sites (tiny commissions, slow).

## Revenue ladder
| Product | Price | Role |
|---|---|---|
| 5 Texts That Win Back Missed Calls | Free | Lead magnet → email list |
| Ghost-Proof Kit | $27 | Entry product |
| Unghosted System | $67 | Core (most popular) |
| Pro Bundle | $127 | Premium implementation |
| Ghost Club | $19/mo or $159/yr | Recurring: new seasonal campaigns monthly |

## Stack (≈ $1/month fixed)
Cloudflare (domain, hosting, email forwarding, analytics) · Payhip (checkout, delivery, VAT, upsells, coupons, affiliates, abandoned cart, memberships) · Stripe/PayPal · MailerLite (email automations) · Zapier free (routing) · Tally (support + feedback forms, **live**).

## Folder map
| Path | What |
|---|---|
| `products/src/` | Product content (Markdown source of truth) |
| `products/dist/pkg/` | **Upload-ready ZIPs and the free PDF for Payhip** |
| `products/dist/pdf, docx` | Individual branded PDFs and editable Word files |
| `site/` | The website (deploy this folder). `site/config.js` holds every link |
| `content/pages/` | Support + legal page sources |
| `marketing/` | Acquisition plan, emails, SEO articles, pins, video scripts, community, partners, calendar |
| `ops/` | Owner setup, launch checklist, automation, financials, dashboard, maintenance, support macros |
| `tools/` | Build scripts (see `ops/AUTOMATION.md`) |

## Owner's monthly time
About **1.5 hours per month** after setup: 15 min/week for support, plus the monthly Club upload, affiliate payouts and dashboard numbers. Details in [`ops/MAINTENANCE.md`](ops/MAINTENANCE.md).
