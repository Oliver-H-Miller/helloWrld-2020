import base64
import re

def parse(x):
    data = str(base64.b64decode(x))
    p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    pattern = re.compile(r'RSSI: (.\d\d)')
    test_str = u"TEXT WITH SOME MAC ADDRESSES 00:24:17:b1:cc:cc TEXT CONTINUES WITH SOME MORE TEXT 20:89:86:9a:86:24"
    
    macAddr = re.findall(p, data)
    signalStr = re.findall(pattern, data)
    results = [macAddr, signalStr]
    return results


def main():
    l = ""
    with open("f.txt","r") as f:
        for line in f:
            l += line
    print(parse(l))
if __name__ == '__main__':
    main()
