gcloud functions deploy function-3 \
    --gen2 \
    --region=us-central1 \
    --runtime=python311 \
    --source=. \
    --entry-point=export_resources \
    --set-secrets='PORT_LOGIN=port-login:latest' \
    --trigger-http
