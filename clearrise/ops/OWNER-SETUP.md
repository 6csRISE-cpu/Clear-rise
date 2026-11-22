# Owner Setup: Your Only Required Actions

Everything that *can* be built without your identity, money or signature is already built. These are the steps that legally or practically need **you**: account ownership, identity verification, payouts and a purchase. Total time is about **2–2.5 hours**, once.

When you finish a step, paste the link or ID it produces into a message to Claude (or into `site/config.js` yourself), and the rest is wired up for you.

> Use one email address for every account below (ideally a new one just for the business). Turn on two-factor login wherever it's offered.

---

## Step 1 — Buy the domain + hosting + business email (Cloudflare) · 20 min · ~$10–12/yr
1. Create a free account at **cloudflare.com**.
2. Go to **Domain Registration → Register Domains** and buy **`clearrisetools.com`** (checked available on Nov 22, 2026 at ~$12/yr; Cloudflare sells at cost). *Alternatives if it's gone: `useclearrise.com`, `clearrisekit.com`.*
3. **Workers & Pages → Create → Pages → Connect to Git** → choose the GitHub repo `Clear-rise`, branch `claude/autonomous-digital-business-qdjpdr` (or `main` after you merge), **build command: none**, **output directory: `clearrise/site`** → Deploy.
4. In the Pages project → **Custom domains** → add `clearrisetools.com`.
5. **Email → Email Routing** → create `support@clearrisetools.com` → forward to your personal inbox.
6. **Analytics & Logs → Web Analytics** → add the site → copy the token → send it to Claude (goes in `analyticsToken`).

*Why Cloudflare:* free hosting that allows commercial use, free email forwarding, free privacy-friendly analytics, and at-cost domain pricing, all in one dashboard. Every future push to the repo redeploys the site automatically.

## Step 2 — Payments: Payhip + Stripe/PayPal · 45 min · $0/month
1. Sign up at **payhip.com** (Free plan: 5% per sale, no monthly fee).
2. **Settings → Payment** → connect **Stripe** and/or **PayPal**. *This is the identity/bank verification step only you can do.*
3. **Settings → Account** → store name **ClearRise**, support email `support@clearrisetools.com`.
4. Create these products. Copy each description from `ops/PAYHIP-LISTINGS.md` and upload the files from `products/dist/pkg/`:

| Product | Type | Price | Upload |
|---|---|---|---|
| 5 Texts That Win Back Missed Calls | Digital, "free / $0+" | $0 | `ClearRise-5-Texts-Free-Guide.pdf` |
| ClearRise Follow-Up Kit | Digital | $27 | `ClearRise-Starter-Kit.zip` |
| ClearRise Revenue Recovery System | Digital | $67 | `ClearRise-Revenue-Recovery-System.zip` |
| ClearRise Pro Bundle | Digital | $127 | `ClearRise-Pro-Bundle.zip` |
| Campaign Club (monthly) | Membership | $19/month | Welcome post + `ClearRise-Club-2026-12-december.zip` |
| Campaign Club (annual) | Membership | $159/year | Same as monthly |

5. **Marketing → Coupons**: `UPGRADE27` = $27 off the System (limit one per customer) · `PRO67` = $67 off the Pro Bundle.
6. **Marketing → Upsells**: on the Kit checkout, offer the System; on the System checkout, offer Pro. *(If your Payhip plan doesn't show upsells, skip this step. The emails handle upgrades.)*
7. **Marketing → Abandoned cart emails** → ON, and paste the text from `marketing/emails/email-sequences.md` §C.
8. **Marketing → Affiliates** → ON, **30%** commission, cookie 60 days.
9. **Make a $0 test purchase of the free guide, and a real $27 purchase with a 100%-off test coupon** to confirm delivery works. (Create a temporary coupon `TEST100`, then delete it.)
10. Send Claude the 6 product URLs + the affiliate sign-up URL. They go into `site/config.js`, and every "Opening soon" button becomes a live "Buy" button.

## Step 3 — Email: MailerLite · 30 min · $0/month to start
1. Sign up at **mailerlite.com** (free plan). Verify the domain `clearrisetools.com` when prompted. MailerLite shows DNS records: add them in Cloudflare → DNS (copy and paste).
2. **Settings → Company** → your business name and **mailing address** (legally required in marketing emails).
3. Create groups: `free-guide`, `buyer-starter`, `buyer-system`, `buyer-pro`, `club`.
4. In **Payhip → Settings → Integrations → MailerLite**, connect your account.
5. Routing each product to its group: create one free **Zapier** zap per product: *Payhip "New Sale" → filter by product → MailerLite "Create/Update Subscriber" in that group.* (5 zaps; the free plan is enough at launch volumes.)
6. Build the automations by pasting from `marketing/emails/email-sequences.md`. *If you'd rather not, give Claude access to MailerLite (or hire a VA for ~1 hour) and send them that file.*

## Step 4 — Business details for the legal pages · 5 min
Send Claude: **(a)** your legal name or business entity, **(b)** a business mailing address (a PO box or virtual mailbox is fine), **(c)** your state. They fill the Terms, Privacy and email footers.

## Step 5 — Search engines · 10 min
1. **Google Search Console** → add `clearrisetools.com` (verify via Cloudflare DNS) → Sitemaps → submit `sitemap.xml`.
2. **Bing Webmaster Tools** → "Import from Google Search Console."

## Step 6 (optional, recommended) — Social profiles for short video · 20 min
Create **YouTube**, **TikTok** and **Instagram/Facebook** accounts named "ClearRise" with the support email. Bio: "Free templates that win back missed calls for home-service businesses ↓" + link to the free guide. The 12 scripts in `marketing/video/` are ready to produce. Posting can be handed to a VA or a scheduling tool.

---

### Things you should know (and decide only if you want to)
- **Taxes:** Payhip handles EU/UK VAT on digital goods. U.S. state sales tax on digital products only becomes an obligation after state thresholds (typically $100k in sales or 200 orders in a state). Ask an accountant once revenue is consistent.
- **Business entity:** you can start as a sole proprietor. An LLC is worth discussing with an accountant once sales are steady.
- **Payhip Plus ($29/mo, 2% fee)** pays for itself above ~$1,000/month in sales. Switch when the dashboard shows that.
