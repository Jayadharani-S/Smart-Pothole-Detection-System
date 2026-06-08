# Dataset Documentation

## Overview

This project uses a custom dataset for pothole detection. Due to GitHub's file limitations and the large number of files in the dataset (>100 files), the dataset is hosted on Google Drive.

## Download Instructions

### Access the Dataset
📁 **[Google Drive Folder](https://drive.google.com/drive/folders/1I4IXa26R2rt_J7R4uXe7_NQQ8Gn6SEik)**

### Steps to Download:
1. Click the link above
2. Click the download button (folder icon with arrow) to download the entire dataset
3. Extract the downloaded ZIP file to your project root directory
4. Ensure the dataset folder is at the same level as your scripts and training files

## Dataset Structure

The dataset should contain:
- **Images**: All training and validation images in appropriate directories
- **Annotations**: XML or YOLO format annotations corresponding to images
- **Directory layout**: Organized for easy processing by the conversion and splitting scripts

## File Size & Requirements

- **Total size**: Large dataset (>100 files)
- **Recommended storage**: At least 1-2 GB of free disk space
- **Processing time**: Dataset conversion and splitting may take several minutes

## Dataset Preparation Workflow

Once downloaded and extracted, follow these steps:

```bash
# 1. Convert annotations from XML to YOLO format
cd scripts
python convert_xml_to_yolo.py

# 2. Split dataset into training and validation sets
python split_dataset.py

# 3. Return to root and train model
cd ..
python train.py
```

## Notes

- ⚠️ Do NOT commit the dataset folder to Git (it's already in `.gitignore`)
- The dataset is stored externally to maintain repository size efficiency
- All users need to download the dataset independently before training
- Keep the dataset in the expected directory structure for scripts to work correctly

## Troubleshooting

- If scripts can't find the dataset, verify it's extracted in the correct location
- Check that the folder structure matches what the conversion scripts expect
- Refer to `convert_xml_to_yolo.py` for exact expected directory structure