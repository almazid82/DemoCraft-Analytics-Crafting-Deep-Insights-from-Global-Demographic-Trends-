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


