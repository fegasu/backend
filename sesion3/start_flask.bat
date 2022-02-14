@echo off
cls
echo INICIANDO EL SERVIDOR WEB FLASK
set FLASK_APP=servi.py
set FLASK_ENV=development
@call flask run  
