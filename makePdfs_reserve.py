import os, sys
from PIL import Image
from collections import defaultdict
from PyPDF2 import PdfFileMerger
####################################################################
###   Function for Converting Images to Pdfs and to merge them   ###
####################################################################

def makePdf(images, vendor, storage_dir, moduleNum):
    assert os.path.exists(storage_dir)
    validImages = []
    for image in images:
        if not os.path.exists(image):
            print("Warning !!! The image at location "+image+" is not found !!!")
        else:
            validImages.append(image)

    if len(validImages) < 1:
        raise NotImplementedError("No valid image found")

    validPdfs = []
    imgObjects = []
    for img in validImages:
        imgName = img.split('/')[-1].split('.')[0]
        storagePath = os.path.join(storage_dir, imgName+".pdf")
        if img.endswith(".pdf"):
            os.system("cp "+img+" "+storagePath)
        else:
            imObj = Image.open(img)
            imObj1 = imObj.convert('RGB')
            storagePath = os.path.join(storage_dir, imgName+".pdf")
            imObj1.save(storagePath)
        validPdfs.append(storagePath)

    merger = PdfFileMerger()
    for validPDF in validPdfs:
        merger.append(validPDF)
    final_outputPath = os.path.join(storage_dir, str(moduleNum)+"_"+vendor+".pdf")
    merger.write(final_outputPath)
    merger.close()
    


        
####################################################################################
####           Assembling and Aggregrating According to Array Number            ####
####################################################################################

def assemble_and_segregrate(ImageDict, vendor, storage_dir):

    for key in ImageDict.keys():
        #print(ImageDict[key])
        assert os.path.exists(ImageDict[key])
        
    visual_image_dir = ImageDict["Visual"]
    
    DarkLED_atRoomTemp_image_dir = ImageDict["DarkLED_atRoomTemp"]
    ForwardBias_atRoomTemp_image_dir = ImageDict["ForwardBias_atRoomTemp"]
    #TEC_atRoomTemp_image_dir = ImageDict["TEC_atRoomTemp"]

    #DarkLED_atFreeze_image_dir = ImageDict["DarkLED_atFreeze"]
    #ForwardBias_atFreeze_image_dir = ImageDIct["ForwardBias_atFreeze"]
    #TEC_atFreeze_image_dir = ImageDict["TEC_atFreeze"]

    #DarkLED_atRoomTemp_data_dir = ImageDict["DarkLED_data_atRoomTemp"]
    #ForwardBias_atRoomTemp_data_dir = ImageDict["ForardBias_data_atRoomTemp"]
    #TEC_atRoomTemp_data_dir = ImageDict["TEC_data_atRoomTemp"]

    #DarkLED_atFreeze_data_dir = ImageDict["DarkLED_data_atFreeze"]
    #ForwardBias_atFreeze_data_dir = ImageDict["ForardBias_data_atFreeze"]
    #TEC_atFreeze_data_dir = ImageDict["TEC_data_atFreeze"]

    
    
    visual_images = os.listdir(visual_image_dir)
    for i in range(len(visual_images)):
        visual_images[i] = os.path.join(visual_image_dir, visual_images[i])

    DarkLED_atRoomTemp_images = os.listdir(DarkLED_atRoomTemp_image_dir)
    for i in range(len(DarkLED_atRoomTemp_images)):
        DarkLED_atRoomTemp_images[i] = os.path.join(DarkLED_atRoomTemp_image_dir, DarkLED_atRoomTemp_images[i])

    Forward_atRoomTemp_images = os.listdir(ForwardBias_atRoomTemp_image_dir)
    for i in range(len(Forward_atRoomTemp_images)):
        Forward_atRoomTemp_images[i] = os.path.join(ForwardBias_atRoomTemp_image_dir, Forward_atRoomTemp_images[i])


    """
    TEC_atRoomTemp_images = os.listdir(TEC_atRoomTemp_image_dir)
    for i in range(len(TEC_atRoomTemp_images)):
        TEC_atRoomTemp_images[i] = os.path.join(TEC_atRoomTemp_image_dir, TEC_atRoomTemp_images[i])

    DarkLED_atRoomTemp_data = os.listdir(DarkLED_atRoomTemp_data_dir)
    for i in range(len(DarkLED_atRoomTemp_data)):
        DarkLED_atRoomTemp_data[i] = os.path.join(DarkLED_atRoomTemp_data_dir, DarkLED_atRoomTemp_data[i])

    ForwardBias_atRoomTemp_data = os.listdir(ForwardBias_atRoomTemp_data_dir)
    for i in range(len(ForwardBias_atRoomTemp_data)):
        ForwardBias_atRoomTemp_data[i] = os.path.join(ForwardBias_atRoomTemp_data_dir, ForwardBias_atRoomTemp_data[i])

    TEC_atRoomTemp_data = os.path.join(TEC_atRoomTemp_data_dir)
    for i in range(len(TEC_atRoomTemp_data)):
        TEC_atRoomTemp_data[i] = os.path.join(TEC_atRoomTemp_data_dir, TEC_atRoomTemp_data[i])

    
    DarkLED_atFreeze_data = os.listdir(DarkLED_atFreeze_data_dir)
    for i in range(len(DarkLED_atFreeze_data)):
        DarkLED_atFreeze_data[i] = os.path.join(DarkLED_atFreeze_data_dir, DarkLED_atFreeze_data[i])

    ForwardBias_atFreeze_data = os.listdir(ForwardBias_atFreeze_data_dir)
    for i in range(len(ForwardBias_atFreeze_data)):
        ForwardBias_atFreeze_data[i] = os.path.join(ForwardBias_atFreeze_data_dir, ForwardBias_atFreeze_data[i])

    TEC_atFreeze_data = os.listdir(TEC_atFreeze_data_dir)
    for i in range(len(TEC_atFreeze_data)):
        TEC_atFreeze_data[i] = os.path.join(TEC_atFreeze_data_dir, TEC_atFreeze_data[i])

    DarkLED_atFreeze_images = os.listdir(DarkLED_atFreeze_image_dir)
    for i in range(len(DarkLED_atFreeze_images)):
        DarkLED_atFreeze_images[i] = os.path.join(DarkLED_atFreeze_image_dir, DarkLED_atFreeze_images[i])

    ForwardBias_atFreeze_images = os.listdir(ForwardBias_atFreeze_image_dir)
    for i in range(len(ForwardBias_atFreeze_images)):
        ForwardBias_atFreeze_images[i] = os.path.join(ForwardBias_atFreeze_image_dir, ForwardBias_atFreeze_images[i])

    TEC_atFreeze_images = os.listdir(TEC_atFreeze_image_dir)
    for i in range(len(TEC_atFreeze_images)):
        TEC_atFreeze_images[i] = os.path.join(TEC_atFreeze_image_dir, TEC_atFreeze_images[i])
    

    """

    
    segregated_images = defaultdict(list)
    for itemPath in visual_images:
        itemName = itemPath.split("/")[-1].split(".")[0]
        itemSplit = itemName.split("_")[0]
        moduleNum = eval(itemSplit)
        segregated_images[moduleNum].append(itemPath)

    for itemPath in DarkLED_atRoomTemp_images:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)

    for itemPath in ForwardBias_atRoomTemp_images:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)


    """

    for itemPath in TEC_atRoomTemp_images:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)

    for itemPath in DarkLED_atRoomTemp_data:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)

    for itemPath in ForwardBias_atRoomTemp_data:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)

    for itemPath in TEC_atRoomTemp_data:
	itemName = itemPath.split("/")[-1].split(".")[0]
	moduleNum = eval(itemName.split("_")[0])
	segregated_images[moduleNum].append(itemPath)

    for itemPath in DarkLED_atFreeze_images:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)

    for itemPath in ForwardBias_atFreeze_images:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)

    for itemPath in TEC_atFreeze_images:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)

    for itemPath in DarkLED_atFreeze_data:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)

    for itemPath in ForwardBias_atFreeze_data:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)

    for itemPath in TEC_atFreeze_data:
        itemName = itemPath.split("/")[-1].split(".")[0]
        moduleNum = eval(itemName.split("_")[0])
        segregated_images[moduleNum].append(itemPath)


    """



    for key in segregated_images.keys():
        images = []
        images.append(segregated_images[key][0])
        images.append(segregated_images[key][1])
        images.append(segregated_images[key][2])
        #images.append(segregated_images[key][3])
        #images.append(segregated_images[key][7])
        #images.append(segregated_images[key][8])
        #images.append(segregated_images[key][9])
        makePdf(images, vendor, storage_dir)




ImageDict = {}
ImageDict["Visual"] = "/Users/abhishekdas/Desktop/QCPlotData/HPK/Visual"
ImageDict["DarkLED_atRoomTemp"] = "/Users/abhishekdas/Desktop/QCPlotData/HPK/Dark_LED"
ImageDict["ForwardBias_atRoomTemp"] = "/Users/abhishekdas/Desktop/QCPlotData/HPK/ForwardBias"
assemble_and_segregrate(ImageDict, "HPK", "/Users/abhishekdas/Desktop/Storage/HPK")

