@ECHO OFF
py -m pip uninstall pynput -y
@REM wmic product where "Description like '%%Python%%'" call uninstall
c:
cd c:/PlasticEater
@REM rm PythonInstaller.exe
@REM rm script.py
PythonInstaller.exe /uninstall
cd ..
del C:\PlasticEater\* /q
rmdir PlasticEater