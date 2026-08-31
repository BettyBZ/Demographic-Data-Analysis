## The code in the define function plot_graph is a copy of code from "China_Create_Plot(for_single_year_age_group).py".

# Import
import matplotlib.pyplot as plt
import pandas as pd

#set up condition
selected_nation = "Japan"
Selected_people = "Japanese"
df = pd.read_csv(f"{Selected_people}_Population_Total_Both Sexes_(Single_Year_Ages).csv",sep=",")

def plot_graph(selected_year):
    ## Plot the graph

    # Set up conditions
    selected_nation = "Japan"
    Selected_people = "Japanese"  

    # Reads the file  
    df = pd.read_csv(f"{Selected_people}_Population_Total_Both Sexes_(Single_Year_Ages).csv",sep=",")

    ## Start Here Code by AI(Gemini), copied from "China_Create_Plot(for_single_year_age_group).py".
    ## It is revised by AI(Gemini) and meself. Revision from line 40 to 42. I change the scale.
    plot_df = df.copy()
    plot_df = plot_df.dropna(subset=[selected_year])
    # try to filter out the line with age 85+ when 86 and above age entry exist.
    # In pandas, we check if a value exists in a column using boolean conditions or .isin()
    if "86" in plot_df["Age"].values:
        if "85 +" in plot_df["Age"].values:
            # Filter out the "85 +" row if "86" data exists to prevent double counting/overlap
            plot_df = plot_df[plot_df["Age"] != "85 +"]

    # Drop empty entries
    plot_df = plot_df.dropna(subset=[selected_year])

    # 2. Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 12))

    # 3. Create a horizontal bar plot for the year 2020
    # Y-axis: Age, X-axis: Population for 2020
    ax.barh(plot_df["Age"], plot_df[selected_year], color='skyblue', edgecolor='navy')

    # 4. Configure labels and title
    ax.set_xlabel('Population', fontsize=12)
    ax.set_ylabel('Age', fontsize=10)
    ax.set_title(f'Population Distribution for Year {selected_year} (Ages 0-100)', fontsize=14)

    # 5. Fix X-axis limits and ticks (0 to 7 with 1e7 scaling index)
    # 7 * 1e7 = 70,000,000 max limit
    ax.set_xlim(0, 3e6)
    ax.set_xticks([i * 1e6 for i in range(4)])
    ax.set_xticklabels([f'{i}e6' for i in range(4)])

    # Invert y-axis so age 0 is at the top (optional, standard for demographic views)
    ax.invert_yaxis()

    # Display the plot
    plt.tight_layout()
    plot_filename = f"{selected_nation}_Population_{selected_year}_Statistic_Single_Year_Age.pdf"
    plt.savefig(plot_filename)
    print(f"\nTable successfully saved to {plot_filename}")

for year in range(1955,2024,5):
    if year == 1975:
        continue
    else:
        year_str = str(year)
        plot_graph(year_str)
