import base64
import re
import datetime
import os
from os import listdir
from os.path import isfile, join

valued = []
values = []


def parse_current(filename):
    x = str(filename)
    values.append(x)
    bruh = getvalued(x,len(values)-1)
    if bruh != "F":
        valued.append(bruh)
    return bruh



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
    return len(addys)
    # print(counter)
    # print(parse(l))
def main():
    x ="hype"
    # loadFiles()
def loadFiles():
    cwd = os.getcwd()
    mypath = cwd + "/dining/diningdata/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    counter = 0
    times = []
    onlyfiles.sort()
    with open("./dining/output.txt","w") as f:
        for file in onlyfiles:
            l = parse_previous(file)
            if type(l) is not type("bruh") and l is not 0:
                values.append(l)
                time = float(file.strip(".txt"))
                curr_time = datetime.datetime.fromtimestamp(time)
                times.append(curr_time.strftime("%Y-%m-%d %H:%M"))
            # if l and isinstance(l,int):
            #     f.write(f"{l}\n")
        for i in range(len(values)):
            bruh = getvalued(values[i],i)
            if bruh != "F":
                valued.append(bruh)
        for i in range(len(valued)):
            f.write(f"{valued[i]} time: {times[i]}\n")
    with open("./dining/diningdata.txt","w") as f:
        for i in range(len(valued)):
            f.write(f"{valued[i]}, time: {times[i]}\n")
def getvalued(value,i):
    list = []
    for j in range(-5,6):
        if i + j > 0 and i + j < len(values) - 1:
            list.append(values[i+j])
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


if __name__ == '__main__':
    main()


loadFiles()
