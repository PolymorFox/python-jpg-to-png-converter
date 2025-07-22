from PIL import Image
import os
import shutil

def convert_to_png(image_paths: list | str,save_directory: str):
    save_location =os.path.abspath(save_directory)

    if not os.path.exists(save_directory):
        try:
            os.mkdir("images")
        except FileExistsError:
            pass
        save_location = os.path.abspath("images")
    else:
        try:
            os.mkdir(save_directory)
        except FileExistsError:
            pass
    if type(image_paths).__name__ == "list":
        for image in image_paths:
            if image.endswith(".png"):
                print(f"Skipping {image}, already a png")
                shutil.move(image, save_location)
                continue
        
            try:
                jpg_image = Image.open(image)
                image_name = f"{image.split(".")[0]}.png"
                jpg_image.save(image_name)
                try:
                    shutil.move(image_name,save_location)
                except shutil.Error:
                    pass
                    continue
                

            except FileNotFoundError:
                print(f"Skipping image {image} as it doesn't exist")
                continue
    elif type(image_paths).__name__ == "str":
        with os.scandir(image_paths) as iter:
            for entry in iter:
                if entry.is_dir():
                    continue
                elif entry.name.endswith(".png"):
                    print(f"Skipping {entry.name}, already a png")
                    shutil.move(entry.path, save_location)
                elif entry.name.endswith(".jpg"):
                    img = Image.open(entry.path)
                    file_name = f"{os.path.splitext(entry.name)[0]}.png"
                    img.save(file_name)
                    shutil.move(file_name, save_location)




