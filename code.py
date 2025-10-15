#!/usr/bin/env python3
"""
Human-friendly analysis of the ROBO-GAP dataset.

This script reads the dataset and computes the distribution of perceived robot genders.
It prints a summary and saves both a bar chart and a pie chart of the distribution.

The colours used for the charts match those in the presentation: blue for masculine,
grey for neutral and pink for feminine.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Define a consistent colour palette matching the presentation
COLORS = {
    'masculine': '#5078A0',  # blue
    'neutral': '#9AA0A8',    # grey
    'feminine': '#C77B98',   # pink
}


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load the ROBO-GAP dataset.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A pandas DataFrame containing the dataset.

    Raises:
        SystemExit: If the file is not found.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        raise SystemExit(f"Sorry, I couldn't find '{filepath}'. Please ensure the dataset is in the correct location.")


def analyze_gender_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Compute counts of robots by perceived gender category.

    Args:
        df: DataFrame with a 'gender_category' column.

    Returns:
        A Series of counts for the categories 'masculine', 'neutral', and 'feminine'.

    Raises:
        ValueError: If the 'gender_category' column is missing.
    """
    if 'gender_category' not in df.columns:
        raise ValueError("The dataset must contain a 'gender_category' column.")
    # Ensure a consistent order of categories with fill_value to handle missing categories
    counts = df['gender_category'].value_counts().reindex(
        ['masculine', 'neutral', 'feminine'], 
        fill_value=0
    )
    return counts


def plot_distribution(counts: pd.Series, output_path: str) -> None:
    """
    Create and save a bar chart of gender distribution using a custom colour palette.

    Args:
        counts: Series with counts for each category.
        output_path: File path where the plot will be saved.
    """
    total = counts.sum()
    percentages = (counts / total * 100).round(1)
    bar_colours = [COLORS.get(cat, '#5078A0') for cat in counts.index]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(counts.index, counts.values, color=bar_colours)
    ax.set_title('Distribution of Perceived Robot Genders', pad=20)
    ax.set_xlabel('Perceived Gender Category')
    ax.set_ylabel('Number of Robots')
    
    # Add percentage labels - fixed offset of 1 units above each bar
    for x, (count, pct) in enumerate(zip(counts.values, percentages.values)):
        ax.text(x, count + 1, f'{pct:.1f}%', ha='center', va='bottom', fontsize=10)
    
    # Adjust layout to prevent title cutoff
    plt.subplots_adjust(top=0.92)
    plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0.3)
    plt.close()


def plot_pie(counts: pd.Series, output_path: str) -> None:
    """
    Create and save a pie chart of gender distribution using a custom colour palette.

    Args:
        counts: Series with counts for each category.
        output_path: File path where the plot will be saved.
    """
    total = counts.sum()
    percentages = (counts / total * 100).round(1)
    labels = [f"{cat.capitalize()} ({pct:.1f}%)" for cat, pct in zip(counts.index, percentages.values)]
    pie_colours = [COLORS.get(cat, '#5078A0') for cat in counts.index]
    plt.figure()
    plt.pie(counts.values, labels=labels, colors=pie_colours, startangle=90)
    plt.title('Perceived Robot Gender Distribution')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def main() -> None:
    """
    Main function to execute the gender distribution analysis.
    """
    print("Welcome! This script analyses the perceived gender distribution of robots in the ROBO-GAP dataset.")
    print("\nDataset: ROBO-GAP (Perugia et al., 2022)")
    print("Source: https://robo-gap.unisi.it/")
    
    data_file = 'ROBO-GAP_dataset.csv'
    print(f"\nLoading data from '{data_file}'...")
    df = load_data(data_file)
    
    print("Computing gender distribution...")
    counts = analyze_gender_distribution(df)
    total = counts.sum()
    percentages = counts / total * 100
    
    print("\nHere is the breakdown of robots by perceived gender:")
    for cat, count, pct in zip(counts.index, counts.values, percentages.values):
        print(f"  {cat.capitalize()}: {count} robots ({pct:.1f}%)")
    
    # Save the bar chart
    bar_path = 'gender_distribution_bar.png'
    print(f"\nSaving bar chart to '{bar_path}'...")
    plot_distribution(counts, bar_path)
    
    # Save the pie chart
    pie_path = 'gender_distribution_pie.png'
    print(f"Saving pie chart to '{pie_path}'...")
    plot_pie(counts, pie_path)
    
    print("\nAnalysis complete. The bar and pie charts are saved and ready to use!")


if __name__ == '__main__':
    main()