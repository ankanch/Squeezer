@echo off
echo setting up Squeezer environment...
pip install virtualenv && virtualenv venv && .\venv\Scripts\activate && pip install -r requirements.txt