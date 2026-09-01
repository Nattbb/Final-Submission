# 🌍 Global World Development Indicators Analysis (2000–2023)
**AnalystLab Africa — Data Analytics Capstone Project**

---

## 📌 Executive Summary
This project provides an end-to-end data analytics study evaluating global economic performance, public health indicators, internet adoption, and carbon intensity using the World Bank's **World Development Indicators (WDI)** dataset.

The analysis cleans and reshapes 24 years of observational data across 200+ countries to analyze how economic growth (`GDP Per Capita`) interacts with public health (`Life Expectancy`), digital transformation (`Internet Users %`), and environmental sustainability (`CO2 Per Capita`).

---

## 🎯 Project Objectives
- Clean, unpivot, and transform wide-format World Bank CSV data into a tidy relational model using **Python (`pandas`)**.
- Analyze key socio-economic metrics across regions and income classifications.
- Build an interactive **Tableau Dashboard** to enable multi-metric exploratory data analysis.
- Provide strategic, data-backed recommendations for global policy stakeholders.

---

## 🛠️ Technology Stack
- **Data Transformation & Cleaning:** Python (Pandas, NumPy, Google Colab)
- **Data Visualization & Analytics:** Tableau Desktop / Tableau Public
- **Documentation & Reporting:** WeasyPrint / HTML to PDF engine
- **Version Control & Hosting:** GitHub

---

## 📊 Key Indicators Tracked

| Indicator Code | Metric Name | Category | Analytical Focus |
|---|---|---|---|
| `NY.GDP.MKTP.CD` | GDP (Current US$) | Economy | Total Economic Output |
| `NY.GDP.PCAP.CD` | GDP Per Capita (Current US$) | Living Standard | Individual Economic Wealth |
| `SP.DYN.LE00.IN` | Life Expectancy at Birth | Health | Quality of Healthcare & Life |
| `SP.POP.TOTL` | Total Population | Demographics | Metric Normalization |
| `EN.ATM.CO2E.PC` | CO2 Emissions (Per Capita) | Environment | Ecological Footprint |
| `IT.NET.USER.ZS` | Internet Users (% of Population) | Technology | Digital Readiness & Adoption |

---

## 🧹 Data ETL & Cleaning Pipeline
The raw dataset (`WDI_CSV.csv`) contains wide-format columns for each year from 1960 to 2023. The Python cleaning script (`scripts/data_cleaning.py`) performs the following steps:
1. **Filtering Target Indicators:** Isolates the 6 target metrics.
2. **Unpivoting (Melting):** Transforms year columns (2000–2023) into vertical rows.
3. **Filtering Aggregates:** Excludes regional and income-group aggregates (e.g., *World*, *Sub-Saharan Africa*, *High Income*) to preserve country-level granular data.
4. **Pivoting to Tidy Format:** Converts cleaned indicators into individual columns.
5. **Exporting:** Saves structured data as `WDI_Cleaned_Data.csv`.

---

## 💡 Key Analytical Insights
1. **Health vs. Wealth Logarithmic Curve:** Incremental economic growth in low-income nations yields dramatic life expectancy increases ($0–$12k USD). Above $15k USD per capita, health improvements diminish and plateau around 80+ years.
2. **Digital Economy Acceleration:** Nations with internet adoption rates above 60% exhibit higher service-sector expansion and sustained GDP growth trajectories.
3. **Green Decoupling:** Emerging economies experience rising CO2 emissions alongside GDP growth, whereas advanced nations show economic output growth alongside stabilizing or declining per capita carbon emissions.

---

## 🚀 How to Run the Project

### 1. Run Data Cleaning in Python
```bash
python scripts/data_cleaning.py
