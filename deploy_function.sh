gcloud functions deploy function-2 \
    --gen2 \
    --region=us-central1 \
    --runtime=python311 \
    --source=./src/gcp \
    --entry-point=hello_http \
    --trigger-http
