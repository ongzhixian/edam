REM 12345678901234567890123456789012345678901234567890123456789012345678901234567890
REM PURPOSE
REM Batch file to read logs
REM 
REM SET APP_ENGINE=C:\Apps\Google\CloudSDK\google-cloud-sdk\platform\google_appengine
REM Note: To save to file use a redirection operator (> or >>)

REM Do a 1-time read log files
gcloud app logs read

REM To stream logs use tail as in the below command-line
REM gcloud app logs tail
