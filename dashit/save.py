import base64
import re
import datetime
completed = []
inprogress = {}
import os
from os import listdir
from os.path import isfile, join

def parse_now(x):
    data = str(base64.b64decode(x))
    p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    pattern = re.compile(r'RSSI: (.\d\d)')

    macAddr = re.findall(p, data)
    # signalStr = re.findall(pattern, data)
    # results = [macAddr, signalStr]
    for add in macAddr:
        if add not in inprogress.keys():
            inprogress[add] = datetime.datetime.now()
    for complete in completed:
        if(datetime.datetime.now()+datetime.timedelta(minutes = 5) < complete['start']):
            completed.remove(complete)
    for key in inprogress.keys():
        if key not in macAddr:
            start = macAddr[key]
            end = datetime.datetime.now()
            time = end - start
            if time > datetime.timedelta(minutes = 1) and time < datetime.timedelta(hours = 1):
                complete.append({"time":time,"start":datetime.datetime.now()})
            del inprogress[key]
    sum = None
    for complete in completed:
        sum += complete.time
    return sum.total_seconds/(60*len(completed))


def parse_previous(filename):
    x = ""
    cwd = os.getcwd()
    mypath = cwd + "/diningdata/"
    try:
        with open(mypath+filename,"r") as f:
            for line in f:
                x += line
        data = x
    except:
        return filename
    p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    pattern = re.compile(r'RSSI: (.\d\d)')
    macAddr = re.findall(p, data)
    # signalStr = re.findall(pattern, data)
    # results = [macAddr, signalStr]
    time = float(filename.strip(".txt"))
    curr_time = datetime.datetime.fromtimestamp(time)
    for add in macAddr:
        if add not in inprogress.keys() :
            inprogress[add] = curr_time
    if len(macAddr) != 0:
        for complete in completed:
            if(curr_time+datetime.timedelta(minutes = 15) < complete['start']):
                completed.remove(complete)
    keys = set()
    for key in inprogress.keys():
        if key not in macAddr:
            start = inprogress[key]
            end = curr_time
            time = end - start
            if time > datetime.timedelta(minutes = 1) and time < datetime.timedelta(minutes= 20):
                completed.append({"time":time,"start":curr_time})
            keys.add(key)
    for key in keys:
        del inprogress[key]
    sum = datetime.timedelta(0)
    for complete in completed:
        sum += complete['time']
    if len(completed) > 0:
        print(f"Filename:{filename} Count:{len(completed)} MacAddr:{len(macAddr)}")
    return 0 if not len(completed) else sum.total_seconds()/(60*len(completed))

# def parse_previous(filename):
#     x = ""
#     cwd = os.getcwd()
#     mypath = cwd + "/diningdata/"
#     try:
#         with open(mypath+filename,"r") as f:
#             for line in f:
#                 x += line
#         data = x
#     except:
#         return filename
#     p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
#     pattern = re.compile(r'RSSI: (.\d\d)')
#     macAddr = re.findall(p, data)
#     # signalStr = re.findall(pattern, data)
#     # results = [macAddr, signalStr]
#     time = float(filename.strip(".txt"))
#     curr_time = datetime.datetime.fromtimestamp(time)
#     bruh = {}
#     for addy in macAddr:
#         if addy not in bruh.keys():
#             bruh[addy] = 0
#         else:
#             bruh[addy] += 1
#     addys = set()
#     for b in bruh.keys():
#         if bruh[b] > 1:
#             addys.add(b)
#     return len(addys)
    # for add in macAddr:
    #     if add not in inprogress.keys() :
    #         inprogress[add] = curr_time
    # if len(macAddr) != 0:
    #     for complete in completed:
    #         if(curr_time+datetime.timedelta(minutes = 15) < complete['start']):
    #             completed.remove(complete)
    # keys = set()
    # for key in inprogress.keys():
    #     if key not in macAddr:
    #         start = inprogress[key]
    #         end = curr_time
    #         time = end - start
    #         if time > datetime.timedelta(minutes = 1) and time < datetime.timedelta(minutes= 20):
    #             completed.append({"time":time,"start":curr_time})
    #         keys.add(key)
    # for key in keys:
    #     del inprogress[key]
    # sum = datetime.timedelta(0)
    # for complete in completed:
    #     sum += complete['time']
    # if len(completed) > 0:
    #     print(f"Filename:{filename} Count:{len(completed)} MacAddr:{len(macAddr)}")
    # return 0 if not len(completed) else sum.total_seconds()/(60*len(completed))


def main():
    cwd = os.getcwd()
    mypath = cwd + "/diningdata/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    counter = 0
    with open("output.txt","w") as f:
        for file in onlyfiles:
            l = parse_previous(file)
            if l is not 0:
                f.write(f"{l}\n")
            # if l and isinstance(l,int):
            #     f.write(f"{l}\n")
    # print(counter)
    # print(parse(l))
if __name__ == '__main__':
    main()
