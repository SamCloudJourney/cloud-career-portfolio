#!/usr/bin/env python3
"""
Verify which tickers from the global insider world list are actually tradable on
Trading 212, using the official T212 API.

USAGE:
  1. In the Trading 212 app: Settings -> API (Beta) -> generate a key (read scope is enough).
  2. export T212_API_KEY="your_key_here"          (live account)
     # or set T212_BASE=https://demo.trading212.com for a practice-account key
  3. python3 verify_t212.py

It pulls the FULL instruments list (cached locally; the endpoint is rate-limited to
1 request / 50s) and reports which of our world-list tickers match by ISIN/ticker/name.

NOTE: your API key stays on your machine. Read the T212 API Terms re: usage.
"""
import os, sys, json, time, urllib.request

BASE = os.environ.get("T212_BASE", "https://live.trading212.com")
KEY  = os.environ.get("T212_API_KEY")
CACHE = "t212_instruments.json"

# World-list candidates (edit freely). Plain tickers; we match loosely against T212's
# namespaced tickers (e.g. AAPL_US_EQ) and names.
WORLD_LIST = [
    # US
    "HOOD","NVRI","NCLH","IFF","AUPH","MNSO","RDN","FUN","MEOH","NSP","TXO","GPGI",
    "AWRE","AAT","EYE","BLND","SOFI","GGB","SGML","QNT","AUR","COE",
    # UK (London)
    "RAT","AJB","MPAC","DOCS","SRC","BLND","KRM",
    # EU
    "CLARI","CON","SCR","MTLN","RAY","ORK","MONT","AZE","SUY1V","RUSTA","BRAV",
    # non-Western (expected NOT on T212 - sanity check)
    "TOU","1378","AXIA","J36","INDUSINDBK","064350","9607","UOS","6027","3393","TPIA",
]

def get(path):
    if not KEY:
        sys.exit("Set T212_API_KEY (and optionally T212_BASE). See header.")
    req = urllib.request.Request(BASE + path, headers={"Authorization": KEY})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def load_instruments():
    if os.path.exists(CACHE):
        return json.load(open(CACHE))
    print("Fetching full instrument list (1 req / 50s limit)...")
    data = get("/api/v0/equity/metadata/instruments")
    json.dump(data, open(CACHE, "w"))
    print(f"Cached {len(data)} instruments -> {CACHE}")
    return data

def main():
    inst = load_instruments()
    # build quick indices
    by_ticker_prefix = {}
    for it in inst:
        t = (it.get("ticker") or "")
        by_ticker_prefix.setdefault(t.split("_")[0].upper(), []).append(it)
    names = [(it.get("name","").upper(), it) for it in inst]

    print(f"\n{'INPUT':10} {'ON T212?':9} MATCH (ticker | name | currency)")
    print("-"*80)
    for sym in WORLD_LIST:
        hits = by_ticker_prefix.get(sym.upper(), [])
        if hits:
            h = hits[0]
            print(f"{sym:10} {'YES':9} {h.get('ticker'):16} {h.get('name','')[:34]:34} {h.get('currencyCode','')}")
        else:
            # fallback: loose name contains
            nm = [it for n,it in names if sym.upper() in n][:1]
            if nm:
                h = nm[0]
                print(f"{sym:10} {'MAYBE':9} {h.get('ticker'):16} {h.get('name','')[:34]:34} {h.get('currencyCode','')}")
            else:
                print(f"{sym:10} {'NO':9} -- not found --")

if __name__ == "__main__":
    main()
