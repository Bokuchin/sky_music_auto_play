#!/usr/bin/env python3

import json
import csv


a = open('guresenbon.txt', 'r', encoding="utf-8")
b = json.load(a)
c = b[0]["songNotes"][0]["key"]
print(c)#=>2key0

d = b[0]["songNotes"]


midi = [48,50,52,53,55,57,59,60,62,64,65,67,69,71,72]
li = []
buf = 0
for i, e in enumerate(d):
    li.append([e["time"], 144, midi[int(e["key"][4])]])
    if i+1 < len(d):
        if d[i+1]["time"] != e["time"]:
            if buf == 0:
                li.append([e["time"]+95, 128, midi[int(e["key"][4])]])
            else:
                for j in range(buf+1):
                    li.append([e["time"]+95, 128, midi[int(d[i-j]["key"][4])]])
            buf = 0
        else:
            buf += 1
#saigo no key wo hanasu noga kakikomete inai        


fh = open("guresenbon.csv", "w")
writer = csv.writer(fh)
for i in range(len(li)):
    writer.writerow(li[i])



fh.close()
a.close()