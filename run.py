import os

path = "D:\\desktop\\Mahjong_V2.0.v123i.yolov5pytorch\\train\\labels\\"

with open("D:/desktop/target.txt") as f2:
    set1 = set()
    list2 = []
    for line in f2:
        list2.append(line[:2])
        if line[:2] not in set1:
            set1.add(line[:2])

set1 = sorted(set1)
dict1 = {}
num = 0
for i in set1:
    dict1[i] = num
    num += 1

fileList = os.listdir(path)
for i in fileList:
    lines = open(path + i).readlines()
    fp = open(path + i, 'w')
    for s in lines:
        ind1 = int(s.split(' ')[0])
        ind2 = dict1[list2[ind1]]
        if ind1 < 10:
            s = str(ind2) + s[1:]
        else:
            s = str(ind2) + s[2:]
        fp.write(s)
    fp.close()

f = open(path + 'classes.txt', 'w')
for i in set1:
    f.write(i+'\n')
f.close()
