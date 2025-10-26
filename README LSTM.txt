README: Biological Cell Data Analysis and Forecasting
This script is designed for the analysis and time-series forecasting of biological cell data using a combination of deep learning and machine learning techniques. It processes data from a consolidated CSV file to perform treatment-specific forecasting, evaluate model performance, and visualize the results.

Overview
The main goals of this script are:

1.Treatment-Specific Analysis: Process data for different biological treatments, identified by unique filenames.

2.Time-Series Forecasting: Utilize a single LSTM (Long Short-Term Memory) neural network model to forecast key cell features like cell area, speed, and acceleration.

3.Feature Selection: Employ a Random Forest model to identify the most significant exogenous features that impact the target variables.

4.Performance Evaluation: Calculate a range of statistical metrics (MAE, RMSE, MAPE, and P-Value) to assess the accuracy and statistical significance of the forecasts.

5.Data Visualization & Export: Generate graphs for each cell's forecast and consolidate all metrics into a final summary table for easy review.

Setup and Requirements
This code is best run in a Google Colab or a similar Jupyter Notebook environment.

1.Install Libraries: Run the following command in a separate notebook cell to install all the necessary dependencies:

Bash

!pip install neuralforecast==3.0.1 pandas matplotlib scikit-learn

2. Data Preparation: Ensure that your data file, named Combined_SummaryTable.csv, is located in the same directory as the script. This file must contain mandatory columns such as image_number (time point), ObjectNumber (cell ID), filename (treatment identifier), and the data columns you intend to analyze.

Configuration
You can customize the script's behavior by adjusting the global parameters at the top of the file:

treatment_full_filenames: A dictionary linking short aliases (e.g., "CELL_LINE_1") to the full filenames representing each treatment.

HORIZON: The number of future time steps (hours) to forecast.

MIN_TOTAL_HOURS_FOR_FORECAST: The minimum total number of time steps a cell must have to be included in the analysis.

LSTM_INPUT_SIZE: The length of the historical context window used by the LSTM model.

How the Script Works
The script executes the following steps automatically:

Iterate Through Treatments: It loops through each treatment defined in the treatment_full_filenames dictionary.

Data Preprocessing: For each treatment, it loads and filters the data, handling missing values through interpolation to ensure a continuous time series.

Global Feature Selection: It uses a Random Forest Regressor on the training data of all cells within a treatment to identify the top 20 most important exogenous features.

Training and Forecasting: A single LSTM model is trained on the combined training data of all eligible cells for a given treatment. The model then generates forecasts for the last HORIZON hours.

Performance Evaluation: It compares the forecasted values to the actual data, calculating metrics like MAE, RMSE, and MAPE. It also uses a linear regression to determine the statistical significance of the forecast and marks it as a "good forecast" if the p-value of the slope is less than 0.05.

6. File Generation: The script creates a new directory, forecast_results_by_treatment, with a subdirectory for each treatment.

Graphs: PNG files are saved, visualizing the historical data against the forecast for each cell.

CSV Files: Two CSV files are generated per treatment: one with detailed forecast vs. actual comparisons and another with per-cell performance metrics.

7. Global Summary: A final, comprehensive CSV table named all_forecast_metrics_summary_table.csv is saved, summarizing the results from all treatments and cells.

8. Automatic Download: At the end of the run, the entire results directory is compressed into a ZIP file (forecast_results_by_treatment.zip) and automatically downloaded to your local machine.

Expected Output
Upon completion, you will find the following in your working directory:

forecast_results_by_treatment/: A folder containing subdirectories for each treatment.

Inside each treatment folder: graphs (.png) and two CSV summary tables.

all_forecast_metrics_summary_table.csv: A single, consolidated CSV file with all the performance metrics.

forecast_results_by_treatment.zip: A compressed archive of the entire results directory.

If you encounter a FileNotFoundError, please ensure Combined_SummaryTable.csv is correctly placed. Warnings about individual cells being skipped indicate they may not contain enough data for a valid time-series analysis.