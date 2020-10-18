import base64
import re

def parse(x):
    data = str(base64.b64decode(x))
    p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    pattern = re.compile(r'RSSI: (.\d\d)')
    
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
