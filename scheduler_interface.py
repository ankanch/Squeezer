from jobscheduler import runTask
from subprocess import Popen
import threading

def watchScheduler():
    while True:
        print("\nwatchScheduler():Starting... " )
        p = Popen("python main.py", shell=True)
        p.wait()
        print("\nTerminated.")
