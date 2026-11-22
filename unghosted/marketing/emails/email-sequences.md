# Unghosted Email Sequences

All sequences live in **MailerLite** (free plan, automations included). Payhip's native MailerLite integration adds every customer to MailerLite; a free Zapier zap per product ("New Payhip sale → add/update MailerLite subscriber in group") puts each buyer in the right group. Each group triggers one automation below. Setup steps are in `ops/OWNER-SETUP.md`.

| MailerLite group | Added when… | Automation |
|---|---|---|
| `free-guide` | Someone downloads the free guide | A. Nurture (7 emails / 14 days) |
| `buyer-starter` | Buys the Ghost-Proof Kit | B1. Starter onboarding + upgrade |
| `buyer-system` | Buys the System | B2. System onboarding + Pro/Club offer |
| `buyer-pro` | Buys the Pro Bundle | B3. Pro onboarding + Club offer |
| `club` | Joins Ghost Club | D. Club welcome (monthly pack sent as a broadcast on the 1st) |
| *(all buyers)* | Day 21 after purchase | E. Feedback request |

**Rule:** when someone buys, remove them from the `free-guide` group so they stop getting the nurture sequence (MailerLite automation setting: "remove from group").

Merge fields: `{$name}` = first name (fallback "there"). Sender: "Alex at Unghosted" *(use a real first name of whoever answers support, or the brand alone, "Unghosted")*. Footer must include the mailing address (MailerLite adds it automatically from account settings).

---

## A. Free-guide nurture (7 emails over 14 days)

**A1 · Immediately**
Subject: Your 5 texts are here (+ one thing to do today)
> Hi {$name},
>
> Here's your free guide: **5 Texts That Win Back Missed Calls** → [Download the PDF]({{FREE_GUIDE_URL}})
>
> If you do only one thing today, do this: open your phone or field-service app, search the settings for "missed call text," and paste Text #1. It takes five minutes.
>
> Then call your own number from another phone, let it ring out, and make sure the text arrives. That's it. You've plugged the biggest leak in most service businesses.
>
> Over the next two weeks I'll send you a few more short, useful emails: quote follow-ups, reviews, rebooking. No fluff.
>
> — Unghosted
>
> P.S. Reply and tell me your trade. I read every reply.

**A2 · Day 2**
Subject: The text that revives "dead" quotes
> Hi {$name},
>
> Most quotes aren't lost to a cheaper competitor. They're lost to silence.
>
> Here's the single best follow-up I know. Send it 21 days after a quote goes quiet:
>
> > "Hi {First}, I'll close out your {job} quote this week so I'm not bugging you. If you went another way, totally fine. Would you mind telling me why? One word is plenty."
>
> It works because it's honest, it's easy to answer, and it gives people permission to say "actually… can we still do it?"
>
> Full 5-touch sequence here: [How to follow up on a quote]({{SITE}}/guides/quote-follow-up-templates.html)

**A3 · Day 4**
Subject: Why "just checking in" doesn't work
> Hi {$name},
>
> "Just checking in" gives the customer nothing to respond to. Every follow-up should *give* them something:
>
> - an answer ("the question most people ask is…")
> - an option ("I can do a smaller version for around $X")
> - a date ("I can hold Thursday or Friday")
>
> The option is the magic one. When price is the silent objection, a smaller option lets people reply without admitting it.
>
> The full Ghost-Proof Kit has all five touches written out, plus phone scripts and a tracker, for $27: [Get the Kit]({{STARTER_URL}})

**A4 · Day 6**
Subject: Your best marketing is already in your invoices
> Hi {$name},
>
> Quick question: when did you last contact a customer you worked for 6–12 months ago?
>
> For most service businesses the answer is "never." But those people already trust you, and many of them are due for the same job again.
>
> A simple rebooking text:
> > "Hi {First}, it's been about a year since we did your {job}, which is usually when it's due again. Want me to get you on the schedule?"
>
> Intervals for 12 trades: [Rebooking reminders by trade]({{SITE}}/guides/customer-rebooking-reminders.html)

**A5 · Day 8**
Subject: How to get reviews without breaking Google's rules
> Hi {$name},
>
> The best review system is one sentence, said out loud at the end of every job:
>
> > "If you're happy with how this turned out, it'd really help us if you left a quick Google review. I'll text you the link."
>
> Then text the link within two hours. One reminder three days later. Done.
>
> Two things to never do: offer discounts for reviews, or send only happy customers to Google. Both break Google's rules (and the FTC's).
>
> Full guide: [Get more Google reviews]({{SITE}}/guides/get-more-google-reviews-home-service.html)

**A6 · Day 11**
Subject: The whole system, in one place
> Hi {$name},
>
> Over the last week and a half you've seen pieces of it: missed-call texts, quote follow-ups, rebooking, reviews.
>
> The **Unghosted System** puts all six campaigns together (plus cancellation recovery, referrals and maintenance plans), with a 30-day rollout that turns on one campaign a week.
>
> - Branded guide + editable Word files
> - Tracker & scorecard spreadsheet
> - Every template in a CSV for your texting app
> - 10 AI prompts to make it sound like you
>
> $67, one time, with a 30-day money-back guarantee. One recovered job pays for it.
>
> [Get the System]({{SYSTEM_URL}})

**A7 · Day 14**
Subject: Last note (and a question)
> Hi {$name},
>
> This is the last email in this series. From here you'll get one short, useful email a week.
>
> If Unghosted isn't right for you right now, no problem. Keep the free texts, they're yours.
>
> If you want the full system, it's here: [Unghosted System]({{SYSTEM_URL}}), or the [Pro Bundle]({{PRO_URL}}) if you'd like trade-specific campaigns and staff scripts too.
>
> And one question: **what's the hardest part of following up with customers in your business?** Hit reply. Your answer shapes what we build next.

---

## B1. Starter (Ghost-Proof Kit) onboarding

**B1-1 · Immediately**
Subject: Your Ghost-Proof Kit + the 15-minute setup
> Thanks for your order, {$name}! Your files are in your Payhip receipt (and here: [Download]({{PAYHIP_LIBRARY}})).
>
> Start with page 1 of the PDF, "Start here (15 minutes)." By the end of today you'll have missed-call text-back running and your quote follow-ups on the calendar.
>
> **Upgrade any time in the next 30 days** and your $27 comes off the System: use code **UPGRADE27** at checkout → [Unghosted System]({{SYSTEM_URL}})

**B1-2 · Day 3**
Subject: Did your missed-call text arrive?
> Quick check: did you test your missed-call text by calling your own number? If it didn't arrive, search your app's help center for "missed call text back" or reply to this email with the app you use and we'll point you in the right direction.

**B1-3 · Day 10**
Subject: You've got new jobs covered. What about past customers?
> The Ghost-Proof Kit wins back *new* jobs. The System adds the money already in your customer list: rebooking, cancellation saves, reviews, referrals and maintenance plans.
>
> Code **UPGRADE27** takes $27 off until {30 days after purchase}. → [Upgrade to the System]({{SYSTEM_URL}})

**B1-4 · Day 25**
Subject: Your upgrade credit expires in 5 days
> Just a heads-up: your $27 upgrade credit (code UPGRADE27) expires in 5 days. After that, no more reminders about it. → [Upgrade]({{SYSTEM_URL}})

## B2. System onboarding

**B2-1 · Immediately**
Subject: Your Unghosted System: start here
> Welcome, {$name}! Download your files: [Library]({{PAYHIP_LIBRARY}}).
>
> Open the System PDF and jump to **"The 30-Day Rollout."** This week: missed-call text-back + quote follow-ups. One campaign per week after that.
>
> Tip: open `Unghosted-Follow-Up-Tracker.xlsx` in Excel or Google Sheets and log every quote from today. The Scorecard tab calculates your recovered revenue automatically.

**B2-2 · Day 7**
Subject: Week 2: the review engine
> This week, turn on the Review Engine (Campaign 4). The whole thing is one sentence at the end of every job plus one text. Get your Google review link first. Instructions are on the first page of Campaign 4.

**B2-3 · Day 14**
Subject: Week 3: your first rebooking batch
> Time to pull your first rebooking list: export customers, filter by last job date, send R1. Need the intervals? They're in the table at the top of Campaign 2.

**B2-4 · Day 18**
Subject: Make it specific to your trade
> The **Pro Bundle** adds six trade packs (HVAC, plumbing, cleaning, lawn, electrical, pest), each with a 12-month campaign calendar, plus staff scripts and a 90-day plan. Upgrade for the difference with code **PRO67** → [Pro Bundle]({{PRO_URL}})
>
> Or, if you'd rather not plan campaigns at all, **Ghost Club** sends you a ready-made seasonal campaign on the 1st of every month for $19/mo. → [Join]({{CLUB_URL}})

**B2-5 · Day 28**
Subject: Week 4 + your first scorecard
> Last rollout step: cancellation recovery and the reminder pair. Then on the 1st, fill in your scorecard. What's your recovered revenue so far? Reply and tell us. We love hearing real numbers (and we'll never share them without asking).

## B3. Pro onboarding

**B3-1 · Immediately**
Subject: Your Pro Bundle: where to start
> Welcome, {$name}! [Download your files]({{PAYHIP_LIBRARY}}).
>
> 1. Open the **Implementation Playbook** → Part 1, the 90-Day Plan.
> 2. Open **Trade Packs** → your trade → the 12-month calendar. Circle this month.
> 3. Run the 20-minute staff meeting with Part 2 (Staff Scripts) this week.
>
> Your bonus Ghost Club pack is in the bundle too.

**B3-2 · Day 10**
Subject: Has your team used the call flow yet?
> The 5-step call flow (Playbook, Part 2) is the fastest win for teams: answer, repeat back, qualify, *book don't quote*, confirm. Print it and put it by every phone.

**B3-3 · Day 21**
Subject: Never plan a campaign again
> You've got the calendar. Ghost Club gives you each month's campaign fully written, on the 1st: texts, emails, a Google post, a social post and one quick fix. $19/mo, cancel anytime. → [Join Ghost Club]({{CLUB_URL}})

---

## C. Abandoned cart (Payhip built-in)

Payhip → Settings → Abandoned cart emails → ON. Customize the text:

Subject: You left something behind
> Hi there, it looks like you didn't finish checking out for **{product}**. No pressure. If you had a question, just reply to this email and we'll answer it.
>
> Most owners make the price back with a single recovered job, and you're covered by a 30-day money-back guarantee.
>
> [Complete your order]({cart_link})

*Do not add a discount by default. It trains people to abandon carts. Test a 10% code only if recovery rate is under 5% after 60 days.*

---

## D. Ghost Club

**D1 · Welcome (immediately on joining)**
Subject: Welcome to Ghost Club: this month's pack is inside
> Welcome, {$name}! This month's pack is here: [Download]({{CURRENT_PACK_URL}}). New packs arrive on the 1st of every month by email.
>
> Each pack takes about an hour to run: a checklist, a ready-to-send campaign, a Google post, a social post, a 10-minute fix and one number to track.
>
> Cancel any time from your Payhip receipt. You keep everything you've received.

**D2 · Monthly delivery (broadcast to `club` group, 1st of each month)**
Subject: {Month} pack: {theme}
> Hi {$name}, your **{Month} Campaign Pack** is ready: **{theme}**.
>
> [Download the {Month} pack]({{PACK_URL}})
>
> This month in one line: {one-sentence summary}.
>
> Your checklist is on page 2. Total time: about an hour.

**D3 · Annual renewal reminder (7 days before renewal, annual members)**
Subject: Your Ghost Club renews in 7 days
> A quick heads-up: your annual Ghost Club membership renews on {date} for $159. No action needed to continue. To cancel, use the link in your Payhip receipt or reply to this email.

**D4 · Cancellation follow-up (when a member cancels)**
Subject: Sorry to see you go (one quick question)
> Thanks for being a member, {$name}. You keep every pack you received. Could you reply with one word on why you left? (Price / too busy / not useful / other). It helps us make the Club better.

---

## E. Feedback request (day 21 after any purchase)
Subject: 2 quick questions (30 seconds)
> Hi {$name}, you've had Unghosted for three weeks. Could you answer two quick questions? → [Take the 30-second survey](https://tally.so/r/Yj4Mkz?email={$email})
>
> 1. Have you used any of the templates with a real customer yet?
> 2. What's one thing we should add or fix?
>
> If anything isn't working for you, reply here. We'd rather fix it than lose you.

---

## F. Weekly newsletter (broadcast, every Tuesday 7am)

Format: **one tip, one template, one link.** Under 200 words. Written in advance in batches of 12 (see `marketing/CONTENT-CALENDAR.md`).

Template:
> Subject: {tip headline}
>
> Hi {$name},
>
> **This week's tip:** {2–3 sentences}
>
> **Steal this template:**
> > {template}
>
> **Read more:** {link to guide}
>
> — Unghosted
