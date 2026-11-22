# End-to-End Customer Journey Test Plan

**Launch gate:** buy buttons don't go live (`site/config.js` links stay empty) until **every test below passes** and the compliance review in `ops/COMPLIANCE-REVIEW-PACKET.md` is done.

**What's already tested automatically** (re-run with `node tools/test_site.mjs && python3 tools/test_packages.py`):
- **Site checks, 248 passing:** every page loads without errors, every internal link resolves, no sideways scrolling on a phone, buy buttons are disabled while unconfigured and point to the right Payhip URL once configured, the calculator math is right, and support/partner links go to the live forms.
- **Package checks, 63 passing:** each ZIP contains exactly the right files, every PDF renders, spreadsheets open, every template is typed, and no old branding appears.

**What can only be tested with your live accounts** is below. Run it once before launch, and again after any change to Payhip, MailerLite or Zapier. Claude can run most of it with you if you connect the accounts.

## Setup for testing
- **Two test inboxes:** your main email, plus a second address (e.g. a Gmail with a "+test" alias: `you+t1@gmail.com`). Payhip and MailerLite treat aliases as separate customers.
- **Coupon `TEST100`:** 100% off, all products, limit 20 uses. **Delete it after testing.**
- **One real card purchase:** pay for the $27 Kit once with a real card, then refund it. Costs about $1–2 in fees, and it's the only way to prove the real payment path works.
- **Test log:** copy the table below into a sheet; fill in Pass/Fail, date and evidence (screenshot or email subject + time).

## The tests

| ID | Journey step | How to test | Expected result | Pass/Fail | Evidence |
|---|---|---|---|---|---|
| **A1** | Free guide captures email | In a private browser window, click "Free guide" on the site → complete the $0 Payhip checkout with test inbox 1 | Payhip shows the download; receipt email arrives; customer appears in Payhip → Customers | | |
| A2 | Free guide downloads the right file | Open the download | `Unghosted-5-Texts-Free-Guide.pdf`, 4 pages | | |
| **A3** | Subscriber reaches MailerLite | MailerLite → Subscribers | Test inbox 1 is in group `free-guide` within 5 min | | |
| **A4** | Nurture sequence starts | Wait for A1 email | "Your 5 texts are here" arrives within 5 min; links work; unsubscribe link present; mailing address in footer | | |
| A5 | Sequence timing | Check MailerLite automation activity at day 2 (or temporarily set delays to minutes on a copy) | A2 sends after the configured delay; no duplicates | | |
| A6 | Unsubscribe works | Click unsubscribe in A1 | Status = unsubscribed; no further emails | | |
| **B1** | Kit purchase, real card | Buy the Kit at $27 with a real card (test inbox 2) | Payment succeeds; download page shows `Unghosted-Ghost-Proof-Kit.zip`; receipt arrives | | |
| **B2** | Correct files delivered | Unzip the download | Exactly: Texting Rules PDF, Kit PDF + DOCX, tracker XLSX, Starter CSV, READ-ME (matches `tools/test_packages.py`) | | |
| B3 | Buyer routed in MailerLite | MailerLite | Test inbox 2 is in `buyer-starter` and **removed from** `free-guide` | | |
| **B4** | Onboarding starts | Inbox | B1-1 "Your Ghost-Proof Kit + the 15-minute setup" arrives with the UPGRADE27 code | | |
| B5 | Refund works | Payhip → Sales → refund the B1 order | Card refunded (check statement in 5–10 days); refund email to buyer; sale marked refunded | | |
| **C1** | Upgrade coupon works | Checkout for System with `UPGRADE27` | Price drops $67 → $40 | | |
| C2 | Coupon is restricted | Try `UPGRADE27` on Pro and on Ghost Club | Rejected | | |
| C3 | Pro upgrade coupon | Checkout for Pro with `PRO67` | Price drops $127 → $60; rejected on other products | | |
| C4 | Checkout upsell (if enabled) | Add the Kit to cart | System upsell offer appears at checkout | | |
| **D1** | System & Pro deliver correct files | `TEST100` checkouts for System, Pro and Partner License | Each ZIP matches its manifest in `tools/test_packages.py` | | |
| **E1** | Subscription starts | Join Ghost Club monthly with `TEST100` (or the real $19, refunded after) | Membership active; welcome post and current pack downloadable; D1 welcome email arrives; in group `club` | | |
| **E2** | **Subscription renews** | Keep one real $19 subscription active over the first billing date (or use Payhip's shortest billing interval on a hidden $1 test plan, if available) | Day 31: second charge succeeds; access continues; receipt arrives | | |
| **E3** | **Cancellation stops billing** | Cancel the membership from the buyer's receipt link | Payhip shows "cancelled / no next payment"; at the next billing date **no charge** occurs; buyer keeps access to delivered packs | | |
| E4 | Failed payment handling | (If Payhip supports test cards for memberships) a card that declines on renewal | Payhip sends a failed-payment email and retries or cancels per settings | | |
| E5 | Annual renewal reminder | MailerLite date automation for annual members | D3 reminder scheduled 7 days before renewal | | |
| **F1** | Abandoned cart email | Start a Kit checkout with test inbox 1, enter email, close the tab | Abandoned-cart email arrives (Payhip timing); link restores checkout | | |
| **G1** | Affiliate attribution | Create a test affiliate (test inbox 2) → open their link in a private window → buy the Kit with a real card | Payhip records a 30% commission to the affiliate; then refund and confirm the commission reverses | | |
| G2 | Attribution across products | Click an affiliate link to the *free guide*, then buy the Kit in the same session | Note whether Payhip credits the affiliate (decides which link partners should share) | | |
| **H1** | Support form | Submit https://tally.so/r/db9DvD | Owner gets the Tally notification email within minutes | | |
| H2 | Support email | Email `support@` (once the domain exists) or the store support address | Arrives in owner inbox; reply goes out from the right address | | |
| H3 | Response time | Owner replies using `ops/SUPPORT-MACROS.md` | Reply within 2 business days (the promise on the site) | | |
| **I1** | Partner application | Submit https://tally.so/r/KpVJZX | Owner notified; review copy coupon + affiliate link sent within 2 business days | | |
| **J1** | Feedback survey | Open https://tally.so/r/Yj4Mkz?email=test@example.com | Form loads; hidden email captured on submit | | |
| **K1** | Mobile purchase | Repeat A1 and a `TEST100` Kit checkout on a phone | Works end to end; downloads open on the phone | | |
| L1 | Analytics | Visit the site from the test devices | Visits appear in analytics within 24 hours | | |

## After testing
1. Delete `TEST100`, remove test subscribers, refund any test charges.
2. Record the date and result in `ops/LAUNCH-CHECKLIST.md`.
3. Only then paste the Payhip links into `site/config.js` and redeploy.

## Re-test triggers
Any change to Payhip products/files, coupons, MailerLite automations or groups, Zapier zaps, or the site's config, plus once a quarter: run A1–A4, B1–B4 (with `TEST100`), E3 and H1.
