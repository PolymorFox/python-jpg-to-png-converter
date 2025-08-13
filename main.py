import argparse
from converter import convert_to_png

parser = argparse.ArgumentParser()
parser.add_argument("--images",type=str,default=None)
parser.add_argument("--save_path",type=str,default="Images")

args = parser.parse_args()

image_paths = args.images.split(",")
save_path = args.save_path

for image in image_paths:
    convert_to_png(image,save_path)



