import os
from os import listdir
from os.path import isfile, join

def findAllFn(myPath):
    myList = [f for f in listdir(myPath) if isfile(join(myPath, f))]
    return myList

targetPath = "yout path"

labelList = findAllFn(targetPath)

for txt in labelList:
    f = open(join(targetPath,txt))
    lines = f.readlines()
    fw = open(join(targetPath,txt),"+w")
    str1 = str(0)+lines[0][2:]
    fw.write(str1)