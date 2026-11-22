# Maintenance Schedule (minimum owner involvement)

## Weekly: 15 minutes (pick one day, e.g. Monday)
- ☐ Check the support inbox + Tally submissions. Reply using `ops/SUPPORT-MACROS.md`. Process any refund requests in Payhip.
- ☐ Glance at Payhip sales. Anything odd (a spike of refunds, failed payments)?

## Monthly: about 45 minutes (on the 1st)
- ☐ **Club pack:** download the new pack Claude committed (`products/dist/pkg/Unghosted-Ghost-Club-YYYY-MM-*.zip`), upload it to the Payhip membership, send the MailerLite broadcast (template D2). *(Or let Claude do it if MailerLite/Payhip are connected.)*
- ☐ **Dashboard:** enter last month's numbers in `ops/Owner-Dashboard.xlsx` (Payhip → Analytics; MailerLite → Reports; Cloudflare → Web Analytics). Or paste screenshots to Claude and ask it to fill them in.
- ☐ **Affiliates:** Payhip → Affiliates → pay balances by PayPal.
- ☐ **Review** the 2 new draft guides (optional, 10 min). Merge or leave as-is.

## Quarterly: about 1 hour
- ☐ Ask Claude for a performance review: "Here's my dashboard. What's the single biggest improvement?" Implement only changes backed by numbers.
- ☐ Check that nothing in the stack changed price or terms (Payhip, MailerLite, Cloudflare, Zapier).
- ☐ Update the year in `products/src/*` if needed, and re-run the build.

## Annually
- ☐ Renew the domain (auto-renew in Cloudflare; just keep the card current).
- ☐ Accountant check-in: sales tax thresholds, entity, deductions.
- ☐ Refresh the stats on the sales page with the latest published research.

## Decision triggers (act only when these happen)
| Signal | Action |
|---|---|
| Monthly sales > $1,000 for 2 months | Switch Payhip to Plus ($29/mo, 2% fee) |
| MailerLite list > free-plan limit | Upgrade MailerLite or prune inactive subscribers |
| Refund rate > 10% | Ask refunders why (template in macros); fix the product page or product |
| Free-guide conversion < 2% of visitors | Test a new headline on the free-guide section |
| Visitors → sales < 0.5% after 1,000+ visitors | Review pricing page + checkout (ask Claude) |
| 3+ customers ask for the same trade | Add a trade pack for it |
| 50+ sales and refund rate < 5% | Consider a small paid test (Google Ads on "missed call text template") |
