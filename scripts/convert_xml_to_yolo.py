import os
import xml.etree.ElementTree as ET

RAW_ANN_DIR = "../raw_data/annotations"
RAW_IMG_DIR = "../raw_data/images"
OUT_LABEL_DIR = "../dataset/labels/all"

os.makedirs(OUT_LABEL_DIR, exist_ok=True)

def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x_center = (box[0] + box[1]) / 2.0
    y_center = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return x_center * dw, y_center * dh, w * dw, h * dh

for xml_file in os.listdir(RAW_ANN_DIR):
    tree = ET.parse(os.path.join(RAW_ANN_DIR, xml_file))
    root = tree.getroot()

    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    label_path = os.path.join(
        OUT_LABEL_DIR, xml_file.replace(".xml", ".txt")
    )

    with open(label_path, "w") as f:
        for obj in root.iter("object"):
            xmlbox = obj.find("bndbox")
            b = (
                float(xmlbox.find("xmin").text),
                float(xmlbox.find("xmax").text),
                float(xmlbox.find("ymin").text),
                float(xmlbox.find("ymax").text),
            )
            bb = convert((w, h), b)
            f.write(f"0 {' '.join(map(str, bb))}\n")

print("✅ XML to YOLO conversion done.")