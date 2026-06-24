# 💡 SAVED IDEA — "Data Liberation" / Compliance Archive for small UK firms leaving legacy software

*Status: PROMISING — to revisit. Captured 24 June 2026.*
*Emerged from the bottom-up gap hunt; pressure-tested live in conversation.*

---

## One-line pitch
**"I free small UK firms from the software bully — I extract their old records from the practice software they're leaving and hand them a clean, searchable, compliant archive they own, so they can finally cancel the expensive old system."**

---

## The pain (why anyone pays)
- Small UK accountancy / law / recruitment firms are locked into ageing practice software (IRIS, CCH, Sage, LEAP, Proclaim, Bullhorn, etc.).
- They're legally required to **keep records for 6–7 years** (HMRC for accountants; longer for solicitors).
- So even when they switch to a newer/cheaper system, they're **scared to cancel the old one** — because the old software is the only place their history lives. The vendor knows this and charges them to stay (lock-in = the vendor's retention weapon).
- Pain is a **painkiller, not a vitamin**: expensive (£3,500+/yr to stay), urgent (at switching moment), recurring (every firm that switches), and they can't fix it themselves.

## The buyer
- Owners/partners/practice managers at **3–50 person** UK firms.
- Universe: ~40,000+ UK accountancy practices, ~9,000+ law firms, thousands of recruitment agencies.
- They judge the work on **output** ("did my data come out, can I search it?"), NOT on the founder's credentials — so a 19-year-old with no track record can win. Age is invisible when the result is undeniable.

## The product
- A **separate, standalone, read-only archive** of the OLD records only.
- **NOT connected to their new software.** It's a frozen "museum" of history they must retain but rarely touch. This is deliberate — read-only + no integration = nothing fragile to break or maintain.
- Two data piles when a firm switches: (a) *active* data migrates into the new system [fragile, high-stakes — avoid early]; (b) the *historical tail* goes into the vault [safe, low-stakes — THIS is the wedge].

## Business model (evolved through hard questions)
- **Core revenue: one-off liberation fee, £1,500–£6,000 per firm** for the skilled extraction + clean-up work. *The money is in the WORK, not in holding data.*
- **Storage is a commodity — do NOT build the business on charging rent to hold files.** (A customer could DIY with Dropbox; "pay me to hold your files" just makes you a smaller bully with no moat. This was a key realisation.)
- **They self-host the vault** (their cloud / their server / their PC with backups) → *you hold nothing* → no custodian risk.
- **Recurring revenue comes from VOLUME + PARTNERSHIPS, not per-firm rent:**
  - Steady flow of new firms switching (one-off-per-customer, recurring-in-aggregate, like removals/conveyancers).
  - **Best channel: partner with the NEW software vendors** — migration friction is their #1 sales blocker; they refer you on every signup. Warm, repeatable, scalable, no data risk.

## Delivery
- **"Pre-built vault" deployed to the customer's own kit** (on-premise / local install). USB = the **installer/toolkit**, NOT the permanent home of the data (USBs die — data must live on their durable, backed-up system). Encrypt any USB that ever touches real data.
- **Build calmly at home, then deliver** — don't do the skilled parsing live on-site under pressure (until a format is bulletproof after ~20 reps).
- **Stage 1 (now): local, hands-on** — first ~10 clients, build trust, learn formats, get paid. *Doesn't scale (caps at driving distance) — that's fine for learning.*
- **Stage 2 (later): same vault, delivered remotely** — they upload an export, you send an installer / set up over screen-share → serve the whole UK. Same asset, bigger reach. This is the path to £1m.

## How it's built (tech reality)
- **Claude Code = build shop** (writes parsers, the vault app, deploy config). The **Claude API** powers the deployed product at runtime (separate, pay-per-token, but cheap — a migration is a bounded batch, pennies–pounds per firm).
- **Architecture: deterministic code does ~90% of parsing** (a legacy export has fixed structure — crack it once, reuse forever, £0/firm). **LLM handles only the fuzzy 10%** (undocumented fields, entity resolution like "J Smith Ltd" = "John Smith Limited"). This is cheaper, more reliable, and the per-system parser is the **compounding moat**.

## Security (because you become responsible for sensitive data)
- **Biggest win = don't hold the data** (self-host model removes ~90% of risk — you're not a honeypot).
- Stand on giants: deploy on **AWS/Azure** so infra security is theirs; never roll your own crypto; encryption in transit + at rest; proper auth + MFA; audit logs; encrypted backups.
- **Get ONE professional pen-test before real data touches it.** AI can confidently write *insecure* code; verify it.
- **Never claim "unhackable"** (red flag). Back residual risk with: **Ltd company** (~£50, shields personal assets), **cyber + professional-indemnity insurance**, **liability cap in contract**, **ICO registration** (~£40–60/yr), minimise + delete data fast.
- Optional advanced: **zero-knowledge / client-side encryption** (a breach yields gibberish). A v2 move.

## Competitive landscape (researched — honest)
- **Software vendors** (LEAP Transitions, Clio, TaxCalc, Access Legal): migrate data *into their own product* only — won't archive what you leave. Conflicted.
- **Enterprise legacy-archivers** (Archive360, AvenDATA, Arkivum, Stalis, RLDatix Galen, WellData): do exactly this job *but for NHS trusts / HMCTS / big corporates* — enterprise-priced, six-figure, sales-heavy.
- **IT-support shops** (GoodChoice IT, Cloud2Me): general IT/hosting migrations, not productised data archiving.
- **THE GAP:** the **small firm (3–50 people)** is stuck in the middle — too small for the enterprise archivers, abandoned by the conflicted vendors. "Real category, mis-aimed incumbents" = a winnable wedge. *Not empty space — but genuinely under-served at the small end.*

## Client acquisition — hunt the TRIGGER moment
Nobody wants "an archive" — they want it the moment they decide to leave. Hunt the triggers:
1. **Vendor price hikes** → whole cohorts leave at once (AccountingWeb threads erupt).
2. **Product end-of-life / discontinuation** → forced migration + forced archiving, with a deadline.
3. **PE roll-ups** raising prices → customers flee.
4. **Forum complaint threads** (AccountingWeb "Any Answers," r/uklaw, LegalFutures) → literal warm leads asking "how do I get my old data out?"
5. **Anyone who just signed a new system** → has the archive problem *right now*.

Channels: be the helpful "data person" in forums → direct outreach at trigger moments → partner with switching-advisors (IT support, consultants) → **🏆 partner with the new software vendors (best, repeatable, scalable).**

## Why it fits THIS founder (19, London, £10k, solo, no network, AI-native)
- ✅ Output-judged, not credential-gated (age invisible).
- ✅ Buyers self-identify (forum threads, trigger events).
- ✅ Low liability (read-only archive of their own data) vs. the high-trust compliance ideas (AML, CQC) that a 19-yo can't sell.
- ✅ Cash from day one (one-off fee), not a 12-month SaaS ramp.
- ✅ Founder's superpower (obsessive reverse-engineering of one messy format) IS the moat.
- ✅ Cheap to run; scales from local → UK-wide without a team.

## Open questions / next steps when we revisit
1. **Pick ONE source system to specialise in first** — ideally one with a LIVE trigger (a vendor mid-price-hike or sunsetting a product) so a whole cohort is migrating now. *(Next research task: find the live trigger.)*
2. Validate willingness-to-pay: confirm the £1.5–6k one-off price holds with 5 real firms.
3. Confirm the legal/GDPR handling of taking custody of data even temporarily (DPA template, ICO registration).
4. Build the **proof demo**: messy fake export → parsed → de-duplicated → searchable read-only vault, with encryption/auth/audit stubbed in.
5. Map the new-vendor partnership pitch (which replacement vendors have the worst migration friction = most motivated to refer you).
6. Decide Stage-1 geography (London/local first) and first 10 target firms.

---

*Cross-reference: this idea sits in the "vertical-software lock-in / data liberation" theme that scored 9/10 founder-fit in the gap hunt (`opportunity-analysis.md` and the gap-discovery workflow). Revisit alongside the workflow's verified survivors.*
