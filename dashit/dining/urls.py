from . import views,api
from django.urls import path,include


urlpatterns = [
    path('api/test',api.data_practice,name = "practice"),
    path('api/bruh',api.data_received,name = "practice data_received")
    # path("vote",views.vote,name = "vote"),

]
