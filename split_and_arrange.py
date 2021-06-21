import os, sys



def crawl(lines, start_index):
    index = start_index
    while True and index < len(lines):
        if lines[index].startswith("LineSerial"):
            line = lines[index].split("=")
            LineSerial = line[1]
            ModuleNum = LineSerial.split("_")[-1]
            break
        index += 1
    count = 0
    index = start_index
    statement = ""
    while True and index < len(lines):
        this_line = lines[index]
        if this_line.startswith("[Data]"):
            count += 1
        if count > 32:
            break
        statement += this_line + "\n"
        index += 1

    return ModuleNum, statement, index
    

def split_and_arrange(filePath, biasType):
    assert os.path.exists(filePath)
    fileDir = os.path.dirname(filePath)
    f = open(filePath, "r")
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line[:-2]
    first_index = lines.index("[Data]")
    common_file_headers_asList = lines[:first_index]
    common_file_headers = ''
    for item in common_file_headers_asList:
        common_file_headers += item+"\n"

    #print(common_file_headers)
    crawl_index = first_index
    while crawl_index < len(lines):
        moduleNum, statement, crawl_index = crawl(lines, crawl_index)
        outfilePath = os.path.join(fileDir, moduleNum+"_"+biasType+".data")
        fout = open(outfilePath, "w")
        fout.write(statement)
        fout.close()
    
    


split_and_arrange("SiPM_32_Modules_21_20_19_22_30_25_28_23_LED_Dark_sipmdata.data", "DarkLED")
