import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


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
