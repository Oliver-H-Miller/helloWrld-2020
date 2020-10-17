from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.
class Food(models.Model):
    name = models.TextField()
    food_id = models.UUIDField(default=uuid4)
    rating = models.FloatField()

class Customer(User):
    phone = models.CharField(max_length=11)
    user_id = models.UUIDField(default=uuid4)

class Rating(models.Model):
    rating = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name ="ratings")
    rating_id = models.UUIDField(default = uuid4)

class Meal(models.Model):
    meal_id = models.UUIDField(default = uuid4)
    food = models.ManyToMany(Food)
    shape = models.TextField()

class DiningHall(models.Model):
    name = models.TextField()
    avg_wait = models.FloatField()
    curr_wait = models.FloatField()
    description = models.TextField()
    breakfast = models.ManyToMany(Meal)
    lunch = models.ManyToMany(Meal)
    dinner = models.ManyToMany(Meal)


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
