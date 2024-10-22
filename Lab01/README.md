# LLMOps Lab 01 - README

## Objective
The objective of this lab is to provide students with hands-on experience in managing and operationalizing Large Language Models (LLMs). We will be using **GCP Colab Enterprise** but this will work on any platform with GCP access. This lab will guide you through using and then fine-tuning with custom data efficiently using **Low-Rank Adaptation (LORA)** and how to optimize the operational aspects of LLMs for real-world applications.

By the end of this lab, you will:
- Understand how to fine-tune LLMs.
- Learn to monitor resource utilization, performance, and costs.


## Prerequisites

- Basic knowledge of Python programming and Jupyter notebooks
- Understanding of AI/ML concepts, particularly large language models (LLMs)
- Access to **GCP Colab Enterprise** (recommended)

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

## Step by Step

1. open Collab Enterprise. Likely you can get some free credits and [try it out](https://cloud.google.com/colab/pricing)
2. open the console https://console.cloud.google.com/vertex-ai/colab/notebooks
3. Import from URL and then select this url
   ```https://raw.githubusercontent.com/methodical-company/caltech-llmops/refs/heads/main/Lab01/Lab01_Step1.ipynb   ```
4. Run through Steps. Once it gets to `.train()` you can let it run (it will take awhile) and add a new notebook for Step2 (Import -> URL):
   ```https://raw.githubusercontent.com/methodical-company/caltech-llmops/refs/heads/main/Lab01/Lab01_Step2.ipynb ```
5. Run troug Steps until completion.
6. (optionally) later on if Step1 has finished you can test it with Step3 (Import -> URL):
   ```https://raw.githubusercontent.com/methodical-company/caltech-llmops/refs/heads/main/Lab01/test_Lab01clean_Step3_optional.ipynb```

   

## Lab Structure

The lab consists of the following key sections:

1. Getting Setup with tools and data
2. Loading a Foundational Model
3. Running the Base Foundational Model
4. Tokanize the Data
5. Setup Lora
6. Customizing Training Arugments
7. Train the Model (two variations Step 1 and Step 2)
8. Save the model to disc for easy versioning and deployment
9. Test the fine tuned model

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

4. When should you fine tune?
    - a) Always.
    - b) Ony if foundational model does not do the job.
    - c) when you want a smaller model.
    - d) Only when testing.

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
