# Financial Model Summary

Full live model: `ops/Unghosted-Financial-Model.xlsx` (v2, partner-led). Change any blue cell and everything recalculates. **These are planning estimates based on stated assumptions, not predictions or guarantees.** A new store has no sales history, and the first 90 days of real data will replace these guesses.

## Unit economics (per order, Base mix)

| | |
|---|---|
| Average order value (35% Kit / 45% System / 20% Pro) | **$65.00** |
| Payhip fee (5%) | −$3.25 |
| Card processing (2.9% + $0.30) | −$2.19 |
| Expected refunds (5%) | −$3.25 |
| Partner/affiliate commission (30% on ~40% of sales: partner-led launch) | −$7.41 |
| **Net per order** | **≈ $48.90 (≈ 75% margin)** |

Ghost Club: $19/month, about $17 net per member per month after fees.

## Operating costs

| Item | Cost | When |
|---|---|---|
| Domain (unghostedhq.vercel.app) | ~$12/year | Now |
| Hosting, email forwarding, analytics (Cloudflare) | $0 | Now |
| Store & checkout (Payhip Free) | $0/mo + 5% per sale | Now |
| Payment processing (Stripe/PayPal) | ~2.9% + $0.30 per sale | Per sale |
| Email marketing (MailerLite Free) | $0 | Until the free-plan subscriber limit |
| Forms (Tally Free), automation (Zapier Free) | $0 | Now |
| **Total fixed cost at launch** | **≈ $1/month** | |
| *Later:* Payhip Plus | $29/mo (saves 3%/sale) | Above ~$1,000/mo sales |
| *Later:* MailerLite paid tier | roughly $10–$30/mo | When the list outgrows the free plan |
| *Optional:* Google Workspace business inbox | ~$7/mo | When support volume grows |

**Break-even:** the first sale covers a year of fixed costs. There is no meaningful break-even hurdle. The real cost is time and traffic.

## 12-month scenarios

| | Conservative | Base | Strong (optimistic) |
|---|---|---|---|
| Month-1 visitors | 300 | 500 | 800 |
| Monthly visitor growth | 15% | 22% | 30% |
| Visitor → buyer | 0.8% | 1.2% | 1.8% |
| Visitor → free guide | 4% | 6% | 8% |
| Share of sales via partners | 30% | 40% | 50% |
| **Month 3:** orders / gross / net | 4 / $223 / $170 | 11 / $736 / $541 | 30 / $2,258 / $1,627 |
| **Month 6:** orders / gross / net | 5 / $345 / $264 | 20 / $1,366 / $1,014 | 66 / $5,092 / $3,701 |
| **Month 12:** orders / gross / net | 13 / $806 / $619 | 64 / $4,561 / $3,415 | 320 / $24,901 / $18,191 |
| Club members at month 12 | 3 | 20 | 132 |
| **Year-1 gross revenue** | **≈ $5,000** | **≈ $22,700** | **≈ $102,000** |
| **Year-1 net profit** | **≈ $3,800** | **≈ $16,900** | **≈ $74,600** |

*The Strong case assumes traffic compounds 30% a month for a full year, which only happens if SEO and affiliates both work well. Treat it as an upper bound, not a plan.*

## Targets and required volumes (Base assumptions)

| Monthly net profit target | Orders/month needed | Visitors/month needed |
|---|---|---|
| $1,000 | ~21 | ~1,400 |
| $3,000 | ~62 | ~4,100 |
| $5,000 | ~103 | ~6,800 |
| $10,000 | ~205 | ~13,700 |

*(Excludes Club revenue, which lowers these numbers as membership grows. The "Targets" sheet recalculates for any target you enter.)*

## Customer acquisition cost
- **Organic (SEO, communities, video):** $0 cash; the cost is content production, which the monthly scheduled task covers.
- **Partners/affiliates (primary channel):** 30% of the sale (~$19.50 on the average order), paid only after a sale. Partner-referred visitors are counted in the visitor numbers above.
- **Partner License ($297):** not included in the model. Treat it as upside until real sales show up.
- **Paid ads:** not used at launch. Only test once there are 50+ sales and a measured conversion rate. The break-even cost per acquisition is about $50 per order.

## Subscription churn
Assumed 7–12% of Club members cancel per month (typical for low-priced content subscriptions). At 9% churn, the average member stays about 11 months, for a lifetime value of about **$190 net**. The dashboard tracks actual churn monthly.
