
import pandas as pd

# ---- 1. Load the full bulk file ----
INPUT_FILE = "WDICSV.csv"
OUTPUT_FILE = "wdi_education_filtered.csv"

df = pd.read_csv(INPUT_FILE)

# ---- 2. Indicators: Education & Literacy theme ----
indicator_codes = [
    "SE.ADT.LITR.ZS",      # Literacy rate, adult total
    "SE.ADT.LITR.FE.ZS",   # Literacy rate, adult female
    "SE.ADT.LITR.MA.ZS",   # Literacy rate, adult male
    "SE.PRM.ENRR",         # School enrollment, primary (% gross)
    "SE.SEC.ENRR",         # School enrollment, secondary (% gross)
    "SE.TER.ENRR",         # School enrollment, tertiary (% gross)
    "SE.PRM.CMPT.ZS",      # Primary completion rate, total
    "SE.PRM.ENRR.FE",      # Primary enrollment, female
    "SE.PRM.ENRR.MA",      # Primary enrollment, male
    "SE.ENR.PRIM.FM.ZS",   # Gender parity index, primary enrollment
    "SE.XPD.TOTL.GD.ZS",   # Government expenditure on education (% GDP)
    "SP.POP.TOTL",         # Population, total (context)
    "NY.GDP.PCAP.CD",      # GDP per capita, current US$ (context)
]

# ---- 3. Countries: Kenya + comparators + regional/world aggregates ----
country_codes = [
    "KEN",  # Kenya
    "UGA",  # Uganda
    "TZA",  # Tanzania
    "RWA",  # Rwanda
    "ETH",  # Ethiopia
    "NGA",  # Nigeria
    "ZAF",  # South Africa
    "SSF",  # Sub-Saharan Africa (aggregate)
    "WLD",  # World (aggregate)
]

filtered = df[
    df["Indicator Code"].isin(indicator_codes)
    & df["Country Code"].isin(country_codes)
]

filtered.to_csv(OUTPUT_FILE, index=False)

print(f"Done. Filtered {len(df):,} rows down to {len(filtered):,} rows.")
print(f"Saved to: {OUTPUT_FILE}")
print("Upload this file to Claude to continue.")
