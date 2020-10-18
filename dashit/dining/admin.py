from django.contrib import admin
from .models import DiningHall,Food,Time
from django.contrib.auth.models import Permission

admin.site.register(Food)
admin.site.register(DiningHall)
admin.site.register(Time)
admin.site.register(Permission)
