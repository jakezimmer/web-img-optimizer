import glob, os
from subprocess import call
from subprocess import check_output, check_call
print(os.getcwd())
sum = 0
sizesaved = 0

ACTUALLYDOIT = True
DOGIFS = False
USEMP4 = False
DOJPGS = True
DOPNGS = True
print("")
print("Welcome to the optimizer!")
print("The optimizer will find all the gifs, jpgs, and pngs in a folder and its")
print("subfolders and optimize them.")
print("")
print("If you want we can just print out the files it will effect or we can")
print("actually run the conversion.")
print("")
print("WARNING")
print("The conversion will replace the files it converts so its a good idea to")
print("not actually run the first time.")
print("This is the folder we are going to optimize the images in:")
print(os.getcwd())
print("")
ACTUALLYDOIT = "y"==input("Do you want to actually run the conversions? (y/n)")
DOGIFS = "y"==input("Do you want to optimize gifs? (y/n)")
if (DOGIFS):
    print("gifs are large files. We can save a little space by optimizing the gifs")
    print("but we can save even more space by converting them to mpeg-4 files.")
    print("If you choose to use mpeg-4 files, we will keep the filenames the same (___.gif)")
    print("so that nothing needs to be renamed in your html files.")
    USEMP4 = "y"==input("Do you want to use mpeg-4? (y/n)")
DOJPGS = "y"==input("Do you want to optimize jpgs? (y/n)")
DOPNGS = "y"==input("Do you want to optimize pngs? (y/n)")




def getsize(file):
    return os.path.getsize(file)


if (DOGIFS):
    if (USEMP4):
        for file in glob.glob("**/*.gif", recursive=True):
            print(file)
            filesize = getsize(file)
            if(ACTUALLYDOIT):
                (call(["ffmpeg", "-xerror", "-y", "-i", file, "-movflags", "faststart", "-pix_fmt", "yuv420p", "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2", file]))
            sizesaved = sizesaved + filesize - getsize(file)
            sum=sum+1
        for file in glob.glob("**/*.GIF", recursive=True):
            print(file)
            filesize = getsize(file)
            if(ACTUALLYDOIT):
                (call(["ffmpeg", "-xerror", "-y", "-i", file, "-movflags", "faststart", "-pix_fmt", "yuv420p", "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2", file]))
            sizesaved = sizesaved + filesize - getsize(file)
            sum=sum+1
    else:
        for file in glob.glob("**/*.gif", recursive=True):
            print(file)
            filesize = getsize(file)
            if(ACTUALLYDOIT):
                (call(["gifsicle","-O3", "--colors", "127" ,file ,"-o", file]))
            sizesaved = sizesaved + filesize - getsize(file)
            sum=sum+1
        for file in glob.glob("**/*.GIF", recursive=True):
            print(file)
            filesize = getsize(file)
            if(ACTUALLYDOIT):
                (call(["gifsicle","-O3", "--use-colormap", "web" ,file ,"-o", file]))
            sizesaved = sizesaved + filesize - getsize(file)
            sum=sum+1

if (DOJPGS):
    for file in glob.glob("**/*.jpg", recursive=True):
        print(file)
        filesize = getsize(file)
        if(ACTUALLYDOIT):
            (call(["convert" ,file ,"-quality", "50", file]))
        sizesaved = sizesaved + filesize - getsize(file)
        sum=sum+1

    for file in glob.glob("**/*.JPG", recursive=True):
        print(file)
        filesize = getsize(file)
        if(ACTUALLYDOIT):
            (call(["convert" ,file ,"-quality", "50", file]))
        sizesaved = sizesaved + filesize - getsize(file)
        sum=sum+1

if (DOPNGS):
    for file in glob.glob("**/*.png", recursive=True):
        print(file)
        filesize = getsize(file)
        if(ACTUALLYDOIT):
            (call(["pngquant" ,"-Q", "5", "--ext", ".png", "--force", file]))
        sizesaved = sizesaved + filesize - getsize(file)
        sum=sum+1

    for file in glob.glob("**/*.PNG", recursive=True):
        print(file)
        filesize = getsize(file)
        if(ACTUALLYDOIT):
            (call(["pngquant" ,"-Q", "5", "--ext", ".png", "--force", file]))
        sizesaved = sizesaved + filesize - getsize(file)
        sum=sum+1


print("total number of files processed:")
print(sum)

print("total bytes saved:")
print(sizesaved)
