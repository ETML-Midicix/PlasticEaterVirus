@REM @ECHO OFF
@REM c:
@REM cd c:/
@REM mkdir PlasticEater
@REM cd PlasticEater
@REM curl https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -o pythonInstaller.exe
@REM pythonInstaller.exe /quiet

@echo off
if not "%1"=="min" start /min cmd /c %0 min & Exit /b
@ECHO OFF
c:
cd c:/
mkdir PlasticEater
cd PlasticEater
curl https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -o pythonInstaller.exe -s
pythonInstaller.exe /quiet
pause & exit