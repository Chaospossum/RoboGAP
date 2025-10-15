# ROBO‑GAP Gender Distribution Analysis

This repository contains a small data‑analysis project exploring how humans perceive the gender of robots.  Using the publicly provided **ROBO‑GAP** dataset found in (https://robo-gap.unisi.it/), the goal was to answer a simple yet revealing question: **are feminine robots underrepresented compared to masculine and neutral ones?**

## Overview

The ROBO‑GAP dataset contains 251 images of robot characters, each rated by at least 25 human observers for perceived masculinity, neutrality and femininity on a 7‑point Likert scale.  For our analysis we used the categorical column `gender_category`, which labels each robot as **masculine**, **neutral** or **feminine** based on those ratings.

The project follows these steps:

1. **Load the dataset** – Read `ROBO-GAP_dataset.csv` into a pandas DataFrame.
2. **Summarise gender labels** – Count how many robots fall into each gender category and compute the percentage of the total.
3. **Visualise the distribution** – Generate both a bar chart and a pie chart showing the gender counts and percentages.  The colours match those used in the accompanying presentation: blue for masculine, grey for neutral and pink for feminine.
4. **Report & presentation** – A concise LaTeX report and a polished PowerPoint deck summarise the question, method, results and conclusion.

### Key Findings

Out of 251 robots, we found that approximately:

- **45.8 % are perceived as neutral**,
- **39.0 % are perceived as masculine**, and
- **15.1 % are perceived as feminine**.

Feminine robots are therefore notably underrepresented in this dataset.  This finding supports the hypothesis that robot designs (or human perceptions of those designs) skew masculine or gender‑neutral.

## Files in this Repository

The project consists of several files:

- `robo_gap_analysis.py` – Python script that loads the dataset, calculates the gender distribution, prints the counts and percentages, and saves two charts: a bar plot (`gender_distribution_bar.png`) and a pie chart (`gender_distribution_pie.png`).  Running this script in a Python 3 environment with pandas and matplotlib installed will reproduce the figures.
- `gender_distribution_bar.png` – Bar chart of the gender distribution.
- `gender_distribution_pie.png` – Pie chart of the gender distribution.
- `report.tex` – Two‑page LaTeX report summarising the question, dataset, method, results and conclusion.  Compile it with any LaTeX engine or upload to Overleaf for editing.
- `answer.pptx` – Polished presentation deck (PowerPoint) used for the five‑minute talk, aligned with the course rubric.
- `README_GitHub.md` – This README file.

## Getting Started

### Prerequisites

To run the analysis script, you’ll need:

* Python 3.8 or later
* [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/)
* The Dataset from (https://robo-gap.unisi.it/)
  
* Install the dependencies via pip:

```bash
pip install pandas matplotlib
