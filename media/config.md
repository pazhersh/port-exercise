## Writing A config.json

So you want to write your own config.json, aye? Don't worry, I've got you covered.

First thing first, you should get yourself familiar with JQ (json query, its a json query language); The entity serialization itself is done with it.

The file structure:
```js
{
    "resources": [
        {
            "service": "serviceName", // this is the gcp service to be used. you cant find all available services `gcp services list` - it will show you '<your-service-name>.googleapis.com'.
            "resourcePath": ["path", "to", "resource"], // the path to your resource in the service's api. you can find all of them in gcp's documentation
            "selectors": {
                "project": [
                    "gcpProjectId" // the gcp project to look for recources in. you can put in as many projects as you want.
                ],
                "zone": [
                    "us-central1" // the gcp zone to look for resources in.you can put in as many zones as you want.
                ]
                // if there are multiple projects and zones, than in each project, all zones will be queried for resources.
            },
            "portEntityMapping": [
                {
                    // this is where the meat of the config is.
                    // for each resource object recieved by the list query (as defined above), it's json will be transformed by the mapping.
                    // this entirte object is just a big JQ query object. the result of querying it against the gcp resource is what we later upload to port.
                    "entrypoint": "entrypointJQ",  // mandatory - where in the gcp resource json should we start running?
                    "identifier": "identifierJQ", // mandatory - port identifier
                    "title": "titleJQ", // mandatory - port identifier
                    "blueprint": "\"blueprintName\"", // mandatory - the port blueprint to upload the result as
                    "properties": { // mandatory - the port properties
                        // what comes here is based on your defined blueprint
                        "description": ".description", // example - create a description string property in port, and take the gcp resources '.description' property as value
                    }
                },
                // if you add multiple mappings, than each will be run on the original json of the gcp resource, so that each will create a different entity.
                // you can add as many mappings as you want, and all resulted entities will be uploaded to port
            ]
        },
        // you can add as many resource definitions as you want
    ]
}
```

Still confused? Than you can take at our samples than!
[config.json](/samples/config.json) - a config.json example. note that the regions and zones are not neccessarily real and some are there just as an example.
[blueprints.json](/samples/blueprints.json) - the blueprint definitions that the sample config.json is configured for.
