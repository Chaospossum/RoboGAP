# RoboGAP
ROBO‑GAP Gender Distribution Analysis

This repository contains a small data‑analysis project exploring how humans perceive the gender of robots. Using the publicly provided ROBO‑GAP dataset, the goal was to answer a simple yet revealing question: are feminine robots underrepresented compared to masculine and neutral ones?

Overview

The ROBO‑GAP dataset contains 251 images of robot characters, each rated by at least 25 human observers for perceived masculinity, neutrality and femininity on a 7‑point Likert scale. For our analysis we used the categorical column gender_category, which labels each robot as masculine, neutral or feminine based on those ratings.

The project follows these steps:

Load the dataset – Read ROBO-GAP_dataset.csv into a pandas DataFrame.

Summarise gender labels – Count how many robots fall into each gender category and compute the percentage of the total.

Visualise the distribution – Generate both a bar chart and a pie chart showing the gender counts and percentages. The colours match those used in the accompanying presentation: blue for masculine, grey for neutral and pink for feminine.

Report & presentation – A concise LaTeX report and a polished PowerPoint deck summarise the question, method, results and conclusion.

Key Findings

Out of 251 robots, we found that approximately:

45.8 % are perceived as neutral,

39.0 % are perceived as masculine, and

15.1 % are perceived as feminine.

Feminine robots are therefore notably underrepresented in this dataset. This finding supports the hypothesis that robot designs (or human perceptions of those designs) skew masculine or gender‑neutral.

Files in this Repository

The project consists of several files:

robo_gap_analysis.py – Python script that loads the dataset, calculates the gender distribution, prints the counts and percentages, and saves two charts: a bar plot (gender_distribution_bar.png) and a pie chart (gender_distribution_pie.png). Running this script in a Python 3 environment with pandas and matplotlib installed will reproduce the figures.

gender_distribution_bar.png – Bar chart of the gender distribution.

gender_distribution_pie.png – Pie chart of the gender distribution.

report.tex – Two‑page LaTeX report summarising the question, dataset, method, results and conclusion. Compile it with any LaTeX engine or upload to Overleaf for editing.

answer.pptx – Polished presentation deck (PowerPoint) used for the five‑minute talk, aligned with the course rubric.

README_GitHub.md – This README file.

Getting Started
Prerequisites

To run the analysis script, you’ll need:

Python 3.8 or later

pandas
 and matplotlib

Install the dependencies via pip:

pip install pandas matplotlib

Running the Analysis

Ensure that ROBO-GAP_dataset.csv and robo_gap_analysis.py are in the same directory.

Run the script:

python robo_gap_analysis.py


The script will print the gender counts and percentages to the console and save both charts as PNG files. These images can be inserted into the report or presentation.

Usage

This repository can be used as a starting point for further exploration of the ROBO‑GAP dataset or as a template for small data‑science projects. You are welcome to fork or clone the repository and extend the analysis (for example, by exploring perceived robot age or performing statistical tests). See the report for suggestions on limitations and future work.

Credits and License

The ROBO‑GAP dataset was provided as part of the MAT2007 programming project at Maastricht University. The analysis and accompanying report/presentation were created by a student for that course. Feel free to adapt or build upon this project for educational purposes.

Contact

For questions about the dataset or the project, please refer to the MAT2007 course materials or contact the course tutor. To report issues with this repository, open an issue on GitHub.
