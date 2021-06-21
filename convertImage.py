import os, sys
import whatimage
import pyheif
from PIL import Image


def convert_HEIF_to_PDF(imageFile, convert_format, storage_dir, verbose=False):
    assert os.path.exists(imageFile)
    assert os.path.exists(storage_dir)
    heifImg = pyheif.read_heif(imageFile)
    metadata = heifImg.metadata
    imgName = imageFile.split("/")[-1].split(".")[0]
    fileOutPath = os.path.join(storage_dir, imgName+"."+convert_format)
    pi = Image.frombytes(mode=heifImg.mode, size=heifImg.size, data=heifImg.data)
    pi.save(fileOutPath, format=convert_format)
    if verbose == True:
        print("Converted Image saved to "+fileOutPath)




###################################################
def assemble_Images_and_convert(input_Storage_dir, Image_format, output_storage_dir, output_format):
    assert os.path.exists(input_Storage_dir)
    files_in_Storage_Dir = os.listdir(input_Storage_dir)
    ims_to_convert = []
    for f in files_in_Storage_Dir:
        if f.endswith(Image_format):
            ims_to_convert.append(os.path.join(input_Storage_dir, f))
        else:
            continue



    for im in ims_to_convert:
        convert_HEIF_to_PDF(im, output_format, output_storage_dir)


input_storage_dir = "/Users/abhishekdas/Desktop/QCPlotData/HPK/Visual"
output_storage_dir = "/Users/abhishekdas/Desktop/Storage/HPK"

assemble_Images_and_convert(input_storage_dir, "HEIC", output_storage_dir, "pdf")

