%%bash 
gcloud init --skip-diagnostics
gcloud config set project caltech-439204
gcloud config set compute/region us-central1
export NAME="lab03-2-`gcloud config get-value account | tr -cd 'a-z0-9' |  cut -c1-63`"
gcloud services enable run.googleapis.com \
    cloudbuild.googleapis.com
gcloud projects add-iam-policy-binding caltech-439204 \
    --member=serviceAccount:240830225929-compute@developer.gserviceaccount.com \
    --role=roles/cloudbuild.builds.builder
gcloud run deploy $NAME --source .