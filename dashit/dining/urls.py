from . import views,api
from django.urls import path,include

urlpatterns = [
    path('api/test',api.data_practice,name = "practice"),
    path('api/bruh',api.data_received,name = "practice data_received"),
    path('api/data',api.data,name="data"),
    path('hall/<str:hall>', views.dining_hall_view, name = "specific_hall") ,
    path("",views.index,name = "index")   

]
