#!/usr/bin/env python3
# Weighted opportunity scoring. Each idea scored 1-10 on 10 criteria.
# For "Competition", 10 = wide-open / weak incumbents, 1 = brutal, well-funded knife-fight.
# Weights emphasise the things that actually determine EV for a solo, no-network,
# £10k, AI-leveraged 19yo founder: defensibility, low competition, and realistic
# probability of crossing £100k and especially £1m ARR.

CRITERIA = ["FMF","Ease","Rev","Def","AI","Comp","Speed","P100k","P1m","Large"]
WEIGHTS  = {"FMF":1.0,"Ease":1.0,"Rev":1.0,"Def":1.5,"AI":0.75,
            "Comp":1.5,"Speed":1.0,"P100k":1.5,"P1m":2.0,"Large":0.75}
WSUM = sum(WEIGHTS.values())

# idea : [FMF, Ease, Rev, Def, AI, Comp, Speed, P100k, P1m, Large]
ideas = {
# --- INTELLIGENCE / DATA ---
"Planning Application Intelligence":        [6,6,6,3,7,2,6,5,3,3],
"Tender Intelligence":                      [6,6,7,3,7,2,6,5,3,3],
"Procurement Intelligence":                 [6,5,7,3,7,2,5,5,3,4],
"Public Filing Intelligence":               [6,6,6,3,8,3,6,5,3,3],
"Alternative Data Platform":                [7,3,8,5,7,4,3,4,3,5],
"Future Companies Database":                [6,4,6,4,7,5,4,4,3,3],
"Defence Supply Chain Intelligence":        [8,3,7,6,6,6,2,3,3,5],
"Grid / Energy Infrastructure Intelligence":[8,5,8,7,7,7,4,6,5,6],
"Grant Intelligence":                       [5,6,5,3,7,2,6,4,2,3],
"Private Company Intelligence":             [6,4,7,4,7,3,4,4,3,4],
"Executive Movement Intelligence":          [5,6,6,4,7,5,5,5,3,3],
"M&A Intelligence":                         [7,4,7,4,7,4,3,4,3,4],
"Infrastructure Project Intelligence":      [8,5,7,6,7,6,4,5,4,5],
"Government Contract Intelligence":          [6,5,7,3,7,2,5,5,3,4],
"Data Centre Tracker":                      [8,6,6,5,7,6,5,5,4,4],
"Solar Farm Tracker":                       [7,6,5,5,7,6,5,4,3,3],
"Battery Storage Tracker":                  [7,6,5,5,7,7,5,4,3,3],
"Housing Development Tracker":              [6,6,5,3,7,3,6,4,3,3],
"Regeneration Project Tracker":            [6,5,4,4,7,5,5,4,2,3],
"Public Sector Spend Tracker":             [5,6,5,3,7,2,6,4,2,3],
"Supplier Intelligence Database":          [6,5,6,4,7,4,5,4,3,4],
"Startup Funding Tracker":                 [6,6,5,2,7,2,6,4,2,3],
"Industry Intelligence Terminal":          [7,3,8,5,6,5,2,4,3,5],
# --- AI AGENTS ---
"Autonomous Research Agent":               [7,5,6,3,8,2,5,4,3,4],
"AI Equity Analyst":                       [8,5,7,4,8,3,5,5,3,4],
"AI Due Diligence Agent":                  [7,4,7,5,8,5,3,4,3,4],
"AI Acquisition Scout":                    [8,5,7,6,8,6,4,6,5,5],
"AI Competitor Monitoring Agent":          [6,6,5,3,8,3,6,4,3,3],
"AI Tender Agent":                         [6,5,7,4,8,2,5,5,3,4],
"AI Grant Agent":                          [5,5,5,3,8,2,5,4,2,3],
"AI Planning Agent":                       [6,5,6,5,8,5,4,5,4,4],
"AI Market Mapping Agent":                 [7,5,6,4,8,4,5,4,3,4],
"AI Supplier Discovery Agent":             [6,5,6,4,8,4,5,4,3,4],
"AI Prospecting Agent":                    [5,5,6,2,8,2,6,4,2,3],
"AI Procurement Agent":                    [6,4,7,4,8,3,4,5,3,4],
"AI M&A Agent":                            [7,4,7,5,8,5,3,4,3,4],
"AI Startup Scout":                        [7,5,6,4,8,4,5,4,3,4],
# --- VERTICAL SOFTWARE ---
"School Operations Platform":              [3,4,6,6,6,5,3,5,4,5],
"School Staffing Platform":                [3,4,6,6,7,5,3,5,4,5],
"Childcare Software":                      [3,4,6,6,6,5,3,5,4,5],
"Tender Management Platform":              [6,4,7,5,7,3,3,5,4,5],
"Planning Consultant Software":            [6,5,6,6,7,6,4,6,5,5],
"Property Research Platform":              [6,5,6,4,7,3,4,4,3,4],
"Procurement Workflow Platform":           [6,4,7,5,7,3,3,5,4,5],
"Consultancy Operating System":            [5,4,6,5,7,4,3,4,3,4],
"Vertical CRM":                            [4,4,6,5,6,3,4,5,4,5],
# --- SEARCH ENGINES ---
"Planning Search Engine":                  [6,6,4,2,7,3,6,3,2,2],
"Tender Search Engine":                    [6,6,4,2,7,2,6,3,2,2],
"Procurement Search Engine":               [6,6,4,2,7,2,6,3,2,2],
"Defence Supplier Search Engine":          [8,4,5,5,7,7,4,4,3,3],
"Infrastructure Search Engine":            [7,5,5,4,7,6,5,4,3,3],
"Acquisition Search Engine":               [7,5,6,4,7,5,5,4,3,4],
"Business Opportunity Search Engine":      [6,4,5,3,7,4,4,3,2,3],
# --- ACQUISITION / DEAL FLOW ---
"Website Acquisition Scanner":             [6,7,5,4,8,5,6,5,3,3],
"SaaS Acquisition Scanner":                [7,6,6,4,8,4,6,5,4,4],
"Small Business Acquisition Database":     [7,6,7,6,8,6,5,6,5,5],
"Search Fund Deal Flow Platform":          [8,5,8,7,8,7,4,6,5,6],
"Local Monopoly Finder":                   [7,6,6,5,8,7,5,5,4,4],
"Industry Roll-Up Scanner":                [7,5,7,6,8,6,4,5,4,5],
# --- HYBRID ---
"Bloomberg for Planning Applications":     [6,4,7,4,7,3,3,4,3,4],
"Bloomberg for Infrastructure":            [8,4,8,6,7,6,3,5,4,6],
"Bloomberg for Procurement":               [6,4,7,4,7,3,3,4,3,4],
"Bloomberg for Defence Suppliers":         [8,3,7,6,7,7,2,3,3,5],
"PitchBook for Retail Investors":          [7,4,7,4,8,4,3,4,3,5],
"Crunchbase for Infrastructure":           [7,5,6,5,7,6,4,5,4,5],
"Opportunity Operating System":            [6,3,6,3,7,5,3,3,2,3],
"AI-Powered Opportunity Radar":            [6,4,6,3,8,4,4,3,2,3],
# --- MY ADDITIONS (hidden / asymmetric) ---
"SME Deal Origination Engine (off-market sourcing-as-a-service)": [8,6,8,7,8,7,5,7,5,6],
"Done-for-you Tender Agency (outcome-priced, niche)":            [7,7,7,5,8,5,7,7,5,4],
"Vertical AI for Planning Consultants (DFY research+reports)":   [6,6,6,6,8,6,5,6,5,5],
"Regulated Compliance/Reporting Agent (SECR/EPR/buildingsafety)":[5,6,6,6,8,7,5,6,5,5],
"AI Equity Research for under-covered UK small caps":            [9,6,6,4,8,5,5,5,3,4],
"Companies House Change-Signal Intelligence":                    [7,7,6,4,8,5,6,5,4,4],
"Energy Procurement / PPA Intelligence":                         [7,4,7,6,7,7,3,5,4,5],
"Data-Centre Site Origination Intelligence":                     [8,4,8,7,7,8,3,5,5,6],
"Council / Local-Gov Decision Monitoring (lobby+dev intel)":     [6,6,6,5,8,6,5,5,4,4],
"AI Ops Copilot for a Boring Vertical (e.g. surveying/EPC)":     [5,5,7,6,8,6,4,6,5,6],
"Litigation / Claims / Funding Intelligence":                    [6,3,7,6,7,7,3,4,4,5],
}

def weighted(scores):
    return sum(scores[i]*WEIGHTS[CRITERIA[i]] for i in range(10))/WSUM

ranked = sorted(ideas.items(), key=lambda kv: weighted(kv[1]), reverse=True)

print(f"{'#':>3}  {'SCORE':>5}  IDEA")
print("-"*78)
for i,(name,sc) in enumerate(ranked,1):
    print(f"{i:>3}  {weighted(sc):>5.2f}  {name}")

print("\n\n=== TOP 10 SUB-SCORE DETAIL ===")
hdr = "  ".join(f"{c:>5}" for c in CRITERIA)
print(f"{'IDEA':<52} {hdr}  WTD")
for name,sc in ranked[:10]:
    row = "  ".join(f"{v:>5}" for v in sc)
    print(f"{name:<52} {row}  {weighted(sc):.2f}")
