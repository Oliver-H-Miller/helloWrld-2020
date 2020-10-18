import base64
import re
import datetime
import os
from os import listdir
from os.path import isfile, join
import time
valued = []
values = []
devices = []
from .models import *



def parse_current(filename):
    x = str(filename)
    x = parse(x)
    joe = {'value':x,"time":(datetime.datetime.fromtimestamp(time.time()) - datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')}
    with open("./dining/output.txt","a") as f:
        f.write(f"{x}      Time:{joe['time']}\n")
    values.append(joe)
    bruh = getvalued(x,len(values)-1)
    joed = {**joe,"wait":bruh}
    if bruh != "F":
        valued.append(joed)
    return joed



def parse_previous(filename):
    x = ""
    cwd = os.getcwd()
    mypath = cwd + "/dining/diningdata/"
    try:
        with open(mypath+filename,"r") as f:
            for line in f:
                x += line
    except:
        return filename
    return parse(x)
    # addys = set()
    # for addy in macAddr:
    #     addys.add(addy)

def parse(data):
    p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    pattern = re.compile(r'RSSI: (.\d\d)')
    macAddr = re.findall(p, data)
    # signalStr = re.findall(pattern, data)
    # results = [macAddr, signalStr]
    # time = float(filename.strip(".txt"))
    # curr_time = datetime.datetime.fromtimestamp(time)
    bruh = {}
    for addy in macAddr:
        if addy not in bruh.keys():
            bruh[addy] = 0
        else:
            bruh[addy] += 1
    addys = set()
    for b in bruh.keys():
        if bruh[b]:
            addys.add(b)
    # print(len(addys))
    # print(len(addys))
    return len(addys)
    # print(counter)
    # print(parse(l))
def main():
    loadFiles()

def loadFiles():
    # data = Time.objects.all()
    # for d in data:
    #     d.delete()
    cwd = os.getcwd()
    mypath = cwd + "/dining/diningdata/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    counter = 0
    onlyfiles.sort()
    with open("./dining/output.txt","w") as f:
        for file in onlyfiles:
            l = parse_previous(file)
            if type(l) is not type("bruh") and l is not 0:
                time = float(file.strip(".txt"))
                curr_time = datetime.datetime.fromtimestamp(time) - datetime.timedelta(hours = 4)
                values.append({"value":l,"time":curr_time})
                f.write(f"{l}      Time:{curr_time.strftime('%Y-%m-%d %H:%M')}\n")
            # if l and isinstance(l,int):
            #     f.write(f"{l}\n")
        for i in range(len(values)):
            bruh = getvalued(values[i]['value'],i)
            if bruh != "F":
                valued.append({**values[i],"wait":bruh})
        # for i in range(len(valued)):
        #     f.write(f"{valued[i]['wait']}\n")
    with open("./dining/diningdata.txt","w") as f:
        for i in range(len(valued)):
            f.write(f"{valued[i]['value']},{valued[i]['time']},{valued[i]['wait']}\n")
            # Time.objects.create(devices = valued[i]['value'],time = valued[i]['time'],wait=valued[i]['wait'])
    # print(len(valued))
def getvalued(value,i):
    list = []
    for j in range(-5,6):
        if i + j > 0 and i + j < len(values) - 1:
            list.append(values[i+j]['value'])
    return coolmath(list,value)
def isoutlier(val,iqr,q1,q3):
    iqr *= 1.5
    if (q1-iqr) > val or (q3 + iqr) < val:
        return True
    return False
def coolmath(list,value):
    list.sort()
    mid = len(list)/2
    q = mid/2
    q1 = 0
    q3 = 0
    if q % 1 != 0:
        # print("yes")
        q1 = (list[int(q//1)] + list[int(q//1)+1])/2
        q3 = (list[int(q//1)+int(mid)] + list[int(q//1)+1+int(mid)])/2
    else:
        # print("no")
        q1 = list[int(q)]
        q3 = list[int(q)+int(mid)]
    iqr = q3 - q1
    if iqr != 0 and isoutlier(value,iqr,q1,q3):
        return "F"
    timeconstant = .5
    waittimeconstant = 4.5
    randomconstant = .4
    temp = int(((sum(list)/len(list))-value*randomconstant) * timeconstant - waittimeconstant)
    return temp if temp > 0 else 0

loadFiles()
if __name__ == '__main__':
    main()
