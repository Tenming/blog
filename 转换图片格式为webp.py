from PIL import Image
from pathlib import Path
import os

def to_webp(image_path:str):
    to_webp_path = Path(image_path).with_suffix('.webp').absolute().as_posix()
    with Image.open(image_path) as image:
        options = {
            "lossless": False,
            "quality": 80,
            "transparent": True,
        }
        image.save(to_webp_path, "webp", **options)

def process_folder(folder_path:str):
    for root, _, files in os.walk(folder_path):
        for file in files:
            print(f"root: {root}\nfile: {file}\nfull path: {os.path.join(root, file)}")
            if file.endswith('.png'):
                to_webp(os.path.join(root, file))
if __name__ == "__main__":
    print("输入文件夹路径")
    file = input()
    process_folder(file)