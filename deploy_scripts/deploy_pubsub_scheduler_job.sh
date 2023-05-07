gcloud scheduler jobs create pubsub invoke-function-4 \
    --schedule='*/5 * * * *' \
    --location=us-central1 \
    --topic=entity_events \
    --message-body-from-file=samples/config.json
    # TODO: commandline-editable config
