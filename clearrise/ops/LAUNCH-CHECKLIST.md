# Launch Checklist: Honest Status

Legend: ✅ done and verified · 🟡 built, waiting on an owner account step · ⬜ not started

**Overall status: BUILT, NOT YET LAUNCHED.** The business can't take money until the owner creates the Payhip/Stripe accounts (identity and bank verification can't be done on your behalf). Nothing below is claimed as live unless it says verified.

## Product
| Item | Status | Evidence |
|---|---|---|
| Free guide (3-page PDF) | ✅ | `products/dist/pkg/ClearRise-5-Texts-Free-Guide.pdf` |
| Follow-Up Kit ($27): 10-page PDF, DOCX, XLSX, CSV | ✅ | `ClearRise-Starter-Kit.zip` |
| Revenue Recovery System ($67): 2 PDFs (25 pages), DOCX, XLSX, CSVs | ✅ | `ClearRise-Revenue-Recovery-System.zip` |
| Pro Bundle ($127): 4 PDFs + bonus pack, DOCX, XLSX, CSVs | ✅ | `ClearRise-Pro-Bundle.zip` |
| Campaign Club packs: Dec 2026, Jan 2027, Feb 2027 | ✅ | `ClearRise-Club-*.zip` |
| Tracker/scorecard formulas recalculate correctly | ✅ | Recalculated in LibreOffice, no errors |
| Visual QA of PDFs | ✅ | Cover + interior pages rendered and checked |

## Storefront
| Item | Status | Evidence |
|---|---|---|
| Sales page with calculator, pricing, FAQ, guarantee | ✅ | `site/index.html`, screenshots at 1280px and 390px, no horizontal scroll |
| 6 SEO guides + guides index + sitemap + robots | ✅ | `site/guides/`, `site/sitemap.xml` |
| Support page, Terms, Privacy, Refund policy | ✅ | `site/support.html`, `site/legal/` |
| Legal name / address / state filled in | 🟡 | Needs owner Step 4 |
| Domain `clearrisetools.com` | 🟡 | Available on Nov 22, 2026 (~$12/yr). Purchase needs owner (Step 1) |
| Hosting live | 🟡 | Ready for Cloudflare Pages (Step 1, ~5 min) |
| Analytics | 🟡 | Code in place; needs the Cloudflare token |

## Checkout, delivery & payments
| Item | Status | Evidence |
|---|---|---|
| Payhip product listings written | ✅ | `ops/PAYHIP-LISTINGS.md` |
| Upload-ready product ZIPs | ✅ | `products/dist/pkg/` |
| Payhip account + Stripe/PayPal connected | 🟡 | Owner identity/bank verification (Step 2) |
| Buy buttons | 🟡 | Show "Opening soon" until Payhip links go in `site/config.js` (one paste each) |
| Test purchase end to end | ⬜ | After Step 2 |
| Coupons, upsells, abandoned cart, affiliates | 🟡 | Configured in Payhip during Step 2; all copy written |

## Email & automation
| Item | Status | Evidence |
|---|---|---|
| 7 sequences written (nurture, 3 onboarding, abandoned cart, club, feedback) + newsletter format | ✅ | `marketing/emails/email-sequences.md` |
| MailerLite account, domain auth, groups, automations | 🟡 | Owner Step 3 |
| Payhip → MailerLite routing | 🟡 | Native integration + Zapier, Step 3 |

## Support
| Item | Status | Evidence |
|---|---|---|
| Support form (Tally) | ✅ Published | https://tally.so/r/db9DvD: published via the Tally API in your account. (This sandbox's network blocks tally.so, so open it once yourself to confirm.) |
| Feedback survey (Tally) | ✅ Published | https://tally.so/r/Yj4Mkz (same note) |
| Support email `support@clearrisetools.com` | 🟡 | Cloudflare Email Routing after domain purchase |
| Support reply macros + refund process | ✅ | `ops/SUPPORT-MACROS.md`, `site/legal/refunds.html` |

## Marketing
| Item | Status | Evidence |
|---|---|---|
| Acquisition plan (ranked channels, funnel math) | ✅ | `marketing/ACQUISITION-PLAN.md` |
| 6 SEO guides live-ready + 24 queued topics | ✅ | |
| 12 Pinterest pins + upload CSV | ✅ | `marketing/pinterest/` |
| 12 faceless short-video scripts | ✅ | `marketing/video/` |
| Community answer bank | ✅ | `marketing/community/` |
| Affiliate program design + outreach emails + prospect sheet | ✅ | |
| 90-day calendar | ✅ | `marketing/CONTENT-CALENDAR.md` |
| Social accounts | ⬜ | Optional owner Step 6 |
| Search Console sitemap submission | 🟡 | Owner Step 5 |

## Operations
| Item | Status |
|---|---|
| Financial model (live formulas, 3 scenarios, targets) | ✅ `ops/ClearRise-Financial-Model.xlsx` |
| Owner dashboard (auto KPIs vs targets) | ✅ `ops/Owner-Dashboard.xlsx` |
| Maintenance schedule | ✅ `ops/MAINTENANCE.md` |
| Monthly content automation (Club pack + 2 guides) | ✅ Scheduled task (see README) |

## Go-live definition
The business counts as **launched** when all of these are true:
1. The domain resolves to the site over HTTPS
2. Every buy button opens a Payhip checkout
3. A real test purchase delivers files and triggers the onboarding email
4. The free guide delivers and triggers the nurture sequence
5. Analytics shows the test visits
6. The support email forwards to the owner
