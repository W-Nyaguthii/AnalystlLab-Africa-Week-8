# Education & Literacy in Kenya: A Regional Development Analytics Study

**AnalystLab Internship - Week 8 Final Capstone Project**
**Author:** Primrose Wambui

An end-to-end data analytics project benchmarking Kenya's school enrollment, literacy, and education
financing against six East & Southern African peer countries and global averages, using World Bank
World Development Indicators (WDI) data from 1990–2024.

---

## Objective

How does Kenya's education system compare to its regional peers, and where should stakeholders focus
improvement efforts? This project applies the full data analytics workflow - sourcing, cleaning, analysis, visualization, and reporting - to answer that question using publicly available development data.

## Data Source

- **World Bank World Development Indicators (WDI)**
  https://datatopics.worldbank.org/world-development-indicators/
- 13 indicators covering literacy, school enrollment (primary/secondary/tertiary), completion rates,
  gender parity, and government education spending
- 9 countries/aggregates: Kenya, Uganda, Tanzania, Rwanda, Ethiopia, Nigeria, South Africa, Sub-Saharan Africa (regional aggregate), World
- Coverage: 1990–2024

## Tools Used

- **Python** (pandas) — data cleaning, reshaping, and statistical analysis
- **Power BI Desktop** — interactive dashboard with KPI cards, slicers, and cross-filtered visuals
- **DAX** — custom measures to correctly surface each country's most recent reported value per indicator
- **Excel** — clean data export formatted for Power BI import

## Methodology

1. **Scoping** — narrowed the ~1,400-indicator WDI bulk file down to 13 education/literacy indicators across 9 countries, rather than working with the full multi-gigabyte dataset.
2. **Cleaning** — reshaped from wide (year columns) to tidy long format, standardized types, checked for duplicates, and deliberately left missing values as null rather than imputing them.
3. **Calculated fields** — derived primary enrollment gender gap, literacy gender gap, and an education-spending-per-capita proxy not directly available in the raw indicators.
4. **Analysis** — combined time-series trend analysis (for densely-reported indicators like enrollment) with point-in-time cross-country comparison (for sparsely-reported indicators like literacy), plus pooled correlation analysis between education spending and enrollment outcomes.
5. **Dashboard** — built in Power BI using a `Latest Value` DAX measure that finds each country's most recent *non-blank* reported year per indicator, since different countries and indicators have very different reporting cadences (e.g. literacy is surveyed roughly once a decade).

## Key Findings

- Kenya's primary enrollment is near-universal (~98%, 2023); the steepest drop in Kenya's education pipeline occurs between secondary (84%) and tertiary (10%) education, not between primary and secondary.
- Kenya outperforms Uganda, Tanzania, Ethiopia, Nigeria, and Rwanda on secondary enrollment by a wide margin, positioning it as a regional leader rather than an average performer.
- Education spending (% of GDP) and secondary enrollment show a moderate positive correlation (Pearson r = 0.42, r² ≈ 0.18) across the comparator set — spending level alone explains only part of the outcome.
- Literacy data is structurally sparse (measured via infrequent censuses, not annual reporting) - Kenya's most recent WDI literacy figure dates to 2000, which limits how confidently it can be used for current-state claims.
- A data-quality anomaly (a sharp, likely spurious dip in Kenya's 2019 primary enrollment figure) is documented and flagged rather than treated as a real policy signal.

Full findings, insights, and recommendations are in
[`WDI_Education_Kenya_Final_Report.pdf`].

*Prepared as part of the AnalystLab Data Analytics Internship program.*
