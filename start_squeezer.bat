@echo off
echo "Squeezer 0.1"
echo "Starting Squeezer Scheduler..."
start cmd.exe /c .\start_jobscheduler.bat
echo "Starting Web Interface..."
start cmd.exe /c .\start_webinterface.bat
