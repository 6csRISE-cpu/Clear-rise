# Compliance Review Packet (for a TCPA / advertising attorney)

**Launch gate:** don't sell any paid product until a qualified attorney has reviewed *The Texting Rules* guide and the message-type labels on the templates. A "not legal advice" disclaimer doesn't replace accurate instructions. Our customers will act on them.

## What Unghosted is
A digital product that gives small home-service businesses (HVAC, plumbing, electrical, cleaning, lawn care, pest control and others) templates for texts, emails and phone calls: missed-call replies, quote follow-ups, appointment messages, review requests, rebooking, referral and maintenance-plan offers. Buyers send these messages to their own customers (homeowners) from their own phones or business texting tools.

## What we'd like reviewed (about 25 pages)
1. `products/dist/pdf/00-texting-rules.pdf`: *The Texting Rules*, the 4-type framework (Reply / Service / Marketing / Automated marketing), consent language, opt-outs, quiet hours, records, email. **Priority 1.**
2. Message-type labels on each campaign:
   - `01-missed-call-and-quote-kit.pdf`: Parts 1, 2, 4
   - `02-revenue-recovery-system.pdf`: campaign headers and the Review Engine
   - `Templates-Import-*.csv`: `message_type` column
3. Review-request material for Google policy and the FTC Consumer Reviews and Testimonials Rule: `02-revenue-recovery-system.pdf`, Campaign 4.
4. Affiliate/partner terms and disclosure requirements: `site/legal/affiliates.html`.
5. Our own Terms, Privacy and Refund pages: `site/legal/`.

## Specific questions for counsel
1. Is classifying **automatic missed-call text-back** (the business replies by automated text to a caller's missed call, staying strictly on the caller's request) as a customer-initiated "Reply" with no further consent reasonable under the TCPA and the major mini-TCPAs (FL, OK, MD, WA, NJ)? Any content limits?
2. Are **quote follow-up texts** (up to 5 over ~21 days, about a quote the consumer requested, after oral or written OK to text noted in the CRM) appropriately treated as informational, requiring prior express (not written) consent? Does the analysis change if the texts are sent automatically by field-service software?
3. Are **review requests** after a completed job informational (Type 2) rather than telemarketing?
4. We tell users to treat **rebooking/"your tune-up is due" texts** as marketing requiring prior express written consent, even when sent one at a time by hand. Is that conservative position sound, or overly strict in a way that should be explained differently?
5. Is our **sample written-consent checkbox** sufficient for prior express written consent (including E-SIGN), and for Florida's FTSA and Oklahoma's OTSA?
6. **Quiet hours:** we instruct 8 a.m.–8 p.m. recipient-local for all non-emergency texts. Accurate as a universal safe practice? Any state stricter?
7. **Frequency:** we instruct a maximum of 3 marketing messages per 24 hours per person. Accurate for the states that cap it?
8. **Opt-outs:** we instruct honoring any reasonable revocation immediately (≤10 business days), across all non-essential messages, with at most one confirmation text. Is this right given the FCC's 2024 revocation order, the delayed "revoke-all" provision and the **FCC's 2026 order (FCC 26-67, reported effective Nov 25, 2026)**? Should we change the wording now?
9. **EBR:** we tell users not to rely on the established-business-relationship exemption for texts. Correct framing?
10. **Record retention:** we recommend keeping consent records ≥5 years. Appropriate?
11. **Our own liability:** do the Terms (license, "your responsibilities," limitation of liability) adequately allocate responsibility for how buyers use the templates? Any additional disclaimers or placement needed?
12. **Affiliate program:** are our FTC Endorsement Guide disclosure requirements and prohibited-practices list adequate? Should partners (bookkeepers, consultants) be required to use specific disclosure wording with their clients?
13. **Canada:** we include a one-line CASL note. Should we restrict sales to the U.S. until the guidance covers Canada properly?

## Research notes (what we verified and how)
| Point | Status | Source checked |
|---|---|---|
| FCC "one-to-one consent" rule vacated, Jan 24, 2025 (*Insurance Marketing Coalition v. FCC*, 11th Cir.) | Confirmed, multiple law-firm sources | e.g. Morrison Foerster, Kelley Drye summaries |
| Revocation by "any reasonable means," honored within ≤10 business days, effective Apr 11, 2025 | Confirmed via secondary sources | ActiveProspect, Day Pitney summaries |
| "Revoke-all" provision delayed (reported to Jan 31, 2027) | Secondary sources only | econsent.org summary; **verify** |
| FCC 26-67 (Sept 30, 2026): businesses may designate exclusive revocation methods; reported effective Nov 25, 2026; FNPRM on shortening the 10-day window | **Secondary sources only.** The FCC site wasn't reachable from our research environment | FCC fact sheet (DOC-424844A1), CommLaw Group, Rosenberger Law summaries; **verify** |
| Quiet hours 8 p.m. in FL, MD, WA; 3-per-24-hour caps in FL, MD, NJ, OK | Vendor and secondary summaries | Klaviyo, JustCall summaries; **verify** |
| CTIA: conversational (implied), informational (express), promotional (express written) | Vendor summaries | Bandwidth, Infobip, SimpleTexting; **verify** against the CTIA document |
| Google: no incentives, no selective solicitation of positive reviews, no discouraging negative reviews, no staff review quotas | Google help pages | support.google.com/contributionpolicy/answer/7400114 |
| FTC Consumer Reviews and Testimonials Rule (16 CFR Part 465), effective Oct 21, 2024: bans sentiment-conditioned incentives and review suppression | FTC / Federal Register | federalregister.gov 2024-18519 |
| FTC Endorsement Guides: affiliates must disclose material connections clearly and conspicuously, near the recommendation | FTC "What People Are Asking" page and secondary summaries | ftc.gov endorsement guides FAQ |
| EBR periods (18 months purchase / 3 months inquiry) | From the regulation text, not re-verified this session | 47 CFR 64.1200(f)(5); **verify** |

*A legal-research database (Midpage) connected to this workspace was unavailable during research (account payment past due). Re-running the citations through it, or through counsel, is recommended.*

## Finding a reviewer
- Search "TCPA defense attorney" or ask your state bar's lawyer-referral service. Firms that advise SMS marketing platforms are a good fit.
- Ask for a **flat-fee review** of a ~25-page guide plus terms, with redlines. Send this packet and the PDFs.
- After review, update `products/src/starter/00-texting-rules.md` and rebuild (`ops/AUTOMATION.md`), then record the review date in `ops/LAUNCH-CHECKLIST.md`.
