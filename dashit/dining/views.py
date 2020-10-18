from django.shortcuts import render
import requests
from dining.models import DiningHall
from django.http import HttpResponse, Http404


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
    return render(request, 'main.html', {'dining_courts': [
    {'name': 'JerseyMikes', 'busy': range(5), 'isLive': True, 'timeEstMin': 16},
    {'name': 'Chick-fil-A', 'busy': range(4), 'isLive': True, 'timeEstMin': 9},
    {'name': 'Hillenbrand', 'busy': range(2), 'isLive': False, 'timeEstMin': 4},
    {'name': 'Earhart', 'busy': range(2), 'isLive': False, 'timeEstMin': 4},
    {'name': 'Wiley', 'busy': range(3), 'isLive': False, 'timeEstMin': 8},
    {'name': 'Windsor', 'busy': range(1), 'isLive': False, 'timeEstMin': 11},
    {'name': 'Ford', 'busy': range(1), 'isLive': False, 'timeEstMin': 16},
    ]})




# Create your views here.
