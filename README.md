# Smart Pothole Detection System using YOLOv8

## Dataset

The dataset for this project is stored in Google Drive due to its size (>100 files):

📁 **[Download Dataset](https://drive.google.com/drive/folders/1I4IXa26R2rt_J7R4uXe7_NQQ8Gn6SEik)**

> Note: The dataset is too large to host on GitHub, so we use Google Drive for storage. Download the dataset and extract it to the project directory before running the training scripts.

## Steps to Run

### 1. Download Dataset
- Click the link above to access the Google Drive folder
- Download and extract the dataset to your local project directory

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Convert annotations
```bash
cd scripts
python convert_xml_to_yolo.py
```

### 4. Split dataset
```bash
python split_dataset.py
```

### 5. Train model
```bash
cd ..
python train.py
```

### 6. Copy best weights
```bash
cp runs/detect/pothole_detector/weights/best.pt model/
```

### 7. Run frontend
```bash
cd app
streamlit run app.py
```

For more details about the dataset, see [DATASET.md](DATASET.md)