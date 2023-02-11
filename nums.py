import os
from collections import defaultdict

path = "D:\\desktop\\mahjong.v5i.yolov5pytorch\\train\\labels\\"

with open(path+"classes.txt") as f2:
    list2 = []
    for line in f2:
        list2.append(line[:2])

dict1 = defaultdict(int)

fileList = os.listdir(path)
for i in fileList:
    if i == "classes.txt":
        continue
    lines = open(path + i).readlines()
    for s in lines:
        ind1 = int(s.split(' ')[0])
        dict1[list2[ind1]] += 1

dict1 = sorted(dict1.items(), key=lambda d: d[1], reverse=True)

for i in dict1:
    print(i)
