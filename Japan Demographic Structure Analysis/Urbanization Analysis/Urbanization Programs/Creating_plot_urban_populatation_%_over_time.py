# Creating a plot of china urban population percentage over time
## This ploting code is written by AI mostly
import pandas as pd
import matplotlib.pyplot as plt

# make "Sex" selection (code write by my own)
selected_sex = "Both Sexes"
selected_people = "Japanese"
selected_nation = "Japan"
input_filename = f"{selected_people}_Population_{selected_sex}(%_live_in_Urban).csv"
df = pd.read_csv(input_filename,sep=",")

# pull out the zeros
df_cleaned = df.dropna(subset=["live_in_urban_percentage"])

#Code past from Gemini starts here with my own revision only at line 13
plt.figure(figsize=(8, 5))
plt.plot(
    df_cleaned["Year"],
    df_cleaned["live_in_urban_percentage"],
    marker="o",
    linestyle="-",
    color="b",
    label="Urban Population %",
)

# Add titles and labels
plt.title(f"{selected_nation} {selected_sex} Urban Population Percentage Over Time")
plt.xlabel("Year")
plt.ylabel("Percentage")

# Set y-axis limits from 0 to 1
plt.ylim(0, 1)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save the graph
output_filename = (
    f"{selected_nation} {selected_sex} Urban population percentage overtime.pdf"
)
plt.tight_layout()
plt.savefig(output_filename, format="pdf", bbox_inches="tight")