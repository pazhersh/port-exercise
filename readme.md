# Paz's GCP to Port Exporter
###### a.k.a. clouds are pretty cool, y'know?

This is a module to export data from your google cloud into Port™ organization.

Deployment should be rather simple, and includes just a few steps described later in this readme.

## How It Works

The module includes two main resources:

The `CloudFunction` export function - Responsible for reading the cloud data, converting it to entities, and exporting to port. Triggerred by the following pubsub.

The `PubSub` entity events - The messages pushed here should match the config.json schema; This defines what resources the export function reads and how it serializes them to entities.


Aditional resources include:

The `SchedulerJob` scheduler job - Periodically pushes a message to the entity events. Causes a scheduled export based on a config.json set on deployment.

The `Secret` port login - A secret with the the port logging parameters.


The export function's source architecture (its this library! yay!) is described in the following chart
![](./media/flowchart.svg)

## Configuration, Configuration, Configuration
You'll probably first want to configure your deployment.

There are three things you'll need to set manually:
- `secrets/port_login.json` - This is where you set the login parameters to port so that the exporter function could connect to it. The required values could be found on the bottom left of [port website](https://www.getport.io), under `Help` > `Credentials`.
- `config.json` - You'll probably want to [write your own one](/media/config.md) and use. If you do, go in the `terraform/main.tf` file and change the `raw_config` variable to your config file (should be `= file(path/to/your/file)`). \
By default `samplse/config.json` will be used.
- Depending on how you created the google repo, you might want to change the exporter functions' build parameters; Namely `build_config.source.repo_source.repo_name` and `build_config.source.repo_source.branch_name` in `terraform/resource.tf`


For your first deployment you could configure your port with `samples/blueprints.json` and use `samples/config.json`. That way everything should work out of the box.

You could always change your scheduler job config.json to fit your port blueprints later, and use `terraform apply` to change it.

If you know what you're doing you might also want to eddit `terraform/roles.tf`. All roles set by this project on your gcp project are set in it.

## How To Deploy

### What you'll need
First, you'll need a [Google Account](https://www.gmail.com) (duh), and subscribe to the [Google Cloud Provider](https://console.cloud.google.com/) (also duh).

You'll also need this project locally, and have Terraform available.

The google cloud cli `gcloud` is also recommanded to be installed.


### Set A Function Source Repo

First, you need to make sure that you have a source repo with this project on your GCP project.

This can be done in the [GCP Repos Console](https://source.cloud.google.com/repo/connect).

You could either mirror the code from the github (`https://github.com/pazhersh/port-exercise.git`), or clone locally and upload it there.

### Enable The Required Cloud Services

This could be done via the GCP web ui, but is recommanded to enable via the following `gcloud` command:
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

### Terraform Deploy

Terraforming deployment is pretty straight forward.
In the project's directory:

* init terraform:
```bash
terraform init
```

* apply terraform:
##### note that the `-auto-aprove` is not mandatory
```bash
terraform apply -auto-aprove
```

### Enjoy life

You're done deploying!

## What now?

So you have the solution deployed, but how do you use it now that its up there in the cloud?

Well first of all, it should work on its own. By default the scheduler job is set to run every 5th minute, and therefore, if everything was deployed currectly, than it should export resources to port every 5 minutes. (you can also manually cause the job to execute on other minutes if you so desire; its accessible in the scheduler job page)

Otherwise, you could push messages to entity events (the PubSub). The message should be the config-file you want the exporter to run with (see the chapter about writing a config.json).

Don't like to work hard and manually? GCP has a whole lot of ways to use eventarc to push messages to PubSubs, you just have to decide what and when! and then configure it! oh and don't forget to make sure that the message is config.json complient!
