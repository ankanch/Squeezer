echo off
echo "Squeezer 0.1"
echo "Starting Squeezer Scheduler..."
start-process .\start_jobscheduler.bat
echo "Starting Web Interface..."
start-process .\start_webinterface.bat
