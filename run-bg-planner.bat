@echo off
:loop
start /wait "" "%~dp0planner-bg.exe"
timeout /t 60 /nobreak >nul
goto loop