#Plot(1_years_old_and_Specific_Women_Age_Range_Population_Ratio)
# This code is partcially write by my own. 
# I also past some part of the code from "Plot(%of_people_with_selected_sex_slected_year_in_city).py". This code is write by AI(Gemini).

# Import
import pandas as pd
import matplotlib.pyplot as plt

# Set up condition
selected_people = "Japanese"
selected_nation = "Japan"
women_selected_age_starts = 0
women_selected_age_ends = 100

# read file
input_filename = f"{selected_nation} 1 year old and ({women_selected_age_starts}-{women_selected_age_ends}) Women Ratio(Each Year population sensus).csv"
data = pd.read_csv(input_filename,sep=",")

# Decrease the sensus year to the year of this ratio
data["Year"]-=1
df = pd.DataFrame(data)

## This part is copied from file "Plot(%of_people_with_selected_sex_slected_year_in_city).py", and modified
fig, ax = plt.subplots(figsize=(14, 6))

# Right y-axis: Live in Urban Percentage (Line Chart)
color = "tab:orange"
ax.set_ylabel(f"Percentage", color=color, fontsize=12)
ax.plot(
    df["Year"],
    df["Ratio"],
    color=color,
    linewidth=2,
    marker="o",
    markersize=3,
    label="Percentage",
)
ax.tick_params(axis="y", labelcolor=color)
ax.set_ylim(0, 0.17) 

# Title and layout formatting
plt.title(
    f"{selected_nation} ratio between population born(in 1 year) and ({women_selected_age_starts} - {women_selected_age_ends}) Women Population",
    fontsize=14,
    pad=15,
)
fig.tight_layout()

# Display the plot
output_filename = f"{selected_nation} ratio between population born(in 1 year) and ({women_selected_age_starts} - {women_selected_age_ends}) Women Population.pdf"
plt.savefig(output_filename)
