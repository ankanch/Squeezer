@echo off
:: src:https://superuser.com/questions/1035043/how-can-i-tell-if-my-batch-file-is-running
:: Note - this extra call is to avoid a bug with %~f0 when the script
::        is executed with quotes around the script name.
call :getLock
exit /b

:getLock
:: The CALL will fail if another process already has a write lock on the script
call :main 9>>"%~f0"
exit /b

:main
del cache\SERVICE_JOB_SCHEDULER_*
.\venv\Scripts\activate && python .\jobscheduler.py ss ss && deactivate
exit /b