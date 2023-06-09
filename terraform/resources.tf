resource "google_service_account" "exporter_account" {
  account_id   = "exporter-account"
  project = local.project
  display_name = "Exporter Account"
}

resource "google_cloudfunctions2_function" "export_function" {
  name        = "export_function"
  project = local.project
  location    = "us-central1"

  build_config {
    runtime     = "python311"
    entry_point = "export_resources"
    source {
      repo_source {
        project_id = local.project
        repo_name = "github_pazhersh_port-exercise"
        branch_name = "master"
      }
    }
  }
  
  service_config {
    max_instance_count = 1
    available_memory   = "256M"
    timeout_seconds    = 60
    service_account_email = google_service_account.exporter_account.email

    secret_environment_variables {
      key        = "PORT_LOGIN"
      project_id = local.project
      secret     = google_secret_manager_secret.port_login.secret_id
      version    = "latest"
    }
  }

  event_trigger {
    trigger_region = "us-central1"
    event_type = "google.cloud.pubsub.topic.v1.messagePublished"
    pubsub_topic = google_pubsub_topic.entity_events.id
    retry_policy = "RETRY_POLICY_RETRY"
  }

}

resource "google_pubsub_topic" "entity_events" {
  name = "entity_events"
  project = local.project

  message_retention_duration = "900s" # 15 minutes
}

resource "google_cloud_scheduler_job" "scheduler_job" {
  project = local.project
  name        = "scheduler_job"
  schedule    = "*/5 * * * *"
  region = "us-central1"

  pubsub_target {
    topic_name = google_pubsub_topic.entity_events.id
    data       = base64encode(local.raw_config)
  }
}

resource "google_secret_manager_secret" "port_login" {
  secret_id = "port_login"
  project = local.project

  replication {
    user_managed {
      replicas {
        location = "us-central1"
      }
    }
  }  
}

resource "google_secret_manager_secret_version" "port_login" {
  secret = google_secret_manager_secret.port_login.name

  secret_data = jsonencode(file("${path.root}/secrets/port_login.json"))
  enabled = true
}
