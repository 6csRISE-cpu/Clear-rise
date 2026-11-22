# Financial Model (v3)

## Actual results to date
| Metric | Actual |
|---|---|
| Sales | **0**. Checkout isn't live yet |
| Revenue | **$0** |
| Customers, refunds, subscribers | **0** |
| Money spent | **$0** (no purchases made; every account so far is on a free tier) |

Everything below is an **assumption**, not a result. Once sales start, `ops/Owner-Dashboard.xlsx` holds the actual numbers and replaces these assumptions.

---

## Unit economics per one-time order (Base assumptions)

| Line | Amount | Basis |
|---|---|---|
| Average order value (35% Kit $27 / 45% System $67 / 20% Pro $127) | **$65.00** | Assumed mix; the System is the product we optimize for |
| Payhip fee (Free plan) | −$3.25 | 5% (Payhip pricing, 2026) |
| Card processing | −$2.19 | ~2.9% + $0.30 (Stripe/PayPal standard rate) |
| Refunds | −$3.25 | Assumed 5% (30-day guarantee) |
| Partner/affiliate commission | −$7.41 | 30% commission × ~40% of sales via partners (after refunds) |
| **Net per order** | **≈ $48.90 (≈ 75%)** | |

**Direct vs. partner sale:** a direct $65 order nets ≈ $56.30; a partner-referred one nets ≈ $37.80 after the $18.50 commission (30% of $61.75 after refunds).

**Ghost Club** ($19/mo): ≈ $17.20 net per member-month after fees. Offered only *after* a purchase. Assumed 8% of buyers join (Base), with 9% monthly churn (average life ≈ 11 months, ≈ $190 net lifetime value).

## Operating costs

| Item | Cost | Status |
|---|---|---|
| Domain (e.g. unghostedhq.com) | ~$12/year | Not bought (owner decision) |
| **Hosting with clear commercial-use terms** | **$0–$20/month** | **Decision needed.** Vercel Hobby (current preview) is personal/non-commercial only per Vercel's terms, so selling requires Vercel Pro (~$20/mo) or another host whose current terms allow it (Cloudflare Pages Free has no explicit commercial ban, but describes Free as "for personal or hobby projects"; read their current terms before relying on it) |
| Payhip (store, checkout, delivery) | $0/mo + 5% per sale | Free plan; Plus ($29/mo, 2%) pays off above ~$1,000/mo sales |
| Card processing | ~2.9% + $0.30 per sale | Per sale |
| MailerLite (email) | $0 to start; ~$10–$30/mo as the list grows | Free plan limits apply |
| Zapier (Payhip → MailerLite routing) | $0 (free tier) | |
| Tally (forms) | $0 (free tier) | Live |
| Attorney review of *The Texting Rules* | **One-time, quote needed** (ask for a flat fee) | Launch gate |
| Test purchase + refund | ~$1–2 in fees | Launch gate |

**Fixed monthly cost in the model:** Conservative $1 (all free tiers) · Base $21 (paid hosting) · Strong $51 (paid hosting + paid email tier).

## 12-month scenarios (assumptions)

| | Conservative | Base | Strong (upper bound) |
|---|---|---|---|
| Month-1 visitors (incl. partner-referred) | 300 | 500 | 800 |
| Monthly visitor growth | 15% | 22% | 30% |
| Visitor → buyer / → free guide | 0.8% / 4% | 1.2% / 6% | 1.8% / 8% |
| Share of sales via partners | 30% | 40% | 50% |
| **Month 3:** orders / gross / net | 4 / $223 / $171 | 11 / $736 / $532 | 30 / $2,258 / $1,601 |
| **Month 6:** orders / gross / net | 5 / $345 / $265 | 20 / $1,366 / $1,005 | 66 / $5,092 / $3,675 |
| **Month 12:** orders / gross / net | 13 / $806 / $620 | 64 / $4,561 / $3,406 | 320 / $24,901 / $18,165 |
| **Year 1 gross** | ≈ $5,000 | ≈ $22,700 | ≈ $102,300 |
| − Refunds | $298 | $1,135 | $4,093 |
| − Payhip + processing | $420 | $1,916 | $8,634 |
| − Partner commissions | $420 | $2,587 | $14,734 |
| − Fixed costs | $12 | $252 | $612 |
| **Year 1 net** | **≈ $3,800** | **≈ $16,800** | **≈ $74,200** |

*The Strong case requires traffic to grow 30% a month for a year. Treat it as a ceiling, not a target. Year-1 numbers exclude the one-time attorney fee (quote needed) and the Partner License ($297, not modeled).*

## Targets and required volume (Base)
| Monthly net profit | Orders/month | Visitors/month |
|---|---|---|
| $1,000 | ~21 | ~1,400 |
| $3,000 | ~62 | ~4,100 |
| $5,000 | ~103 | ~6,900 |

## Customer acquisition cost (CAC)
- **Partner-referred:** the commission is the CAC: ~$18.50 per average order, paid only after a sale.
- **Organic (communities, email, SEO):** $0 cash; the cost is time (owner/VA hours) and the monthly content task.
- **Paid ads:** none. If tested later, the break-even CAC is ≈ $49 per order (more if buyers upgrade or join Ghost Club). Don't test before 25+ real sales.

## First 90 days: what matters
The goal for the first 90 days is **evidence**, not the projection: 25+ sales, a measured conversion rate, at least 3 active partners, and a refund rate below 10%. See `marketing/ACQUISITION-PLAN.md`, 90-day validation plan.
