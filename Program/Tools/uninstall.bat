@ECHO OFF
py -m pip uninstall pynput -y
py -m pip uninstall pyautogui -y
py -m pip uninstall Pillow -y
cd c:/PlasticEater
PythonInstaller.exe /uninstall
del screenshots\* /q
rmdir screenshots
del data\* /q
rmdir data
cd ..
del C:\PlasticEater\* /q
rmdir PlasticEater