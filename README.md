# Welcome to the Image Optimizer
This optimizer performs [lossy compression](https://en.wikipedia.org/wiki/Lossy_compression)
If you're looking for lossless compression this is a [good one](https://github.com/joedicastro/img4web)

---
## Pre-requisites

The script uses python 3 which you can download from [here](https://www.python.org/downloads/) if you dont already have it

Additionally, it uses 
- [gifsicle](https://www.lcdf.org/gifsicle/)
- [ffmpeg](https://www.ffmpeg.org/)
- [pngquant](https://pngquant.org/)
- [ImageMagick](http://www.imagemagick.org/script/index.php)


These can be downloaded from their sites or if you are running Debian or Ubuntu, can be downloaded with apt or apt-get
    
    sudo apt install ffmpeg, gifsicle, pngquant, imagemagick

---

## Usage

To actually use the script, copy the `shrinkImages.py` file to the folder containing your images. Then run the script like you would any other python script.

The script can be used to do a dry run (aka not actually convert) to determine which files are going to be affected. Running the script will guide you through this process.