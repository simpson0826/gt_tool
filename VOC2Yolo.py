API_description = """
***** FILE SPLIT AND MATCH COPY *****
Created on Fri Aug  4 14:44:56 2023

@author: Simpson_Huang

Instructions: Translate VOC to Yolo format
*************************************

"""

import os
import argparse
import xml.etree.ElementTree as ET


parser = argparse.ArgumentParser(
    prog = 'VOC2Yolo.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=API_description)

parser.add_argument('-xml_folder', action='store', type=str, help = 'The absolute path to the XML folder')
parser.add_argument('-outputfolder', action='store', type=str, help = 'The absolute path to the  Outputfolder')
args = parser.parse_args()

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)




def main():
    xml_files = os.listdir(args.xml_folder)
    for xml_file_name in xml_files:
        #print(xml_file_name)
        if os.path.splitext(xml_file_name)[1] != ".xml":
            continue
        xml_file_path = os.path.join(args.xml_folder, xml_file_name)
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        outputfilename = xml_file_name.replace('.xml', '.txt')
        outputfile = open(os.path.join(args.outputfolder,outputfilename), 'w')
        for obj in root.iter('object'):
            #difficult = obj.find('difficult').text
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            outputfile.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')
        outputfile.close()

if __name__ == "__main__":
    main()