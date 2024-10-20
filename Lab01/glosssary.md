

# Glossary of Terms

### **LLMOps**
A practice focused on managing the operational aspects of deploying and maintaining Large Language Models (LLMs) in production environments. This includes tasks such as model deployment, monitoring, scaling, cost management, and ensuring responsible AI practices.

### **GCP Colab Enterprise**
Google Cloud Platform's enterprise version of Colaboratory (Colab), providing enhanced resources, security features, and integration with GCP services for scalable machine learning and data science workloads.

### **g2-standard-24**
A machine type on Google Cloud Platform that includes 24 virtual CPUs (vCPUs) and a significant amount of RAM, optimized for high-performance computing tasks.

### **NVIDIA L4 GPUs**
Graphics Processing Units designed by NVIDIA, optimized for AI inference and video processing tasks. In this lab, two NVIDIA L4 GPUs are used to accelerate model training and inference.

### **100 GB Standard Disk (pd-standard)**
A persistent disk type on GCP offering standard performance for block storage. It provides reliable and scalable storage for virtual machine instances.

### **GPU Memory**
The amount of memory available on a GPU, crucial for training and running large machine learning models. In this lab, each NVIDIA L4 GPU provides significant memory capacity.

### **Fine-Tuning**
The process of taking a pre-trained machine learning model and adjusting it to perform a specific task by training it on a smaller, task-specific dataset.

### **Low-Rank Adaptation (LORA)**
A technique for fine-tuning large models efficiently by introducing low-rank matrices, which reduces the number of trainable parameters and resource consumption during training.

### **Model Deployment**
The process of making a trained machine learning model available for use in a production environment, allowing it to serve predictions to end-users or systems.

### **Monitoring and Alerts**
Systems and processes for tracking the performance and health of deployed models and infrastructure. Alerts notify administrators when certain performance thresholds are breached.

### **Cost Management**
The practice of monitoring and controlling expenditures associated with cloud resources to optimize spending and resource utilization.

### **Responsible AI**
Principles and practices aimed at ensuring AI systems are developed and used ethically, considering fairness, transparency, accountability, and mitigation of biases.

### **GCP Cloud Console**
A web-based interface for managing Google Cloud resources, including virtual machines, storage, networking, and monitoring tools.

### **Python**
A high-level, interpreted programming language widely used in data science, machine learning, and web development due to its readability and extensive libraries.

### **Jupyter Notebook**
An open-source web application that allows users to create and share documents containing live code, equations, visualizations, and narrative text.

### **Hyperparameters**
Configurable parameters in machine learning models that are set before the training process begins, influencing the learning process and model performance.

### **Compute Resources**
Hardware resources required to perform computational tasks, including CPUs, GPUs, memory, and storage.

### **Bias Detection**
Techniques used to identify and mitigate biases in AI models to promote fairness and prevent discrimination against certain groups.

### **Fairness Metrics**
Quantitative measures used to assess the fairness of AI models across different demographic groups or attributes.

### **Auto-Scaling**
A method of dynamically adjusting computational resources allocated to applications based on current demand to ensure optimal performance and cost efficiency.

### **Continuous Integration/Continuous Deployment (CI/CD)**
Practices in software development where code changes are automatically tested and deployed, enabling rapid and reliable delivery of applications and updates.

### **Model Drift**
The degradation of a machine learning model's performance over time due to changes in the underlying data patterns that were not present in the training data.

### **Federated Learning**
A machine learning approach where models are trained across multiple decentralized devices holding local data samples, without exchanging the data itself, enhancing privacy.

### **Hugging Face Model Hub**
An open platform for sharing and accessing pre-trained models for natural language processing and other machine learning tasks.

### **Vertex AI**
Google Cloud's unified artificial intelligence platform that helps developers and data scientists build, deploy, and scale ML models faster using pre-trained and custom tooling.

### **AWS SageMaker**
Amazon Web Services' fully managed service that provides developers and data scientists with the ability to build, train, and deploy machine learning models at scale.

### **Azure Machine Learning**
Microsoft Azure's cloud service that enables data scientists and developers to build, train, and deploy machine learning models.

### **Pip**
A package installer for Python that allows users to install and manage additional libraries and dependencies not included in the Python standard library.

### **requirements.txt**
A file used in Python projects to specify the packages and their versions required to run the project. It facilitates environment replication and dependency management.

### **Hyperparameter Tuning**
The process of systematically adjusting hyperparameters to optimize the performance of a machine learning model.

### **Latency**
The time delay between a user's action and the response from the system, critical in evaluating the performance of deployed models, especially in real-time applications.

### **Accuracy**
A metric for evaluating classification models, representing the proportion of true results (both true positives and true negatives) among the total number of cases examined.

### **Compute Engine**
Google Cloud's Infrastructure-as-a-Service product that offers scalable virtual machines running in Google's data centers.

### **Resource Utilization**
The measurement of how effectively computing resources (CPU, GPU, memory, disk) are being used by applications or processes.

### **Model Overfitting**
A modeling error in machine learning where a model is too closely fitted to the training data and may fail to generalize to new, unseen data.

### **Scaling Strategies**
Approaches to adjust computational resources based on workload demands, including vertical scaling (adding more power to existing machines) and horizontal scaling (adding more machines).

### **Data Preprocessing**
The process of cleaning and transforming raw data into an understandable format for machine learning models.

### **Pandas**
An open-source Python library providing high-performance, easy-to-use data structures, and data analysis tools.

### **NumPy**
A fundamental package for scientific computing with Python, providing support for arrays, mathematical functions, and linear algebra operations.

### **TensorFlow**
An open-source machine learning framework developed by Google, used for building and deploying machine learning and deep learning models.

### **PyTorch**
An open-source machine learning library developed by Facebook's AI Research lab, known for its flexibility and dynamic computation graph.

### **Matplotlib**
A Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments.

### **Seaborn**
A Python data visualization library based on Matplotlib, providing a high-level interface for drawing attractive statistical graphics.

### **Scikit-learn**
An open-source Python library that provides simple and efficient tools for predictive data analysis, including classification, regression, clustering, and dimensionality reduction.

### **Data Augmentation**
Techniques used to increase the amount and diversity of data by adding modified copies of existing data or creating new synthetic data.

### **Batch Size**
The number of training examples used in one iteration during the training of a machine learning model.

### **Learning Rate**
A hyperparameter that controls how much the model is adjusted during training each time the model weights are updated.

### **Epoch**
One complete pass through the entire training dataset during the training process.

### **Regularization**
Techniques used to reduce the risk of overfitting by adding additional information or constraints to a model.

### **Dropout**
A regularization technique where randomly selected neurons are ignored during training, which helps prevent overfitting.

### **Model Checkpointing**
The practice of saving the current state of a model at certain points during training, allowing for resuming training or rollback if needed.

### **Model Serving**
The process of hosting a trained machine learning model to provide predictions (inference) to end-users or systems.

### **Inference**
Using a trained machine learning model to make predictions on new, unseen data.

### **Data Loader**
A component that handles loading and batching data during the training or inference processes in machine learning workflows.

### **Early Stopping**
A method used during training to halt the process when the performance on a validation dataset starts to degrade, preventing overfitting.

### **Evaluation Metrics**
Standards used to measure the performance of a machine learning model, such as precision, recall, F1-score, mean squared error, etc.

### **Learning Rate Scheduler**
A technique that adjusts the learning rate during training based on a predefined schedule or in response to certain triggers.

### **Cross-Validation**
A statistical method used to estimate the performance of machine learning models by partitioning the original dataset into a training set to train the model and a test set to evaluate it.

### **Activation Function**
A function used in neural networks to introduce non-linearity, allowing the network to learn complex patterns. Examples include ReLU, sigmoid, and tanh functions.

### **Loss Function**
A function that measures how well the model's predictions match the actual data, guiding the optimization process during training.

### **Backpropagation**
An algorithm used to calculate the gradient of the loss function with respect to the weights of the neural network, essential for training deep learning models.

### **Random Seed**
A value used to initialize a pseudorandom number generator, ensuring reproducibility of experiments by producing the same sequence of random numbers.

### **Reproducibility**
The ability to achieve consistent results using the same methodology and data, crucial for verifying and validating scientific findings.

### **Normalization**
The process of scaling individual samples to have unit norm or adjusting values to a common scale without distorting differences in the ranges of values.

### **Data Split**
Dividing the dataset into separate subsets for training, validation, and testing to evaluate model performance effectively.

### **Cloud Storage**
A service model in which data is maintained, managed, and backed up remotely, available to users over a network (typically the internet).

### **Version Control (Git)**
A system that records changes to files over time so that specific versions can be recalled later. Git is a widely used version control system in software development.

### **Docker**
An open platform for developing, shipping, and running applications inside lightweight, standalone containers, which package software with all its dependencies.

### **Containerization**
The process of packaging an application and its dependencies into a container so it can run consistently across different computing environments.

### **Kubernetes**
An open-source system for automating deployment, scaling, and management of containerized applications, often used in managing cloud-native applications.

### **Command Line Interface (CLI)**
A text-based user interface used to interact with software and operating systems by typing commands into a console or terminal.

### **API (Application Programming Interface)**
A set of definitions and protocols for building and integrating application software, allowing communication between different software components.

### **Endpoint**
A specific URL or network address at which a web service or application can be accessed by a client.

### **JSON (JavaScript Object Notation)**
A lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate.

### **YAML (YAML Ain't Markup Language)**
A human-readable data serialization language commonly used for configuration files and in applications where data is being stored or transmitted.

### **Logging**
The process of recording information about a system's operation, typically used for debugging, monitoring, and auditing purposes.

### **Error Handling**
The practice of anticipating, detecting, and resolving errors that occur in software applications to prevent system crashes or unintended behavior.

### **Resource Quotas**
Limits set on the amount of computing resources (CPU, memory, storage) that can be used by applications or users in a cloud environment.

### **Persistent Disk**
A durable storage device that can be attached to virtual machine instances, retaining data independently of the instance's lifecycle.

### **Data Scientist**
A professional who uses statistical methods, algorithms, and machine learning techniques to extract insights and knowledge from data.

### **Machine Learning Engineer**
An engineer focused on the design and implementation of machine learning models and systems that can process large amounts of data efficiently.

### **Notebook Kernel**
The computational engine that executes the code contained in a Jupyter notebook document.

### **CUDA (Compute Unified Device Architecture)**
A parallel computing platform and programming model developed by NVIDIA for general computing on graphical processing units (GPUs).

### **Model Compression Techniques**
Methods used to reduce the size of a machine learning model, such as quantization, pruning, and knowledge distillation, to improve efficiency.

### **Optimization Algorithms**
Algorithms used in training machine learning models to minimize the loss function, such as stochastic gradient descent (SGD), Adam, and RMSProp.

### **Data Pipeline**
A set of processes that extract, transform, and load data from one system to another, facilitating data flow and processing.

### **Scaling Up (Vertical Scaling)**
Increasing the capacity of existing hardware or software by adding more resources (e.g., CPU, memory) to handle increased workloads.

### **Scaling Out (Horizontal Scaling)**
Adding more machines or instances to a system to distribute the load and handle increased demand.

### **Security in AI**
The practice of protecting AI systems from threats and vulnerabilities, including data breaches, adversarial attacks, and ensuring data privacy.

### **Adversarial Attacks**
Attempts to fool machine learning models by providing deceptive input, potentially causing the model to make errors or behave unpredictably.

### **Data Governance**
The overall management of the availability, usability, integrity, and security of the data employed in an organization or system.

### **Terraform**
An open-source infrastructure-as-code software tool that enables you to define and provide data center infrastructure using a declarative configuration language.

### **Ansible**
An open-source automation tool used for configuration management, application deployment, and task automation.

### **MLflow**
An open-source platform designed to manage the end-to-end machine learning lifecycle, including experimentation, reproducibility, deployment, and a central model registry.

### **Experiment Tracking**
The process of recording and managing all relevant information about model training runs to facilitate analysis and reproducibility.

### **Cloud IAM (Identity and Access Management)**
A framework of policies and technologies for ensuring that the proper people in an enterprise have the appropriate access to technology resources.

### **Hyperparameter Optimization**
Systematically tuning hyperparameters to improve the performance of machine learning models, often using techniques like grid search or random search.

### **Data Cleaning**
The process of detecting and correcting (or removing) corrupt or inaccurate records from a dataset to improve data quality.

### **Model Serving Frameworks**
Software tools that facilitate the deployment and serving of machine learning models in production environments, such as TensorFlow Serving or TorchServe.

### **Notebook Extensions**
Plugins or add-ons that enhance the functionality of Jupyter notebooks, providing features like code linters, spell checkers, and execution timing.

### **Cloud Billing Account**
An account associated with a cloud provider used to manage billing information, payment methods, and to track costs associated with cloud resource usage.

### **Service Account**
A special type of account used by applications or virtual machines to interact with other services, providing authentication and access control.

### **SSH (Secure Shell)**
A network protocol that provides administrators with a secure way to access a remote computer, encrypting all traffic to prevent eavesdropping.

### **Horizontal Scaling**
Adding more instances to a system, allowing it to handle more work by distributing the load across multiple machines.

### **Vertical Scaling**
Enhancing the capacity of a single machine by adding more resources, such as CPU, RAM, or storage.

### **Compute Engine Quotas**
Limits set by Google Cloud Platform on the amount of Compute Engine resources (like CPUs, GPUs) that can be used to prevent resource abuse.

### **Resource Monitoring**
The continuous tracking and reporting of resource usage metrics, such as CPU, memory, disk I/O, and network traffic, to optimize performance and detect anomalies.

### **Alerting Systems**
Mechanisms set up to notify administrators or users when specific conditions are met or thresholds are exceeded, aiding in proactive system management.

### **Model Inference Latency**
The time it takes for a deployed machine learning model to process an input and produce an output, critical for real-time applications.

### **Infrastructure as Code (IaC)**
The process of managing and provisioning computing infrastructure through machine-readable definition files, rather than physical hardware configuration.

### **ReLU (Rectified Linear Unit)**
An activation function used in neural networks, defined as the positive part of its argument: `f(x) = max(0, x)`, introducing non-linearity into models.

