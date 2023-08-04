API_description = """
***** FILE SPLIT AND MATCH COPY *****
Created on Fri Aug  4 14:44:56 2023

@author: Simpson_Huang

Instructions: Split copy file to Train/Test folder
*************************************

"""

import os
import os.path
import shutil  #Python檔案複製相應模組
import argparse
import random

parser = argparse.ArgumentParser(
        prog='file_name_match.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=API_description)

parser.add_argument('-source_dir', action = 'store', type = str, help = 'The absolute path to the source folder.')
parser.add_argument('-label_dir', action = 'store', type = str, help = 'The absolute path to the GT folder.')
parser.add_argument('-output_dir', action = 'store', type = str, help = 'The absolute path to the output folder.')
parser.add_argument('-rate', action = 'store', type = float, help = 'The number of splits')
args = parser.parse_args()

def copyFile():
    s=[]
    for filename in os.listdir(args.source_dir):
        if filename.endswith('jpg') or filename.endswith('jpeg'):  
            #print(filename)
            s.append(filename)
    filenumber=len(s)
    #print(filenumber)
    percentage=args.rate
    picknumber=int(filenumber*percentage)
    sample = random.sample(s, picknumber)
    #print (sample)
    for name in sample:
        shutil.copy(os.path.join(args.source_dir,name), os.path.join(args.output_dir,name))
    return



def main():
    assert (os.path.exists(args.source_dir)), "The source folder cannot be found"
    assert (os.path.exists(args.label_dir)), "The GT folder cannot be found"
    #assert (os.path.exists(args.output_dir)), "The folder path of image root cannot be found"
    if (os.path.exists(args.output_dir) == False):
        os.mkdir(args.output_dir)
        print("output_dir make dir ok")
    copyFile()
##1.將指定A目錄下的檔名取出,並將檔名文字和檔案字尾拆分出來
    img=os.listdir(args.output_dir)  #得到資料夾下所有檔名稱
    for fileNum in img: #遍歷資料夾
        if not os.path.isdir(fileNum): #判斷是否是資料夾,不是資料夾才打開
            #print (fileNum)  #打印出檔名
            imgname= os.path.join(args.output_dir,fileNum)
            #print (imgname)  #打印出檔案路徑
            (imgpath,tempimgname) = os.path.split(imgname); #將路徑與檔名分開
            (shotname,extension) = os.path.splitext(tempimgname); #將檔名文字與檔案字尾分開
            #print (shotname,extension)
            #print ("~~~")
##2.將取出來的檔名文字與特定字尾拼接,再與路徑B拼接,得到B目錄下的檔案	
            tempxmlname='%s.txt'%shotname	
            txtname=os.path.join(args.label_dir,tempxmlname)
            #print(txtname)
##3.根據得到的txt檔名,將對應檔案拷貝到指定目錄C
            shutil.copy(txtname,args.output_dir)
        
if __name__ == "__main__":
    main()