# LLMOps Lab 01 - README

## Objective
The objective of this lab is to provide students with hands-on experience in managing and operationalizing Large Language Models (LLMs) using **GCP Colab Enterprise**. This lab will guide you through deploying, fine-tuning, and monitoring LLMs while balancing cost, performance, and responsible AI practices. Specifically, we will focus on fine-tuning models efficiently using **Low-Rank Adaptation (LORA)** and how to optimize the operational aspects of LLMs for real-world applications.

By the end of this lab, students will:
- Understand how to deploy and fine-tune LLMs on GCP.
- Learn to monitor resource utilization, performance, and costs.
- Be familiar with responsible AI practices in the context of LLMs.

## GCP Colab Enterprise Runtime Configuration

This lab is configured to run on **GCP Colab Enterprise** with the following runtime settings:

- **Machine type**: g2-standard-24
- **GPUs**: NVIDIA L4 (x2)
- **Disk**: 100 GB Standard Disk (pd-standard)

### Cost Information
- **Approximate runtime cost**: The estimated cost for this lab setup on GCP Colab Enterprise is approximately **$3.11 per hour**. The machine type (g2-standard-24) includes 2 NVIDIA L4 GPUs, with 45 GB of total GPU memory.
- **Training time**: The fine-tuning process takes about 1 hour per run, consuming around **37 GB of GPU memory** out of the available 45 GB.

It is essential to manage your usage effectively and only fine-tune the models when absolutely necessary to keep costs low and avoid resource wastage.

## Fine-Tuning with LORA

For this lab, we will use **Low-Rank Adaptation (LORA)** as a fine-tuning technique. LORA is an efficient method that reduces the number of trainable parameters by introducing low-rank matrices. This approach allows you to fine-tune large models faster and with fewer resources.

### Why LORA?

- **Efficiency**: LORA reduces memory and compute requirements by focusing only on essential parts of the model during fine-tuning.
- **Scalability**: You can scale up to larger models without overwhelming the available GPU memory.
- **Cost**: Since LORA is resource-efficient, it helps lower training costs and time, making it ideal for running multiple iterations.

However, remember that **fine-tuning** should only be performed when necessary, as over-tuning models can result in diminishing returns, excessive resource usage, and increased costs.

## Getting Started

1. open Collab Enterprise. Likely you can get some free credits and [try it out](https://cloud.google.com/colab/pricing)
2. open the console https://console.cloud.google.com/vertex-ai/colab/notebooks
3. Import from URL and then select this url
   ```
   https://raw.githubusercontent.com/methodical-company/caltech-llmops/refs/heads/main/Lab01/Lab01_clean.ipynb
   ```
   

## Lab Structure

The lab consists of the following key sections:

1. **Introduction to LLMOps**  
   Learn the operational challenges of deploying and maintaining large language models and how to address them using GCP.

2. **Model Deployment on GCP**  
   Deploy a pre-trained LLM on GCP Colab Enterprise, configure the environment, and ensure optimal performance using the NVIDIA L4 GPUs.

3. **Fine-tuning with LORA**  
   Use the LORA method to fine-tune your model for specific tasks. This section includes practical steps for reducing resource consumption and training time.

4. **Monitoring and Alerts**  
   Set up monitoring systems to track GPU and CPU utilization, disk space, and performance metrics such as latency and accuracy. Implement alert systems to ensure model performance remains within acceptable thresholds.

5. **Cost and Resource Management**  
   Learn techniques to monitor and manage the cost of running LLMs at scale, using GCP's built-in cost management tools.

6. **Responsible AI**  
   Understand responsible AI principles in model deployments, including ethical considerations, bias detection, and fairness evaluation. Learn how to adjust model outputs to adhere to responsible AI guidelines.

## Expanding the Exercise

Here are some suggestions on how to expand your learning:

1. **Deploy Different Models**:  
   Experiment with deploying various models (e.g., GPT-3, BERT) and compare their operational performance and cost profiles.

2. **Fine-tune with Larger Datasets**:  
   Try using larger datasets for fine-tuning to explore the impact on performance, cost, and time. Monitor how this affects GPU usage and runtime.

3. **Optimize Auto-scaling**:  
   Implement auto-scaling techniques for your model deployment to dynamically adjust resources based on demand, ensuring that you maintain cost-effectiveness.

4. **CI/CD for Continuous Model Updates**:  
   Integrate a CI/CD pipeline to automate model updates and reduce manual intervention when pushing new versions of the LLM into production.

5. **Explore Different Cloud Platforms**:  
   Deploy the model on other cloud platforms like AWS or Azure and compare the operational metrics, including cost, scalability, and ease of use.

## Prerequisites

- Basic knowledge of Python programming and Jupyter notebooks
- Understanding of AI/ML concepts, particularly large language models (LLMs)
- Access to **GCP Colab Enterprise** (recommended)

## Quiz

At the end of the lab, you can test your knowledge with the following quiz:

1. What is the primary benefit of using **LORA** for fine-tuning models?
    - a) Reduces the number of trainable parameters
    - b) Increases model size
    - c) Slows down the training process
    - d) Requires more resources

2. How much GPU space does the training process consume in this lab?
    - a) 25 GB
    - b) 37 GB
    - c) 45 GB
    - d) 50 GB

3. What machine type is used in this lab?
    - a) n1-standard-24
    - b) e2-standard-24
    - c) g2-standard-24
    - d) g4-standard-24

4. How long does the fine-tuning process take per training run?
    - a) 30 minutes
    - b) 1 hour
    - c) 2 hours
    - d) 4 hours

5. What GPU is used in this lab's runtime configuration?
    - a) NVIDIA Tesla V100
    - b) NVIDIA T4
    - c) NVIDIA L4
    - d) NVIDIA A100

6. What is the approximate cost per hour for this lab's runtime?
    - a) $1.50
    - b) $3.11
    - c) $5.20
    - d) $10.00

7. Why should you only fine-tune models when necessary?
    - a) Fine-tuning improves model accuracy in all cases.
    - b) Fine-tuning can increase resource consumption and cost.
    - c) It is faster to fine-tune all models at once.
    - d) Fine-tuning reduces model size significantly.

8. What tool is used to monitor cost and resource usage in this lab?
    - a) GCP Cloud Console
    - b) AWS Cost Explorer
    - c) Azure Monitor
    - d) None of the above

9. What is the main purpose of LLMOps?
    - a) Fine-tuning models
    - b) Monitoring model performance
    - c) Managing the operational aspects of LLMs
    - d) Building new models from scratch

10. What is the total GPU memory available in this lab setup?
    - a) 16 GB
    - b) 32 GB
    - c) 45 GB
    - d) 64 GB

## License
This project is licensed under the Apache 2 - see the LICENSE file for details.
