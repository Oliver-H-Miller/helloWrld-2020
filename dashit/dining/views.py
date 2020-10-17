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
    return HttpResponse("Sucessfully reached " + this_hall.name)
    # return render(request, "error.html", {"message":this_hall.name})
    # return render(request, hall_template, context)

def index(request):
    render(request,"error.html",{"message":""})



# Create your views here.
