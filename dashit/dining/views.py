from django.shortcuts import render
import requests
from dining.models import DiningHall
from django.http import HttpResponse, Http404
from .models import Time,DiningHall,Food

def server(x):
    def func(request):
        return render(request,x)
    return func
def jmikes(request):
    time = int(Time.objects.order_by("-id").all()[0].wait)
    return render(request,"details.html",{"current":time})
def dining_hall_view(request,hall):

    # hall_template = [something].html
    try:
        this_hall = DiningHall.objects.get(name=hall)

    except DiningHall.DoesNotExist:
        raise Http404("You requested the hall named " + searchTerm + ", which does not appear in our database.")
    context = {"name": this_hall.name, "wait": this_hall.avg_wait}
    #return HttpResponse("Sucessfully reached " + this_hall.name)
    return render(request, "dininghall.html")
    # return render(request, "error.html", {"message":this_hall.name})
    # return render(request, hall_template, context)

def index(request):
    currentWaitTime = Time.objects.order_by("-id").all()[0].wait
    time = int(currentWaitTime/5)
    isAlive = time > 0
    return render(request, 'main.html', {'dining_courts': [
    {'name': 'JerseyMikes', 'busy': range(time), 'isLive': True, 'timeEstMin': 16, 'desc': "Great subs but beware the long wait times! To combat this, we've set up live data so you can pick the best time to avoid the line."},
    {'name': 'Chick-fil-A', 'busy': range(0), 'isLive': False, 'timeEstMin': 0, 'desc': "The best Chicken sandwich, with extreme line efficiency.. except on Sundays."},
    {'name': 'Hillenbrand', 'busy': range(2), 'isLive': False, 'timeEstMin': 4, 'desc': "A dining hall, nothing remarkable. Very good wait times on average."},
    {'name': 'Earhart', 'busy': range(2), 'isLive': False, 'timeEstMin': 4, 'desc': "A dining hall, nothing remarkable. Very good wait times on average."},
    {'name': 'Wiley', 'busy': range(3), 'isLive': False, 'timeEstMin': 8, 'desc': "A dining hall, nothing remarkable. Very good wait times on average."},
    {'name': 'Windsor', 'busy': range(1), 'isLive': False, 'timeEstMin': 11, 'desc': "A dining hall, nothing remarkable. Very good wait times on average."},
    {'name': 'Ford', 'busy': range(1), 'isLive': False, 'timeEstMin': 16, 'desc': "A dining hall, nothing remarkable. Very good wait times on average."},
    ]})




# Create your views here.
