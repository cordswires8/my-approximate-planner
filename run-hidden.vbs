Set WshShell = CreateObject("WScript.Shell")
fileName = "run-bg-planner.bat" 
dim fso, filePath
set fso = CreateObject("Scripting.FileSystemObject")
filePath = fso.GetAbsolutePathName(fileName)
WshShell.Run filePath, 0, false
Set fso = Nothing