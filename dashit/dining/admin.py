from django.contrib import admin
from .models import Food,Customer,Rating,Meal,DiningHall,DiningHallRating,FoodRating,Comment,FoodComment,DiningHallComment,Queue
from django.contrib.auth.models import Permission

admin.site.register(Food)
admin.site.register(Customer)
admin.site.register(Rating)
admin.site.register(Meal)
admin.site.register(DiningHall)
admin.site.register(DiningHallRating)
admin.site.register(FoodRating)
admin.site.register(Comment)
admin.site.register(FoodComment)
admin.site.register(DiningHallComment)
admin.site.register(Queue)
admin.site.register(Permission)
