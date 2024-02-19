# file : ds29_osFileList.py 
# desc : 윈도우 파일 리스트

import os

fnameAry = [] 
folderName = 'C:/Windows/system32'

for dirName, suvDirList, fnames in os.walk(folderName):
    for fname in fnames : 
        fnameAry.append(fname)

print(len(fnameAry))

