# 📊 Cell Tracking & Morphokinetic Feature Extraction

This repository contains CSV tables and a Python script for analyzing morphokinetic and motility data of individual cells extracted from time-lapse microscopy. The project combines image analysis from CellProfiler and post-processing with Python to compute dynamic features like speed and acceleration per cell over time.

---

## 📂 Contents

### 🔹 Input Tables (Exported from CellProfiler)

1. **`Cells_B3_1.csv`**  
   A per-cell table exported from CellProfiler with static and dynamic features, including shape, intensity, and tracking metadata (e.g., Track ID, location, time point).

2. **`Track_B3_1.csv`**  
   The "Object relationships" table exported from CellProfiler, which contains pairwise relations between tracked objects across frames (e.g., parent-child object and image numbers).

---

### 🔹 Python-Generated Tables

3. **`Cells_B3_1_SortedByObjectNumber.csv`**  
   The original `Cells_B3_1.csv` sorted by `ObjectNumber` and `ImageNumber` for consistent alignment with tracking calculations.

4. **`Speed_and_Distance_Table_with_Acceleration.csv`**  
   A computed table containing:
   - Euclidean distance between each cell and its next-frame match
   - Estimated speed (pixels/hour)
   - Acceleration (change in speed between frames)

5. **`Directly_Merged_Cells_Table.csv`**  
   A final merged table combining the cell features from `Cells_B3_1` with the dynamic measurements (distance, speed, acceleration) for each cell, frame by frame.

---

## 🧠 Analysis Goals

- Track individual cells over time.
- Compute motion features for each tracked cell:
  - **Speed**: movement per frame (assuming fixed time interval between frames).
  - **Acceleration**: change in speed over time.
- Merge morphokinetic features and motility metrics for advanced biological analysis.

---

## 🧾 Script Overview

### `cellomic-exelfile.py`

This script performs the following steps:
1. **Sorting** the `Cells_B3_1.csv` by cell and time.
2. **Merging** track relationships with X/Y cell positions.
3. **Calculating**:
   - Distance between frames
   - Speed (pixels/hour)
   - Acceleration per cell
4. **Creating** the final merged table containing all features.

To run the script:

```bash
python cellomic-exelfile.py
