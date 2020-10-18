import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time
import base64
import datetime
from .data import *
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
    data = base64.b64decode(data)
    x = parse_current(data)
    with open(f"./dining/diningdata.txt","a") as f:
        if x['wait'] != "F":
            f.write(f"{x['value']},{x['time']},{x['wait']}\n")
            Time.objects.create(devices=x['value'],time=x['time'],wait=x['wait'])
    with open(f"./dining/diningdata/{time.time()}.txt","wb") as f:
        f.write(data)
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

def data_view(request):
    x = []
    with open("./dining/output.txt","r") as f:
        for line in f:
            x.append(line.strip("\n"))
    return render(request,"bruh.html",{"messages":x})
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
def temp(obj):
    return -1 * obj.wait
def data_received(request):
    if request.method == "GET":
        data = Time.objects.all()
        current = Time.objects.order_by("-id").all()[0]
        beta = [*data]
        beta.sort(key = temp)
        max = beta[0]
        avg = 0
        for dat in data:
            avg += dat.wait
        avg/=len(data)
        return render(request,"data.html",{"current":current,"average":avg,"datas":data,"max":max})
