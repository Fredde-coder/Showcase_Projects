@echo off

REM Navigate to the db service directory and run its tests
cd DB-showcase
python -m unittest discover

REM Navigate to the web backend service directory and run its tests
cd ..\Flask-restful-showcase
python -m unittest discover

REM Navigate to the showcase-projects directory and run npm test
cd ..\React-showcase
npm test -- --watchAll=false