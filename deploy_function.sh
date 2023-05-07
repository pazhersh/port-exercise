gcloud functions deploy function-2 \
    --gen2 \
    --region=us-central1 \
    --runtime=python311 \
    --source=. \
    --entry-point=export_resources \
    --trigger-http
