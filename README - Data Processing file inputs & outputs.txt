Data Processing and Analysis Scripts
This repository contains a series of Python scripts designed to process and analyze cellular data from CSV files. The scripts are organized into a workflow, where the output of one script serves as the input for the next.

1. cellomic-exelfile.py
This script performs several key data manipulation steps, including sorting, tracking object movement, and calculating speed, distance, and acceleration.

Inputs:

Cells_B6_1.csv: A CSV file containing cell object data from a cell profiling experiment. It is used for sorting and calculating cellular properties.

Track_B6_1.csv: A CSV file with tracking data, used to link cells across different images.

photoname_B6.csv: A CSV file that maps image numbers to their corresponding filenames.

Outputs:

Cells_B6_1_SortedByObjectNumber.csv: An intermediate CSV file where the Cells_B6_1.csv data is sorted by ObjectNumber and ImageNumber.

Speed_and_Distance_Table_with_Acceleration_B6.csv: A CSV file that contains calculated speed, distance, and acceleration for each tracked object.

Directly_Merged_Cells_Table_B6.csv: An intermediate CSV file that merges the cellular properties from Cells_B6_1_SortedByObjectNumber.csv with the speed and acceleration data.

Corrected_Updated_Directly_Merged_Cells_Table_B6.csv: The final output of this script, which merges the image filenames with the comprehensive cell data.

2. pybatch_code.py
This script renames the image filenames in the data based on metadata from an Excel file, creating a summary table.

Inputs:

Corrected_Updated_Directly_Merged_Cells_Table_B6.csv: The primary data table output from cellomic-exelfile.py.

xls1.xlsx: An Excel file containing metadata about the experiment, including initials, experiment number, and treatments.

Outputs:

SummeryTable_B6.csv: A new CSV file where the FILENAME column has been replaced with a more descriptive filename generated from the xls1.xlsx metadata.

3. SUMMARYTABLE_CLEANINGDATA.py
This script cleans and filters the summary table by removing inconsistent data, filling in missing values, and handling NaN values.

Inputs:

SummeryTable_B6.csv: The summary table created by pybatch_code.py.

Outputs:

FilteredSummeryTable_B6.csv: An intermediate CSV file containing only the objects that appear in at least 30 consecutive images.

SummeryTableAfterNaNHandlinggg_B6.csv: The final cleaned CSV file, where all missing values (gaps and NaN) have been filled using an imputation method based on surrounding data points.

4. COMBINED_B3_B6.py
This script combines the cleaned summary tables from two separate experiments into a single file for final analysis.

Inputs:

SummeryTableAfterNaNHandling_B3.csv: The cleaned data from a "B3" experiment.

SummeryTableAfterNaNHandling_B6.csv: The cleaned data from a "B6" experiment.

Outputs:

Combined_SummaryTable.csv: A single CSV file that merges the data from both the B3 and B6 experiments.