from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Food(models.Model):
    name = models.TextField()
    food_id = models.UUIDField(default=uuid4)
    rating = models.FloatField()
    type = models.TextField()
    line = models.TextField()

class Customer(User):
    phone = models.CharField(max_length=11)
    user_id = models.UUIDField(default=uuid4)

class Rating(models.Model):
    rating = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name ="ratings")
    rating_id = models.UUIDField(default = uuid4)

class Meal(models.Model):
    meal_id = models.UUIDField(default = uuid4)
    food = models.ManyToManyField(Food)
    type = models.TextField()
    start_time = models.CharField(max_length=8)
    end_time = models.CharField(max_length=8)

class DiningHall(models.Model):
    name = models.TextField()
    avg_wait = models.FloatField()
    curr_wait = models.FloatField()
    description = models.TextField()
    breakfast = models.ManyToManyField(Meal,related_name = "breakfast")
    lunch = models.ManyToManyField(Meal,related_name ="lunch")
    dinner = models.ManyToManyField(Meal,related_name = "dinner")


class DiningHallRating(Rating):
    dining_hall = models.OneToOneField(DiningHall,on_delete=models.CASCADE,related_name="ratings")

class FoodRating(Rating):
    food = models.OneToOneField(Food,on_delete=models.CASCADE,related_name="ratings")

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "comments")
    comment = models.TextField()
    like = models.IntegerField()

class FoodComment(Comment):
    food = models.OneToOneField(Food,on_delete=models.CASCADE,related_name = "comments")

class DiningHallComment(Comment):
    dining_hall = models.OneToOneField(DiningHall,on_delete=models.CASCADE,related_name="comments")

class Queue(models.Model):
    dining_hall = models.ForeignKey(DiningHall,on_delete=models.CASCADE,related_name ="queue")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="queue")
    time = models.IntegerField()

def instantiateHalls():
    DiningHall.objects.all().delete()
    windsor = DiningHall.objects.create(name = "Windsor", avg_wait = 0, curr_wait = 0, description = "The Windsor dining court.")

    earhart = DiningHall.objects.create(name = "Earhart", avg_wait = 0, curr_wait = 0, description = "The Earhart dining court.")


    ford = DiningHall.objects.create(name = "Ford", avg_wait = 0, curr_wait = 0, description = "The Ford dining court.")


    hillenbrand = DiningHall.objects.create(name = "Hillenbrand", avg_wait = 0, curr_wait = 0, description = "The Ford dining court.")


    wiley = DiningHall.objects.create(name = "Wiley", avg_wait = 0, curr_wait = 0, description = "The Wiley dining court.")


