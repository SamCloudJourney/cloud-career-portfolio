# Smart-Money Intelligence Map: Detecting Insider, Director & Institutional Accumulation Across Global Equities

> Research compiled 2026-06-16. Strictly public-information design. Confidence tags: **HIGH** = primary source / multiple corroboration; **MED** = single reputable source; **LOW/FLAG** = unverified, contested, or vendor-marketing claim. Contested academic claims are flagged explicitly throughout.

---

## 1. Executive Summary

**The thesis.** Across four decades of academic evidence, one finding is near-universal: insider *purchases* predict positive abnormal returns (~6–10%/yr in the strongest specifications), while insider *sales* carry little or no signal. The durable edge concentrates in (a) **open-market cash purchases** (US Form 4 code **P**), (b) **"opportunistic" / non-routine** insiders, (c) **clusters** of multiple insiders buying in a short window (~2× the return of solitary buys), and (d) **smaller, low-coverage firms** — though the small-firm effect is method-dependent and disputed (Jeng-Metrick-Zeckhauser find it insignificant).

**The opportunity & the trap.** The signal is real but **capacity- and cost-constrained**: net-of-cost, large-cap, size-capped profitability for outsiders is genuinely contested. The engine's job is therefore not "detect insider buying" — that is commoditised — but to *filter ruthlessly* for the high-conviction subset and *enrich* it with context (valuation, drawdown, dilution risk, cluster, role) so that only the top few signals per week ever generate an alert.

**Global structure.** The US is a single-source firehose (SEC EDGAR, free, structured, real-time-ish). Europe is fragmented across ~20+ national regulators/exchanges under EU MAR Article 19 — same legal concept (PDMR "managers' transactions," 3-business-day deadline, €5k de minimis), wildly different access (regulator-hosted vs exchange-hosted vs private storage; only the Netherlands/AFM offers confirmed structured CSV/XML export). The UK's DTR 3%+1% major-holdings threshold is the most sensitive early-accumulation tripwire in the world.

**Build recommendation.** Start US-only on EDGAR (free, best structured data, the 10b5-1 checkbox is the single most powerful noise filter post-2023). Add the UK (RNS via Investegate) next. Buy a European feed (InsiderScreener ~€25–85/mo, or InsiderPulse) rather than scraping 9 regulators. Layer 13D/activist filings as the high-conviction institutional signal; treat 13F as late/stale context only. Score 0–100, alert only above a high threshold, and exclude the long tail of grants/options/tax/DRIP/microcap noise.

---

## 2. Best Data Sources by Region

### United States — the gold standard, free
- **SEC EDGAR** is the single authoritative source and it is free, structured, and near-real-time. Forms **3/4/5** (insider ownership), **144** (proposed sales, electronic since Apr 2023), **SC 13D/13G** (5% holders), **13F-HR** (institutions), **Form D** (private placements), **8-K** (events/raises/buybacks).
- Access: **EDGAR Full-Text Search** (`efts.sec.gov/LATEST/search-index?q=…&forms=4`), per-company & market-wide **Atom/RSS** feeds, `data.sec.gov` JSON REST APIs, daily/quarterly **full-index**, and the raw **Form 4 XML** inside each filing (carries `transactionCode`, shares, price, and the **Rule 10b5-1 checkbox**). Rules: **≤10 requests/sec** and a **declared User-Agent** are mandatory.
- Free aggregators (US-only): **OpenInsider** (best free Form-4 screener with cluster/CEO filters), **Quiver Quantitative**, **Fintel**, **Finviz**.

### United Kingdom — best free RNS access in the world
- Disclosures are **PDMR notifications** (UK MAR Art. 19; 3-business-day deadline; ~£/€5k de minimis) and **TR-1 major holdings** (3% then each 1% — the earliest tripwire globally), published via **RNS**.
- **Investegate** (investegate.co.uk) — free, comprehensive RNS archive; cleanest scrape target; the best free starting point. **London South East** (lse.co.uk/rns) has a pre-built director-dealings filter (anti-bot/403 on scrape). Official **LSEG RNS Data Feed** (REST + websocket, `rns-distribution.com`) is authoritative/low-latency but enterprise-priced.

### Europe (EU/EEA + Switzerland) — fragmented; buy don't scrape
| Country | Hosted at | Portal | Structured export? |
|---|---|---|---|
| Germany | Regulator (BaFin) | portal.mvp.bafin.de Directors' Dealings | Browse-only (no API/CSV found) |
| Sweden | Regulator (FI) | marknadssok.fi.se Insynsregistret | **CSV/Excel export** (best-in-class) |
| France | Regulator (AMF) | bdif.amf-france.org (BDIF) | PDFs + RSS; structured only via 3rd-party |
| Netherlands | Regulator (AFM) | afm.nl MAR19 register | **CSV + XML export** (only confirmed full export) |
| Italy | Private CONSOB-authorised storage | emarketstorage.com, 1info.it | PDF download, no API |
| Denmark | Regulator (Finanstilsynet OAM) | oam.finanstilsynet.dk | Export/API unverified |
| Norway | Exchange (Euronext Oslo Børs) | newsweb.oslobors.no | JS SPA; consumer API unverified |
| Finland | Exchange (Nasdaq Helsinki) | Nasdaq Helsinki announcements | FIN-FSA has no public DB |
| Switzerland | Exchange SRO (SIX/SER) | ser-ag.com Management Transactions | Scrape-only |

- **Structural takeaway:** hosting entity varies (regulator vs exchange vs private storage). Sweden (CSV) and Netherlands (CSV/XML) are the most data-friendly; the rest need scraping or a vendor.
- **Pan-European feeds (recommended over DIY):** **2iQ Research** (institutional gold standard, ~50 countries, REST API, enterprise pricing), **InsiderScreener** (~16 markets, REST API ~€25–85/mo — best prosumer option), **InsiderPulse** (8 EU markets, sources BaFin/AMF/FCA/AFM/Nasdaq Nordic directly, has API), **Smart Insider** (institutional, 60+ countries, API/SFTP/Snowflake).

### Institutional (global)
- **EDGAR** for 13F / 13D / 13G; **13F.info**, **HedgeFollow**, **WhaleWisdom** (free tier + ~$300/yr API), **Fintel**, **sec-api.io** (dedicated 13D/G API). UK **TR-1** and EU **Transparency Directive** major-holdings (5%, varies) via RNS / national regulators.

---

## 3. Signal Taxonomy

### A. Core insider transactions (US Form 4 codes — the foundation)
**Only Table I code "P" is a genuine open-market, own-cash conviction BUY.** Everything else is compensation, tax, derivative mechanics, or admin.

| Code | Meaning | Signal |
|---|---|---|
| **P** | Open-market / private **purchase** | **HIGHEST — core buy signal** |
| **S** | Open-market / private sale | Bearish-ish but noisy (liquidity/diversification/tax) |
| **A** | Grant / award / other acquisition | Compensation — **exclude** |
| **M** | Exercise/conversion of derivative | Option exercise — **exclude** |
| **F** | Shares withheld for exercise price / tax | Tax/admin — **exclude** |
| **G** | Bona fide gift | No market trade — **exclude** |
| **X** | Exercise of in/at-the-money derivative | Comp mechanics — **exclude** |
| **C** | Conversion of derivative | Admin — **exclude** |
| **D, W, K, L, Z, U, J, V, I, O, H, E** | Disposition to issuer / inheritance / swap / small / voting-trust / tender / catch-all / modifier / etc. | Admin or edge cases — exclude or manual-review |

> Beware mixed filings: a single Form 4 often bundles **M (exercise) + F (tax) + S (sale)** — naive summing mislabels them. Parse per-row.

### B. The "real buying" filter across jurisdictions
- **US:** code P, ownership "D" (direct) or "I" (indirect via trust/LLC), **10b5-1 checkbox NOT checked** (discretionary). The 10b5-1 checkbox (mandatory since 2023) is the single best automated noise filter.
- **UK/EU RNS phrasing — REAL buying:** "purchase of ordinary shares," "market purchase," "acquisition of shares," "beneficial holding increased."
- **UK/EU RNS phrasing — NOISE:** LTIP vesting, option exercise, SAYE/Sharesave, SIP, scrip/bonus shares, DRIP, "shares withheld to cover tax," RSU vesting, "awarded under the … Plan," nominee-to-nominee transfers ("no change in beneficial ownership").
- **MAR vocabulary caveat:** the binding "Nature of transaction" field maps to the closed category list in Commission Delegated Reg (EU) 2016/522 **Art. 10(2)**. The bare code **"Acquisition" is broad** — ESMA confirms it also covers **gifts and inheritances**. So always read it together with (a) **place** (on-venue MIC vs "outside a trading venue"), (b) **price** (nil/nominal = grant/scrip/award, not a buy), and (c) whether it is **"linked to a share-option programme."** The cleanest "informed buying" config = Acquisition + on-venue + non-nil cash price + senior insider + clustered.

### C. Institutional signals (early → late)
- **EARLY / high-conviction:** new **13D** (active intent, ≤5 business days after crossing 5%), **13D Item 4** activist language (board nomination, strategic alternatives, going-private), **13G→13D conversion**, small/concentrated-fund *new* position.
- **LATE / low-info:** large add to an already-public 13F position; widely-reported "whale" 13F (45-day stale, crowded, arbitraged).

### D. Alternative accumulation signals (evidence-graded)
| Signal | Evidence | How to detect |
|---|---|---|
| **Cluster buying** (≥3 distinct insiders, short window) | **HIGH.** Alldredge-Blank: 2.1% vs 1.2%/mo; Kang-Kim-Wang: 3.8% vs 2.0% over 21 days (~2×) | Form 4 code P, dedupe by CIK, 7–15d rolling window |
| **Opportunistic (non-routine) insiders** | **HIGH.** Cohen-Malloy-Pomorski: 82 bps/mo VW; routine ≈ 0 | Flag insiders who break their calendar pattern |
| **Founder / family accumulation via holdco/trust** | **HIGH** (Anderson-Reeb; Villalonga-Amit founder-CEO premium) | Form 4 ownership "I" + footnote/"By:" line → vehicle-to-insider map; 13D/G Item 2 + group rule |
| **Insider participation in PIPEs / private placements** | **HIGH** (Krishnamurthy et al.; Floros et al. — certification flips the negative base rate positive) | Match Form D / 8-K Item 3.02 raise to Form 4 acquisitions at deal price; check S-1/S-3 selling-holder list |
| **Insider take-up in rights issues / discounted placings** | **MED** (insiders net buyers around placings, net sellers around rights issues) | UK RNS placing/subscription + PDMR; US 8-K/424B + Form 4 |
| **Buybacks after drawdowns** | **HIGH cross-section** (ILV +12%/4yr, value names +45%; ASR 7d-CAR ~2.0% vs OMR ~0.7%); long-run drift contested (Fama) | 8-K (auth) + Item 703 10-Q/10-K table (execution); SC TO-I (tenders); ASR in MD&A |
| **Strategic investor / supplier-customer equity stake** | **HIGH when bundled with product-market/tech relationship** (Allen-Phillips; Chan et al. +0.6–0.8%); raw CVC weak/conditional | 13D (operating-co filer), 8-K Item 1.01, Form D |
| **Sovereign wealth / govt-backed stake** | Announcement **reliably +~2.1%** (Kotter-Lel), amplified by transparency; long-run contested ("SWF discount", passivity drag) | 13D/13G by SWF vehicle (GIC, Temasek, ADIA, Norges/NBIM, PIF…); 8-K; Form D |
| **Insider buying vs short-seller disagreement** | **MED-HIGH** (Wang-Zheng: +1.95% next-qtr when insiders buy into a short spike; shorts then reverse) — but **squeeze-reversal caution** (Stice-Lawrence: post-attack pops often fully reverse) | Code-P buys + elevated short interest / activist-short report date |
| **"Contradictory" buys after earnings miss** | **HIGH** (Dargenidou et al.: buys before negative surprises are unusually informative, speed PEAD correction) | Code-P buys in [0,+5d] after an earnings 8-K with negative surprise |
| **Cluster buying after a drawdown / event** | MED-HIGH (insiders are contrarian, buy dips; Marin-Olivier: purchases peak month before positive jumps) | Code-P cluster within window after negative event |
| **Directors taking fees in shares** | **LOW / thin — no isolating study**; code-A non-cash, weaker than P | Form 4 code A + $0 price + "in lieu of cash fees" footnote; confirm voluntariness in DEF 14A |

---

## 4. Signal Quality Scoring Model (0–100)

A weighted additive model. Compute a raw score, apply multiplicative **kill-switch penalties** (Section 5), then map to alert tiers. Weights are a defensible starting point grounded in the evidence; **backtest and recalibrate** before trusting them.

| # | Factor | Max pts | Scoring logic |
|---|---|---|---|
| 1 | **Transaction type** | 20 | Open-market cash purchase (code P / "market purchase") = 20; PIPE participation at deal price = 14; placing take-up = 10; code A fees-in-shares = 3; anything else = 0 |
| 2 | **Insider role** | 12 | Founder/CEO/**CFO**/Chairman = 12; other C-suite/exec director = 9; non-exec director = 6; 10% holder = 5; other = 2. *(Note: CFO purchases are empirically ~5pp/yr MORE informative than CEO — Wang-Shin-Francis; 10% holders the least informative tier.)* |
| 3 | **Cluster** | 15 | 5+ distinct insiders (≤15d) = 15; 3–4 = 11; 2 = 6; 1 = 0 |
| 4 | **Size vs context** | 12 | Scale by **% of insider's prior holding / $ vs annual salary / $ vs ADV** — NOT raw dollar size. Meaningful (>~50% salary or materially increases stake) = up to 12; token = 0. *(Cziraki-Gider: % returns are NEGATIVELY correlated with raw trade size — the most informative buys are small/infrequent conviction trades. Normalise, don't reward absolute $.)* |
| 5 | **Conviction / discretion** | 8 | Discretionary (10b5-1 box unchecked) & "opportunistic" (breaks routine) = 8; routine/calendar = 2; 10b5-1 planned = 0 |
| 6 | **Timing context** | 12 | Buy after large drawdown / earnings miss / litigation / short attack / sector panic = up to 12; into strength = low |
| 7 | **Valuation & balance sheet** | 8 | Cheap (high B/M, low EV/EBITDA) + solid balance sheet (low net debt, runway) = 8; expensive/distressed = low/negative |
| 8 | **Company size / coverage** | 6 | Lower analyst coverage / small-mid cap (but above microcap floor) = 6; mega-cap saturated = 2. *(Causal: Wu — losing one analyst at a ≤5-coverage firm raises insider 6-mo purchase abnormal return ~16%. But small-firm effect is method-contested per JMZ — keep weight modest.)* |
| 9 | **Insider track record** | 4 | Prior buys preceded gains = 4; poor/none = 0–2 |
| 10 | **Ownership meaningfulness** | 3 | Buy materially raises stake = 3; rounding error = 0 |
| 11 | **Strategic-scarcity / theme fit** | 3 | Bottleneck/future-theme/strategic-scarcity fit = 3 |
| — | **Conflicting insider selling (penalty)** | −10 | Other insiders selling open-market same window = up to −10 |

**Tiering:** 80–100 = high-conviction alert; 60–79 = watchlist; <60 = log only. **Kill switches** (Section 5) can zero out or hard-cap the score regardless of points.

---

## 5. False-Positive Filter (exclude or downgrade)

**Hard EXCLUDE (never a buy signal):**
1. Grants/RSUs/options — codes **A, M, X, C** (compensation, not conviction).
2. Tax-withholding — code **F** (automatic at vesting).
3. Gifts/inheritance — codes **G, W**; voting-trust **Z**; dispositions to issuer **D**.
4. DRIP / dividend reinvestment (footnote "dividend reinvestment").
5. ESPP / SAYE / SIP routine scheme purchases (footnote "under the Plan"; discount-to-market price).

**DOWNGRADE / kill-switch (real buy, but discount heavily):**
6. **10b5-1 plan trades** — checkbox set (scheduled, not opportunistic).
7. **Tiny/symbolic buys** — below a $ floor and below a %-of-salary/holding floor (drop code **L** small acquisitions).
8. **Loan/margin-funded or pledged** purchases — academically underperform; check pledging disclosure.
9. **Compliance buys** — only to meet stock-ownership guidelines (check policy + whether insider was below threshold near a deadline).
10. **Illiquid microcap / penny-stock / promotional** — liquidity & market-cap floor; flag abnormal volume without 8-K news, promotional activity, thin float; cross-ref SEC trading suspensions.
11. **Buys preceding dilution** — scan forward 30–90d for S-1/S-3/424B/8-K offerings; downgrade if a dilutive raise follows (unless the insider bought *into* the raise = positive).
12. **Toxic-PIPE terms** — variable-conversion/repricing/death-spiral structures (Brophy et al.; Chaplinsky-Haushalter deep contingent discounts) → negative.

---

## 6. Technical Architecture

```
                ┌─────────────────────────────────────────────────────────┐
                │ 1. INGEST (per-source connectors, scheduled)             │
                │  • EDGAR FTS + Atom + Form4 XML (US, free, ≤10 req/s, UA)│
                │  • Investegate/LSE RNS (UK, scrape)                      │
                │  • EU feed: InsiderScreener / InsiderPulse API (paid)    │
                │    OR direct national registers (SE CSV, NL CSV/XML…)   │
                │  • 13D/13G/13F/Form D/8-K (EDGAR)                        │
                └───────────────┬─────────────────────────────────────────┘
                                │ raw filings → object store (S3) + queue
                ┌───────────────▼─────────────────────────────────────────┐
                │ 2. NORMALISE                                             │
                │  • Parse XML/HTML/PDF → canonical Transaction schema     │
                │  • Map transaction codes/RNS phrases → {BUY, SELL, NOISE}│
                │  • Entity resolution: person/vehicle → insider identity  │
                │    (Form 4 "I" footnotes + "By:" line; 13D Item 2; group)│
                │  • Ticker mapping → instrument master                    │
                └───────────────┬─────────────────────────────────────────┘
                ┌───────────────▼─────────────────────────────────────────┐
                │ 3. FILTER & MATCH                                        │
                │  • Apply false-positive rules (Section 5)                │
                │  • Match ticker to Trading 212 instrument list           │
                │    (drop anything not tradable in your account)         │
                └───────────────┬─────────────────────────────────────────┘
                ┌───────────────▼─────────────────────────────────────────┐
                │ 4. ENRICH (market + fundamental context)                │
                │  • Price, drawdown, market cap, ADV/liquidity            │
                │  • Balance sheet, dilution/share-count trend             │
                │  • Cluster detection (group by issuer, rolling window)   │
                │  • News / recent filings / short-interest                │
                └───────────────┬─────────────────────────────────────────┘
                ┌───────────────▼─────────────────────────────────────────┐
                │ 5. SCORE (0–100 model, Section 4) + kill switches        │
                └───────────────┬─────────────────────────────────────────┘
                ┌───────────────▼─────────────────────────────────────────┐
                │ 6. AI RESEARCH MEMO (LLM)  → 7. RANK → 8. ALERT (>thresh)│
                │  Store all; surface only top-tier. Telegram/email/web.   │
                └─────────────────────────────────────────────────────────┘
```

**Stack suggestion (lean):** Python ingest workers; PostgreSQL (filings + transactions + scores) with object storage for raw filings; a scheduler (cron/Airflow/Prefect); an LLM API for memo generation (use the latest Claude model for the research-memo step — strong long-context summarisation over filings); a notifier (Telegram bot / email). Respect each source's rate limits and ToS.

**Trading 212 matching note:** Trading 212 has no official public instrument API. Maintain your instrument universe manually (export your watchlist / use the CSV of supported instruments) and match by ISIN where possible (more robust than ticker across venues), falling back to ticker+exchange.

---

## 7. MVP Build Plan (phased)

**Phase 0 — US Form-4 buy detector (week 1–2).** Poll EDGAR Atom feed for form type 4; fetch & parse Form 4 XML; keep code **P**, drop the rest; respect 10 req/s + User-Agent. Store to Postgres. Output a daily CSV/Telegram of all open-market insider buys. *Deliverable: you see every US insider open-market buy each day.*

**Phase 1 — Filter + cluster + score (week 3–4).** Add false-positive rules (10b5-1 checkbox, $ floor, microcap floor), cluster detection (≥3 CIKs / 15 days), and the 0–100 score. Match to your Trading 212 universe. *Deliverable: ranked, filtered, tradable shortlist.*

**Phase 2 — Enrichment + AI memo (week 5–6).** Add price/drawdown/market-cap/liquidity/dilution + recent news/filings; generate an LLM research memo per top candidate; alert only ≥80. *Deliverable: decision-ready alerts.*

**Phase 3 — UK (week 7–8).** Add Investegate RNS ingest; map PDMR phrasing to BUY/NOISE; add TR-1 major-holdings as an early-accumulation signal.

**Phase 4 — Institutional overlay (week 9–10).** Add 13D/Item-4 activist detection + 13G→13D conversions; 13F only as stale context.

**Phase 5 — Europe (week 11+).** Subscribe to InsiderScreener/InsiderPulse API (cheaper & cleaner than scraping 9 regulators); or start with Sweden (CSV) + Netherlands (CSV/XML) DIY.

**Backtest before trusting weights.** Validate the score against forward returns on historical Form 4 data; expect the durable edge in small/mid-caps and clusters, and expect net-of-cost returns to be thinner than gross.

---

## 8. Example Alert Format

```
🟢 SMART-MONEY ALERT — Score 87/100 (HIGH CONVICTION)
─────────────────────────────────────────────
TICKER: XYZ  | XYZ Industries plc (LSE, GBp)  | Tradable on T212: ✅ (ISIN GB00XXXXXXXX)
SIGNAL: Cluster open-market buy — 4 insiders in 9 days

INSIDERS
 • J. Smith (CEO, founder)   £412,000  market purchase  +38% to holding   2026-06-12
 • A. Patel (CFO)            £96,000   market purchase                    2026-06-11
 • R. Lee (Chair)            £150,000  market purchase                    2026-06-05
 • M. Cole (Non-exec)        £22,000   market purchase                    2026-06-04
 Discretionary (no 10b5-1 / no plan).  No insider selling in window.

CONTEXT
 • Price -41% from 12-mo high; bought after FY earnings miss (2026-05-30)
 • Mkt cap £310m (small-cap, low coverage: 2 analysts) | ADV ~£1.1m (liquid enough)
 • Net cash positive; no equity raise filed in last 12m; share count flat
 • Valuation: EV/EBITDA 6.1x vs 5-yr avg 11x

SCORE BREAKDOWN
 Txn type 20 | Role 12 | Cluster 11 | Size 11 | Discretion 8 | Timing 11
 Valuation 7 | Size/coverage 5 | Track record 3 | Ownership 3 | Theme 2 | Selling 0
 KILL SWITCHES: none triggered

AI MEMO: Founder + CFO + Chair + NED all buying with personal cash into a
post-miss 41% drawdown, no dilution on the horizon, net cash, cheap vs history.
Textbook opportunistic cluster. Risks: single FY miss may signal demand softness;
small-cap liquidity. Watch next trading update.

FILINGS: [RNS PDMR links] | DISCLAIMER: research only, not advice.
```

---

## 9. Sources / APIs / Feeds to Investigate (40)

**US — official:** 1) SEC EDGAR Full-Text Search (efts.sec.gov) · 2) EDGAR Atom/RSS feeds · 3) data.sec.gov REST APIs · 4) EDGAR full-index & Form 4 XML · 5) SEC DERA Insider Transactions Data Sets *(FLAG: confirm current URL)*.
**US — aggregators:** 6) OpenInsider · 7) Quiver Quantitative (API) · 8) Fintel (API) · 9) Finviz Elite · 10) WhaleWisdom (13F/13D, API) · 11) 13F.info · 12) HedgeFollow · 13) sec-api.io (13D/G API) · 14) GuruFocus · 15) Washington Service *(institutional)* · 16) VerityData/InsiderScore *(institutional)* · 17) InsiderTracking/INK (US+Canada).
**UK:** 18) Investegate (free RNS — best free start) · 19) London South East lse.co.uk/rns · 20) LSE/LSEG RNS Data Feed (rns-distribution.com, paid) · 21) FCA ESS major-holdings (TR-1) · 22) ADVFN Director Deals Tracker · 23) Hargreaves Lansdown / Sharecast director deals · 24) Apify Investegate RNS Aggregator.
**Europe — national registers:** 25) BaFin Directors' Dealings (DE) · 26) Finansinspektionen Insynsregistret (SE, CSV) · 27) AMF BDIF (FR, +RSS) · 28) AFM MAR19 register (NL, CSV/XML) · 29) CONSOB / eMarketStorage / 1INFO (IT) · 30) Finanstilsynet OAM (DK) · 31) Euronext Oslo Børs NewsWeb (NO) · 32) Nasdaq Helsinki announcements (FI) · 33) SIX Exchange Regulation Management Transactions (CH).
**Europe — aggregators:** 34) 2iQ Research (API, institutional) · 35) InsiderScreener (~€25–85/mo API — best prosumer) · 36) InsiderPulse (8 EU markets, API) · 37) Smart Insider (API/SFTP/Snowflake) · 38) MarketScreener · 39) Koyfin (Capital IQ-sourced) · 40) Simply Wall St.

*(Pricing/API availability for institutional vendors and several retail tools is contact-sales / unverified — confirm directly. data.gouv.fr "transactions dirigeants" is third-party scraped, not official AMF.)*

---

## 10. Legal & Ethical Boundaries

- **Public information only.** Every source above is a mandated public disclosure (SEC filings, RNS, regulator registers) or a licensed aggregator of them. **Never** use hacked, leaked, private, confidential, or otherwise non-public ("material non-public information") material — trading on MNPI is illegal insider trading.
- **Respect access terms.** Honour robots.txt, rate limits (SEC ≤10 req/s + User-Agent), and each site's Terms of Service. RNS/LSEG and many aggregators license their feeds — commercial redistribution requires a licence; personal research use is generally permitted but verify. Prefer official APIs/feeds over scraping where they exist.
- **Data protection.** EU/UK registers deliberately omit some personal data (e.g., DOB); don't re-identify or re-publish beyond what's disclosed. Keep within GDPR if storing EU personal data.
- **No manipulation / no advice.** This is a *research-discovery* tool. Do not use it to coordinate trading, amplify promotions, or manipulate thin stocks. Outputs are research, **not financial advice**; flag accordingly.
- **Provenance & honesty.** Treat vendor coverage/performance claims as marketing until verified; preserve confidence tags; surface contested findings rather than overstating the edge.

---

## Appendix — Contested / flagged claims (carry these caveats into design)
- **Small-firm effect:** strong in Lakonishok-Lee & Seyhun (informativeness method) but **not significant in Jeng-Metrick-Zeckhauser** (performance-evaluation method). Don't treat as universal — keep the size weight modest.
- **Net-of-cost outsider edge:** gross insider-purchase returns are real (~6–10%/yr top specs), but recent replication finds returns **shrink or vanish** after transaction costs and trade-size caps, concentrating in small/illiquid names. Capacity-limited.
- **Buyback long-run drift (ILV):** robust in event-time/FF models but **contested under calendar-time tests** (Fama 1998; Mitchell-Stafford). Announcement-window return is the more robust component.
- **SWF & strategic-investor long-run:** announcement pop reliably positive; long-run **debated** (passivity/"SWF discount" drag vs value-creation when active/transparent).
- **Kang-Kim-Wang (cluster 3.8% vs 2.0%):** working-paper status unconfirmed; magnitude corroborated via secondary reviews.
- **Fees-in-shares:** no study isolates it as a return predictor — low-weight corroborator only.
- **Vendor pricing/API & some regulator export/API availability:** several "contact-sales" or absence-of-evidence findings — verify before building dependencies.
