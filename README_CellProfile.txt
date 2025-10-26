README

# CellProfiler Pipeline for Cell Segmentation and Tracking

This repository contains a CellProfiler pipeline designed for automated segmentation and tracking of cells in time-lapse microscopy images. The pipeline includes preprocessing, object identification, feature measurement, and exporting results for downstream analysis.

## Overview

The pipeline performs the following steps:
1. **Image Loading**: Load multi-channel grayscale microscopy images.
2. **Metadata Extraction**: Extract metadata such as timepoints and channels from filenames.
3. **Intensity Rescaling**: Normalize image intensities.
4. **Feature Enhancement/Suppression**: Enhance or suppress specific features (e.g., speckles).
5. **Object Identification**:
   - Primary objects: Cells
6. **Object Conversion**: Convert identified objects to binary masks.
7. **Area Measurement**: Measure area occupied by objects.
8. **Object Shape & Intensity Measurement**: Compute morphological and intensity features.
9. **Texture Measurement**: Calculate texture features.
10. **Tracking**: Track cells over time using the Overlap method.
11. **Saving Images**: Save segmented and tracked images.
12. **Export to Spreadsheet**: Export all measurements to `.csv` files for further analysis.



## Dependencies

- [CellProfiler 4.2.8](https://cellprofiler.org/releases/)


## How to Use

1. Open **CellProfiler**.
2. Load the pipeline:
   - `File` → `Open Project...` → select `finel_pipeline.cpproj`.
3. Set the **Default Input Folder** to your image directory (`input_images/`).
4. Set the **Default Output Folder** to desired output location.
5. Run the pipeline:
   - Click **Analyze Images**.
6. Results:
   - Segmented images saved to `output/`.
   - CSV measurement files saved to `output_data/`.

## Notes

- File names must follow the pattern used in `Metadata` module to extract date/time metadata.
- Adjust typical object diameter and thresholding settings as needed for different datasets.
- Permissions:
   - Ensure the output folders have write permissions (avoid system folders like `Program Files`).

