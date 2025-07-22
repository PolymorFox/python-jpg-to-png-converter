# Python JPG to PNG Converter

Easily convert one or more JPG images to PNG format using this Python script.

## Requirements

- Python (3.x recommended)
- [Pillow](https://pypi.org/project/pillow/) library

## Installation

Install Pillow with pip:

```
pip install -r requirements.txt
```

## Usage

To convert a single image or multiple images, run:

```
python main.py --image <path_to_image1.jpg,path_to_image2.jpg,...> --destination <output_folder>
```

- `<path_to_image1.jpg,path_to_image2.jpg,...>`: Comma-separated list of JPG image paths.
- `<output_folder>`: Folder where converted PNG images will be saved.

**Example:**

``` 
python main.py --image photo1.jpg,photo2.jpg --destination converted_images
```