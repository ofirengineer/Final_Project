
K-Means Clustering with PCA Visualization

This project performs K-Means clustering on a dataset, optionally applying Principal Component Analysis (PCA) for dimensionality reduction and visualization.
It includes an Elbow Method plot to help determine the optimal number of clusters.

Features:

* Load dataset from CSV
* Select relevant features for clustering
* Standardize features
* Apply PCA to visualize data in 2D
* Use Elbow Method to find optimal k
* Perform K-Means clustering
* Visualize clusters in PCA space

Dataset:
The dataset should be a CSV file named Combined\_SummaryTable.csv.
Required format:

* One column named "filename" (excluded from clustering)
* All other columns should contain numeric features for clustering

Requirements:
The script requires the following Python packages: pandas, numpy, scikit-learn, matplotlib, seaborn

Usage:

1. Place your Combined\_SummaryTable.csv in the same directory as the script
2. Run the script
3. The script will:

   * Load and standardize data
   * Perform PCA (2 components)
   * Plot the Elbow Method chart
   * Run K-Means with the chosen k
   * Visualize clusters
   * Add a "Cluster" column to the dataset with the assigned cluster for each row

Output:

1. Elbow Method Plot – Helps determine optimal k
2. Clustered Scatter Plot (PCA) – Points colored by cluster label
3. Updated dataset including the Cluster column

Notes:

* Adjust the optimal\_k value in the script according to the Elbow Method result
* If PCA is skipped, the scatter plot will use the first two features of the dataset