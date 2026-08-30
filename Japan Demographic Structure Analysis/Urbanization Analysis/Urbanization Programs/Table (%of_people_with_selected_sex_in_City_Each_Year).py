# Create table for the percentage of Chinese people live in city for each year
# This code in write by my own and revised by AI(Gemini). I learn the pandas system with AI ( Gemini).

# Import
import pandas as pd

# Set up conditions
selected_sex = "Male"
selected_nation = "Japan"
selected_people = "Japanese"

# Read file
df = pd.read_csv(f"{selected_people} Population Original Data(from UN).csv",sep=",")
df.columns = df.columns.str.strip()

# Create filter
df_filtered = df[(df["Age"]=="Total")&(df["Sex"]==selected_sex)&(df["Area"].isin(["Urban","Total"]))].copy()

# check and make population numeric
value_col = "Value" if "Value" in df_filtered.columns else df_filtered.columns[-1]
df_filtered[value_col] = pd.to_numeric(df_filtered[value_col],errors="coerce")

# Sort the "Year"
def sort_year(year_str):
    year_str = str(year_str).strip()
    try:
        return int(year_str)
    except ValueError:
        return 999

def sort_source_year(source_year_str):
    source_year_str = str(source_year_str).strip()
    try:
        return int(source_year_str)
    except ValueError:
        return 999


df_filtered["Year_Sort"] = df_filtered["Year"].apply(sort_year)
df_filtered["Source_Year_Sort"] = df_filtered["Source Year"].apply(sort_source_year)

#Sort data by Year_Sort and Source_Year_Sort (descending for source year)
df_filtered = df_filtered.sort_values(by=["Year_Sort","Source_Year_Sort"],ascending=[True,False])

#drop duplicate for the same Year and Area, keep the latest Source Year Data
df_filtered = df_filtered.drop_duplicates(subset=["Year", "Area"],keep="first")

# create pivot table
pivot_df = df_filtered.pivot_table(
    index=["Year", "Year_Sort"],
    columns = "Area",
    values= value_col,
    aggfunc="first",
).reset_index()

# Sort by year
pivot_df = pivot_df.sort_values("Year_Sort")

# create DataFrame
result_df = pd.DataFrame()
result_df["Year"] = pivot_df["Year"]

# set up values and calculations
urban_pop = pivot_df["Urban"] if "Urban" in pivot_df.columns else 0
total_pop = pivot_df["Total"] if "Total" in pivot_df.columns else 1

result_df["Urban_population"] = urban_pop
result_df["Total_population"] = total_pop
result_df["live_in_urban_percentage"] = result_df["Urban_population"]/result_df["Total_population"]

# Create Table
file_name = f"{selected_people}_Population_{selected_sex}(%_live_in_Urban).csv"
result_df.to_csv(file_name,index=False)
print(f"successfully save to {file_name}")