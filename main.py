# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os,sys
path1 = "I:\暂时文件夹2"
dirs = os.listdir(path1)

i=0
for dir in dirs:
    newname = "2022-" + dir[4:6] +"-"+dir[6:8]
    os.rename(path1+"\\"+str(dir),path1+"\\"+newname)
print(path1)
