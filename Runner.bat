@echo off
color 0c

title Generate Simultaneous Clicks for any URL

:a
set /p "loopCount=HitCount:"
set /p "test_browser=BrowserName:"
set /p "url=URL:"
python script.py %loopCount% %test_browser% %URL%

pause
cls
goto :a