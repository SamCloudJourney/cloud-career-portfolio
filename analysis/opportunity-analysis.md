# Highest-Probability Online Businesses — Strategic Analysis

*Prepared for a 19-year-old UK founder · £10k capital · AI-native build capability · no network, no audience, no credentials*
*Date: 24 June 2026*

---

## 0. The brutal thesis (read this first)

Three uncomfortable truths set the frame for everything below:

**1. Coding is not your bottleneck — distribution and trust are.** You told me to assume AI coding is free. Correct. But that means *everyone* has free coding. The constraint that actually kills founders like you is **getting a stranger with a budget to pay you**, with no brand, no network, and no track record. Every idea must be judged primarily on: *can a nobody acquire paying customers here?*

**2. Most of your list is a graveyard of commoditising data terminals.** I researched the live market. The "intelligence platform" ideas you're most drawn to are already occupied by **funded incumbents racing to the bottom**:
   - **Planning data:** Barbour ABI, Glenigan, LandTech, Searchland, Nimbus, Planning Pipe — *and* new entrants like SiteLens at **£29/month** and PlanWire on API. The moat is already gone; it's a price war.
   - **Procurement/tender intelligence:** Stotles (£475/mo), Tussell (enterprise), Tracker Intelligence, PSIP (£199/mo). Multiple well-funded players.
   - **AI bid-writing:** **AutogenAI has raised ~$65m at a ~£1.4bn valuation with ~$36m ARR.** Plus mytender.io, AutoRFP, CleanTender, SwiftBid, bidtogether, RFP Quest. This is a knife-fight against people with 100× your capital.
   - **Grant finding:** Swoop, Grantify, GrantMatchr, Granter, GrantFinder.

   A pure "we aggregate public data and show it in a dashboard" product has **no defensibility** when AI makes scraping + structuring trivial *for your competitors too*. You'd be entering a commoditised market with a commodity product. That's the lowest-EV thing you can do.

**3. The winning shape is narrow.** The ideas that survive scrutiny share four traits:
   - **Budget-holding buyers** with acute, quantifiable pain (not "nice to have").
   - **A data or workflow moat that compounds** — something that gets *harder to copy the longer you run it*, not easier.
   - **The product does the work / produces the outcome**, rather than just displaying information.
   - **Being small, fast, and obsessive is an advantage**, not a handicap — a niche too small or too painful for the incumbents to bother with.

Everything that follows is optimised for **expected value**, not for what sounds impressive at a dinner party.

---

## Scoring methodology

Each idea scored 1–10 on your ten criteria. **"Competition" is scored so that 10 = wide-open / weak incumbents and 1 = brutal, well-funded knife-fight.** Weights reflect what actually drives EV for *your* situation:

| Criterion | Weight | Why |
|---|---|---|
| Probability of £1m ARR | **2.0** | This is the goal. Weighted highest. |
| Defensibility | 1.5 | A commodity at £1m ARR gets competed to zero. |
| Competition (10 = empty) | 1.5 | You can't out-spend incumbents; you must avoid them. |
| Probability of £100k ARR | 1.5 | Survival / proof the dog eats the food. |
| Founder-market fit | 1.0 | Obsession compounds; you'll outlast competitors. |
| Ease of starting | 1.0 | £10k and one person. |
| Revenue potential | 1.0 | Ceiling. |
| Speed to first revenue | 1.0 | Cash + morale + learning loop. |
| AI leverage | 0.75 | Necessary but no longer differentiating (everyone has it). |
| Probability of becoming large | 0.75 | Lottery ticket upside, deliberately under-weighted. |

Weighted score = Σ(score × weight) / 12.0. The scoring engine (`analysis/score.py`) computes this deterministically so the ranking is internally consistent rather than vibes.

---

## PART 1 — The opportunity landscape

I kept all 78 of your ideas in play and added 11 of my own. Rather than re-list yours, here's the **structural map** of where value actually is, with the market reality attached.

### Cluster A — Pure data/intelligence terminals (mostly traps)
Planning, tender, procurement, grant, public-filing, startup-funding trackers. **Verdict: avoid the crowded ones.** Public data + AI = zero moat; the incumbents have the same AI you do *plus* distribution. The *only* survivors here are niches the incumbents ignore because the data is too painful to assemble (see Cluster D).

### Cluster B — AI agents that *display* findings (weak)
"Research agent", "competitor monitoring", "prospecting agent". These are features, not companies. Easy to build, easy to clone, no buyer lock-in. Low defensibility scores throughout.

### Cluster C — Vertical software for a niche profession (decent, slow)
School ops, childcare, planning-consultant software, procurement workflow. Real retention and stickiness, but: **poor founder-market fit** (you have no relationship with head teachers or nursery managers), slow enterprise-ish sales, and you'd be guessing at a workflow you've never lived. Good businesses for *someone* — not obviously for you.

### Cluster D — Deal-flow & acquisition intelligence (your strongest zone)
Off-market deal origination, search-fund deal flow, small-business acquisition databases, roll-up scanners. **This is where founder-market fit, a real structural tailwind, weak/fragmented incumbents, and high buyer willingness-to-pay all line up.** UK research shows a massive succession wave — ~46,000 "exit-ready" UK targets identified in the search-fund/ETA ecosystem, with most *not* listed on any marketplace. The value isn't "a list" — it's *finding the businesses nobody else can see.* That's a research/pattern-recognition game, which is literally your edge.

### Cluster E — Energy / grid / infrastructure intelligence (your strongest *thematic* zone)
Grid connections, data-centre power, battery storage, solar, PPA intelligence. **Genuine structural boom** (AI data-centre power demand, electrification, grid-queue reform) with **budget-holding buyers** (developers, investors, EPCs, equipment suppliers, advisers) and **a hard data moat** — the data is messy and scattered enough that the £29/mo commoditisers won't touch it, and the giants think it's too small *for now*. Excellent founder-market fit with your infrastructure/defence/future-trends interests.

### Cluster F — Outcome-priced "done-for-you" services with an AI engine (fast cash, lower ceiling)
A niche bid agency, a planning-research service, a compliance-reporting service — *priced on the outcome*, powered by AI behind the scenes. **Fastest path to first revenue** and you learn the customer intimately, which de-risks a later software pivot. Lower long-run ceiling and you must avoid it depending on your personal brand.

### My 11 additions (the hidden / asymmetric ones)
1. **SME Deal Origination Engine** — off-market acquisition sourcing-as-a-service. *(Ranked #1.)*
2. **Data-Centre Site Origination Intelligence** — who's building where, land + power + planning + connection, sold to developers/investors. *(#4.)*
3. **Done-for-you Tender Agency, outcome-priced, single niche** — AI engine, human polish, paid on wins. *(#5.)*
4. **Regulated Compliance/Reporting Agent** (SECR, EPR packaging, building-safety) — recurring, sticky, deadline-driven.
5. **Vertical AI for planning consultants** — done-for-you research + draft reports as a service-then-software.
6. **AI Ops Copilot for a boring vertical** (surveying, EPC assessors, environmental consultants).
7. **Energy Procurement / PPA Intelligence.**
8. **Companies House Change-Signal Intelligence** — real-time corporate-event signals (director changes, charges, filings) as a feed.
9. **Council / Local-Gov Decision Monitoring** — planning + procurement + committee decisions for developers/lobbyists.
10. **AI equity research for under-covered UK small caps** — *strongest pure founder-market fit, but weak monetisation* (retail won't pay enough).
11. **Litigation / Claims / Funding Intelligence** — high value, high data-difficulty moat, slow.

---

## PART 2 — Full ranking (best → worst)

*Weighted score in brackets. Generated by `analysis/score.py`.*

| # | Score | Opportunity |
|---|---|---|
| 1 | 6.58 | **SME Deal Origination Engine (off-market sourcing-as-a-service)** |
| 2 | 6.29 | **Search Fund Deal Flow Platform** |
| 3 | 6.23 | **Grid / Energy Infrastructure Intelligence** |
| 4 | 6.06 | **Data-Centre Site Origination Intelligence** |
| 5 | 6.04 | **Done-for-you Tender Agency (outcome-priced, niche)** |
| 6 | 5.98 | **Small Business Acquisition Database** |
| 7 | 5.90 | **AI Acquisition Scout** |
| 8 | 5.85 | **Regulated Compliance/Reporting Agent** |
| 9 | 5.81 | **Vertical AI for Planning Consultants (DFY)** |
| 10 | 5.71 | **AI Ops Copilot for a Boring Vertical** |
| 11 | 5.58 | Planning Consultant Software |
| 12 | 5.54 | Infrastructure Project Intelligence |
| 13 | 5.54 | Local Monopoly Finder |
| 14 | 5.52 | Industry Roll-Up Scanner |
| 15 | 5.52 | Bloomberg for Infrastructure |
| 16 | 5.44 | Data Centre Tracker |
| 17 | 5.42 | Energy Procurement / PPA Intelligence |
| 18 | 5.33 | Companies House Change-Signal Intelligence |
| 19 | 5.33 | Council / Local-Gov Decision Monitoring |
| 20 | 5.25 | Crunchbase for Infrastructure |
| 21 | 5.17 | AI Equity Research for under-covered UK small caps |
| 22 | 5.12 | SaaS Acquisition Scanner |
| 23 | 5.12 | Litigation / Claims / Funding Intelligence |
| 24 | 5.04 | Battery Storage Tracker |
| 25 | 5.04 | AI Planning Agent |
| 26 | 4.94 | Website Acquisition Scanner |
| 27 | 4.92 | Solar Farm Tracker |
| 28 | 4.92 | Bloomberg for Defence Suppliers |
| 29 | 4.88 | Defence Supplier Search Engine |
| 30 | 4.83 | AI Equity Analyst |
| 31 | 4.75 | AI Due Diligence Agent |
| 32 | 4.75 | AI M&A Agent |
| 33 | 4.75 | School Staffing Platform |
| 34 | 4.73 | Defence Supply Chain Intelligence |
| 35 | 4.73 | Acquisition Search Engine |
| 36 | 4.71 | Executive Movement Intelligence |
| 37 | 4.71 | Tender Management Platform |
| 38 | 4.71 | Procurement Workflow Platform |
| 39 | 4.71 | Infrastructure Search Engine |
| 40 | 4.69 | School Operations Platform |
| 41 | 4.69 | Childcare Software |
| 42 | 4.67 | AI Market Mapping Agent |
| 43 | 4.67 | AI Startup Scout |
| 44 | 4.62 | Alternative Data Platform |
| 45 | 4.60 | Industry Intelligence Terminal |
| 46 | 4.58 | AI Supplier Discovery Agent |
| 47 | 4.56 | Public Filing Intelligence |
| 48 | 4.56 | PitchBook for Retail Investors |
| 49 | 4.54 | AI Tender Agent |
| 50 | 4.52 | Supplier Intelligence Database |
| 51 | 4.50 | AI Procurement Agent |
| 52 | 4.48 | Vertical CRM |
| 53 | 4.46 | Tender Intelligence |
| 54 | 4.44 | M&A Intelligence |
| 55 | 4.42 | Future Companies Database |
| 56 | 4.38 | Planning Application Intelligence |
| 57 | 4.35 | Procurement Intelligence |
| 58 | 4.35 | Government Contract Intelligence |
| 59 | 4.35 | AI Competitor Monitoring Agent |
| 60 | 4.31 | Private Company Intelligence |
| 61 | 4.31 | Property Research Platform |
| 62 | 4.31 | Consultancy Operating System |
| 63 | 4.29 | Housing Development Tracker |
| 64 | 4.29 | Autonomous Research Agent |
| 65 | 4.25 | Regeneration Project Tracker |
| 66 | 4.23 | Bloomberg for Planning Applications |
| 67 | 4.23 | Bloomberg for Procurement |
| 68 | 3.94 | AI-Powered Opportunity Radar |
| 69 | 3.92 | Grant Intelligence |
| 70 | 3.92 | Public Sector Spend Tracker |
| 71 | 3.88 | Startup Funding Tracker |
| 72 | 3.85 | AI Prospecting Agent |
| 73 | 3.83 | Opportunity Operating System |
| 74 | 3.81 | AI Grant Agent |
| 75 | 3.79 | Business Opportunity Search Engine |
| 76 | 3.73 | Planning Search Engine |
| 77 | 3.60 | Tender Search Engine |
| 78 | 3.60 | Procurement Search Engine |

**Pattern to notice:** the bottom of the table is dominated by **pure search engines and single-dataset trackers** in crowded markets. The top is dominated by **deal-flow / acquisition intelligence, energy-infrastructure intelligence, and outcome-priced services**. The market did the sorting; the scores just made it legible.

---

## PART 3 — Top 10 / 25 / 50

**Top 10**
1. SME Deal Origination Engine
2. Search Fund Deal Flow Platform
3. Grid / Energy Infrastructure Intelligence
4. Data-Centre Site Origination Intelligence
5. Done-for-you Tender Agency (outcome-priced, niche)
6. Small Business Acquisition Database
7. AI Acquisition Scout
8. Regulated Compliance/Reporting Agent
9. Vertical AI for Planning Consultants (DFY)
10. AI Ops Copilot for a Boring Vertical

**Top 25** add: 11 Planning Consultant Software · 12 Infrastructure Project Intelligence · 13 Local Monopoly Finder · 14 Industry Roll-Up Scanner · 15 Bloomberg for Infrastructure · 16 Data Centre Tracker · 17 Energy Procurement/PPA Intelligence · 18 Companies House Change-Signal Intelligence · 19 Council/Local-Gov Decision Monitoring · 20 Crunchbase for Infrastructure · 21 AI Equity Research (UK small caps) · 22 SaaS Acquisition Scanner · 23 Litigation/Claims/Funding Intelligence · 24 Battery Storage Tracker · 25 AI Planning Agent.

**Top 50** add (26–50): Website Acquisition Scanner · Solar Farm Tracker · Bloomberg for Defence Suppliers · Defence Supplier Search Engine · AI Equity Analyst · AI Due Diligence Agent · AI M&A Agent · School Staffing Platform · Defence Supply Chain Intelligence · Acquisition Search Engine · Executive Movement Intelligence · Tender Management Platform · Procurement Workflow Platform · Infrastructure Search Engine · School Operations Platform · Childcare Software · AI Market Mapping Agent · AI Startup Scout · Alternative Data Platform · Industry Intelligence Terminal · AI Supplier Discovery Agent · Public Filing Intelligence · PitchBook for Retail Investors · AI Tender Agent · Supplier Intelligence Database.

*(51–78 are the commoditised trackers, search engines, and feature-not-company agents. Treat the whole bottom third as "do not start.")*

---

## PART 4 — Top 10 deep dives

> Format per idea: **why it ranks · market · customer · revenue model · MVP · technical difficulty · time to launch · time to first revenue · major risks · competitive landscape · roadmap.**

### 1. SME Deal Origination Engine *(off-market acquisition sourcing-as-a-service)*
- **Why it ranks #1:** Rare alignment of (a) a real structural tailwind — the baby-boomer business-succession wave, tens of thousands of profitable UK SMEs with no succession plan; (b) buyers with *enormous* willingness to pay — a searcher, micro-PE fund, family office or strategic acquirer will pay handsomely for proprietary, *off-market* deal flow because one closed deal is worth six-to-seven figures to them; (c) **a moat that is research, not code** — finding owners who haven't decided to sell yet is a pattern-recognition game, your exact strength; (d) fragmented, weak incumbents (brokers are offline and conflicted; data tools like the US "Clearly Acquired"/"Aligned IQ" haven't nailed the UK off-market layer).
- **Market:** UK lower-mid-market M&A + the booming ETA/search-fund and SME-PE space; thousands of active acquirers, each with budget.
- **Customer:** Searchers, self-funded acquirers, small PE/roll-up funds, family offices, corporate development teams, M&A advisers.
- **Revenue model:** Tiered subscription for the data/feed (£200–£2,000/mo) **+ success/introduction fee on closed deals** (the asymmetric upside). Start with subscription for cash-flow predictability.
- **MVP:** Pick *one sector × one region* (e.g. UK HVAC/plumbing firms, or independent opticians, or fire-safety/compliance contractors). Build a structured database that fuses Companies House (financials, director ages, charges, filing patterns), website/online signals, and "succession-risk" scoring (owner age, no obvious successor, declining filing activity, etc.). Deliver a weekly shortlist of *off-market* targets matching a buyer's thesis, with a one-page AI dossier each.
- **Technical difficulty:** Medium. The hard part is **signal quality**, not engineering — turning messy public data into a "this owner will likely sell in 18 months" score.
- **Time to launch:** 4–8 weeks to a usable single-sector MVP.
- **Time to first revenue:** 4–10 weeks (you can pre-sell the first cohort before the product is "done").
- **Major risks:** (1) Proving sourcing ROI is lumpy — deals are slow. Mitigate by charging subscription, not just success fees. (2) Credibility as a 19-year-old selling to sophisticated buyers — mitigate by letting the *output* sell (a free sample list of 10 genuinely off-market targets is undeniable). (3) Data/PECR/GDPR care around outreach — keep it B2B and compliant.
- **Competitive landscape:** US incumbents exist but the UK off-market layer is under-served; brokers are the real "competitor" and they're weak, conflicted, and offline.
- **Roadmap:** M1–2 one-sector MVP + 5 design-partner acquirers → M3–4 prove off-market hit-rate, add success fees → M5–8 expand sectors, productise the dossier agent → M9–12 multi-sector feed + the optional kicker: *use your own engine to acquire (or broker) a business yourself.*

### 2. Search Fund Deal Flow Platform
- **Why:** Same tailwind as #1, narrower ICP (search funds specifically). Slightly smaller buyer universe → marginally lower score, but the buyers are even more sophisticated and underserved.
- **Market/customer:** Global search-fund community (growing fast), UK + diaspora.
- **Revenue:** Subscription £300–£1,500/mo + deal success fees.
- **MVP:** Thesis-matching deal feed + outreach automation for searchers.
- **Difficulty:** Medium. **Launch:** 6–10 wks. **First revenue:** 6–12 wks.
- **Risks:** Niche size; community is relationship-driven (you must earn trust in the searcher community — but it's reachable online via Twitter/LinkedIn/forums, no "network" required).
- **Landscape:** Insights CRM, Clearly Acquired, Aligned IQ, Searcher.com — none own UK off-market. **Roadmap:** essentially a focused variant of #1.

### 3. Grid / Energy Infrastructure Intelligence
- **Why:** The single best *thematic* fit for you and a genuine multi-decade boom (AI data-centre power demand, electrification, grid-queue reform). **A hard data moat** — connection queues, REPD, TEC registers, DNO data, planning, land — is painful enough to assemble that commoditisers stay out and giants haven't bothered *yet*.
- **Market:** Renewables developers, battery/solar/data-centre developers, investors/funds, EPCs, equipment suppliers, advisers — all with real budgets.
- **Customer:** Origination/development teams and infrastructure investors.
- **Revenue:** £500–£5,000/mo seats; enterprise data licences higher.
- **MVP:** A single high-value lens — e.g. **"every battery-storage / data-centre project in the UK: site, capacity, planning status, grid-connection status, owner, stage"** — updated weekly with alerts.
- **Difficulty:** Medium-high (data assembly). **Launch:** 8–12 wks. **First revenue:** 10–16 wks (longer, enterprise-ish sales).
- **Risks:** Slower sales cycle; you have no energy network (mitigate via obsessive public-domain mastery — your strength); incumbents (e.g. infrastructure data providers) moving down-market.
- **Landscape:** Fragmented; no dominant UK-native "Bloomberg for the energy buildout." **Roadmap:** one asset class → adjacent asset classes → analytics/forecasting → enterprise data licensing.

### 4. Data-Centre Site Origination Intelligence
- **Why:** The hottest sub-vertical of #3 — AI is driving a land-and-power land-grab. Highest "competition = wide open" score (8). Buyers (hyperscalers' partners, developers, land agents, investors) have *vast* budgets.
- **Market:** Smaller buyer count but huge deal sizes.
- **Revenue:** High-ticket data licences / retainers (£2k–£10k+/mo).
- **MVP:** Map of viable UK sites by land availability + power/grid headroom + planning + ownership; flag emerging opportunities.
- **Difficulty:** High (power/grid data). **Launch:** 10–14 wks. **First revenue:** 12–20 wks.
- **Risks:** Concentrated buyer base; long sales; deep domain learning curve. **Landscape:** nascent. **Roadmap:** UK → expand criteria → advisory/data hybrid.

### 5. Done-for-you Tender Agency (outcome-priced, single niche)
- **Why:** **Fastest cash** and fastest learning. You don't compete with AutogenAI's software — you sell a *result* (won contracts) to SMEs in one niche, with AI doing 80% of the drafting behind the scenes. 62% of bid teams already use AI; SMEs don't have bid teams — that's your wedge.
- **Market:** Huge — 100k+ UK public contract notices/year; millions of SMEs locked out of bidding.
- **Customer:** SMEs in one vertical (e.g. cleaning, care, facilities, IT-managed-services) chasing public contracts.
- **Revenue:** Retainer + win bonus (outcome pricing). Clear ROI.
- **MVP:** You + Claude Code pipeline: find relevant tenders → qualify → draft compliant responses → human polish. Literally win one contract for one client.
- **Difficulty:** Low-medium. **Launch:** 2–4 wks. **First revenue:** 2–6 wks.
- **Risks:** Service, not software → lower ceiling and *must not* become dependent on your personal brand (mitigate by productising into a repeatable agency/then-software). Quality bar for compliant bids is real.
- **Landscape:** Crowded in *software*, far less so in *outcome-priced single-niche service*. **Roadmap:** win-rate proof → productised agency → SaaS layer for the niche → adjacent niches.

### 6. Small Business Acquisition Database
- **Why:** The "data product" sibling of #1 — broader, more self-serve, lower ACV but faster volume. Sells to the same booming acquirer base.
- **Revenue:** £49–£499/mo self-serve subscriptions. **MVP:** searchable, enriched, succession-scored UK SME database. **Difficulty:** Medium. **Launch:** 6–10 wks. **First revenue:** 6–12 wks.
- **Risks:** Lower defensibility than bespoke origination; commoditisation pressure. **Landscape:** brokers + nascent data tools. **Roadmap:** data → alerts → workflow → success fees (converges toward #1).

### 7. AI Acquisition Scout
- **Why:** The agent that *operationalises* #1/#6 — runs a buyer's thesis continuously and surfaces+dossiers targets. Best as a feature/tier of the above, not standalone.
- **Revenue:** Add-on seat. **MVP:** thesis-in → ranked targets + dossiers out. **Difficulty:** Medium. **Launch:** 6–10 wks. **First revenue:** with #1.
- **Risks:** Thin as a standalone (cloneable). **Roadmap:** bundle into the origination engine.

### 8. Regulated Compliance / Reporting Agent
- **Why:** Sticky, recurring, deadline-driven, and **regulation = a moat that competitors must also climb**. Boring on purpose (low competition, high willingness to pay).
- **Market:** Any UK firm above a reporting threshold (SECR energy/carbon, EPR packaging, building-safety, ESG/CSRD-adjacent).
- **Customer:** Finance/ops/compliance leads at mid-market firms (or the consultants who serve them).
- **Revenue:** £200–£2,000/mo per firm; annual cycle. **MVP:** pick *one* regime; ingest data → produce the compliant report/submission.
- **Difficulty:** Medium (domain accuracy is the moat). **Launch:** 8–12 wks. **First revenue:** 8–14 wks.
- **Risks:** Regulatory accuracy liability; regime change. **Landscape:** legacy consultants + spreadsheets — weak, beatable. **Roadmap:** one regime → adjacent regimes → become the "compliance OS" for a vertical.

### 9. Vertical AI for Planning Consultants (done-for-you)
- **Why:** Planning *consultants* are a budget-holding, under-served professional buyer (vs. the over-crowded planning-*data* market). Sell them research + draft reports as a service that becomes software.
- **Market:** Thousands of UK planning consultancies + property developers.
- **Revenue:** Per-report or retainer → seat-based SaaS. **MVP:** feed a site → AI produces a planning-research pack / draft statement. **Difficulty:** Medium. **Launch:** 6–10 wks. **First revenue:** 6–12 wks.
- **Risks:** You don't know the workflow — must co-build with 2–3 design partners. **Landscape:** data tools crowded, *workflow AI for the consultant* far less so. **Roadmap:** service → embedded software → expand to allied property pros.

### 10. AI Ops Copilot for a Boring Vertical
- **Why:** The pure "vertical AI captures labour spend" thesis (construction copilots like Trunk Tools/Togal show the pattern). High ceiling, sticky, but **weakest founder-market fit** for you — you'd be entering a trade you don't know.
- **Market/customer:** A specific trade — surveyors, EPC assessors, environmental consultants, etc.
- **Revenue:** Seat-based SaaS £100–£1,000/seat/mo. **MVP:** automate the single most painful document/report task in that trade. **Difficulty:** Medium-high. **Launch:** 10–14 wks. **First revenue:** 10–16 wks.
- **Risks:** Domain access; you need design partners who'll teach you the workflow. **Landscape:** under-served per-niche. **Roadmap:** one task → adjacent tasks → vertical platform.

---

## PART 5 — The single best opportunity & your next 12 months

### The pick: **SME Deal Origination Engine** — a data-driven, off-market acquisition-sourcing product, started in **one sector**.
### The strong alternative (if you want the *thematic* dream): **Grid / Energy Infrastructure Intelligence.**

**Why the deal-origination engine wins for *you specifically*, brutally:**

- **It plays to your only real edges.** You have no network, no brand, no credentials, no capital advantage. What you *do* have is obsessive research, pattern recognition, and free AI. Off-market deal origination is *literally a research-and-pattern-recognition business*. The moat is "can you find the seller nobody else found?" — not "can you raise more money than AutogenAI?" (you can't).
- **The buyer pays a lot and is reachable by a nobody.** A searcher or micro-PE buyer judges you on one thing: *did you hand me a real, off-market, on-thesis target?* A 19-year-old with a great list beats a 50-year-old broker with a bad one. Your age is invisible when the output is undeniable. You can win your first customers with a **free sample list** — no warm intro required.
- **The tailwind is real and durable.** The succession wave runs for a decade-plus. You are not betting on a fad.
- **It compounds.** Every week you run it, your succession-signal model, your sector knowledge, and your relationships with acquirers get better — and *harder to copy*. That's the opposite of a £29/mo planning dashboard.
- **The side-effect is a free education in the exact thing you're curious about** — investing, markets, business quality, deal-making. In 12 months you'll understand SME acquisition better than 99% of people, which opens doors (advisory, your own search, a fund) even if the product itself plateaus.
- **It dodges every one of your constraints:** no big funding, no team, no licence, no industry connections needed to *start*, and it does **not** depend on personal branding (the data does the selling).

**Why not the others, bluntly:**
- *Planning/tender/procurement/grant intelligence (most of your list):* commoditised, funded incumbents, price war. **Don't.**
- *AI bid-writing:* you'd be a flea fighting a £1.4bn elephant. **Don't.**
- *AI equity research for retail (your highest pure passion-fit):* lovely fit, **but retail investors won't pay enough** and you'd drift toward needing an audience/personal brand — a constraint you explicitly ruled out. Keep it as a hobby/marketing channel, not the business.
- *Grid/energy intelligence:* genuinely excellent and arguably higher *ceiling* — pick this instead **if** you have the patience for slower, enterprise-style sales and want to go deep on infrastructure. It's #3 for a reason. The only thing keeping it behind deal-origination is *speed and accessibility of first revenue for a no-network founder*. If anything in your gut pulls hard toward energy, switch — the EV gap is small and founder obsession breaks ties.

### What I'd do in the next 12 months if I were you

**Months 0–1 — Choose the wedge and pre-sell before building.**
- Pick **one sector × one region** where (a) lots of owner-operated SMEs, (b) ageing owners, (c) active acquirers exist. Good candidates: HVAC/plumbing/electrical contractors, fire & security, dental/optical practices, accountancy/bookkeeping firms, MSP/IT support, environmental/compliance services.
- Manually build a **proof list of 25 genuinely off-market targets** in that niche using Companies House + web signals. Do it by hand first — *feel* the signal before you automate it.
- Take that list to 20 acquirers (searchers, small PE, roll-ups — all findable on LinkedIn/Twitter/SearchFunder, no network needed) and offer a free sample. Goal: **3 design partners** who say "I'd pay for this."

**Months 1–3 — Build the v1 engine and get to first revenue.**
- With Claude Code, build the pipeline: Companies House ingestion → enrichment → **succession-risk scoring** → weekly thesis-matched shortlist → one-page AI dossier per target.
- Charge from week one. Subscription (£250–£750/mo) to start; layer success fees once trust exists. **Target: £2–4k MRR by end of M3.** First revenue should land inside 6–10 weeks.

**Months 3–6 — Prove the off-market hit-rate and tighten the moat.**
- Track the metric that matters: *of the targets we surfaced, how many entered a real conversation / agreed to sell?* That number is your entire pitch.
- Improve scoring with every outcome (this is your compounding moat). Add outreach automation (compliant, B2B). **Target: £8–12k MRR, 15–25 paying acquirers.**

**Months 6–9 — Expand sectors and productise the agent.**
- Add 2–3 adjacent sectors using the same engine. Turn the dossier generation into a polished "AI Acquisition Scout" tier. Introduce success-fee deals. **Target: £20–30k MRR.**

**Months 9–12 — Multi-sector feed + the asymmetric kicker.**
- Become the default off-market deal source for UK lower-mid-market acquirers in your sectors. Hit **£40k+ MRR (~£500k ARR run-rate), on track for £1m within ~18–24 months.**
- The kicker: you now have proprietary visibility into the best-quality, genuinely-for-sale small businesses in the country. *Use your own engine to broker or acquire one yourself* (with partners' capital). That optionality — the ability to become a principal, not just a vendor — is worth more than the SaaS multiple.

### The honest expected-value statement
Most founders fail; you probably will too on your first serious attempt — that's the base rate, not a comment on you. The point of this pick is that it **fails cheaply and teaches expensively**: low cost to start, fast feedback, and even the "failure" case leaves you with rare expertise in SME acquisition and a network of acquirer relationships. That asymmetry — limited downside, compounding upside, education either way — is the whole game at 19. **Pick one wedge this week. Build the proof list by hand. Put it in front of 20 buyers before you write production code.** The bottleneck is not the build. It never was.

---

*Appendix: scoring model and all sub-scores in `analysis/score.py` — run `python3 analysis/score.py` to reproduce the ranking.*
*Sources consulted: SiteLens/PlanWire/Crucible (planning-data market & pricing); PSIP/Stotles/Tussell (procurement intelligence & pricing); TechCrunch/VentureBeat/GetLatka/Tracxn (AutogenAI funding & ARR); Clearly Acquired/Searcher Insights/Aligned IQ/ExitRadar (UK succession & deal-sourcing); Bessemer/NEA/Qubit Capital (vertical-AI thesis); GOV.UK Defence Industrial Strategy 2025 & Tussell (defence SME spend); Swoop/Grantify/GrantMatchr (grants market).*
