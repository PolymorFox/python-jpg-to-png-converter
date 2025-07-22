import argparse
from converter import convert_to_png

parser = argparse.ArgumentParser()
parser.add_argument("--image",type=str,default=None)
parser.add_argument("--destination",type=str,default=None)

args = parser.parse_args()


if args.image == '':
    print("An empty list of images was provided")
    exit(1)
elif args.destination == '':
    print("No save directory was specified, using default images/ directory")
    exit(1)

if ',' not in args.image:
    images = []
    images.append(args.image)
elif ',' in args.image:
    images = args.image.split(',')

destination = args.destination

convert_to_png(images,destination)



