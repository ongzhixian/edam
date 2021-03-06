@ECHO OFF
REM 12345678901234567890123456789012345678901234567890123456789012345678901234567890
REM Original intention is to write a batch file that will conveniently run the 
REM Google App Engine development server.
REM Does not work because it REQUIRES python 2.7
REM If try running python 3, will received the following error message:
REM Traceback (most recent call last):
REM  File "~\dev_appserver.py", line 102, in <module>
REM    assert sys.version_info[0] == 2
REM AssertionError

SET APP_ENGINE=C:\Apps\Google\CloudSDK\google-cloud-sdk\platform\google_appengine
SET APP_PATH=C:\src\github.com\ongzhixian\edam
python %APP_ENGINE%\dev_appserver.py --port=38011 %APP_PATH%

REM Clearing the datastore
REM python %APP_ENGINE%\dev_appserver.py --clear_datastore=yes %APP_PATH%

REM Script to run
REM python main.py