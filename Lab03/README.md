# Lab 03: Deploying models

## Step 1

Manually deploy the a model to produciton with the following steps:

1. 


## Step 2: Vertex AI Model Garden: LLM Deployment Workflow

This README provides an overview of deploying Large Language Models (LLMs) using Vertex AI Model Garden. We'll guide you through the complete workflow, from model selection to deployment and monitoring, including integrating Llama Guard for safeguarding your model.

## #1. **Model Selection**

Vertex AI Model Garden offers pre-trained, fine-tuned, and custom models. You can start by browsing the available LLMs for various use cases, including general-purpose models and domain-specific ones.

#### Steps:
- Navigate to [Vertex AI Model Garden](https://cloud.google.com/vertex-ai) to explore available LLMs.
- Select an appropriate model based on your requirements (e.g., GPT, T5, etc.).

### 2. **Model Customization**

For more refined outcomes, you can fine-tune the LLM with your own dataset. Vertex AI allows you to customize models efficiently using transfer learning methods such as LORA (Low-Rank Adaptation).

#### Steps:
- Use Vertex AI’s fine-tuning capabilities via [Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines).
- Ensure proper dataset formatting and preparation for optimal fine-tuning.

### 3. **Model Deployment**

Deploy the fine-tuned or pre-trained model to Vertex AI’s scalable infrastructure. Vertex AI handles the necessary scaling, load balancing, and serving infrastructure.

#### Steps:
- Deploy the model using Vertex AI’s deployment service for easy endpoint creation. Documentation on model deployment is available [here](https://cloud.google.com/vertex-ai/docs/predictions/getting-predictions).
- Specify compute requirements, such as GPU instances, for efficient real-time inferencing.

### 4. **Incorporating Llama Guard for Model Safety**

To ensure that your LLM operates within ethical and safe boundaries, it’s crucial to integrate tools like **Llama Guard**. Llama Guard provides safeguards such as filtering out harmful content and protecting against unintended model outputs.

#### Steps:
- Review and implement **Llama Guard’s** card in Vertex AI for details on safety integrations. You can find the Llama Guard Card [here](https://console.cloud.google.com/vertex-ai/publishers/meta/model-garden/llama-guard).
- Set up monitoring and trigger conditions to ensure that your LLM is performing within acceptable safety standards.

### 5. **Model Monitoring and LLMops**

Once your LLM is deployed, continuous monitoring is essential. Vertex AI offers built-in observability tools to track key metrics like response times, cost, and accuracy.

#### Steps:
- Enable **Vertex AI Model Monitoring** to track your model's performance and detect data drift.
- Set up alerts for anomalous behavior or performance degradation. Further reading on model monitoring can be found [here](https://cloud.google.com/vertex-ai/docs/model-monitoring).

### 6. **Ongoing Maintenance and Retraining**

As your LLM continues to operate in production, you may need to retrain it with updated data to keep it relevant and effective.

#### Steps:
- Retrain the model using the [Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines) for continuous integration and continuous delivery (CI/CD) of LLMs.
- Schedule periodic reviews to ensure ongoing alignment with business and compliance goals.

