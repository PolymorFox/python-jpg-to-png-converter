# Python JPG to PNG Converter

Easily convert one or more JPG images to PNG format using this Python script.

## Requirements

- Python (3.x recommended)
- [Pillow](https://pypi.org/project/pillow/) library

---

## Installation

Install any dependecies using pip:

```
pip install -r requirements.txt
```

If you encounter any errors during installation of dependecies, you can create a virtual environment, activate it and install the dependecies:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

---

## Usage

### Arguments

- `--images`[Required]: Path to image[s] for converter to convert
- `--save_path`[Optional]: Path to folder where to save images, if not specified will default to `Images`

### Examples


```
python main.py --images photo1.jpg,photo2.jpg
```
Will convert `photo1.jpg` and `photo2.jpg`, create a folder called `Images` and move them to `Images`

```
python main.py --images photo1.jpg,photo2.jpg --save_path my_images
```

Will convert `photo1.jpg` and `photo2.jpg` and move them to the folder called `my_images`