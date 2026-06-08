from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="configs/data.yaml",
    epochs=10,
    imgsz=640,
    batch=8,
    name="pothole_detector"
)
