from ultralytics import YOLO

model = YOLO("model/best.pt")

results = model("test.jpg", show=True, save=True)