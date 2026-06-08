import os
import random
import shutil

IMG_SRC = "../raw_data/images"
LBL_SRC = "../dataset/labels/all"

IMG_DST = "../dataset/images"
LBL_DST = "../dataset/labels"

for p in ["train", "val"]:
    os.makedirs(f"{IMG_DST}/{p}", exist_ok=True)
    os.makedirs(f"{LBL_DST}/{p}", exist_ok=True)

images = [f for f in os.listdir(IMG_SRC) if f.endswith((".jpg", ".png"))]
random.shuffle(images)

split = int(0.8 * len(images))
train_imgs = images[:split]
val_imgs = images[split:]

def move(files, subset):
    for img in files:
        name = os.path.splitext(img)[0]
        shutil.copy(f"{IMG_SRC}/{img}", f"{IMG_DST}/{subset}/{img}")
        shutil.copy(f"{LBL_SRC}/{name}.txt", f"{LBL_DST}/{subset}/{name}.txt")

move(train_imgs, "train")
move(val_imgs, "val")

print("✅ Dataset split into train and val.")