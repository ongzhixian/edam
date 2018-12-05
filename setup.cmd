@ECHO OFF
REM gcloud config set --project hci-admin
REM gcloud config set SECTION/PROPERTY VALUE [--installation]  GCLOUD_WIDE_FLAG ...]

gcloud init
gcloud app create
REM gcloud config set project hci-admin