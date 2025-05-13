from PIL import Image
from pathlib import Path
import os


def to_webp(image_path: str):
    to_webp_path = Path(image_path).with_suffix(".webp").absolute().as_posix()
    with Image.open(image_path) as image:
        options = {
            "lossless": False,
            "quality": 80,
            "transparent": True,
        }
        image.save(to_webp_path, "webp", **options)
        print(f"webp格式图片已保存至{to_webp_path}")


def process_folder(folder_path: str, target_dir: str):
    if target_dir != "":
        for _, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".png"):
                    print(f"file: {file}")
                    to_webp(os.path.join(target_dir, file))
    else:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".png"):
                    print(f"file: {file}")
                    to_webp(os.path.join(root, file))


if __name__ == "__main__":
    print("输入文件夹路径")
    file = input()
    print("保存根目录，空白为同一目录下")
    target_dir = input()
    process_folder(folder_path=file, target_dir=target_dir)
