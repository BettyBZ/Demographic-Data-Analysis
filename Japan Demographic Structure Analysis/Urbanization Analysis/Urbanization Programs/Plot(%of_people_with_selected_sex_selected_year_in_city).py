# Plot(%of_people_with_selected_sex_slected_year_in_city)

# import
import pandas as pd
import matplotlib.pyplot as plt

#Set up Conditions
selected_year = "2020"
selected_sex = "Both Sexes"
selected_people = "Japanese"
selected_nation = "Japan"
data = pd.read_csv(f"{selected_nation}_Population_{selected_year}_{selected_sex}(%_live_in_Urban).csv")
# start here the code write by AI(Gemini)
df = pd.DataFrame(data)

# Create figure and axis objects with subplots
fig, ax1 = plt.subplots(figsize=(14, 6))

# Left y-axis: Total Population (Bar Chart)
color = "tab:blue"
ax1.set_xlabel("Age", fontsize=12)
ax1.set_ylabel("Total Population", color=color, fontsize=12)
ax1.bar(df["Age"], df["Total_population"], color=color, alpha=0.6, label="Total Population")
ax1.tick_params(axis="y", labelcolor=color)

# Reduce clutter on the X-axis by only showing labels at specific intervals (e.g., every 5 years)
plt.xticks(range(0, len(df)), df["Age"], rotation=0)

# Right y-axis: Live in Urban Percentage (Line Chart)
ax2 = ax1.twinx()
color = "tab:orange"
ax2.set_ylabel("Live in Urban Percentage", color=color, fontsize=12)
ax2.plot(
    df["Age"],
    df["live_in_urban_percentage"],
    color=color,
    linewidth=2,
    marker="o",
    markersize=3,
    label="Urban Percentage",
)
ax2.tick_params(axis="y", labelcolor=color)
ax2.set_ylim(0, 1)  # Optional: adjust limits to better fit percentage spread

# Title and layout formatting
plt.title(
    f"{selected_nation} {selected_sex} {selected_year} Combo Plot: Total Population (Bars) vs. Urban Percentage (Line) by Age",
    fontsize=14,
    pad=15,
)
fig.tight_layout()

# Display the plot
output_filename = f"{selected_nation}_Population_{selected_year}_{selected_sex}(%_live_in_Urban_single_age_group).pdf"
plt.savefig(output_filename)