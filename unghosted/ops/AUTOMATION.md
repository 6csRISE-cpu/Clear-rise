# Automation Architecture

```
                 ┌────────────── TRAFFIC (evergreen) ──────────────┐
                 │ Google (SEO guides) · Affiliates · Short video   │
                 │ Communities · Pinterest                          │
                 └──────────────────────┬──────────────────────────┘
                                        ▼
               unghostedhq.netlify.app (Cloudflare Pages, auto-deploys from GitHub)
               sales page · calculator · guides · support · legal
                    │                                   │
        "Free guide" │                           "Buy" │
                    ▼                                   ▼
             PAYHIP $0 product                   PAYHIP checkout
             (email captured,                    (Stripe/PayPal, VAT, instant
              PDF delivered)                      file delivery, upsells, coupons,
                    │                             abandoned-cart email, affiliates,
                    │                             membership billing & dunning)
                    └──────────────┬────────────────────┘
                                   ▼
                  Payhip → MailerLite (native) + Zapier (per-product group)
                                   ▼
          MAILERLITE automations: nurture · onboarding · upsell · club · feedback
                                   ▼
          TALLY: support form → owner inbox · feedback survey (day 21)
                                   ▼
          DASHBOARD: Payhip + MailerLite + Cloudflare numbers → Owner-Dashboard.xlsx
```

## What runs with zero involvement

| Function | Tool | How |
|---|---|---|
| Checkout & payments | Payhip + Stripe/PayPal | Hosted checkout |
| Product delivery | Payhip | Instant download link on screen and by email |
| Taxes (EU/UK VAT) | Payhip | Calculated and collected automatically |
| Lead capture | Payhip $0 product | Email captured on download |
| Free-guide nurture (7 emails) | MailerLite | Group trigger |
| Customer onboarding (per product) | MailerLite | Group trigger |
| Upsells | Payhip checkout upsell + onboarding emails | Automatic |
| Abandoned cart | Payhip | Built-in email |
| Subscription billing, renewals, failed-payment retries | Payhip memberships | Built-in |
| Annual renewal reminder | MailerLite | Date-based automation |
| Feedback collection | MailerLite → Tally | Day-21 email |
| Basic support / FAQ | Support page + Tally form | Self-serve first; form to inbox |
| Affiliate tracking | Payhip | Built-in |
| Site deploys | Netlify Free (project `unghostedhq`, unghostedhq.netlify.app) | Claude deploys via the Netlify connector after each change. Optional: link the repo in Netlify (Project configuration → Build & deploy → Link repository; branch `claude/autonomous-digital-business-qdjpdr`, base directory `unghosted/site`) so every push publishes automatically |
| Analytics | Cloudflare Web Analytics + Payhip + MailerLite reports | Built-in |
| **Monthly acquisition + content work** | **Claude scheduled task (20th)** | Researches 20 new partner prospects + drafts personalized first emails, writes next month's Partner Drop, Ghost Club pack and 1 SEO guide, rebuilds, runs all automated tests, commits, redeploys |

## What still needs a human (and how little)

| Task | Why it can't be automated | Time |
|---|---|---|
| Send partner outreach emails (drafted monthly) | Personal relationships; sent by a person from the business inbox | ~2 hrs/week while launching (VA-able) |
| Answer support emails/forms | Judgment and refunds; most questions are pre-answered by the support page | ~15 min/week |
| Approve refunds | Money movement | Inside the 15 min |
| Upload the monthly Club pack to Payhip + send the broadcast | Requires your Payhip/MailerLite login (Claude can do it if you connect those accounts) | 10 min/month |
| Pay affiliates | Payhip doesn't auto-pay affiliates; you send PayPal payouts | 10 min/month |
| Review the draft guides Claude commits | Brand protection | 10 min/month (optional) |
| Fill in the monthly dashboard | Pulling numbers from 3 dashboards | 10 min/month (or ask Claude) |

## Regenerating products and the site

```bash
cd unghosted
python3 tools/build_products.py      # Markdown → HTML, DOCX, CSV, XLSX
node tools/render_pdfs.mjs           # HTML → branded PDFs
bash tools/package.sh                # → products/dist/pkg/*.zip (Payhip uploads)
python3 tools/build_site.py          # guides, legal, support, sitemap
node tools/og_and_shots.mjs          # social share image
node tools/make_pins.mjs             # Pinterest pins
node tools/test_site.mjs             # automated site checks (248)
python3 tools/test_packages.py       # product file checks (63)
python3 tools/build_financials.py    # financial model
```

To add a new Club month: add `products/src/club/YYYY-MM-month.md` (copy the format of an existing one), then run the first three commands. To add a guide: add a Markdown file to `marketing/seo/articles/` and run `build_site.py`.
