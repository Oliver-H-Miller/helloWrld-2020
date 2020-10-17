import base64
data = ""
with open("f.txt","r") as f:
    for line in f:
        data += line.strip("\n")


x = base64.b64decode(data)
print(str(x))
