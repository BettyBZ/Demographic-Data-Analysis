
# Python 3
# filename: Create_Table(for_single_year_age_group)
# Authors: Betty Botian Zhang, bz2443@nyu.edu
# AI Assistant: Gemini
"""In this program, I read the original data from UN.
Then, I only pick the data from the most recent source 
year. I put all the data for population distribution for
single age togethor in one table. 
"""
## This code is written by AI(Gemini), and revised by me and AI(Gemini).
import matplotlib.pyplot as plt
import pandas as pd

# set up conditions 
selected_area = "Total"
selected_sex = "Both Sexes"
selected_people = "Japanese"
selected_nation = "Japan"

# Read the file
df = pd.read_csv(f"{selected_people} Population Original Data(from UN).csv",sep=",")

df.columns = df.columns.str.strip()

#Test Code
# Print out Available Data
# print("Available Years:",sorted([str(year) for year in df["Year"].dropna().unique()]),)
# print("Available Area:",df["Area"].unique())
# print("Available Age Groups (sample):",df["Age"].unique()[:10])

years_numeric = pd.to_numeric(df["Year"], errors="coerce")

# create the filter
df_filtered = df[(df["Area"]==selected_area)&(df["Sex"]==selected_sex)&(~df["Age"].str.contains(" - "))&(~df["Age"].isin(["Unknown", "Total"]))&(years_numeric % 5==0)].copy()

# sort the data
def sort_age(age_str):
    age_str = str(age_str).strip()
    if age_str.endswith("+"):
        return int(age_str[:-1])
    try:
        return int(age_str)
    except ValueError:
        return 999

def sort_source_year(source_year_str):
    source_year_str = str(source_year_str).strip()
    try:
        return int(source_year_str)
    except ValueError:
        return 999

# Apply the age sorting order 
df_filtered["Age_Sort"] = df_filtered["Age"].apply(sort_age)
df_filtered["Source_Year_Sort"] = df_filtered["Source Year"].apply(sort_source_year)

#Sort data by Year_Sort and Source_Year_Sort (descending for source year)
df_filtered = df_filtered.sort_values(by=["Age_Sort","Source_Year_Sort"],ascending=[True,False])

#drop duplicate for the same Year and Area, keep the latest Source Year Data
df_filtered = df_filtered.drop_duplicates(subset=["Year","Age"],keep="first")

# this step fix the sequence after pivoting
sorted_ages_unique = df_filtered["Age"].unique()
df_filtered["Age"] = pd.Categorical(df_filtered["Age"], categories = sorted_ages_unique, ordered=True)
# create the table 
pivot_table = df_filtered.pivot(
    index="Age", columns="Year", values="Value"
)
print(f"\n---- Population Table for {selected_area} Area (Single Age Groups) ---")
print(pivot_table.head(15))

output_filename = f"{selected_people}_Population_{selected_area}_{selected_sex}_(Single_Year_Ages).csv"
pivot_table.to_csv(output_filename)
print(f"\nTable successfully saved to {output_filename}")
