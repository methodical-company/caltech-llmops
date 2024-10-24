# caltech-llmops
Class at Caltech on LLMOps by Brian Ray

How to run these labs:
1. Log into GCP Console https://console.cloud.google.com/ Use the link from the slides if in caltech class.
1. Navigate to Colab Enterprise https://console.cloud.google.com/vertex-ai/colab/notebooks
1. Navigate to the notebooks in this repository for example https://github.com/methodical-company/caltech-llmops/blob/main/Lab01/Lab01_Step1.ipynb
1. Get the Raw link <img width="337" alt="link" src="https://github.com/user-attachments/assets/233100d7-e176-482c-ad90-e5674efa88e0">
1. go back to collab and hit the upload button, click url, paste the url.
1. Pick a runtime <img width="460" alt="runtime 1" src="https://github.com/user-attachments/assets/434d1471-d03c-4896-b9d7-5abddc8866d8">
1. pick from template <img width="579" alt="runtime 2" src="https://github.com/user-attachments/assets/376dc634-6413-4c7a-9e1a-797df5bfe8c4">
1. once it starts you should see a GPU attached to the notebook  <img width="351" alt="gpu" src="https://github.com/user-attachments/assets/c0d8545d-0760-4b8b-9f99-5680b4e8e00b">
1. then you are all set to run each cell in the notebook. 


## Lab 01: Implement LLMS

This lab provides hands-on experience implementing LLMs. The example is Natural Language to SQL with two different pre-built Models

We will kick off a fine-tuning for a large language models (LLM) using GCP Colab Enterprise, using LORA. 

[Lab 01](./Lab01)

## Lab 02: Model Trials

This lab we take 2 different model implementation and make them comparable and measure performance in batch.

[Lab 02](./Lab02)

## Lab 03: Pushing Models into Produciton

This lab will show 2 different ways to push models into production.

[Lab 03](./Lab03)

## Lab 04: App Dev for LLMOps

This lab puts it all together walks you through how to create a simple test application to interact with your deployed model. 

[Lab 04](./Lab04)

