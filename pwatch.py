from np_tools import processwatch as PWATCH

print("TEST>>>Web Interface Status:",PWATCH.checkService(PWATCH.SERVICE_WEB_INTERFACE))
print("TEST>>>Job Scheduler Status:",PWATCH.checkService(PWATCH.SERVICE_JOB_SCHEDULER))