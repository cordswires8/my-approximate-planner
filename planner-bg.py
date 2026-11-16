from pathlib import Path
import json
from datetime import datetime
import os
from win11toast import toast
#import asyncio

# current_date = "2026-12-12"
# current_time = "08:00:00"

def get_name():
    with open("users.json", "r", encoding="utf-8") as fl:
        name = json.load(fl)
        return name

#username = get_name()

def check_json_precise(current_date, current_time, username, tasks_precise):
    file = Path(os.path.basename("/MyApproximatePlanner/precise.json"))
    if file.exists():
        with open("precise.json", "r", encoding="utf-8") as fl:
            data = json.load(fl)
            dates_in_data = []
            for i in data[username].keys():
                dates_in_data.append(i)
            if current_date in dates_in_data:
                time_in_data = []
                for n in data[username][current_date].keys():
                    time_in_data.append(n)
                for time in time_in_data:
                    if time == current_time:
                        tasks_precise.append(data[username][current_date][time])
            else:
                pass
    else:
        pass

#check_json_precise(current_date, current_time, username, tasks_precise)

#this function creates both the list and the value for matching with the approximate dict timeframes
def check_json_approx(current_date, current_time, username, tasks_approx):
    file = Path(os.path.basename("/MyApproximatePlanner/approx.json"))
    if file.exists():
        with open(r"approx.json", "r", encoding="utf-8") as fl:
            data = json.load(fl)
            dates_in_data = []
            for i in data[username].keys():
                dates_in_data.append(i)
            if current_date in dates_in_data:
                time_in_data = []
                for n in data[username][current_date].keys():
                    time_in_data.append(n)
                for time in time_in_data:
                    if f"{str(time)[:5]}:00" == current_time:
                        tasks_approx.append(data[username][current_date][time])
                return(len(time_in_data))
            else:
                pass
    else:
        pass

#frequency = check_json_approx(current_date, current_time, username, tasks_approx)

def match_dicts(frequency):
    match frequency:
        case 3:
            return 8
        case 4:
            return 6
        case 6:
            return 4
        case 8:
            return 3

#frequency = match_dicts(frequency)

def send_notifs(current_time, tasks_approx, tasks_precise, frequency):
    if len(tasks_approx)!=0:
        toast(f"{current_time[:5]}", f"Your scheduled tasks for the next {frequency} hours are: {tasks_approx[0]}.")
    if len(tasks_precise)!=0:
        toast(f"{current_time[:5]}", f"Here is what you planned to do at this time: {tasks_precise[0]}.")

#send_notifs(current_time, tasks_approx, tasks_precise)

# #async def main():
#     #loop = asyncio.get_running_loop()

#     while True:
#         username = get_name()
#         current_date = datetime.now().date()
#         current_date = str(current_date)
#         current_time = datetime.now().time()
#         current_time = f"{str(current_time)[:5]}:00"
#         tasks_precise = []
#         tasks_approx = []

#         check_json_precise(current_date, current_time, username, tasks_precise)
#         frequency = check_json_approx(current_date, current_time, username, tasks_approx)
#         frequency = match_dicts(frequency)
#         send_notifs(current_time, tasks_approx, tasks_precise, frequency)

#         #await asyncio.sleep(60)

# #asyncio.run(main())

username = get_name()
current_date = datetime.now().date()
current_date = str(current_date)
current_time = datetime.now().time()
current_time = f"{str(current_time)[:5]}:00"
tasks_precise = []
tasks_approx = []

check_json_precise(current_date, current_time, username, tasks_precise)
frequency = check_json_approx(current_date, current_time, username, tasks_approx)
frequency = match_dicts(frequency)
send_notifs(current_time, tasks_approx, tasks_precise, frequency)