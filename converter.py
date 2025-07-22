from PIL import Image
import os
import shutil

def convert_to_png(image_paths: list,save_directory: str):
    save_path = save_directory

    if not os.path.exists(save_directory):
        try:
            os.mkdir("images")
        except FileExistsError:
            pass
        save_path = "images"
    else:
        try:
            os.mkdir(save_path)
        except FileExistsError:
            pass

    for image in image_paths:
        if ".png" in image:
            print(f"Skipping {image}, already a png")
            shutil(image, save_path)
            continue
    
        try:
            jpg_image = Image.open(image)
            image_name = f"{image.split(".")[0]}.png"
            jpg_image.save(image_name)
            try:
                shutil.move(image_name,save_path)
            except shutil.Error:
                pass
                continue
            

        except FileNotFoundError:
            print(f"Skipping image {image} as it doesn't exist")
            continue

            