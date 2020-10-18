import requests
import json
from datetime import date
# rom di import models

def setJSON(today):
  weekday = today.weekday()
  # dd/mm/YY
  page = requests.get("https://api.hfs.purdue.edu/menus/v2/locations")
  # print(page.content)
  content = str(page.content)
  jsoncontent = content[2:len(content) - 1]
  jsoncontent = jsoncontent.replace("\\\'","&#39;")
  f = open("menus" + today.strftime("%d-%m-%Y") + ".json", "w")
  f.write(jsoncontent)
  f.close()

def test():
  today = date.today()
  weekday = today.weekday()
  setJSON(today)
  
  jsonfile = open("menus" + today.strftime("%d-%m-%Y") + ".json", "r")
  jsoncontent = jsonfile.read()
  jsonfile.close()
  
  data = json.loads(jsoncontent)
  for p in data['Location']:
    
    print('Name: ' + p['Name'])
    hours = p['NormalHours']
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
      print(p['Name'] + " is having " + meal_obj + " from " + start_time + " to " + end_time)
    
    ## ALREADY RETRIVED:
    # TIMES
    # NAMES

def setModels():
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
  for p in data['Location']:
    
    print('Name: ' + p['Name'])
    hours = p['NormalHours']
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
      print(p['Name'] + " is having " + meal_obj + " from " + start_time + " to " + end_time)
    
    ## ALREADY RETRIVED:
    # TIMES
    # NAMES

    ## Menu items not found in API.


