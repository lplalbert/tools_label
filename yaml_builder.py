with open("D:/desktop/target.txt") as f1:
    set1 = set()
    for line in f1:
        if line[:2] not in set1:
            set1.add(line[:2])

set1 = sorted(set1)

f2 = open("D:\\desktop\\Mahjong_V2.0.v123i.yolov5pytorch\\data.yaml", 'w')
f2.write("train: ../train/images\nval: ../valid/images\n\n")
f2.write("nc: "+str(len(set1))+"\n")
f2.write("names: [")
s = []
for i in set1:
    s.append('\''+str(i)+'\'')
f2.write(', '.join(s))
f2.write(']')
f2.close()


