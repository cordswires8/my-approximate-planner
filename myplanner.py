from datetime import datetime
import re
import json
from pathlib import Path

#timeframe dict templates
every2hrs = {'02:00-04:00':None, '04:00-06:00':None, '06:00-08:00':None, '08:00-10:00':None, '10:00-12:00':None, '12:00-14:00':None, '14:00-16:00':None, '16:00-18:00':None, '18:00-20:00':None, '20:00-22:00':None, '22:00-00:00':None, '00:00-02:00':None}
every4hrs = {'04:00-08:00':None, '08:00-12:00':None, '12:00-16:00':None, '16:00-20:00':None, '20:00-00:00':None, '00:00-04:00':None}
every6hrs = {'06:00-12:00':None, '12:00-18:00':None, '18:00-00:00':None, '00:00-06:00':None}
every8hrs = {'08:00-16:00':None, '16:00-00:00':None, '00:00-08:00':None}

#intro
print("Welcome to My Approximate Planner.")
print("Our goal is to enable you to schedule tasks for both timeframes and specified hours of the day.")
print("We hope that this will allow you to balance between strict deadlines and more flexible plans.")

#create json with all the users to help user remember their name
print("Please enter your name: ")
username = str(input())
print(f"Welcome, {username}. Make sure to remember this name - without it you won't be able to edit your saved data and will need to create a new profile for future events.")

#functions checking datetime input errors
def check_error_date(str):

    pattern = r"\d\d/\d\d/\d\d\d\d"
    while re.match(pattern, str) is None:
        print("Please follow the required format: dd/mm/yyyy ")
        str = input()

    error = 0
    while error == 0:
        try: 
            datetime.strptime(str, "%d/%m/%Y").date()
            error+=1
        except ValueError:
            print("Please enter a real date.")
            str = input()

    while datetime.strptime(str, "%d/%m/%Y") <= datetime.now():
        print("Please enter a valid future date.")
        str = input() 

    return str
def check_error_time(str):
    pattern = r"\d\d:\d\d"
    while re.match(pattern, str) is None:
        print("Please follow the required format: hh:mm ")
        str = input()

    error = 0
    while error == 0:
        try: 
            datetime.strptime(str, "%H:%M").date()
            error+=1
        except ValueError:
            print("Please enter real time.")
            str = input()

    return str

#selecting date
print("Please, enter a future date for which you would like to make plans. Required format: dd/mm/yyyy ")
usr_input = check_error_date(input())
date = datetime.strptime(usr_input, "%d/%m/%Y").date()

plans_precise = {}
date_time_task = {}
user_plans_precise = {}

#function for writing PRECISE time+task pairs into a json file: main dict keys = usernames, internal dicts keys = dates
def wrtite_json_precise(username, date, plans_precise, user_plans_precise):
    fl = Path(r"C:\\Users\sulki\source\repos\myplanner\precise.json")
    if fl.exists():
        with open("precise.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            user_key = list(data.keys())[0]
            if user_key == username:
                data[user_key][str(date)] = plans_precise
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2)
            else:
                with open("precise.json", "w", encoding="utf-8") as precise:
                    json.dump(user_plans_precise, precise, indent=2)
    else:
        with open("precise.json", "w", encoding="utf-8") as precise:
            json.dump(user_plans_precise, precise, indent=2)
    

#creates dict for tasks with a PRECISE time of the beginning
print("Do you have any fixed plans for this day? Continue to select time: (y/n)")
if input() != "y":
    pass
else:
    answer = "1"
    while answer == "1":
        print("Please select time. Required format: hh:mm ")
        usr_input2 = check_error_time(input())
        time = datetime.strptime(usr_input2, "%H:%M").time()
        print("Enter the task you would like to schedule for this time. ")
        task = input()
        plans_precise.update({str(f"{time}"):task})
        print("Would you like to add another task or move on to creating a list of plans. (1-another task/2-move on) ")
        answer = input()
    else:
        print("Moving on.")

date_time_task.update({str(date):plans_precise})
user_plans_precise.update({username:date_time_task})
wrtite_json_precise(username, date, plans_precise, user_plans_precise)
print(Path("precise.json").read_text(encoding="utf-8"))

plans_approx = {}
user_plans_approx = {}

#function for selecting how often your lists with tasks will arrive on the chosen date
def frequency(selection):
    match selection:
        case 2: 
            return every2hrs
        case 4:
            return every4hrs
        case 6:
            return every6hrs
        case 8:
            return every8hrs

#function for assigning tasks to timeframes
def iter_through_dict(dict):
    for i in dict.keys():
        print(f"You are adding plans for {i}.")
        print("Press 0 to skip this timeframe or enter the planned tasks.")
        y = input()
        if y == "0":
            continue
        else:
            dict[i] = y

#selecting frequency of the notifs
print("Now you need to select the frequency with which your notifications will arrive.")
print("Press 2 for 'Every 2 hours' -- Press 4 for 'Every 4 hours' -- Press 6 for 'Every 6 hours' -- Press 8 for 'Every 8 hours'")
fr = int(input())
while fr not in [2, 4, 6, 8]:
    print("Incorrect format.")
    print("Press 2 for 'Every 2 hours' -- Press 4 for 'Every 4 hours' -- Press 6 for 'Every 6 hours' -- Press 8 for 'Every 8 hours'")
    fr = int(input())

new_schedule = frequency(fr) #{timeframe:tasks}
iter_through_dict(new_schedule)
plans_approx.update({str(date):new_schedule}) #date:{timeframe:tasks}
user_plans_approx.update({username:plans_approx}) #username:{date:{timeframe:tasks}}

#check on the file paths before turning this code into an .exe

#function for writin json with APPROXIMATE timeframes
def write_json_approx(username, date, user_plans_approx, new_schedule):
    fl = Path(r"C:\\Users\sulki\source\repos\myplanner\approx.json")
    if fl.exists():
        with open("approx.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            user_key = list(data.keys())[0]
            if user_key == username:
                data[user_key][str(date)] = new_schedule
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2)
            else:
                try:
                    with open("approx.json", "w", encoding="utf-8") as approx:
                        json.dump(user_plans_approx, approx, indent=2)
                    print("overwritten everything again")
                except TypeError as err:
                    print("TypeError:", err)
    else:
        try:
            with open("approx.json", "w", encoding="utf-8") as approx:
                json.dump(user_plans_approx, approx, indent=2)
        except TypeError as err:
            print("TypeError:", err)

write_json_approx(username, date, user_plans_approx, new_schedule)
print(Path("approx.json").read_text(encoding="utf-8"))
