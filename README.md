# my-approximate-planner

My vision: a planner app that allows you to create lists of tasks for a selected timeframe instead of a strict schedule.

---
Setup:
1. _planner-main.exe_ - the main program for interviewing the user and accepting information from them (such as username, date, time and tasks). The user can now add multiple entries to different dates without restarting the app.
2. _planner-bg.py_ - a script for a background service that compares the information in the JSON files created by the main program and current time and sends toast notifications when there is a match.
3. _run-bg-planner.bat_ - automates the loop in _planner-bg.py_ (instead of asyncio library) and starts the script every minute.
4. _run-hidden.vbs_ - activates the _.bat_ file in the hidden mode and keeps the console windows from distracting the user. This file can be added to _"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"_ to run automatically upon restart. Alternatively, it can be activated by double-clicking.
---
OS: Windows 11
