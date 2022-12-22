# ChangeLabelClassNumsForYoloTxt
When you first try labelImg to label your own dataset, you might forgot to remove the default classes and just added you're own classes above it.
This will make a problem when you tried to train yolo, after you edit the .yaml file and editing the nc and names for your own data, the compiler while report error while you started training the model, it's because the label txt assign the number of your class after the default classes, which your first class should be 0 but ended to be like 15 for example, and this is the reason your compiler fail to proceed the training process.
So I wrote a small code for newbies like me to refer, open the txt to read the first line and read the txt again but with '+w' so we can rewrite it with the edited line we read before.

```
from os import listdir
from os.path import isfile, join

def findAllFn(myPath):
    myList = [f for f in listdir(myPath) if isfile(join(myPath, f))]
    return myList

targetPath = "your path"

// read filename into list
labelList = findAllFn(targetPath)


for txt in labelList:
    f = open(join(targetPath,txt)) 
    lines = f.readlines() //read the current txt with wrong class nums
    fw = open(join(targetPath,txt),"+w") // open the txt with editable mode
    str1 = str(0)+lines[0][2:] //You might need to change a little depends on the situation
    fw.write(str1) //save the txt
    
```
