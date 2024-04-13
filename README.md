# Generative Tweet ML Pipeline Project

>**April 13th, 2024 - Update**
I am reworking this project to adapt my inference containers to the Sagemaker hosting services through the SageMaker TensorFlow Serving libraries available for the Python SDK. This rework will prolongue the duration of my project, but will allow me to have much more flexibility to train my models in my own GPUs and then host them in Sagemaker.

## Project Overview

[Infrastructure Diagram](https://github.com/adma224/ml-cloud-pipeline-generative-tweets/blob/main/infrastructure_diagram.png)

The Generative Tweet ML Pipeline project is currently under construction. This project is for a machine learning pipeline to generate tweets using advanced natural language processing models. The pipeline is designed to leverage AWS cloud services for scalability, performance, and reliability. My goal is to put my machine learning fundamentals and my AWS certification experience to practice. 

## Goal

Our goal is to develop an end-to-end machine learning pipeline that enables A/B testing of different NLP models for generating tweets. This involves preprocessing data, training models, deploying models for inference, and dynamically comparing their performance to choose the best model.

## Tools and Frameworks

Jupyter Notebooks - data pre-processing and training of LSTM and GPT-2 (I considered using Sagemaker Notebooks, but I already have a 3090ti GPU on my computer)
Visual Studio + Amazon Codewhisperer - rapid development of a CloudFormation Template via the AWS CDK in Python
Tensorflow - Deep Learning framework

*Potentially I will be integrating GitHub actions for a more controlled deployment with CloudFormation, which is more representative of deploying into production in large organizations

## Machine Learning Models

- **LSTM**
- **GPT-2**

## AWS Resources and Their Use

- **Amazon SageMaker**: For training ML models and managing A/B testing between LSTM and GPT-2 models.
- **Amazon S3**: Serves as the primary data lake for storing tweet datasets and model artifacts.
- **AWS Lambda and Amazon API Gateway**: These services  handle requests to the ML models for inference and to manage the API interface for the application.
- **AWS AppSync**: Provides a managed GraphQL service for frontend-backend integration.
- **Amazon QuickSight**: Visualization
- **Amazon Aurora Serverless**: Serverless SQL database with native integration with Quicksight
- **AWS Secrets Manager**: Storing SQL databse credentials
- **IAM**: roles and permissions to access different resources
- **VPC**

## Project Structure

The project consists of multiple components, including Jupyter notebooks for model training and data preprocessing, a CDK-based infrastructure as code for deploying AWS resources, and configuration files.

- `GPT2_model.ipynb` and `LSTM_model.ipynb`: Jupyter notebooks containing the code for training the GPT-2 and LSTM models respectively.
- `Tweet Exploration and Data Preprocessing.ipynb`: A notebook dedicated to data exploration and preprocessing tasks.
- `tweets.csv`: The dataset used for training the models.
- `ml-pipeline/`: The directory containing the AWS CDK application for infrastructure setup, including stack definitions for deploying the necessary AWS resources.

## Functionality and ML Pipeline

Once models are trained, they are deployed to Amazon SageMaker Hosting Services for A/B testing. The pipeline leverages AppSync for frontend interactions, API Gateway for managing requests, and QuickSight for visualization.

## Under Construction

Please note that this project is in active development. 

Stay tuned for updates and enhancements!
