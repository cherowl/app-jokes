# app-jokes
REST APP (Flask, PosgreSQL, Python3.6+)

# This project isn't finished, nevertheless you are able to:
- automaticaly set requirenmets for your venv
- check app with authentication and jokes (for now saving user's request history to db - not ready, but its model exists)
- manage configurations
- testing exists in code (temporaraly)
- see simple docker file

# About loading:
Check env variables CONFIG (it must points to one of the configs from scr/config) and PYTHONPATH (-//- your working dir):
- export CONFIG=/usr/src/app/config/production.py
- export PYTHONPATH=$(pwd)
