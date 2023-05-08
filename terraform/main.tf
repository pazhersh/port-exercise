terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 4.34.0"
    }
  }
}

locals {
  # TODO: variable from commandline
  project = "port-exporter2" # Google Cloud Platform Project ID
  raw_config = file("${path.root}/samples/config.json")
}
