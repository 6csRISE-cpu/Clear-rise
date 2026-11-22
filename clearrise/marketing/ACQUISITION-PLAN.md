# ClearRise Customer Acquisition Plan

**Goal:** get the first 100 paying customers without paid ads, using channels that keep working after the content is created.

## Channel priority (ranked by expected return for *this* audience)

Our buyer is a small home-service business owner (1–15 staff). They search Google when they have a problem, hang out in trade Facebook groups and on YouTube, and trust peers and their industry's coaches more than ads.

| Rank | Channel | Why | Owner time | Status |
|---|---|---|---|---|
| 1 | **SEO guides** (Google) | High purchase intent ("missed call text template"). Evergreen: keeps compounding. | 0 | 6 guides written; 24 more topics queued below |
| 2 | **Affiliates & partners** | Trade coaches, CSR trainers and software consultants already have the audience. 30% commission costs nothing until a sale. | 0 (automated in Payhip) | Program designed; outreach emails written |
| 3 | **Faceless short video** (YouTube Shorts, TikTok, FB Reels) | "Text this, not that" format is easy to make without a face and spreads in trade circles. | 0 if outsourced/AI-made; ~1 hr/week if self-posting | 12 scripts written |
| 4 | **Communities** (trade Facebook groups, Reddit) | Where owners ask "how do I get more reviews?" Value-first answers convert. Must not be spam. | 15 min/week, optional | Answer bank written |
| 5 | **Email list** | Converts free-guide downloaders into buyers. Fully automated. | 0 | Sequences written |
| 6 | **Pinterest** | Lower fit (more homeowners than owners), but free, scheduled once and evergreen. Use for SEO-guide traffic only. | 0 | 12 pins generated |

**Not recommended yet:** paid ads (wait until the conversion rate is known), cold DMs (spammy, brand risk), marketplaces like Etsy (price race to the bottom).

---

## 1. SEO: the compounding engine

**Live guides (6):** missed-call text back · quote follow-up · Google reviews · rebooking reminders · maintenance plan pricing · referral programs.

**Publishing rule:** 2 new guides per month. Each targets one search phrase, gives the real answer for free, and links to the free guide plus one product.

**Next 24 topics (in order):**
1. HVAC tune-up reminder text templates
2. Plumbing estimate follow-up email
3. House cleaning rebooking text templates
4. Lawn care spring cleanup reminder email
5. How to respond to a negative Google review (contractor)
6. Appointment reminder text templates for home services
7. How to handle "your price is too high" (contractor scripts)
8. Cancellation text templates for service businesses
9. Pest control quarterly service reminder template
10. Text message consent for contractors (plain English)
11. Google Business Profile checklist for contractors
12. How to get a Google review link
13. Jobber follow-up templates (how to load them)
14. Housecall Pro review request templates
15. After-hours answering: voicemail scripts for plumbers
16. How to price house cleaning recurring plans
17. Referral card templates for contractors
18. Window cleaning reminder texts
19. Slow season marketing ideas for HVAC
20. Holiday marketing ideas for cleaning businesses
21. How to win back old customers (service business)
22. Thank-you text after service templates
23. Estimate vs quote follow-up: what to say
24. Electrician marketing: EV charger campaign templates

**How new guides get written without the owner:** the monthly scheduled Claude task (see `ops/AUTOMATION.md`) drafts the next two guides, builds them into the site and commits them for review.

**Submit once:** Google Search Console + Bing Webmaster Tools → add `sitemap.xml` (owner step, 5 minutes).

---

## 2. Affiliates & partners

**Program:** Payhip built-in affiliate program. **30% commission** on all products, 60-day cookie. Affiliates sign up from the footer link. Payhip tracks sales; payouts are monthly by PayPal (Payhip's affiliate payouts are handled by the seller, so this is a 10-minute monthly task, listed in the maintenance schedule).

**Who to recruit (in order):**
1. **Trade business coaches & consultants** (HVAC/plumbing/cleaning coaching programs, "sweaty startup" style creators)
2. **CSR / call-handling trainers**
3. **Field-service software consultants** (people who set up Jobber/Housecall Pro for clients)
4. **Trade bloggers & YouTubers** with how-to-run-your-business content
5. **Bookkeepers who specialize in trades**
6. **Trade associations' local chapters** (offer a member discount code instead of commission)

**Outreach email (send from the support inbox; personalize line 1):**

Subject: A resource for your {trade} audience (30% affiliate)
> Hi {Name},
>
> {One genuine sentence about their content.}
>
> I run ClearRise, plain-English text and email templates that help small home-service businesses win back missed calls, follow up on quotes and rebook past customers. It's a practical fit for the owners you work with.
>
> If you'd like to share it, our affiliate program pays **30% on every sale** (products are $27–$127, plus a $19/mo club). Happy to send you the full System free so you can see whether it's worth recommending first.
>
> {Affiliate link}
>
> Either way, thanks for what you put out there.

**Follow-up (7 days later, once):** "Just bumping this in case it got buried. Happy to send the System over for a look, no strings."

**Target:** 40 outreach emails in month 1 → expect roughly 4–8 replies and 2–4 active affiliates. A list-building template is in `marketing/partners/partner-prospects.csv`.

*Owner time: optional. These can be sent by a virtual assistant, or by Claude through a connected email account if you approve that.*

---

## 3. Faceless short video

Format: screen-recorded text messages + captions + voiceover (AI voice or text-to-speech is fine). 20–40 seconds. Same video posted to YouTube Shorts, TikTok, Instagram Reels and Facebook Reels.

Scripts: `marketing/video/short-video-scripts.md` (12 ready). Post 3/week. Batch-produce 12 at a time with a free editor (CapCut or Canva). Every video ends with "Free templates: link in bio" → the free guide.

---

## 4. Communities (value first, never spam)

**Where:** trade-owner Facebook groups (search "HVAC business owners," "cleaning business owners," "lawn care business owners"), r/sweatystartup, r/smallbusiness, trade-specific subreddits' business threads.

**Rules we follow:**
- Read each group's rules first. Many ban self-promotion, so respect that.
- Answer the question fully *in the post*. Link only if the group allows it and it genuinely helps (and to a free guide, not a sales page).
- Never post the same text twice. Never use fake accounts. Never invent results.

Answer bank: `marketing/community/answer-bank.md`.

---

## 5. Email list

Every guide, video and community answer points to **one** free offer: *5 Texts That Win Back Missed Calls.* The nurture sequence (7 emails, 14 days) converts it into sales. Then a weekly newsletter keeps the list warm. See `marketing/emails/email-sequences.md`.

## 6. Pinterest (low priority, zero maintenance)

12 pin images in `marketing/pinterest/`. Upload once with Pinterest's built-in scheduler (2/week over 6 weeks), each linking to a guide. Don't spend more time on it unless analytics show Pinterest referrals.

---

## Funnel math (what has to be true)

| Step | Assumption (starting estimate) |
|---|---|
| Visitors → free-guide signup | 4–8% |
| Visitors → direct purchase | 0.5–1.5% |
| Free-guide subscribers → purchase within 30 days | 3–6% |
| Average order value | ~$65 (after upsells) |

**To reach 100 sales/month** you need roughly 4,000–8,000 visitors/month. That's realistic from SEO by about months 6–12 and affiliates sooner. Months 1–3 will be slower. **These are estimates to test, not promises.** The scorecard in `ops/Owner-Dashboard.xlsx` replaces them with real numbers.
