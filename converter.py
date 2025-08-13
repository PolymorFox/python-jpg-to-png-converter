from PIL import Image
import os
import shutil

def convert_to_png(image_path: str, save_path: str) -> None:
    if not os.path.exists(save_path):
        os.makedirs("Images",exist_ok=True)
        save_directory = "Images"
    else:
        save_directory = save_path

    if image_path is None:
        print("No images were provided")
        exit(1)
    elif image_path.endswith(".png"):
        # Ignore images that already are .png
        shutil.move(image_path,save_path)
    else:
        jpg_image = Image.open(image_path)
        png_filename = f"{image_path.split(".")[0]}.png"

        jpg_image.save(png_filename,format='PNG')
        shutil.move(png_filename,save_directory)
        jpg_image.close()
    