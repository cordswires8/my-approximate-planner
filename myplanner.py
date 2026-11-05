from datetime import datetime
import re

#intro
print("Welcome to My Approximate Planner.")
print("Our goal is to enable you to schedule tasks for both timeframes and specified hours of the day.")
print("We hope that this will allow you to balance between strict deadlines and more flexible plans.")

print("Please enter your name: ")
username = str(input())

#dicts for all info
all_plans_approx = {}
all_plans_precise = {}

#timeframe dict templates
every2hrs = {'02:00-04:00':None, '04:00-06:00':None, '06:00-08:00':None, '08:00-10:00':None, '10:00-12:00':None, '12:00-14:00':None, '14:00-16:00':None, '16:00-18:00':None, '18:00-20:00':None, '20:00-22:00':None, '22:00-00:00':None, '00:00-02:00':None}
every4hrs = {'04:00-08:00':None, '08:00-12:00':None, '12:00-16:00':None, '16:00-20:00':None, '20:00-00:00':None, '00:00-04:00':None}
every6hrs = {'06:00-12:00':None, '12:00-18:00':None, '18:00-00:00':None, '00:00-06:00':None}
every8hrs = {'08:00-16:00':None, '16:00-00:00':None, '00:00-08:00':None}

#checking datetime input errors
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
print(f"Welcome, {username}. Please, enter a future date for which you would like to make plans. Required format: dd/mm/yyyy ")
usr_input = check_error_date(input())
date = datetime.strptime(usr_input, "%d/%m/%Y")

#creates dict for tasks with a specified time of the beginning
print("Do you have any fixed plans for this day? Continue to select time: (y/n)")
if input() != "y":
    pass
else:
    answer = "1"
    while answer == "1":
        print("Please select time. Required format: hh:mm ")
        usr_input2 = check_error_time(input())
        time = datetime.strptime(usr_input2, "%H:%M")
        print("Enter the task you would like to schedule for this time. ")
        task = input()
        all_plans_precise.update({time:task})
        print("Would you like to add another task or move on to creating a list of plans. (1-another task/2-move on) ")
        answer = input()
    else:
        print("Moving on.")

#function for selecting how often your lists with plans will arrive during the chosen date
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

#function for assigning plans to timeframes
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
temp = int(input())

while temp not in [2, 4, 6, 8]:
    print("Incorrect format.")
    print("Press 2 for 'Every 2 hours' -- Press 4 for 'Every 4 hours' -- Press 6 for 'Every 6 hours' -- Press 8 for 'Every 8 hours'")
    temp = int(input())

assigned_schedule = frequency(temp)
iter_through_dict(assigned_schedule)
all_plans_approx.update({date:assigned_schedule})
