import sys
import requests
import json
from datetime import date
from .. import models
from django.http import HttpResponse
# rom di import models

def setHallJSON(today, hall_name):
  weekday = today.weekday()
  # dd/mm/YY
  page = requests.get("https://api.hfs.purdue.edu/menus/v2/locations/" + hall_name + "/" + today.strftime("%Y-%m-%d"))
  content = str(page.content)
  jsoncontent = content[2:len(content) - 1]
  jsoncontent = jsoncontent.replace("\\\'","&#39;")
  f = open(hall_name + "menu" + today.strftime("%d-%m-%Y") + ".json", "w")
  f.write(jsoncontent)
  f.close()

def setJSON(today):
  weekday = today.weekday()
  # dd/mm/YY
  page = requests.get("https://api.hfs.purdue.edu/menus/v2/locations/")
  content = str(page.content)
  jsoncontent = content[2:len(content) - 1]
  jsoncontent = jsoncontent.replace("\\\'","&#39;")
  f = open("menus" + today.strftime("%d-%m-%Y") + ".json", "w")
  f.write(jsoncontent)
  f.close()


def test(request):
  today = date.today()
  weekday = today.weekday()
  jsoncontent = ""
  models.instantiateHalls()
  print("Began test...")
  for hall_obj in models.DiningHall.objects.all():
    setHallJSON(today, hall_obj.name)
    # setJSON(today)
    jsonfile = open(hall_obj.name + "menu" + today.strftime("%d-%m-%Y") + ".json")
    
    jsoncontent = jsonfile.read()
    jsonfile.close()
    print(hall_obj.name)
    if hall_obj.name == "Windsor":
      print(jsonfile)
    ## ALREADY RETRIVED:
    # TIMES



    # NAMES
    
def test_setModels(request):
  today = date.today()
  weekday = today.weekday()
  jsoncontent = ""
  models.instantiateHalls()
  print("Began test...")
  for hall_obj in models.DiningHall.objects.all():
    setHallJSON(today, hall_obj.name)
    # setJSON(today)
    jsonfile = open(hall_obj.name + "menu" + today.strftime("%d-%m-%Y") + ".json")
    jsoncontent = jsonfile.read()
    jsonfile.close()
    try:
      data = json.loads(jsoncontent)
    except:
      # Silently ignore
      continue
    # Json file created.

    #print(hall_obj.name)
    #if hall_obj.name == "Windsor":
    #  print(jsonfile)
    
    for meal_scheduled in data["Meals"]:
      
      if meal_scheduled["Status"] == "Closed":
        # Nothing for this meal
        continue
      for station in meal_scheduled["Stations"]:
        entree = True
      
        if meal_scheduled["Type"] == "Breakfast":
          # If entree is true before this, the item is an entree
          entree = False
          
          # First get the start and end times
          hours = meal_scheduled["Hours"]
          start_time = hours["StartTime"]
          end_time = hours["EndTime"]
          this_line = models.Meal.objects.create(type = station["Name"], start_time = "", end_time = "")
          this_line.save()
          # then instantiate a new meal
          hall_obj.breakfast.add(this_line)
          # line added. Time to add the food options

          for item in station["Items"]:
            food_name = item["Name"]
            try:
              old_food = models.Food.objects.get(name = food_name)
              old_food.save()
              this_line.food.add(old_food)
            except models.Food.DoesNotExist:
                  
              # NAMES
              print("New breakfast option:" + food_name)
              new_food = models.Food.objects.create(name = food_name, type="Breakfast", rating=0)
              new_food.save()
              this_line.food.add(new_food)

        # Dang it
        # Why did you make "breakfast" "lunch" and "dinner" different model fields?
        
        elif meal_scheduled["Type"] == "Lunch":
          # If entree is true before this, the item is an entree
          entree = False
          
          # First get the start and end times
          hours = meal_scheduled["Hours"]
          start_time = hours["StartTime"]
          end_time = hours["EndTime"]
          this_line = models.Meal.objects.create(type = station["Name"], start_time = "", end_time = "")
          this_line.save()
          # then instantiate a new meal
          hall_obj.lunch.add(this_line)
          # line added. Time to add the food options

          for item in station["Items"]:
            food_name = item["Name"]
            try:
              old_food = models.Food.objects.get(name = food_name)
              old_food.save()
              this_line.food.add(old_food)
            except models.Food.DoesNotExist:
                  
              # NAMES
              print("New lunch option:" + food_name)
              new_food = models.Food.objects.create(name = food_name, type="Lunch", rating=0)
              new_food.save()
              this_line.food.add(new_food)

        elif meal_scheduled["Type"] == "Dinner":
          # If entree is true before this, the item is an entree
          entree = False
          
          # First get the start and end times
          hours = meal_scheduled["Hours"]
          start_time = hours["StartTime"]
          end_time = hours["EndTime"]
          this_line = models.Meal.objects.create(type = station["Name"], start_time = "", end_time = "")
          this_line.save()
          # then instantiate a new meal
          hall_obj.lunch.add(this_line)
          # line added. Time to add the food options

          for item in station["Items"]:
            food_name = item["Name"]
            try:
              old_food = models.Food.objects.get(name = food_name)
              old_food.save()
              this_line.food.add(old_food)
            except models.Food.DoesNotExist:
                  
              # NAMES
              print("New dinner option:" + food_name)
              new_food = models.Food.objects.create(name = food_name, type="Dinner", rating=0)
              new_food.save()
              this_line.food.add(new_food)

        else:
          print("You're not supposed to be here.")

  return HttpResponse(jsoncontent)

def testGeneralInfo():
  
  today = date.today()
  weekday = today.weekday()
  setJSON(today)
  
  jsonfile = open("menus" + today.strftime("%d-%m-%Y") + ".json", "r")
  jsoncontent = jsonfile.read()
  jsonfile.close()
  
  today = date.today()
  weekday = today.weekday()
  setJSON(today)
  data = json.loads(jsoncontent)
  for hall in data['Location']:
    
    print('Name: ' + hall['Name'])
    hours = hall['NormalHours']
    weekTimes = hours[0]['Days']
    today_times = None
    #print(weekTimes)
    # print(weekTimes)
    print("Today: " + str(weekday))
    for day in weekTimes:
      if(day['DayOfWeek'] == weekday):
        # print("Day time is " + str(day['DayOfWeek']))
        today_times = day
    if today_times is None: 
      continue
    for meal_time in today_times['Meals']:
      # Replace meal[Name] with django obj
      
      meal_obj = meal_time['Name']
      hours = meal_time['Hours']
      start_time = hours['StartTime']
      end_time = hours['EndTime']
      print(hall['Name'] + " is having " + meal_obj + " from " + start_time + " to " + end_time)
    
    ## ALREADY RETRIVED:
    # TIMES
    # NAMES

    ## Menu items not found in API.


def setModels():
  today = date.today()
  weekday = today.weekday()
  jsoncontent = ""
  models.instantiateHalls()
  for hall_obj in models.DiningHall.objects.all():
    setHallJSON(today, hall_obj.name)
    # setJSON(today)
    jsonfile = open(hall_obj.name + "menu" + today.strftime("%d-%m-%Y") + ".json")
    jsoncontent = jsonfile.read()
    jsonfile.close()
    try:
      data = json.loads(jsoncontent)
    except:
      # Silently ignore
      continue
    # Json file created.

    #print(hall_obj.name)
    #if hall_obj.name == "Windsor":
    #  print(jsonfile)
    
    for meal_scheduled in data["Meals"]:
      
      if meal_scheduled["Status"] == "Closed":
        # Nothing for this meal
        continue
      for station in meal_scheduled["Stations"]:
        entree = True
      
        if meal_scheduled["Type"] == "Breakfast":
          # If entree is true before this, the item is an entree
          entree = False
          
          # First get the start and end times
          hours = meal_scheduled["Hours"]
          start_time = hours["StartTime"]
          end_time = hours["EndTime"]
          this_line = models.Meal.objects.create(type = station["Name"], start_time = "", end_time = "")
          this_line.save()
          # then instantiate a new meal
          hall_obj.breakfast.add(this_line)
          # line added. Time to add the food options

          for item in station["Items"]:
            food_name = item["Name"]
            try:
              old_food = models.Food.objects.get(name = food_name)
              old_food.save()
              this_line.food.add(old_food)
            except models.Food.DoesNotExist:
                  
              # NAMES
              new_food = models.Food.objects.create(name = food_name, type="Breakfast", rating=0)
              new_food.save()
              this_line.food.add(new_food)

        # Dang it
        # Why did you make "breakfast" "lunch" and "dinner" different model fields?
        
        elif meal_scheduled["Type"] == "Lunch":
          # If entree is true before this, the item is an entree
          entree = False
          
          # First get the start and end times
          hours = meal_scheduled["Hours"]
          start_time = hours["StartTime"]
          end_time = hours["EndTime"]
          this_line = models.Meal.objects.create(type = station["Name"], start_time = "", end_time = "")
          this_line.save()
          # then instantiate a new meal
          hall_obj.lunch.add(this_line)
          # line added. Time to add the food options

          for item in station["Items"]:
            food_name = item["Name"]
            try:
              old_food = models.Food.objects.get(name = food_name)
              old_food.save()
              this_line.food.add(old_food)
            except models.Food.DoesNotExist:
                  
              # NAMES
              new_food = models.Food.objects.create(name = food_name, type="Lunch", rating=0)
              new_food.save()
              this_line.food.add(new_food)

        elif meal_scheduled["Type"] == "Dinner":
          # If entree is true before this, the item is an entree
          entree = False
          
          # First get the start and end times
          hours = meal_scheduled["Hours"]
          start_time = hours["StartTime"]
          end_time = hours["EndTime"]
          this_line = models.Meal.objects.create(type = station["Name"], start_time = "", end_time = "")
          this_line.save()
          # then instantiate a new meal
          hall_obj.lunch.add(this_line)
          # line added. Time to add the food options

          for item in station["Items"]:
            food_name = item["Name"]
            try:
              old_food = models.Food.objects.get(name = food_name)
              old_food.save()
              this_line.food.add(old_food)
            except models.Food.DoesNotExist:
                  
              # NAMES
              new_food = models.Food.objects.create(name = food_name, type="Dinner", rating=0)
              new_food.save()
              this_line.food.add(new_food)


  
