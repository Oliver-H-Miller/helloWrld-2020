from django.shortcuts import render
import requests
from dining.models import DiningHall
from django.http import HttpResponse, Http404
def dining_hall_view(request):

    # hall_template = [something].html

    searchTerm = request.GET.get('hall_name')
    try:
        this_hall = DiningHall.objects.get(name='hall_name')

    except DiningHall.DoesNotExist:
        raise Http404("You requested the hall named " + searchTerm + ", which does not appear in our database.")
    context = Context({"name": this_hall.name, "wait": this_hall.avg_wait})
    return HttpResponse("Sucessfully reached " + this_hall.name)
    # return render(request, hall_template, context)



# Create your views here.
