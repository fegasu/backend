@echo off
cls
echo INICIANDO EL SERVIDOR WEB FLASK
set FLASK_APP=index.py
set FLASK_ENV=development
@call flask run  
