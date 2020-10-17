import base64

def parse(x):
    data = str(base64.b64decode(x))
    return data
def main():
    l = ""
    with open("f.txt","r") as f:
        for line in f:
            l += line
    print(parse(l))
if __name__ == '__main__':
    main()
