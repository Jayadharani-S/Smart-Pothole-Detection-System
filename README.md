# Smart Pothole Detection System using YOLOv8

## Steps to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Convert annotations
cd scripts
python convert_xml_to_yolo.py

### 3. Split dataset
python split_dataset.py

### 4. Train model
cd ..
python train.py

### 5. Copy best weights
runs/detect/pothole_detector/weights/best.pt → model/

### 6. Run frontend
cd app
streamlit run app.py