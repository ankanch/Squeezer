@echo off
echo "Squeezer 0.1"
echo "Starting Squeezer Scheduler..."
start  python scheduler_interface.py
echo "Starting Web Interface..."
start python app.py
