combined&normalized_table+distarbition_bar README
# Experimental Data Analysis and Visualization

This project contains Python scripts designed for the processing, analysis, and visualization of experimental data, likely from biological or chemical experiments involving different treatments (B03, B06) and multiple time points. The scripts cover data preprocessing, outlier handling, normalization, generation of various distribution plots (standard and heatmaps), and statistical analysis of forecasting results.

## Table of Contents

1.  Setting Up the Environment and Dependencies
2.  Code Block 1: Combined & Outliers & Normalized Table
3.  Code Block 2: Overall Distribution Plots and Descriptive Statistics (Distribution - Feature_Frequency)
4.  Code Block 3: Distribution Plots by Treatment (לפי טיםולים)
5.  Code Block 4: Feature Distribution Heatmap Over Time - Per Treatment
6.  Code Block 5: Feature Distribution Heatmap Over Time - Not Per Treatment
7.  Code Block 6: Statistical Analysis of Forecast Quality

---

## Setting Up the Environment and Dependencies

The provided code is written in Python and is primarily intended for execution within the Google Colab environment, which facilitates easy file loading and execution.

How to open and run the file in Google Colab:
1.  Open Google Colab: Go to https://colab.research.google.com/.
2.  Upload the .py file:
    * Click on "File" in the menu bar.
    * Select "Upload notebook" (even though it's a .py file, Colab can open and treat it as a notebook if it contains # %% cells or simply run it as a script).
    * Browse and select your .py file (e.g., combined&normalized_table+distarbition_bar.py). Colab will open it in a new tab.
3.  Run the cells: You can run each code block (cell) individually by clicking the play icon next to it, or run all cells by going to "Runtime" -> "Run all".

Dependencies (Libraries):
The code requires the following libraries, which are typically pre-installed in Google Colab or can be easily installed:

* pandas
* matplotlib
* seaborn
* numpy
* scipy
* statsmodels
* openpyxl (To install: !pip install openpyxl --quiet in a Colab cell)

How to upload input files in Google Colab:
1.  Upload CSVs: For each code block that requires an input file, you need to upload it to your Colab working directory.
    * On the left sidebar of the Colab interface, click the folder icon (Files).
    * You can either drag and drop the required CSV files into this panel or click the "Upload to session storage" icon (a file with an arrow pointing up).
    * Important: Ensure that the filenames specified in the code exactly match the names of the uploaded files. To avoid errors, you can right-click on the filename in the Colab Files panel, select "Copy path," and paste it directly into your code.

---

## Code Block 1: Combined & Outliers & Normalized Table

This block (originally part of combined&normalized_table+Distarbition_Bar.ipynb) performs the merging of two dataframes, outlier handling using the IQR method, Z-score normalization (per treatment type), and time synchronization validation.

Purpose:
To combine, clean, and normalize raw data from two different sources ('B03', 'B06') to prepare them for further analysis and visualization.

Required Input Files:
* SummeryTableAfterNaNHandling_B3.csv - Summary table data for Treatment B03, after NaN value handling.
* SummeryTableAfterNaNHandling_B6.csv - Summary table data for Treatment B06, after NaN value handling.

Generated Output Files:
* Combined_SummaryTable_Processed.csv - A CSV file containing the combined data, after outlier treatment and normalization.

Key Functionality:
* Loads and concatenates two CSV files.
* Removes a potential duplicate header row from the second file.
* Handles outliers using the IQR (Interquartile Range) method for numerical columns, excluding identifier columns.
* Performs Z-score normalization for each feature, separately for each treatment type (B03 and B06).
* Validates time synchronization (checks for exactly 30 time points per file).

---

## Code Block 2: Overall Distribution Plots and Descriptive Statistics (Distribution - Feature_Frequency)

This block, based on another part of the original notebook, focuses on displaying data distributions and descriptive statistics.

Purpose:
To provide a visual and statistical overview of the distribution of various parameters within the data.

Required Input Files:
* Combined_SummaryTable_NoNormalization.csv - A CSV file containing the combined data, without normalization. (Note: The file path in the provided code block specifies /content/Combined_SummaryTable_NoNormalization.csv).

Generated Output Files:
* parameter_means_bar_chart.png - A bar chart displaying the mean values of various parameters.
* selected_parameter_distributions.png - A multi-panel plot showing histograms with KDE (Kernel Density Estimate) for selected parameters (e.g., 'Area Shape', 'Acceleration').
* individual_distribution_plots/ (directory) - A directory containing individual distribution plots for each of the selected parameters.
* descriptive_statistics_summary.csv - A CSV file containing a table of descriptive statistics (mean, standard deviation, min, max, etc.) for the numerical parameters.

Key Functionality:
* Loads non-normalized data.
* Calculates and plots the mean of each parameter in a bar chart.
* Generates distribution plots (histograms with KDE) for a predefined set of features, both in a combined plot and as individual plots.
* Computes and exports descriptive statistics.

---

## Code Block 3: Distribution Plots by Treatment (לפי טיםולים)

This block extends the feature distribution analysis by presenting them separately for different treatment groups (B03 and B06), and also performs a statistical Tukey HSD test.

Purpose:
To visually and statistically compare the distribution of key features between different treatment groups, identifying significant differences.

Required Input Files:
* Combined_SummaryTable_NoNormalization.csv - A CSV file containing the combined data, without normalization.

Generated Output Files:
* individual_distribution_plots_overall/ (directory) - Overall distribution plots (similar to Block 2, but saved in a separate directory).
* distribution_plots_treatment1/ (directory) - Distribution plots for Treatment B03.
* distribution_plots_treatment2/ (directory) - Distribution plots for Treatment B06.
* distribution_plots_overlap/ (directory) - Overlaid (stacked) distribution plots for B03 and B06, including statistical significance P-values from a Tukey HSD test.
* descriptive_statistics_summary.csv - A table of descriptive statistics (may overwrite the previous one).

Key Functionality:
* Separates data into treatment groups based on the filename (B03 or B06).
* Generates individual distribution plots for each treatment group.
* Creates overlaid (stacked) distribution plots for direct comparison between treatments.
* Performs pairwise_tukeyhsd (Tukey HSD) test to assess statistical significance between treatment groups for each feature, displaying the P-value on the overlaid plot.

---

## Code Block 4: Feature Distribution Heatmap Over Time - Per Treatment

This code generates heatmaps that show how the distribution of specific features changes over time, separated for each treatment group.

Purpose:
To visualize trends in feature distributions across different time points, highlighting differences between treatments.

Required Input Files:
* Combined_SummaryTable_NoNormalization.csv - A CSV file containing the combined data, without normalization.

Generated Output Files:
* A series of heatmaps (displayed directly in Colab, not saved as image files by this code). For each selected feature and each treatment (B03, B06), a separate heatmap is generated.

Key Functionality:
* extract_treatment function to identify the treatment type (B03 or B06) from the filename.
* plot_distribution_heatmap function that takes a dataframe, treatment name, feature name, and time column.
* Generates a heatmap showing the density of cells (or observations) across different feature value bins over time.

---

## Code Block 5: Feature Distribution Heatmap Over Time - Not Per Treatment

This code is similar to Block 4 but generates a single heatmap showing the distribution of a specific feature over time, without separation by treatment groups.

Purpose:
To provide a general overview of the evolution of a feature's distribution over time for all data combined.

Required Input Files:
* Combined_SummaryTable_NoNormalization.csv - A CSV file containing the combined data, without normalization.

Generated Output Files:
* A single heatmap (displayed directly in Colab, not saved as an image file by this code).

Key Functionality:
* Uses a simplified version of the plot_distribution_heatmap function for the entire dataframe, without separating by treatments.
* Displays the distribution of a feature (defaulting to 'Area Shape') over time.

---

## Code Block 6: Statistical Analysis of Forecast Quality

These two blocks deal with the statistical analysis of forecasting results, likely from an LSTM model. They evaluate "forecast quality" (Good/Bad Forecast) based on MAPE and P-Value, and perform a Chi-square test to examine statistical significance.

Purpose:
To assess the efficacy of the forecasting model and to determine if there are significant differences in forecast quality between different treatments or features.

Required Input Files:
* all_forecast_metrics_summary_table (8).csv - A CSV file containing forecast metrics (MAPE, P-Value, is_good_forecast) for various treatments and features.

Generated Output Files:
* A stacked bar chart (displayed directly in Colab) showing the percentage of "Good" and "Bad" forecasts for P-Value, by feature and treatment.
* chi_square_results.xlsx - An Excel file containing the results of Chi-square tests, including corrected P-values (FDR corrected).

Key Functionality:
* Loads forecast metrics.
* Defines criteria for "good forecast" (MAPE <= 10%, P-Value <= 0.05).
* Summarizes the percentage of good and bad forecasts for each combination of treatment, feature, and metric (MAPE/P-Value).
* Generates stacked bar charts to visualize these percentages.
* Performs a Chi-square test to examine the dependence between treatment type and forecast quality (specifically for P-Value).
* Applies Benjamini-Hochberg (FDR) correction for multiple P-values to control the False Discovery Rate.
* Exports Chi-square test results to an Excel file.