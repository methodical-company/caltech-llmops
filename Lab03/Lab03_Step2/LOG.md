#LOG 

Run `% ./deploy.sh` to deploy the application. See my answers below for the configuration of gcloud.

```

Welcome! This command will take you through the configuration of gcloud.

Settings from your current configuration [default] are:
core:
  disable_usage_reporting: 'False'

Pick configuration to use:
 [1] Re-initialize this configuration [default] with new settings 
 [2] Create a new configuration
Please enter your numeric choice:  1

Your current configuration has been set to: [default]

Choose the account you would like to use to perform operations for this configuration:
 [1] brian.ray@mavenwave.com
 [2] brian@methodical.company
 [3] promptly-dev@methodical-promptly.iam.gserviceaccount.com
 [4] Log in with a new account
Please enter your numeric choice:  2

You are logged in as: [brian@methodical.company].

Pick cloud project to use: 
 [1] caltech-439204
 [2] methodical-prod
 [3] methodical-dev
 [4] methodical-staging
 [5] methodical-qa
 [6] Enter a project ID
 [7] Create a new project

Please enter numeric choice or text value (must exactly match list item):  1

Your current project has been set to: [caltech-439204].

Do you want to configure a default Compute Region and Zone? (Y/n)?  

Which Google Compute Engine zone would you like to use as project default?
If you do not specify a zone via a command line flag while working with Compute Engine resources, the default is assumed.
 [1] us-east1-b
 [2] us-east1-c
 [3] us-east1-d
 [4] us-east4-c
 [5] us-east4-b
 [6] us-east4-a
 [7] us-central1-c
 [8] us-central1-a
 [9] us-central1-f
 [10] us-central1-b
 [11] us-west1-b
 [12] us-west1-c
 [13] us-west1-a
 [14] europe-west4-a
 [15] europe-west4-b
 [16] europe-west4-c
 [17] europe-west1-b
 [18] europe-west1-d
 [19] europe-west1-c
 [20] europe-west3-c
 [21] europe-west3-a
 [22] europe-west3-b
 [23] europe-west2-c
 [24] europe-west2-b
 [25] europe-west2-a
 [26] asia-east1-b
 [27] asia-east1-a
 [28] asia-east1-c
 [29] asia-southeast1-b
 [30] asia-southeast1-a
 [31] asia-southeast1-c
 [32] asia-northeast1-b
 [33] asia-northeast1-c
 [34] asia-northeast1-a
 [35] asia-south1-c
 [36] asia-south1-b
 [37] asia-south1-a
 [38] australia-southeast1-b
 [39] australia-southeast1-c
 [40] australia-southeast1-a
 [41] southamerica-east1-b
 [42] southamerica-east1-c
 [43] southamerica-east1-a
 [44] africa-south1-a
 [45] africa-south1-b
 [46] africa-south1-c
 [47] asia-east2-a
 [48] asia-east2-b
 [49] asia-east2-c
 [50] asia-northeast2-a
Did not print [72] options.
Too many options [122]. Enter "list" at prompt to print choices fully.
Please enter numeric choice or text value (must exactly match list item):  7

Your project default Compute Engine zone has been set to [us-central1-c].
You can change it by running [gcloud config set compute/zone NAME].

Your project default Compute Engine region has been set to [us-central1].
You can change it by running [gcloud config set compute/region NAME].

Your Google Cloud SDK is configured and ready to use!

* Commands that require authentication will use brian@methodical.company by default
* Commands will reference project `caltech-439204` by default
* Compute Engine commands will use region `us-central1` by default
* Compute Engine commands will use zone `us-central1-c` by default

Run `gcloud help config` to learn how to change individual settings

This gcloud configuration is called [default]. You can create additional configurations if you work with multiple accounts and/or projects.
Run `gcloud topic configurations` to learn more.

Some things to try next:

* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic --help` to learn about advanced features of the SDK like arg files and output formatting
* Run `gcloud cheat-sheet` to see a roster of go-to `gcloud` commands.
Updated property [core/project].
Updated property [compute/region].
Operation "operations/acat.p2-240830225929-dbcb1dad-99b6-4a0b-b618-83a81aa5d2ba" finished successfully.
Updated IAM policy for project [caltech-439204].
bindings:
- members:
  - serviceAccount:caltech@caltech-439204.iam.gserviceaccount.com
  - user:brianhray@gmail.com
  role: roles/aiplatform.admin
- members:
  - user:brian@methodical.company
  role: roles/aiplatform.colabEnterpriseAdmin
- members:
  - user:brianhray@gmail.com
  role: roles/aiplatform.colabEnterpriseUser
- members:
  - serviceAccount:service-240830225929@gcp-sa-aiplatform-cc.iam.gserviceaccount.com
  role: roles/aiplatform.customCodeServiceAgent
- members:
  - serviceAccount:service-240830225929@gcp-sa-aiplatform-vm.iam.gserviceaccount.com
  role: roles/aiplatform.notebookServiceAgent
- members:
  - serviceAccount:service-240830225929@gcp-sa-vertex-op.iam.gserviceaccount.com
  role: roles/aiplatform.onlinePredictionServiceAgent
- members:
  - serviceAccount:service-240830225929@gcp-sa-aiplatform.iam.gserviceaccount.com
  role: roles/aiplatform.serviceAgent
- members:
  - serviceAccount:240830225929-compute@developer.gserviceaccount.com
  - serviceAccount:caltech@caltech-439204.iam.gserviceaccount.com
  role: roles/aiplatform.user
- members:
  - serviceAccount:service-240830225929@gcp-sa-artifactregistry.iam.gserviceaccount.com
  role: roles/artifactregistry.serviceAgent
- members:
  - serviceAccount:240830225929-compute@developer.gserviceaccount.com
  - serviceAccount:240830225929@cloudbuild.gserviceaccount.com
  role: roles/cloudbuild.builds.builder
- members:
  - serviceAccount:service-240830225929@gcp-sa-cloudbuild.iam.gserviceaccount.com
  role: roles/cloudbuild.serviceAgent
- members:
  - serviceAccount:service-240830225929@compute-system.iam.gserviceaccount.com
  role: roles/compute.serviceAgent
- members:
  - serviceAccount:service-240830225929@containerregistry.iam.gserviceaccount.com
  role: roles/containerregistry.ServiceAgent
- members:
  - serviceAccount:service-240830225929@gcp-sa-dataform.iam.gserviceaccount.com
  role: roles/dataform.serviceAgent
- members:
  - serviceAccount:240830225929-compute@developer.gserviceaccount.com
  - serviceAccount:240830225929@cloudservices.gserviceaccount.com
  role: roles/editor
- members:
  - user:brianhray@gmail.com
  role: roles/iam.serviceAccountUser
- members:
  - user:brian@methodical.company
  role: roles/owner
- members:
  - serviceAccount:service-240830225929@gcp-sa-pubsub.iam.gserviceaccount.com
  role: roles/pubsub.serviceAgent
- members:
  - serviceAccount:service-240830225929@serverless-robot-prod.iam.gserviceaccount.com
  role: roles/run.serviceAgent
- members:
  - serviceAccount:caltech@caltech-439204.iam.gserviceaccount.com
  - user:brian@methodical.company
  - user:brianhray@gmail.com
  role: roles/secretmanager.secretAccessor
- members:
  - serviceAccount:240830225929-compute@developer.gserviceaccount.com
  - serviceAccount:caltech@caltech-439204.iam.gserviceaccount.com
  - user:brian@methodical.company
  - user:brianhray@gmail.com
  role: roles/storage.admin
etag: BwYlLxNI4go=
version: 1
Please specify a region:
 [1] africa-south1
 [2] asia-east1
 [3] asia-east2
 [4] asia-northeast1
 [5] asia-northeast2
 [6] asia-northeast3
 [7] asia-south1
 [8] asia-south2
 [9] asia-southeast1
 [10] asia-southeast2
 [11] australia-southeast1
 [12] australia-southeast2
 [13] europe-central2
 [14] europe-north1
 [15] europe-southwest1
 [16] europe-west1
 [17] europe-west10
 [18] europe-west12
 [19] europe-west2
 [20] europe-west3
 [21] europe-west4
 [22] europe-west6
 [23] europe-west8
 [24] europe-west9
 [25] me-central1
 [26] me-central2
 [27] me-west1
 [28] northamerica-northeast1
 [29] northamerica-northeast2
 [30] southamerica-east1
 [31] southamerica-west1
 [32] us-central1
 [33] us-east1
 [34] us-east4
 [35] us-east5
 [36] us-south1
 [37] us-west1
 [38] us-west2
 [39] us-west3
 [40] us-west4
 [41] cancel
Please enter numeric choice or text value (must exactly match list item):  32

To make this the default region, run `gcloud config set run/region us-central1`.

This command is equivalent to running `gcloud builds submit --pack image=[IMAGE] .` and `gcloud run deploy lab03-2-brianmethodicalcompany --image [IMAGE]`

Allow unauthenticated invocations to [lab03-2-brianmethodicalcompany] (y/N)?  y

Building using Buildpacks and deploying container to Cloud Run service [lab03-2-brianmethodicalcompany] in project [caltech-439204] region [us-central1]
⠏ Building and deploying new service... Building Container.                                                             
  ✓ Uploading sources...                                                                                                
  ⠏ Building Container... Logs are available at [https://console.cloud.google.com/cloud-build/builds/cbf9e4c5-1f3c-40d6-
  889c-c48a7a5227a7?project=240830225929].                                                                              
  . Creating Revision...                                                                                                
  . Routing traffic...                                                                                                  
  . Setting IAM Policy... 


```