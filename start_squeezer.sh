#!/usr/bin/env bash
echo "Squeezer 0.1"
echo "Starting Squeezer Scheduler..."
python scheduler_interface.py &
echo "Starting Web Interface..."
python app.py &