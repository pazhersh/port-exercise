
resource "google_secret_manager_secret_iam_binding" "port_binding" {
  project = local.project
  secret_id = google_secret_manager_secret.port_login.secret_id

  role = "roles/secretmanager.secretAccessor"
  members = [
    "serviceAccount:${google_service_account.exporter_account.email}"
  ]
}

resource "google_project_iam_binding" "editor" {
  project = local.project
  role    = "roles/editor"

  members = [
    "serviceAccount:${google_service_account.exporter_account.email}"
  ]
}

resource "google_project_iam_binding" "project_token_creator" {
  project = local.project
  role    = "roles/iam.serviceAccountTokenCreator"
  members = [
    "serviceAccount:${google_service_account.exporter_account.email}"
  ]
}

resource "google_project_iam_binding" "function_invoker" {
  project = local.project
  role    = "roles/cloudfunctions.invoker"

  members = [
    "serviceAccount:${google_service_account.exporter_account.email}"
  ]
}

resource "google_project_iam_binding" "eventarc_agent" {
  project = local.project
  role    = "roles/eventarc.serviceAgent"

  members = [
    "serviceAccount:${google_service_account.exporter_account.email}"
  ]
}
