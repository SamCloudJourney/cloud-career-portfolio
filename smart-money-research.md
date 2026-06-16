# Smart-Money Intelligence & Stock-Discovery Engine — Complete Research & Build Manual

> A single, self-contained reference for detecting insider buying, director dealings, strategic accumulation and early institutional positioning across global public equities — and turning those signals into a stock-discovery engine.
> Compiled 2026-06-16. **Strictly public-information design.** See §20 for legal/ethical boundaries.

**Confidence legend:** **HIGH** = primary source / multiple corroboration · **MED** = single reputable source · **LOW / FLAG** = unverified, contested, or vendor-marketing claim. Contested academic claims are flagged inline and collected in §21.

---

## Table of Contents
0. How to use this document
1. Executive summary
2. The evidence base — does insider buying actually predict returns?
3. US insider disclosure (Forms 3/4/5, transaction codes, Form 144, 10b5-1, data access)
4. UK director / PDMR dealings (MAR Art. 19, real-vs-noise phrasing, TR-1, RNS access)
5. Europe & international, country by country (19 jurisdictions)
6. Institutional "smart money" (13F, 13D/13G, major-holding notices)
7. Alternative accumulation signals (cluster, founder, PIPE, buybacks, strategic/SWF, contrarian, fees-in-shares)
8. Signal-quality scoring model (0–100)
9. False-positive filter
10. Data-source map (master table)
11. Trading 212 instrument matching
12. Enrichment data sources (price, fundamentals, short interest, news)
13. Technical architecture
14. Ingestion & parsing (Form 4 XML schema, discovery feeds, libraries, compliance, RNS, EU)
15. Backtesting & validation methodology
16. Operational layer (AI memo, alerting, Postgres schema, orchestration, cost)
17. MVP build plan
18. Example alert format
19. Master source list (websites / APIs / feeds)
20. Legal & ethical boundaries
21. Appendix — contested claims & key academic citations

---

## 0. How to use this document

This is both a **research dossier** (what the signals are, where they live, how reliable they are) and a **build manual** (architecture, parsing, scoring, backtesting, ops). Read §1–§2 for the thesis, §3–§7 for where signals come from, §8–§9 for how to score/filter, §10–§16 for how to build it, §17 for the phased plan. The core design philosophy: **the raw "insider bought" event is commoditised — the value is ruthless filtering for the high-conviction subset plus rich context, so only a handful of signals per week ever alert.**

---

## 1. Executive Summary

**The thesis.** Four decades of academic evidence converge on one robust finding: insider **purchases** predict positive abnormal returns (~6–10%/yr in the strongest specifications); insider **sales** carry little or no signal (people sell for liquidity, diversification, tax). The durable edge concentrates in: (a) **open-market cash purchases** (US Form 4 code **P**); (b) **"opportunistic"/non-routine** insiders; (c) **clusters** of multiple insiders buying in a short window (~2× a solitary buy); (d) **smaller, low-coverage, high-information-asymmetry** firms — though the small-firm effect is *method-dependent and contested*.

**The opportunity & the trap.** The signal is real but **capacity- and cost-constrained**: net-of-cost, large-cap, size-capped profitability for outsiders is genuinely debated, and several studies show the gross edge shrinks or vanishes after realistic spreads and trade-size caps. The engine's job is therefore not "detect insider buying" (commoditised, scraped everywhere) but to *filter ruthlessly* and *enrich* so only the top few signals alert.

**Global structure.** The US is a single-source firehose — SEC EDGAR: free, structured, near-real-time, and the **post-2023 Rule 10b5-1 checkbox is the single most powerful noise filter available**. Europe is fragmented across ~20+ national regulators/exchanges under EU MAR Article 19 (same legal concept — PDMR "managers' transactions," 3-business-day deadline, €5k de minimis — wildly different access). The UK's DTR **3% + each 1%** major-holdings threshold is the most sensitive early-accumulation tripwire in the world.

**Build recommendation.** Start **US-only on EDGAR** (free, best data). Add the **UK** (RNS via Investegate) next. **Buy** a European feed (InsiderScreener ~€25–85/mo, or InsiderPulse) rather than scraping nine regulators. Layer **13D/activist** filings as the high-conviction institutional signal; treat **13F as late/stale context only**. Score 0–100, alert only above a high threshold, exclude the long tail of grants/options/tax/DRIP/microcap noise, and **report calendar-time alpha (not just event-time BHAR) net of costs** when you validate.

---

## 2. The Evidence Base — Does Insider Buying Predict Returns?

Two literatures: **informativeness** (can outsiders profit by mimicking?) and **returns-to-insiders** (what do insiders earn?). Across both, the near-universal result: predictive content is in **purchases**, not sales.

### 2.1 Foundational studies
- **Lakonishok & Lee (2001), *Review of Financial Studies* 14(1):79–111.** ~1M+ transactions, NYSE/AMEX/Nasdaq 1975–1995. Informativeness comes **entirely from purchases**; sales have "no predictive ability." Buy-heavy minus sell-heavy ≈ **4.8% abnormal / ~7.5% raw over 12 months**; concentrated in **smaller firms**. Insiders are contrarian but beat a naive contrarian strategy. [HIGH] — lsvasset.com/pdf/research-papers/Insider-Trades-Informative.pdf · nber.org/papers/w6656
- **Jeng, Metrick & Zeckhauser (2003), *Review of Economics & Statistics* 85(2):453–471.** Performance-evaluation (calendar-time) approach, 1975–1996; 563,863 transactions (214,897 purchases). **Purchase portfolio >50 bps/month risk-adjusted (~6%/yr); +10.2%/yr raw.** Sales: no abnormal return. **~¼ of the return accrues within 5 days, ~½ within the first month.** **CONTESTED nuance:** finds small-firm and top-executive effects **NOT** significant under value-weighting — a direct methodological dissent from Lakonishok-Lee. [HIGH] — direct.mit.edu/rest/article/85/2/453 · nber.org/papers/w6913
- **Cohen, Malloy & Pomorski (2012), *Journal of Finance* 67(3):1009–1043, "Decoding Inside Information."** Splits insiders into **"routine"** (trade same calendar month ≥3 consecutive years → uninformative) vs **"opportunistic"** (everyone else). Long-short on opportunistic: **82 bps/month value-weighted (~10%/yr); 180 bps equal-weighted; routine ≈ 0.** Opportunistic trades predict future news/earnings and draw more SEC enforcement. Most informed: local, non-senior insiders at poorly governed, geographically concentrated firms. Survives post-2000 data. [HIGH] — nber.org/papers/w16454 · dash.harvard.edu (full PDF)
- **Seyhun (1986 JFE; 1992 QJE; 1998 MIT Press book).** Net insider purchases → ~+4.3% abnormal/300 days; sales ~−2.2%. **Aggregate** net insider trading predicted up to **~60% of one-year-ahead aggregate market return variation (1975–1989)**. Crucially: **once realistic ~2% round-trip costs are imposed, outsider mimicking profit shrinks to ~3–3.5%/yr** — the market-efficiency caveat. Strongest in small firms. [HIGH qualitative; MED on exact figures] — semanticscholar Seyhun 1986

### 2.2 What raises signal quality (moderators)
- **Role / seniority.** Top execs > others; **CFO purchases are ~5pp/yr MORE informative than CEO** (Wang, Shin & Francis, JFQA 2012 — CFO buys precede more positive earnings surprises). 10% holders are the **least** informative tier. [HIGH] — ssrn 1787482. *(Counterpoint: JMZ find rank insignificant under value-weighting — contested.)*
- **Cluster / consensus.** **Alldredge & Blank (2019, J. Financial Research):** buys within 2 days of a peer's = **~2.1% next-month vs ~1.2% solitary** (+0.9pp). **Kang, Kim & Wang (2018, working paper):** cluster **3.8% vs 2.0% over 21 days** (~2×), widening to ~2.5pp/90d. [HIGH / MED on KKW pub status] — ssrn 2781761
- **Information asymmetry.** **Wu (Texas A&M)** causal: at ≤5-coverage firms, losing one analyst raises insider 6-mo purchase abnormal return by **~16%**. **Aboody & Lev (2000):** gains larger in R&D-intensive firms. **Idiosyncratic vol (JBF 2016):** +1 SD → +2.6% on purchases. [HIGH] — ssrn 2323537; wiley 0022-1082.00305
- **Opportunistic vs routine** (CMP, above) — the single strongest filter.
- **Contrarian/value timing.** **Rozeff & Zaman (1998), Jenter (2005), Piotroski & Roulstone (2005):** insiders buy after declines, tilt to value/low-P/B, predict reversals; misvaluation explains more of buys than future cash-flow info. **Marin & Olivier (2008):** insider purchases peak the month before large positive jumps. [HIGH; mechanism contested] 
- **Size — relative, not absolute.** **Cziraki & Gider (2021, Review of Finance), "The Dollar Profits to Insider Trading":** % abnormal returns are **NEGATIVELY correlated with raw trade size & frequency**; the most informative trades are **small, infrequent** conviction buys (median insider ≈ $464/yr abnormal profit). **Normalise size to holdings/wealth/salary; do NOT reward absolute $.** [HIGH — important for scoring] — ssrn 2887628

### 2.3 Does it still work? (the contested question)
- SOX (2002, 2-business-day reporting) + decimalization (2001) should erode the outsider edge. **Brochet (2010, Accounting Review):** abnormal returns/volume around **purchase filings are GREATER post-SOX** (faster disclosure → more relevant). [HIGH]
- Recent replications (e.g., *Finance Research Letters* 2024): positive but **smaller** abnormal returns that **vanish or go negative once trade size is capped to realistic amounts**; returns negatively correlated with liquidity → edge concentrates in small/illiquid names. [MED]
- **Bottom line:** gross purchase signal persists (CMP opportunistic; Brochet); **net, large-cap, capacity-adjusted** profitability is genuinely contested. Design conservatively.

---

## 3. US Insider Disclosure

*All SEC facts verified against SEC.gov.*

### 3.1 Forms 3, 4, 5 (Section 16(a))
Filers = directors, officers, and >10% beneficial owners of a registered class.

| Form | What | Deadline |
|---|---|---|
| **Form 3** | Initial statement of beneficial ownership (on becoming an insider) | within **10 days** |
| **Form 4** | Changes in beneficial ownership (the workhorse — buys, sells, grants, exercises) | within **2 business days** of the transaction |
| **Form 5** | Annual catch-up (exempt / previously unreported) | within **45 days** of fiscal year-end |

**Form 4 is the primary feed.** Form 5 is low-signal (cleanup); Form 3 defines the universe to watch. Source: sec.gov/files/forms-3-4-5.pdf

### 3.2 Form 4 transaction codes — exact meanings
**Only Table I code "P" is a genuine open-market, own-cash conviction BUY.** Everything else is compensation, tax, derivative mechanics, or admin.

| Code | Meaning | Signal |
|---|---|---|
| **P** | Open-market / private **purchase** | **HIGHEST — core buy signal** |
| **S** | Open-market / private sale | Bearish-ish, noisy |
| **A** | Grant / award / other acquisition (Rule 16b-3) | Compensation — **exclude** |
| **M** | Exercise/conversion of derivative | Option exercise — **exclude** |
| **F** | Shares withheld for exercise price / tax | Tax/admin — **exclude** |
| **G** | Bona fide gift | No market trade — **exclude** |
| **X** | Exercise of in/at-the-money derivative | Comp mechanics — **exclude** |
| **C** | Conversion of derivative | Admin — **exclude** |
| **D** | Disposition (sale) back to issuer | Buyback/redemption — not open-market |
| **V** | Voluntarily reported early | Modifier flag, not a transaction |
| **I** | Discretionary (broker best-price order) | Often plan-driven — edge case |
| **J** | Other acq/disp (see footnotes) | Manual review |
| **W** | By will / descent | Inheritance — exclude |
| **K** | Equity swap | Derivative — specialised |
| **L** | Small acquisition | De minimis — low signal |
| **U** | Tender in change-of-control | Event-driven |
| **Z** | Voting-trust deposit/withdrawal | Admin |
| **O/E/H** | Out-of-money exercise / derivative expiry | Comp / admin |

> **Mixed-filing trap:** a single Form 4 often bundles **M (exercise) + F (tax) + S (sale)**. Parse per-row; never sum shares naively. The cluster/buy filter must key on **code = P in the non-derivative table**.

### 3.3 Form 144 (proposed sales)
Forward-looking **sell** signal filed *before* sale of restricted/control stock. Required when an affiliate intends to sell >**5,000 shares OR >$50,000** in any 3 months. **Electronic on EDGAR since compliance date Apr 13, 2023** (pre-2023 were paper → thin historical coverage). Source: sec.gov/submit-filings/.../file-form-144-electronically

### 3.4 Rule 10b5-1 plans + the Form 4 checkbox (the key noise filter)
Pre-arranged plans giving an affirmative defense; trades execute on schedule (low discretion). **2022 amendments (effective Feb 27, 2023):** cooling-off for directors/officers = later of **90 days** or **2 business days after next quarterly results, capped 120 days**; **30 days** for others. **Form 4/5 now have a mandatory checkbox** flagging a 10b5-1 trade. **Design insight:** a high-signal buy = **code P + 10b5-1 box NOT checked** (discretionary, opportunistic). This is the single best automated noise filter post-2023. Source: sec.gov/newsroom/press-releases/2022-222

### 3.5 US data access (free, no key)
- **EDGAR Full-Text Search:** `https://efts.sec.gov/LATEST/search-index?q=...&forms=4&startdt=YYYY-MM-DD&enddt=YYYY-MM-DD` (JSON; filings since 2001; CORS-enabled).
- **RSS/Atom:** per-company `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=...&type=4&output=atom`; market-wide real-time `...action=getcurrent&type=4&output=atom`.
- **data.sec.gov REST:** `https://data.sec.gov/submissions/CIK##########.json` (10-digit CIK); XBRL company-facts/concept (financials only — Form 4 transaction data is in the raw XML).
- **Full-index:** `https://www.sec.gov/Archives/edgar/full-index/{YYYY}/QTR{N}/` (master.idx, form.idx); daily-index analogue.
- **Raw Form 4 XML** inside each filing folder carries `transactionCode`, shares, price, and the 10b5-1 flag (schema in §14).
- **Rules:** **≤10 requests/sec**, **declared User-Agent mandatory** (`Name email`), no CORS on data.sec.gov.

### 3.6 US aggregators
| Provider | Free/Paid | Access | Note |
|---|---|---|---|
| **OpenInsider** | Free | scrape (no official API) | Best free Form-4 screener; cluster/CEO filters |
| **Quiver Quantitative** | Freemium + API (~$30/mo) | REST | US-only; + Congress/gov-contract alt-data |
| **Fintel** | Freemium + API (~$15–95/mo) | REST | Forms 3/4/5 + institutional/options |
| **Finviz Elite** | $24.96–39.50/mo | export | Insider data supplementary |
| **GuruFocus** | Paid (GuruAPI) | API | TTM open-market insider, daily |
| **VerityData/InsiderScore**, **2iQ**, **Smart Insider**, **Washington Service** | Paid (institutional) | feed/API | Curated, de-noised; enterprise pricing |

---

## 4. UK Director / PDMR Dealings

### 4.1 Regime
**UK MAR Article 19** — PDMRs (Persons Discharging Managerial Responsibilities) and closely-associated persons. Notify issuer **and FCA within 3 business days**; **de minimis €5,000/calendar year** (UK keeps the default — does **not** adopt the €20k uplift). 30-day closed period before results. Announced via **RNS** ("Director/PDMR Shareholding"). Source: fca.org.uk/markets/market-abuse/regulation

### 4.2 Reading the language — real buying vs noise
**REAL discretionary buying (STRONG):** "Purchase of Ordinary Shares," "On market purchase" / "market purchase," "Acquisition of shares" (when on-venue + non-nil price), "beneficial holding increased."

**NOISE / non-discretionary (down-weight):** LTIP/PSP/RSP vesting, "vesting of awards," option exercise, **SAYE/Sharesave**, **SIP**, scrip/bonus dividend, **DRIP**, "sale of shares to cover tax/social security arising from the vesting," RSU vesting, "awarded under the … Plan," nominee-to-nominee transfers ("no change in beneficial ownership"), nil/0.00p price.

**MAR controlled vocabulary caveat:** the "Nature of transaction" field maps to the closed category list in **Commission Delegated Reg (EU) 2016/522 Art. 10(2)** (template: Implementing Reg 2016/523). The bare code **"Acquisition" is broad** — ESMA confirms it also covers **gifts and inheritances**. Always read it with (a) **place** (on-venue MIC vs "outside a trading venue"), (b) **price** (nil = grant/scrip, not a buy), (c) whether **"linked to a share-option programme."** Cleanest informed-buy config = Acquisition + on-venue + non-nil cash price + senior insider + clustered.

*Verbatim examples (Investegate):* Pantheon Resources "On market purchase"; Transense "Purchase of Ordinary Shares"; Sage Group dual row "Acquisition … following the vesting of a share award under [LTIP]" + "Sale … to cover employee tax" (textbook noise). Note "Transaction in Own Shares" = company **buyback**, a different register.

### 4.3 How vendors classify (for design ideas)
- **Smart Insider:** human analysts record "true nature," screen out noise, flag trades that "depart from normal trading patterns" (genuine conviction); fields incl. a "Director Score." [methodology partly opaque]
- **2iQ:** five "informative" criteria — purchases>sales; top-level insiders; **size as % change in holdings (not $)**; **cluster buying = "consensus of insider opinion"**; small-cap focus. Outputs an Insider Model score.
- **Stockopedia:** buys=signal, sells=noise; **>3 directors buying within 3 months → ~2%/month above market**; consolidates trades in a 4-week window; "Net Purchase Ratio" = (buys−sells)/total; strongest in small-cap value; ~half the return within 60 days.

### 4.4 TR-1 major holdings (the earliest tripwire)
Form **"TR-1: Standard form for notification of major holdings"** under **DTR 5**. **UK issuers: notify at 3%, then EACH 1% thereafter** (up and down) — far earlier than the US 5%. **Non-UK issuers: 5/10/15/20/25/30/50/75%.** Investment managers may use higher 5%/10% initial thresholds (DTR 5.1.5R). **Shareholder→issuer within 2 trading days; issuer→market by end of next trading day.** Aggregates shares + qualifying financial instruments + **long CFDs** (DTR 5.3). Filed to FCA via the **ESS major-holdings portal** (mandatory since 22 Mar 2021); issuer discloses via RNS headline "Holding(s) in Company." [HIGH; exact sub-rule numbers 5.8.3R/5.8.12R are LOW-confidence labels] — handbook.fca.org.uk/handbook/dtr5

### 4.5 UK monitoring sources
| Source | Free/Paid | Access | Note |
|---|---|---|---|
| **Investegate** | Free | scrape (Apify actor exists) | Best free RNS archive; cleanest scrape; metadata-only via actor (follow source_url for body) |
| **London South East** lse.co.uk/rns | Free | scrape (403/anti-bot) | Pre-built director-dealings filter |
| **LSE / LSEG RNS Data Feed** | Paid/enterprise | REST + WebSocket (`rns-distribution.com`, spec v1.3) | Authoritative, low-latency; auth msg within 5s on websocket |
| ADVFN / Hargreaves Lansdown / Sharecast / Shares Mag | Free pages | scrape | Director-deals lists |
| **SharePad** (~£324/yr), **Stockopedia**, **MarketScreener**, **Simply Wall St** | Paid | UI (no clean API) | Good manual research; not automation feeds |
| **Smart Insider**, **2iQ** | Paid (institutional) | API/SFTP/Snowflake | Curated UK + global |

---

## 5. Europe & International — Country by Country (19 jurisdictions)

**Common EU/EEA frame:** EU **MAR Article 19** managers'-transactions — notify issuer **and** competent authority within **3 business days**, **€5,000** annual de minimis (member states may raise to €20,000). Transparency-Directive major-holdings typically **5%** (varies; some lower). Hosting entity varies: **regulator** vs **exchange** vs **private storage**. Below, Tier = ease of automated ingestion.

### 5.1 The original nine
| Country | Hosted at | Portal | Free/Search | Machine access | Tier |
|---|---|---|---|---|---|
| **Germany** | Regulator (BaFin) | portal.mvp.bafin.de/database/DealingsInfo | Yes | Browse-only; no API/CSV found; 12-mo retention; threshold €20k→**€50k from 2026** | 2 (scrape) |
| **Sweden** | Regulator (FI) | marknadssok.fi.se Insynsregistret | Yes | **CSV/Excel export**; data 2016+; libs `djonsson/insynsregistret` (Py), `w3stling/insynsregistret` (Java) | **1 (best)** |
| **France** | Regulator (AMF) | bdif.amf-france.org (BDIF) | Yes | PDFs + **RSS**; structured only via 3rd-party (data.gouv.fr "transactions dirigeants" = scraped by LesTransactions.fr, **not** official) | 2/3 |
| **Netherlands** | Regulator (AFM) | afm.nl MAR19 register | Yes | **CSV + XML export** (cleanest EU) | **1** |
| **Italy** | Private CONSOB-authorised storage | emarketstorage.com (Teleborsa), 1info.it + issuer sites | Yes | PDF download; no API | 3 |
| **Denmark** | Regulator (Finanstilsynet OAM) | oam.finanstilsynet.dk | Yes | Export/API unverified; also Nasdaq Copenhagen | 2/3 |
| **Norway** | Exchange (Euronext Oslo Børs) | newsweb.oslobors.no ("Mandatory notification of trade by primary insider") | Yes (JS SPA) | Consumer API/RSS unverified; SPA JSON endpoints undocumented | 3 |
| **Finland** | Exchange (Nasdaq Helsinki) | Nasdaq Helsinki company announcements ("Managers' transactions") | Yes | FIN-FSA has no public DB; read via exchange feed | 3 |
| **Switzerland** (non-EU) | Exchange SRO (SIX/SER) | ser-ag.com Management Transactions | Yes | Scrape-only; no API/CSV found; names omitted but function shown | 2/3 |

### 5.2 The additional ten
| Country | Hosted at | Portal | Machine access | Thresholds / deadline | Tier |
|---|---|---|---|---|---|
| **Spain** | Regulator (CNMV) | cnmv.es consultations; NOD (directors) + significant-holdings registers | Historical bulk datasets; no documented REST API; scrapeable | MAR Art.19 (no min %, €5k, 3 bd); sig. holdings 4 td | 2 |
| **Belgium** | Regulator (FSMA) | fsma.be/en/managers-transactions-0 | No CSV/API/RSS; scrape HTML | MAR Art.19; **€20,000** (raised Dec 2024); 3 bd | 2 |
| **Ireland** | Split: CBI (authority) + Euronext Dublin (OAM) | centralbank.ie guidance; euronext.com announcements; RNS/Investegate | No central insider DB; parse Euronext/RNS feed | MAR Art.19 (€5k likely, **flag**); 3 bd | 3 |
| **Canada** | Regulator (CSA) — **SEDI** (→ SEDAR+) | sedi.ca | No official API/CSV; SEDI bookmarklet → CSV; INK/insidertracking.com aggregates | Initial 10 cal days; **changes 5 cal days**; 10% early-warning | 2 |
| **Australia** | Split: ASX + ASIC | announcements.asx.com.au; ASX **Appendix 3Y**; ASIC Forms 603/604/605 | No free API; PDFs via markitdigital (scrape) or paid **ComNews**; **PDF parsing needed** | 3Y within 5 bd; substantial holder 5% within 2 bd, ±1% | 3 (hardest) |
| **Japan** | Regulator (FSA) — **EDINET** + TDnet | api.edinet-fsa.go.jp/api/v2 | **Official JSON API v2 + XBRL** (free key); libs `edinet-tools`, edinetdb.com (free API/MCP) | 5% rule: file within 5 bd; ±1% change reports | **1 (best in set)** |
| **Hong Kong** | Exchange (HKEX) — DION/DI | di.hkex.com.hk/di/summary/NSMSumMenu.htm; CCASS searchsdw.aspx | No official API; HTML/query-string, very scrapeable | Substantial 5%; directors any interest; **3 bd** | 2 |
| **Singapore** | Exchange (SGX); rules MAS | sgx.com/securities/company-announcements (Form 7) | No official API; JS site w/ internal JSON; parse Form 7 | 5%; directors/CEO; **2 bd** | 2/3 |
| **India** | SEBI via NSE & BSE | nseindia.com insider-trading & PIT/SAST pages; NSDL SDD | **CSV download** in-UI; JSON endpoints (anti-bot); `NseIndiaApi`; insiderscreener.com | PIT >₹10 lakh/qtr within 2 td; SAST 5% then ±2%, 2 wd | 2 |
| **New Zealand** | Exchange (NZX) | nzx.com/announcements (SPH notices) | No free API (NZX sells feeds); scrape announcements | SPH 5%, ≤2 bd; ±1% movement notices | 3 |

**Pan-EU / Asia aggregators (buy-vs-build):** **2iQ** (≈50 countries, API, institutional), **InsiderScreener** (~16 markets incl. India/EU, REST API ~€25–85/mo — best prosumer), **InsiderPulse** (8 EU markets, sources BaFin/AMF/FCA/AFM/Nasdaq Nordic directly, API), **Smart Insider** (60+ countries, API/SFTP/Snowflake), **EDINET DB** (Japan, free), **INK/insidertracking.com** (Canada+US), **MarketScreener/Koyfin/Simply Wall St** (UI, mostly no clean API). *(Coverage/pricing claims are vendor-stated — verify.)*

---

## 6. Institutional "Smart Money"

### 6.1 Form 13F
Institutional managers with **>$100M** in 13(f) securities; quarterly, **45-day lag** after quarter-end. **Limitations:** long US-listed only (no shorts, cash, bonds, non-US); end-of-quarter **snapshot** (no trade dates/turnover/cost basis); hedging invisible; **confidential-treatment requests** let managers hide accumulation in real time. (Separate Rule 13f-2 / Form SHS short-reporting regime, Oct 2023, is aggregate/confidential.) Source: SEC 13F FAQ

### 6.2 Schedule 13D vs 13G + 2023 amendments
- **13D** = >5% with **control intent** (active, "loud"); **13G** = >5% passive/qualified (three filer types). Beneficial owner = anyone with voting **or** investment power, directly or indirectly (captures trusts/LLCs/nominees).
- **"Modernization of Beneficial Ownership Reporting," adopted Oct 10, 2023** (first deadline change in ~50 yrs):

| Filing | Old → New |
|---|---|
| 13D initial | 10 cal days → **5 business days** |
| 13D amendment | "promptly" → **2 business days** after material change (≥1% presumed material) |
| 13G initial (QII/Exempt) | 45 days after year-end → **45 days after quarter-end** (10% accelerated trigger) |
| 13G initial (Passive) | 10 days → **5 business days** |
| 13G amendment | any change → only on **material change**, 45 days after quarter-end |

Compliance: 13D Feb 5, 2024; 13G Sept 30, 2024. EDGAR cutoff extended to 10pm ET. **Group rule (Rule 13d-5):** persons "acting together" treated as one — detects coordinated sub-5% accumulation across affiliated vehicles.

### 6.3 The activist signal
**Item 4 "Purpose of Transaction"** is the tell: language shifting from "shares acquired for investment" → board nomination, strategic alternatives, opposing a merger, going-private. **13G→13D conversion** = passive holder turning active (strong). 

### 6.4 Signal timing & the 13F staleness trap
- **EARLY / high-conviction:** new **13D** (≤5 bd), Item 4 activist language, 13G→13D, small/concentrated-fund **new** position.
- **LATE / low-info:** large add to an already-public 13F position; widely-reported "whale" 13F (45-day stale, crowded, arbitraged within hours). Practitioner claim that 13F-cloning underperforms by 2–4%/yr [LOW — not peer-reviewed].
- **When 13F still helps:** concentrated "best ideas" (top-10 picks outperform — SSRN 3459526), small/niche less-scraped funds, new positions, **positions backed by a 13D** (independent conviction).

### 6.5 UK TR-1 / EU Transparency vs US
UK **3%+1%** (earliest), EU **5%+** (Transparency Directive 2004/109/EC; 4-trading-day notify, 3-day publish), US **5%** (now 5 bd). The UK threshold remains the most sensitive early-accumulation tripwire.

### 6.6 Institutional data access
EDGAR (13F-HR, SC 13D/13D-A, SC 13G/13G-A); **13F.info**, **HedgeFollow** (also Form 4/13D/G), **WhaleWisdom** (free tier + ~$300/yr API), **Fintel**, **sec-api.io** (dedicated 13D/G API), GuruFocus, Bloomberg/Refinitiv (paid).

---

## 7. Alternative Accumulation Signals

| Signal | Evidence (graded) | Detection |
|---|---|---|
| **Cluster buying** (≥3 distinct insiders, short window) | **HIGH** — Alldredge-Blank 2.1% vs 1.2%/mo; Kang-Kim-Wang 3.8% vs 2.0%/21d (~2×) | Form 4 code P, dedupe by CIK, 7–15d rolling window; weight by count/seniority/$ |
| **Opportunistic (non-routine) insiders** | **HIGH** — CMP 82 bps/mo VW; routine ≈ 0 | Flag insiders breaking their calendar-month pattern (≥3-yr history) |
| **Founder/family accumulation via holdco/trust** | **HIGH** — Anderson-Reeb (family firms outperform); Villalonga-Amit (founder-CEO ~25% premium); family-portfolio alphas ~0.72%/mo; Anderson-Reeb-Zhao (informed trading in family firms) | Form 4 ownership **"I"** + footnote/"By:" line → vehicle→insider map; 13D/G Item 2 + group rule; UK TR-1 controlled-undertaking chains |
| **Insider participation in PIPEs / private placements** | **HIGH** — base rate negative (Hertzel et al. −30%/3yr; Brophy et al. toxic PIPEs underperform) but **insider/affiliate participation flips it positive** (Krishnamurthy et al. 2005; Floros et al. 2019 certification → lower discounts, higher announcement returns) | Match **Form D / 8-K Item 3.02** raise to Form 4 acquisitions **at deal price**; S-1/S-3 selling-holder list; flag variable-conversion/repricing "toxic" terms |
| **Insider take-up in rights issues / discounted placings** | **MED** — insiders net buyers around placings, net sellers around rights issues; full-standby low-discount = quality | UK RNS placing/subscription + PDMR; US 8-K/424B + Form 4 |
| **Buybacks after drawdowns** | **HIGH cross-section** — ILV +12.1%/4yr (value names +45.3%, glamour ~0); ASR 7-day CAR ~2.0% vs OMR ~0.7%; fixed-price tender strongest (Comment-Jarrell). Long-run drift **contested** (Fama/Mitchell-Stafford) | 8-K (authorisation) + **Item 703** 10-Q/10-K table (execution); **SC TO-I** (tenders); ASR in MD&A. *(Note: 2023 daily-buyback rule was VACATED Dec 2023 — monthly Item 703 still applies.)* |
| **Strategic investor / supplier-customer stake** | **HIGH when bundled with product-market/tech relationship** (Allen-Phillips 2000; Chan et al. +0.6–0.8%); raw CVC weak/conditional on industry overlap (Sinha) | 13D (operating-co filer), 8-K Item 1.01, Form D |
| **Sovereign wealth / govt-backed stake** | Announcement **reliably +~2.1%** (Kotter-Lel), amplified by transparency; long-run **contested** ("SWF discount" −2.67pp, passivity drag vs value-creation when active) | 13D/13G by SWF vehicle (GIC, Temasek, ADIA, Norges/NBIM, PIF, QIA…); 8-K; Form D |
| **Insider buying vs short-seller disagreement** | **MED-HIGH** — Wang-Zheng +1.95% next-qtr when insiders buy into a short spike; shorts then reverse — but **squeeze-reversal caution** (Stice-Lawrence: post-attack pops often fully reverse; ~15% of attacks squeeze) | Code-P buys + elevated short interest / activist-short report date |
| **"Contradictory" buys after earnings miss** | **HIGH** — Dargenidou et al.: buys before/around negative surprises are unusually informative, speed PEAD correction | Code-P buys in [0,+5d] after an earnings 8-K with negative surprise |
| **Directors taking fees in shares** | **LOW / thin — no isolating study**; code-A non-cash, weaker than P | Form 4 code **A** + $0 price + "in lieu of cash fees" footnote; confirm voluntariness in DEF 14A. Low-weight corroborator only |

---

## 8. Signal-Quality Scoring Model (0–100)

Weighted additive score, then **multiplicative kill-switch penalties** (§9), then map to alert tiers. Weights are a defensible starting point grounded in §2 evidence — **backtest and recalibrate (§15) before trusting them.**

| # | Factor | Max | Logic |
|---|---|---|---|
| 1 | **Transaction type** | 20 | Open-market cash purchase (code P / "market purchase") = 20; PIPE participation at deal price = 14; placing take-up = 10; code-A fees-in-shares = 3; else 0 |
| 2 | **Insider role** | 12 | Founder/CEO/**CFO**/Chairman = 12; other C-suite/exec dir = 9; non-exec = 6; 10% holder = 5; else 2. *(CFO purchases ~5pp/yr more informative than CEO — Wang-Shin-Francis; 10% holders least informative.)* |
| 3 | **Cluster** | 15 | 5+ distinct insiders (≤15d) = 15; 3–4 = 11; 2 = 6; 1 = 0 |
| 4 | **Size vs context** | 12 | Scale by **% of prior holding / $ vs salary / $ vs ADV** — NOT raw $. Meaningful = up to 12; token = 0. *(Cziraki-Gider: % returns negatively correlated with raw size — normalise.)* |
| 5 | **Conviction / discretion** | 8 | Discretionary (10b5-1 box unchecked) & opportunistic (breaks routine) = 8; routine = 2; 10b5-1 planned = 0 |
| 6 | **Timing context** | 12 | Buy after large drawdown / earnings miss / litigation / short attack / sector panic = up to 12; into strength = low |
| 7 | **Valuation & balance sheet** | 8 | Cheap (high B/M, low EV/EBITDA) + solid balance sheet = 8; expensive/distressed = low/neg |
| 8 | **Company size / coverage** | 6 | Low coverage / small-mid cap (above microcap floor) = 6; mega-cap = 2. *(Causal: Wu — losing 1 analyst at ≤5-coverage firm → +16% purchase abnormal return; but small-firm effect method-contested per JMZ — keep modest.)* |
| 9 | **Insider track record** | 4 | Prior buys preceded gains = 4; poor/none = 0–2 |
| 10 | **Ownership meaningfulness** | 3 | Buy materially raises stake = 3; rounding error = 0 |
| 11 | **Strategic-scarcity / theme fit** | 3 | Bottleneck/future-theme fit = 3 |
| — | **Conflicting insider selling** | −10 | Other insiders selling open-market same window |

**Tiers:** 80–100 = high-conviction alert; 60–79 = watchlist; <60 = log only. Kill switches (§9) can hard-cap/zero regardless of points.

---

## 9. False-Positive Filter

**Hard EXCLUDE (never a buy signal):**
1. Grants/RSUs/options — codes **A, M, X, C**.
2. Tax-withholding — code **F**.
3. Gifts/inheritance **G, W**; voting-trust **Z**; disposition-to-issuer **D**.
4. DRIP / dividend reinvestment (footnote).
5. ESPP / SAYE / SIP routine scheme purchases (footnote "under the Plan"; discount price).

**DOWNGRADE / kill-switch:**
6. **10b5-1 plan trades** (checkbox set).
7. **Tiny/symbolic** buys (below $ floor and %-of-salary/holding floor; drop code **L**).
8. **Loan/margin-funded or pledged** purchases (academically underperform — Garfinkel; check pledging disclosure).
9. **Compliance buys** only to meet ownership guidelines (check policy + whether below threshold near a deadline).
10. **Illiquid microcap / penny-stock / promotional** (liquidity & market-cap floor; flag abnormal volume without 8-K news; cross-ref SEC trading suspensions).
11. **Buys preceding dilution** (scan forward 30–90d for S-1/S-3/424B/8-K offerings; unless insider bought *into* the raise).
12. **Toxic-PIPE terms** (variable-conversion/repricing/death-spiral; deep contingent discounts — Brophy; Chaplinsky-Haushalter).

---

## 10. Data-Source Map (Master Table)

| Source | Geo | Data type | Free/Paid | API/Scrape/RSS | Delay | Reliability | Best use | Legal/compliance |
|---|---|---|---|---|---|---|---|---|
| SEC EDGAR (Forms 3/4/5,144,13D/G,13F,Form D,8-K) | US | All filings | Free | API+RSS+bulk | mins–T+2 | Very high (primary) | Core US feed | Low (public); honour 10/s + UA |
| OpenInsider | US | Form 4 screener | Free | Scrape | ~real-time | High | Cluster/CEO cross-check | Low–med (ToS) |
| Quiver/Fintel/Finviz | US | Form 4 + alt | Freemium/paid | API | real-time | High | US convenience/API | Low–med |
| WhaleWisdom/13F.info/HedgeFollow | US | 13F/13D/G | Free+paid | API (paid) | 45-day (13F) | High | Institutional context | Low |
| Investegate | UK | RNS archive | Free | Scrape | ~real-time | High | Best free UK feed | Med (scrape ToS) |
| LSE.co.uk / ADVFN / HL / Sharecast | UK | Director deals | Free | Scrape | ~real-time | Med-high | UK cross-check | Med |
| LSEG RNS Data Feed | UK | RNS structured | Paid | REST+WS | lowest | Very high | Production UK | Licence required |
| BaFin / FI / AMF / AFM / CONSOB stores / Oslo NewsWeb / Nasdaq Nordic / SIX | EU/EEA/CH | PDMR + holdings | Free | Mixed (SE CSV, NL CSV/XML, others scrape) | T+3 | High (official) | EU DIY ingest | Low; GDPR-aware |
| CNMV/FSMA/CBI/SEDI/ASX/EDINET/HKEX/SGX/NSE-BSE/NZX | Global | PDMR + holdings | Free | Mixed (JP API best; AU PDF hardest) | varies | High (official) | Intl expansion | Low; GDPR/local |
| InsiderScreener / InsiderPulse | EU+ | Insider feed | Freemium + API (~€25–85/mo) | API | ~daily | Med-high | Cheap EU feed | Low (licensed) |
| 2iQ / Smart Insider / VerityData | Global | Curated insider | Paid (institutional) | API/SFTP/Snowflake | ~daily | Very high | De-noised signal | Licence |
| sec-api.io | US | Filings+insider API | Paid (trial) | API | real-time | High | Turnkey US parsing | Licence |

---

## 11. Trading 212 Instrument Matching

**Official Public API (Beta)** — docs.trading212.com/api. Base URLs `https://live.trading212.com` and `https://demo.trading212.com`; API key in `Authorization` header (FLAG: key vs Basic-encoded key:secret disagree across sources — verify on live docs). Available for **Invest + Stocks ISA** accounts only (not SIPP/CFD).

- **Instruments:** `GET /api/v0/equity/metadata/instruments` — **rate limit 1 req / 50s** (cache it!). Returns array with `ticker` (namespaced, e.g. `AAPL_US_EQ` — never construct manually), `isin`, `name`, `shortName`, `currencyCode`, `type`, `workingScheduleId`, `addedOn`, `maxOpenQuantity`.
- **Exchanges:** `GET /api/v0/equity/metadata/exchanges` (1 req/30s) — id, name, workingSchedules; **NO MIC codes** (infer market from ticker segment + name).
- **No official universe CSV export**; use the API endpoint and cache, or inspect the in-app "Browse" network calls (undocumented).
- **Markets:** US (NYSE/NASDAQ), UK (LSE), EU (Xetra/Frankfurt, Euronext, Spain, …); ~10–12k instruments; **fractional shares** (executed internally) → most US/LSE/Euronext names actionable.
- **Matching best practice — ISIN first, ticker second, name last.** Pitfalls: multiple/cross-listings (one company → several ISINs/T212 lines — pick the target listing); **ADRs are a different security/ISIN** (e.g. CSR plc LSE `GB0034147388` vs NASDAQ ADR `US12640Y2054`; ADR ratios ≠ 1:1); **dual-class** (GOOG vs GOOGL); CUSIP→ISIN convert gives only the US line.
- **Python wrappers:** `python-trading212` (jcoelho93 — best for instrument pulls), `trading212-connector`, `edt-andrew/trading212-api`, `Viaduct`, `trading212-mcp-server`; TS ref `bennycode/trading212-api`.
- **FLAG:** API is Beta; **read API-Terms PDF for commercial-use/redistribution** before building on it.

**Pipeline:** pull universe once → cache → build **ISIN→T212-ticker** index (+ name/currency fallback) → match filings ISIN-first → handle ADR/dual-class/multi-listing collisions → flag is_tradable_t212.

---

## 12. Enrichment Data Sources

**Geography is the main constraint** — many free APIs are US-only. Best UK+EU on a budget: **EODHD, Stooq (free), yfinance (fragile), Finnhub/Twelve Data (paid)**.

| Provider | Coverage | Free tier | Paid (approx, verify) | Style | Notes |
|---|---|---|---|---|---|
| **yfinance** (Yahoo, unofficial) | Global (US/UK/EU) | Free | — | Py lib (scrape) | Broadest free price+fundamentals; **ToS/IP-block risk**, breaks on redesigns — fallback only |
| **EODHD** | 60+ exch incl. LSE/Euronext/Xetra | 20 calls/day EOD | EOD $19.99, +Fundamentals $59.99 (incl. insider), **All-in-one $99.99**/mo | REST | **Best low-cost tri-region**; 1000 req/min; commercial = enterprise |
| **FMP** | US free; 46+ exch paid | 250/day US | ~$22–149/mo | REST | Strong fundamentals; intl needs paid [pricing FLAG] |
| **Alpha Vantage** | US-strong | 25/day, 5/min | ~$50–250/mo | REST | Free tier near-unusable; weak intl |
| **Finnhub** | 60+ exch (intl paid) | 60/min, US + **1-yr news** | ~$12–100/mo [FLAG] | REST+WS | Free **news API** useful |
| **Polygon.io** (→massive.com) | **US-only** equities | 5/min EOD | $29/$79/$199/mo | REST+WS | Best US quality; no UK/EU; brand/URL in flux |
| **Tiingo** | US + China (+ADRs) | hourly/daily caps + news | $30–50/mo | REST | No real UK/EU |
| **Twelve Data** | US free; intl paid | 8 credits/min, 800/day | ~$29–329/mo | REST+WS | Credit model |
| **SimFin** | Mostly US | ~5yr history free | low-cost [FLAG] | Py/CSV bulk | Cheap bulk US fundamentals/dilution |
| **Stooq** | Global incl. LSE/Xetra | **Free** CSV | — | CSV-over-HTTP | Great free multi-region price history; no fundamentals |
| **OpenFIGI** (Bloomberg) | Global | **Free** (key→25k jobs/min) | — | REST batch | ISIN/SEDOL/CUSIP↔FIGI/ticker — the free identifier glue; normalise on **ISIN+FIGI** (CUSIP/SEDOL licensed) |

**Short interest:** US **FINRA** bi-monthly Equity Short Interest API + daily short-volume (free); UK **FCA** net-short positions ≥0.5% **daily XLSX** (free; SSR-2025 regime from 13 Jul 2026); EU **SSR national registers** (0.1% report/0.5% public; centralising via **ESAP from 10 Jul 2026**). Lagged — confirming signal only.

**News:** SEC EDGAR Form-4 RSS (US, free); **GDELT 2.0** (global, free); **Google News RSS** (`news.google.com/rss/search?q=...`, free, ToS-gray); Finnhub free news; Yahoo RSS (fragile); UK price-sensitive news = RNS (Investegate/LSE free, scrape).

**Recommended lean stack:** OpenFIGI (ids) + EODHD (price+fundamentals, all regions) with Stooq fallback + FINRA/FCA/EU short interest + SEC-RSS/GDELT/Google-News.

---

## 13. Technical Architecture

```
1. INGEST  →  2. NORMALISE  →  3. FILTER & MATCH  →  4. ENRICH  →  5. SCORE  →  6. AI MEMO  →  7. RANK  →  8. ALERT
```

1. **Ingest** (scheduled connectors): EDGAR FTS+Atom+Form4 XML (US, free, ≤10/s+UA); Investegate/LSE RNS (UK scrape) or LSEG feed; EU via InsiderScreener/InsiderPulse API or direct registers (SE CSV, NL CSV/XML, JP EDINET API); 13D/G/13F/Form D/8-K. Raw filings → object store (S3/R2/B2) + queue.
2. **Normalise:** parse XML/HTML/PDF → canonical Transaction schema; map codes/RNS-phrases → {BUY, SELL, NOISE}; **entity resolution** (person/vehicle→insider via Form 4 "I" footnotes + "By:" line; 13D Item 2; group rule); ticker→instrument.
3. **Filter & match:** apply false-positive rules (§9); match ticker→**Trading 212** universe (ISIN-first); drop non-tradable.
4. **Enrich:** price/drawdown/market-cap/ADV; balance sheet/dilution; cluster detection (group by issuer, rolling window); news/filings/short-interest.
5. **Score:** 0–100 model (§8) + kill switches.
6. **AI memo:** LLM generates a structured research memo (§16).
7/8. **Rank & alert:** store everything; surface only top-tier (≥80) via Telegram/email/dashboard.

**Stack (lean):** Python ingest workers; PostgreSQL (Supabase/Neon free tier to start) + object storage for raw filings; scheduler (cron / GitHub Actions → Prefect); Claude API for memos; Telegram bot / email notifier. Respect each source's rate limits & ToS.

---

## 14. Ingestion & Parsing (engineer-ready)

### 14.1 Form 4 ownership XML schema
Official spec: **"EDGAR Ownership XML Technical Specification"** (v5.x) — sec.gov/info/edgar/ownershipxmltechspec.htm; XSD `ownership4Document.xsd`.

```
<ownershipDocument>
  <schemaVersion> / <documentType>(3|4|5|/A) / <periodOfReport>
  <issuer>: <issuerCik> <issuerName> <issuerTradingSymbol>
  <reportingOwner> (repeatable):
     <reportingOwnerId>: <rptOwnerCik> <rptOwnerName>
     <reportingOwnerRelationship>: <isDirector> <isOfficer> <isTenPercentOwner>
                                    <isOther> <officerTitle> <otherText>   (1/0)
  <nonDerivativeTable> → <nonDerivativeTransaction> (repeatable):
     <securityTitle><value>
     <transactionDate><value>                         (YYYY-MM-DD)
     <transactionCoding>: <transactionFormType>(4)
                          <transactionCode>           (P,S,A,M,F,G,...)
                          <equitySwapInvolved>
                          [10b5-1 flag — see note]
     <transactionTimeliness><value>                   (E on-time | L late → signal)
     <transactionAmounts>: <transactionShares><value>
                           <transactionPricePerShare><value>
                           <transactionAcquiredDisposedCode><value>  (A|D)
     <postTransactionAmounts>: <sharesOwnedFollowingTransaction><value>
     <ownershipNature>: <directOrIndirectOwnership><value>  (D|I)
                        <natureOfOwnership><value>          (free text, e.g. "By Trust")
  <derivativeTable> → <derivativeTransaction>: + <conversionOrExercisePrice>
                       <exerciseDate> <expirationDate> <underlyingSecurity>
  <footnotes> → <footnote id="F1">text</footnote>   (value elems carry <footnoteId id="F1"/>)
```
- **10b5-1 checkbox** (EDGAR Release 23.1, ~Mar 2023): per-transaction boolean inside `<transactionCoding>` — observed tag **`aff10b5One`** [MED — verify against live XSD / a post-2023 `primary_doc.xml`]. Pre-2023: only via footnote regex `/10b5-1/i`.
- **Buy/sell determination:** `transactionCode == 'P'` AND `transactionAcquiredDisposedCode == 'A'` in the non-derivative table = open-market buy.

### 14.2 Discovering new filings
- **Real-time-ish:** Atom `https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=4&output=atom` (poll every few sec within 10/s). Also types 3,5,SC 13D,SC 13G,13F-HR.
- **Batch/backfill:** daily-index `.../edgar/daily-index/{YYYY}/QTR{N}/master.{YYYYMMDD}.idx` (pipe-delimited `CIK|Name|Form|Date|Filename`); quarterly full-index for history.
- **Content search:** EFTS `https://efts.sec.gov/LATEST/search-index?q=...&forms=4&startdt=&enddt=&ciks=&from=` (JSON, since 2001, CORS-OK; **10,000-result cap per query** → split date windows).
- **Per-filing folder:** `https://www.sec.gov/Archives/edgar/data/{CIK}/{accession}/` — resolve actual XML name via `index.json` (newer filings use `primary_doc.xml`; or extract `<XML>` block from the `{accession}.txt` SGML).
- **Per-filer:** `https://data.sec.gov/submissions/CIK{10-digit}.json`.

### 14.3 Open-source libraries
| Tool | Lang | Parses | Note |
|---|---|---|---|
| **edgartools** (dgunning) | Py | 3/4/5→typed `Ownership`, 10-K, XBRL, 13F | **Recommended.** `Company("TSLA").get_filings(form="4").head().obj()`; `get_current_filings()`; `set_identity("Name email")`; ships MCP server |
| secedgar / sec-edgar-downloader | Py | download + indexes | Lower-level |
| python-edgar (edouardswiac) | Py | builds full filing index | Good for discovery table |
| sec-api.io | REST | FTS + insider API + stream | Commercial, turnkey |
| OpenInsider | site | reference impl | Code-interpretation/cluster heuristics |

### 14.4 SEC fair-access (in code)
- **User-Agent mandatory:** `Sample Company Name AdminContact@example.com` (descriptive name + email) — missing UA → 403.
- Send `Accept-Encoding: gzip, deflate`; correct `Host`.
- **≤10 req/s aggregate** across all machines (target 5–8 with jitter); 429/403/503 → exponential backoff. Block lasts ~10 min if exceeded.
- **No CORS** on archive/browse (call from backend); `efts.sec.gov` is CORS-OK.

### 14.5 RNS / Investegate & EU machine access
- **Investegate:** scrape listing pages → JSON (Apify actor `nexgendata/investegate-rns-aggregator`; **isin/exchange null**, body not extracted → follow source_url). Expect **403/anti-bot** on direct scrape → realistic headers, proxies, Playwright, pacing.
- **LSEG RNS Data Feed v1.3:** Announcement **REST** (pull/recovery) + Real-time **WebSocket** (auth msg within 5s). Licensed.
- **Sweden FI:** marknadssok export endpoint; libs `djonsson/insynsregistret` (Py), `w3stling/insynsregistret` (Java) + `blankningsregistret` (short).
- **Netherlands AFM:** **direct CSV + XML export** (cleanest EU — schedule pulls).
- **Germany BaFin:** portal.mvp.bafin.de/database/DealingsInfo — **browse-only**, scrape.
- **Japan EDINET:** official JSON API v2 (`/documents.json?date=...&type=2&Subscription-Key=...`) + XBRL; doc types ~350/360 for 5% reports; `edinet-tools`, edinetdb.com.

---

## 15. Backtesting & Validation Methodology

### 15.1 Event-study basics
- **CAR** (additive) vs **BHAR** (compounded, the real investor experience; overshoots CAR at long horizons — Barber-Lyon 1997).
- **Abnormal-return models:** market-adjusted → market-model (α,β from estimation window) → **factor models (FF3 Mkt/SMB/HML, Carhart-4 +UMD, FF5 +RMW/CMA)**. Factor controls are essential because the raw edge lives in small/value/growth names — otherwise you measure size/value premia, not insider skill. Estimation window (~120–250 days pre-event) must **not** overlap the event window.

### 15.2 The decisive distinction: event-time vs calendar-time
- **Event-time BHAR:** line up trades in event time, compound, average. **Calendar-time portfolio (CTP):** each month form a portfolio of all "in-signal" firms, compute portfolio return, regress on factors → **intercept = alpha**.
- **Fama (1998)** & **Mitchell-Stafford (2000):** long-run BHAR has a "bad-model" problem and ignores **cross-sectional correlation** (events cluster → inflated t-stats); apparent anomalies often **shrink/vanish under calendar-time**. **Report calendar-time Jensen alpha, not just BHAR.** *(Contested: CTP has low power — Loughran-Ritter; use refinements — multiple matched controls, skewness-adjusted/bootstrapped t-stats. Report both methods.)*
- **Eckbo & Smith (1998):** under a performance-evaluation/Jensen-alpha portfolio (Oslo), insider abnormal performance was **zero/insignificant** — a live demonstration the edge can vanish under proper risk-adjustment.

### 15.3 Pitfalls that manufacture false edges
1. **Filing date vs transaction date (biggest trap):** you can only trade **after the FILING date** (Form 4 = T+2, ~17% late). Start the tradeable window at **t+1 after disclosure**, never the trade date — using trade date = look-ahead, inflates returns.
2. **Survivorship/delisting bias:** include later-delisted/bankrupt firms; apply CRSP delisting returns (often large negative), especially in small caps where the signal lives.
3. **Point-in-time fundamentals** (size/B-M as-known-then, not restated).
4. **Illiquidity/microcap concentration:** strongest returns where spreads widest & capacity lowest.
5. **Transaction costs & decimalization:** model per-name spread + commission; **cap simulated size as % of ADV**; report **gross AND net**. Insider profits shrink substantially net of costs (Seyhun); dollar profits small (Cziraki-Gider).

### 15.4 Construction & holding period
- **Long-only on purchases** (sales uninformative → shorting them adds noise/cost; hedge market-wide instead).
- **Equal- vs value-weighting flips the small-firm result** (JMZ robust under VW; Lakonishok-Lee edge mostly EW/smallest names) — **report both; the EW–VW gap is your capacity warning light.**
- **Decile sorts** on signal strength (net-purchase ratio, % of holding, #insiders, role); report monotonic forward returns + top-minus-bottom spread with t-stat.
- **Holding period:** ~½ the edge lands within a month, most within 6 months (JMZ) → **1–6 month holds, ~monthly rebalance**; clusters/high-conviction sustain longer.

### 15.5 Aggregate sentiment overlay
- **Seyhun** aggregate net insider index (predicts ~next 2 months; ~60% of 1-yr-ahead market-return variance 1975–89 — contested OOS). **Jiang-Zaman (2010):** aggregate insider trading predicts market returns via **cash-flow forecasting** (info, not just contrarian). **Vickers Sell/Buy ratio:** **<2.0 bullish, 2.0–6.0 neutral, >6.0 bearish** (the "<1.0 very bullish" cutoff is an extension). Use as a soft overlay, not a hard signal.

### 15.6 Metrics to report
Per score-bucket/decile and overall: **hit rate**; **avg forward abnormal return by bucket (EW & VW, factor-adjusted)** with monotonicity & top-bottom spread + t-stat; **calendar-time Jensen alpha vs FF3/Carhart/FF5** AND event-time BHAR (skewness-adjusted/bootstrapped) — flag divergence; **Sharpe**, **info ratio**; **max drawdown** & recovery; **turnover** + **net-of-cost** returns; **capacity** (ADV-capped). Robustness: gross vs net, EW vs VW, with/without delisting returns, sub-period stability (anomaly weakened post-decimalization/2003).

---

## 16. Operational Layer

### 16.1 AI research memo
**Model:** use the latest Claude Opus tier (e.g. `claude-opus-4-8`) for the memo step — large context (fits the full enrichment bundle without chunking), strong "answer only from supplied data" grounding, and JSON structured output. Cost levers: **Message Batches API (−50%)**, **prompt caching** on the frozen system block, and route only high-score signals to Opus (bulk to a cheaper Sonnet tier). Daily memo run isn't latency-sensitive → batch it.

**System prompt (frozen, cache it):** establishes guardrails — (1) ground strictly in supplied `<signal_data>`; (2) no fabrication / no training-data facts about the issuer; (3) distinguish fact vs inference (hedge inferences); (4) not investment advice; (5) quantify confidence; terse analyst register.

**User message (per-signal):** inject issuer, the Form 4 buy (insider, role flags, dates, filing lag, code, shares, price, % change in holding, direct/indirect), insider 24-mo history, cluster context, valuation/balance-sheet snapshot, the 0–100 score + component breakdown, and an explicit DATA GAPS list. Ask for sections: `thesis, insider_conviction_read, valuation_balance_sheet, catalysts[], risks[], score_rationale, what_would_invalidate[], confidence(enum), disclaimer`.

**Output:** constrain with `output_config.format` JSON schema (`additionalProperties:false`, all sections required) so the memo drops straight into the DB. Read `stop_reason` before parsing (raise max_tokens if truncated). Structured outputs are incompatible with citations/prefill — don't combine.

```python
resp = client.messages.create(
    model="claude-opus-4-8", max_tokens=4000,
    thinking={"type":"adaptive"},
    system=[{"type":"text","text":SYSTEM_PROMPT,"cache_control":{"type":"ephemeral"}}],
    messages=[{"role":"user","content":render_user_message(signal)}],
    output_config={"format":{"type":"json_schema","schema":MEMO_SCHEMA}},
)
```
(For the daily run wrap in `client.messages.batches.create([...])`, custom_id = signal id.)

### 16.2 Alerting
- **Telegram (primary push):** free, instant, mobile. Create bot via @BotFather; `POST https://api.telegram.org/bot<TOKEN>/sendMessage` with `chat_id`, `text`, `parse_mode` (HTML easier than MarkdownV2, which requires escaping ``_*[]()~`>#+-=|{}.!``). Limits: 4096 chars/msg; ~30 msg/s broadcast, ~1/s per chat; handle 429 via `retry_after`.
- **Email (digest):** Amazon SES (~$0.10/1k — leanest) or SMTP2GO free tier; **SendGrid free plan retired May 2025**. Use for daily/weekly digests, not per-signal.
- **Web dashboard (system-of-record):** FastAPI/Flask/Streamlit over the Postgres `alerts`/`memos` tables; triage UI, filters, filing links. Telegram/email link back to it.

### 16.3 Postgres schema (DDL sketch)
Tables: **filings** (raw, immutable; `accession_no` unique, `raw_uri`+`raw_sha256`), **issuers**, **instruments** (issuer_id, ticker, **isin unique**, figi, exchange, **t212_ticker/t212_isin**, is_tradable_t212), **insiders** (cik unique, entity_type), **insider_roles** (N-N insider↔issuer, role flags, observed_from/to), **transactions** (filing_id, insider_id, issuer_id, instrument_id, txn_date, txn_code, acquired_disposed, is_derivative, shares, price, **usd_value generated**, shares_owned_after, ownership_nature; UNIQUE tuple for dedup; partial index `WHERE txn_code='P'`), **scores** (transaction_id, score, **components jsonb**, model_version, **enrichment jsonb** snapshot), **memos** (score_id, **body jsonb**, llm_model, tokens), **alerts** (score_id, channel, status, **dedup_key unique** for idempotency, sent_at). Natural-key UNIQUEs on filings/transactions/alerts give end-to-end idempotency.

### 16.4 Orchestration
- **cron** (intraday) or **GitHub Actions** (`schedule:`, free, secrets/logs — best lean daily) → graduate to **Prefect** for retries/backfill/observability. Skip Airflow unless many interdependent DAGs.
- **Idempotency:** `INSERT ... ON CONFLICT DO NOTHING` on natural keys; amendments (`4/A`) → match `(cik_reporting,txn_date,code,shares,price)`, prefer latest accession; store `raw_sha256`.
- **Backfill:** iterate date windows (EFTS 10k-result cap), upsert. Store raw filings (S3/R2/B2 `form4/{cik}/{accession}.xml`) for reproducibility; `scores.enrichment` snapshot reproduces memos exactly.

### 16.5 Cost envelope (lean, ~3,000 memos/mo)
SEC data **$0**; enrichment **$0–50**; **LLM ~$60–120** (Opus 4.8 raw ~$232 → Batches −50% → ~$116, less with caching / Sonnet for bulk); Telegram **$0**; email **$0–1**; raw storage **~$1**; hosting **$0–10**; Postgres **$0–15**. **Total ≈ $65–160/mo**, dominated by LLM — biggest lever is Batches + caching + Opus-only-for-high-scores → toward ~$70/mo.

---

## 17. MVP Build Plan (phased)

- **Phase 0 (wk 1–2) — US Form-4 buy detector.** Poll EDGAR Atom (type 4); parse Form 4 XML; keep code **P**; 10/s+UA. Store to Postgres; daily CSV/Telegram of all US insider open-market buys.
- **Phase 1 (wk 3–4) — Filter + cluster + score.** False-positive rules (10b5-1 box, $ floor, microcap floor); cluster (≥3 CIK/15d); 0–100 score; match to T212 universe (ISIN-first). → ranked, filtered, tradable shortlist.
- **Phase 2 (wk 5–6) — Enrichment + AI memo.** Price/drawdown/mcap/ADV/dilution + news/filings; LLM memo per top candidate; alert ≥80.
- **Phase 3 (wk 7–8) — UK.** Investegate RNS ingest; map PDMR phrasing; TR-1 early-accumulation signal.
- **Phase 4 (wk 9–10) — Institutional overlay.** 13D/Item-4 activist + 13G→13D; 13F as stale context.
- **Phase 5 (wk 11+) — Europe.** InsiderScreener/InsiderPulse API (or SE CSV + NL CSV/XML + JP EDINET DIY).
- **Always:** backtest the score (§15) against forward returns before trusting weights; expect the edge in small/mid-caps & clusters, and net-of-cost returns thinner than gross.

---

## 18. Example Alert Format

```
🟢 SMART-MONEY ALERT — Score 87/100 (HIGH CONVICTION)
─────────────────────────────────────────────
TICKER: XYZ | XYZ Industries plc (LSE, GBp) | Tradable on T212: ✅ (ISIN GB00XXXXXXXX)
SIGNAL: Cluster open-market buy — 4 insiders in 9 days

INSIDERS
 • J. Smith (CEO, founder)  £412,000  market purchase  +38% to holding  2026-06-12
 • A. Patel (CFO)           £96,000   market purchase                   2026-06-11
 • R. Lee (Chair)           £150,000  market purchase                   2026-06-05
 • M. Cole (Non-exec)       £22,000   market purchase                   2026-06-04
 Discretionary (no 10b5-1). No insider selling in window.

CONTEXT
 • Price -41% from 12-mo high; bought after FY earnings miss (2026-05-30)
 • Mkt cap £310m (small-cap, 2 analysts) | ADV ~£1.1m
 • Net cash positive; no equity raise filed in last 12m; share count flat
 • Valuation: EV/EBITDA 6.1x vs 5-yr avg 11x

SCORE: Txn 20 | Role 12 | Cluster 11 | Size 11 | Discretion 8 | Timing 11
       Valuation 7 | Coverage 5 | Track 3 | Ownership 3 | Theme 2 | Selling 0
KILL SWITCHES: none

AI MEMO: Founder + CFO + Chair + NED all buying personal cash into a post-miss 41%
drawdown, no dilution on the horizon, net cash, cheap vs history. Textbook
opportunistic cluster. Risks: single FY miss may signal demand softness; small-cap
liquidity. Invalidated by: equity raise, further guidance cut, insider selling.

FILINGS: [RNS PDMR links]   DISCLAIMER: research only, not advice.
```

---

## 19. Master Source List (websites / APIs / feeds)

**US official:** EDGAR Full-Text Search (efts.sec.gov) · EDGAR Atom/RSS · data.sec.gov · EDGAR full-index & Form 4 XML · SEC structured-disclosure RSS · SEC DERA Insider Transactions Data Sets [verify URL].
**US aggregators:** OpenInsider · Quiver Quantitative · Fintel · Finviz Elite · WhaleWisdom · 13F.info · HedgeFollow · sec-api.io · GuruFocus · Washington Service · VerityData/InsiderScore · InsiderTracking/INK.
**UK:** Investegate · London South East (lse.co.uk/rns) · LSEG RNS Data Feed (rns-distribution.com) · FCA ESS (TR-1) · ADVFN Director Deals · Hargreaves Lansdown / Sharecast · Apify Investegate actor.
**EU registers:** BaFin DealingsInfo (DE) · FI Insynsregistret (SE, CSV) · AMF BDIF (FR, RSS) · AFM MAR19 (NL, CSV/XML) · CONSOB/eMarketStorage/1INFO (IT) · Finanstilsynet OAM (DK) · Euronext Oslo NewsWeb (NO) · Nasdaq Helsinki (FI) · SIX/SER (CH) · CNMV (ES) · FSMA (BE) · Central Bank of Ireland / Euronext Dublin (IE).
**Intl registers:** SEDI/sedi.ca (CA) · ASX announcements + ASIC Forms 603/604/605 (AU) · EDINET API (JP) · HKEX DI / di.hkex.com.hk + CCASS (HK) · SGX announcements / Form 7 (SG) · NSE/BSE + NSDL SDD (IN) · NZX announcements (NZ).
**EU/Asia aggregators:** 2iQ Research · InsiderScreener · InsiderPulse · Smart Insider · EDINET DB · MarketScreener · Koyfin · Simply Wall St.
**Institutional:** EDGAR 13F/13D/13G · WhaleWisdom · 13F.info · HedgeFollow · Fintel · sec-api.io.
**Enrichment (price/fundamentals):** EODHD · Stooq · yfinance · FMP · Alpha Vantage · Finnhub · Polygon/massive · Tiingo · Twelve Data · SimFin · OpenFIGI.
**Short interest:** FINRA Equity Short Interest (US) · FCA daily XLSX (UK) · ESMA/ESAP + BaFin/AMF/CNMV/CONSOB/AFM (EU).
**News:** SEC Form-4 RSS · GDELT 2.0 · Google News RSS · Finnhub news · exchange RSS.
**Brokerage/matching:** Trading 212 API (docs.trading212.com/api) · python-trading212 · OpenFIGI.
**Tooling:** edgartools (dgunning) · secedgar · python-edgar · insynsregistret libs (djonsson/w3stling) · edinet-tools.

---

## 20. Legal & Ethical Boundaries

- **Public information only.** Every source here is a mandated public disclosure or a licensed aggregator of one. **Never** use hacked, leaked, private, confidential, or otherwise material non-public information (MNPI) — trading on MNPI is illegal insider trading. This engine reads *what insiders are legally required to disclose after they trade* — it does not front-run undisclosed information.
- **Respect access terms.** Honour robots.txt, rate limits (SEC ≤10/s + UA), and each site's ToS. RNS/LSEG and many vendors license their feeds — **commercial redistribution requires a licence**; personal research use is generally permitted but verify (incl. Trading 212 API Terms, CUSIP/SEDOL licensing — normalise on freely-usable ISIN/FIGI).
- **Data protection.** EU/UK registers deliberately omit some personal data (e.g. DOB); don't re-identify or re-publish beyond what's disclosed; stay within GDPR if storing EU personal data.
- **No manipulation / no advice.** This is a research-discovery tool. Don't use it to coordinate trading, amplify promotions, or manipulate thin stocks. Outputs are **research, not financial advice** — label every alert/memo accordingly.
- **Honesty & provenance.** Treat vendor coverage/performance claims as marketing until verified; preserve confidence tags; surface contested findings rather than overstating the edge.

---

## 21. Appendix — Contested Claims & Key Citations

### 21.1 Carry these caveats into design
- **Small-firm effect:** strong in Lakonishok-Lee & Seyhun (informativeness / equal-weighted) but **not significant in JMZ** (value-weighted performance-evaluation). Not universal — keep size weight modest.
- **Raw trade size:** positively related to returns by *volume* (JMZ) but **% returns negatively correlated with raw $ size** (Cziraki-Gider) — normalise to holdings/salary, never reward absolute $.
- **Net-of-cost outsider edge:** gross signal real (~6–10%/yr top specs) but **shrinks/vanishes** after costs and trade-size caps (Seyhun; Eckbo-Smith; FRL 2024) — capacity-limited, concentrates in small/illiquid names.
- **Buyback long-run drift (ILV):** robust in event-time/FF models, **contested under calendar-time** (Fama; Mitchell-Stafford). Announcement-window return is the robust part.
- **SWF & strategic-investor long-run:** announcement pop reliably positive; long-run debated (passivity/"SWF discount" vs value-creation when active/transparent).
- **Contrarian mechanism:** info vs mispricing — both operate (Piotroski-Roulstone); unresolved.
- **Short-attack buys:** Wang-Zheng positive, but **squeeze pops often fully reverse** (Stice-Lawrence) — transient.
- **Kang-Kim-Wang cluster magnitude:** working-paper status; numbers via secondary reviews.
- **Fees-in-shares:** no isolating study — low-weight corroborator only.
- **Aggregate Seyhun 60% R²** and long-run anomaly robustness: contested out-of-sample — soft overlay only.
- **Drake-Roulstone-Thornock** ≠ insider-trading source (it's info-demand/EDGAR-downloads) — use Piotroski-Roulstone / Brochet et al. / Choi et al. instead.
- **Unverified vendor/regulator specifics:** institutional pricing (2iQ, Smart Insider, Verity, LSEG, SharePad), several API/export availabilities (CNMV/HKEX/SGX CSV, Norway/Finland consumer API, BaFin export), Trading 212 auth-header format & commercial-use terms, the `aff10b5One` XML tag spelling, SEC DERA dataset URL — confirm before depending on them.

### 21.2 Key academic citations (for backtest grounding)
Lakonishok & Lee (2001, RFS) · Jeng, Metrick & Zeckhauser (2003, REStat) · Cohen, Malloy & Pomorski (2012, JF "Decoding Inside Information") · Seyhun (1986 JFE; 1992 QJE; 1998 MIT Press) · Wang, Shin & Francis (2012, JFQA — CFO>CEO) · Wu (analyst-coverage causal) · Aboody & Lev (2000, JF — R&D) · Rozeff & Zaman (1998, JF) · Jenter (2005, JF) · Piotroski & Roulstone (2005, JAE) · Marin & Olivier (2008, JF) · Cziraki & Gider (2021, Review of Finance) · Brochet (2010, Accounting Review) · Eckbo & Smith (1998, JF) · Alldredge & Blank (2019, JFR) · Kang, Kim & Wang (2018, WP) · Anderson & Reeb (2003, JF) · Villalonga & Amit (2006, JFE) · Anderson, Reeb & Zhao (2012, JF) · Krishnamurthy, Spindt, Subramaniam & Woidtke (2005, JFI) · Floros, Nagarajan & Sivaramakrishnan (2019, RQFA) · Hertzel, Lemmon, Linck & Rees (2002, JF) · Brophy, Ouimet & Sialm (2009, RFS) · Ikenberry, Lakonishok & Vermaelen (1995, JFE) · Comment & Jarrell (1991, JF) · Allen & Phillips (2000, JF) · Chan, Kensinger, Keown & Martin (1997, JFE) · Kotter & Lel (2011, JFE) · Bortolotti, Fotak & Megginson (2015, RFS) · Dargenidou, Tonks & Tsoligkas (2018, JBFA) · Wang & Zheng (2022, JBFA) · Stice-Lawrence, Wong & Zhao (2025, JAR) · Jiang & Zaman (2010, JBF) · Fama (1998, JFE) · Mitchell & Stafford (2000, JB) · Barber & Lyon (1997) · Kothari & Warner (Econometrics of Event Studies).

---

*End of manual. Built from public sources only; no financial advice. Verify FLAG-ged items before relying on them in production.*
