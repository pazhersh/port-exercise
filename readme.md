must first mirror the repo: https://source.cloud.google.com/repo/connect
or upload repo from local source

enable the required services:
```bash
gcloud services enable \
    cloudbuild.googleapis.com \
    cloudscheduler.googleapis.com \
    secretmanager.googleapis.com \
    pubsub.googleapis.com \
    cloudfunctions.googleapis.com \
    run.googleapis.com \
    eventarc.googleapis.com \
    artifactregistry.googleapis.com \
    compute.googleapis.com
```
