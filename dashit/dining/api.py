import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time
import base64

@csrf_exempt
def data(request):
    if request.method == "POST":
        try:
            data = request.POST['data']
            if not data:
                return render(request,"error.html",{'message':"Bruh Error Occured"})
        except:
            return render(request,"error.html",{'message':"Bruh Error Occured"})
    elif request.method == "GET":
        try:
            data = request.GET['data']
            if not data:
                return render(request,"error.html",{'message':"Bruh Error Occured"})
        except:
            return render(request,"error.html",{'message':"Bruh Error Occured"})
    x = parse(x)
    # with open(f"./dining/diningdata/{time.time()}.txt","wb") as f:
    #     x = base64.b64decode(data)
    #     f.write(x)
    return render(request,"error.html",{"message":"success"})

def commiter(fields):
    dictionary = {}
    for field in fields:
        try:
            dictionary[field] = request.POST['field']
        except:
            return False
    return dictionary

# def signup(request):
#     if request.method == "POST":
#
#     else:


@csrf_exempt
def data_practice(request):
    if request.method == "POST":
        with open("f.txt","w") as f:
            try:
                data = request.POST['data']
                f.write(data)
            except:
                return render(request,"error.html",{'message':"Bruh Error Occurred"})

        return render(request,"error.html",{"message":"Success"})
    elif request.method == "GET" :
        with open("f.txt","w") as f:
            try:
                data = request.GET['data']
                f.write(data)
            except:
                return render(request,"error.html",{'message':"Bruh Error Occurred"})

        return render(request,"error.html",{"message":"Success"})

def data_received(request):
    if request.method == "GET":
        with open("f.txt","r") as f:
            x = ""
            for line in f:
                x += line

        return render(request,"error.html",{"message":x})
