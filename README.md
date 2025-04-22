# DemoCraft-Analytics(Crafting Deep Insights from World Population Trends)
![WPP Rate Analysis](https://github.com/almazid82/DemoCraft-Analytics-Crafting-Deep-Insights-from-Global-Demographic-Trends-/blob/main/wpp%20rate%20analysis.jpg?raw=true)


> "What if you could see the future of our planet — not through predictions, but through patterns hidden in numbers?"

Welcome to **DemoCraft Analytics**, a data-driven journey into the evolving story of the world's population. Using real demographic datasets from trusted global sources, this project uncovers the hidden rhythms behind birth rates, aging populations, life expectancy, urbanization, and the subtle shifts that silently shape the future of nations.

From policy makers and development planners to curious analysts and climate researchers — understanding demographic dynamics is **no longer optional**. It’s essential.

**In this project, we aim to:**
- Visualize global population trends using interactive heatmaps and dynamic charts
- Analyze how different regions are growing, aging, or shrinking
- Correlate population patterns with economic, environmental, and social indicators
- Highlight key demographic insights for data-driven policy recommendations

Stay with us as we decode the human data behind headlines, build predictive models for future trends, and explore how demographics silently define the course of history.

**Let’s not just analyze data — let’s craft a story from it.**

> _Because every number has a name. Every chart has a future._

You can download the World Population 2024 demographic indicators Excel file from the following link:

[Download Excel File](https://github.com/almazid82/DemoCraft-Analytics-Crafting-Deep-Insights-from-Global-Demographic-Trends-/raw/main/World%20PP%202024_GEN_F01_DEMOGRAPHIC_INDICATORS



## 🔍 Analysis Scope

This project will explore:

- Global population trends and growth rates
- Regional analysis (e.g., Africa vs Europe vs Asia)
- Aging population and dependency ratios
- Urban vs rural population changes
- Fertility rate changes over time
- Forecasting population dynamics (optional ML)



# 🌍 Cleaned Global Population Dataset — Estimates Sheet (2024)

This repository contains a cleaned version of the **World Population Prospects 2024** dataset (Estimates Sheet), extracted from the original Excel file provided by the United Nations.

### 📂 Dataset Source
- **File Name:** `World PP 2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx`
- **Sheet Used:** `Estimates`

---

## 📌 Objective

To extract, clean, and prepare population-related demographic indicators from the UN dataset for further analysis, focusing on key metrics such as:

- Total population
- Male and female population
- Population density

---

## ✅ Data Cleaning Workflow

The following steps were performed to prepare the dataset:

### 1. **Loading the Dataset**
```python
import pandas as pd

# এক্সেল ফাইল লোড করা
file_path = r"C:/Users/shams/OneDrive/Pictures/Al MAZID/DemoCraft-Analytics-Crafting-Deep-Insights-from-Global-Demographic-Trends-/World PP 2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx"

# সব শীট লোড করা
dfs = pd.read_excel(file_path, sheet_name=None)

# Estimates শীট থেকে ডেটা লোড
df_main = dfs["Estimates"]

# দরকারি কলাম নির্বাচন
important_columns = [
    "Region, subregion, country or area *",
    "Year",
    "Total Population, as of 1 January (thousands)",
    "Male Population, as of 1 July (thousands)",
    "Female Population, as of 1 July (thousands)",
    "Population Density, as of 1 July (persons per square km)"
]

# শুধুমাত্র গুরুত্বপূর্ণ কলামগুলো বেছে নেওয়া
df_selected = df_main[important_columns]

# প্রথম কয়েকটি সারি দেখা
print(df_selected.head())


# Data type পরিবর্তন করার জন্য
numeric_columns = [
    "Total Population, as of 1 January (thousands)",
    "Male Population, as of 1 July (thousands)",
    "Female Population, as of 1 July (thousands)",
    "Population Density, as of 1 July (persons per square km)"
]

# Object থেকে Numeric Data Type এ রূপান্তর করা
df_selected[numeric_columns] = df_selected[numeric_columns].replace(",", "", regex=True)  # কমা সরানো
df_selected[numeric_columns] = df_selected[numeric_columns].apply(pd.to_numeric, errors='coerce')  # সংখ্যায় রূপান্তর

# নতুন ডাটা টাইপ চেক করা
print(df_selected.dtypes)

# Missing values চেক করা
print(df_selected.isnull().sum())

# Missing values ফিল করা (যদি দরকার হয়)
df_selected.fillna(method='ffill', inplace=True)

# ডাটা টাইপ চেক করা
print(df_selected.dtypes)

# FutureWarning ঠিক করা: `.ffill()` ব্যবহার করা
df_selected = df_selected.ffill()

# যদি Missing Value থাকে, তাহলে তা চেক করা
print(df_selected.isnull().sum())  # এখন NaN আছে কি না দেখতে

df_selected.to_csv("cleaned_population_data.csv", index=False)

``` <--



## 📈 Visual Techniques Planned

- Heatmaps (e.g., year-wise population growth)
- Line graphs (e.g., life expectancy over decades)
- Stacked bar charts (urban vs rural growth)
- Choropleth maps (continent/country-level insights)
- Interactive dashboards (optional in later phase)

---

## 🚀 Future Scope

- Integration with economic and climate indicators
- Predictive modeling using time series forecasting
- AI-powered policy simulations
- Bangla language version of dashboard (for local relevance)

---

## 🤝 Contributions

Want to collaborate? Suggestions, issues, and pull requests are welcome!

---

## © License

This project is open-sourced under the **MIT License**.  
Feel free to use and expand with credit.














