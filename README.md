# Generative Tweet ML Pipeline Project

## Project Overview

The Generative Tweet ML Pipeline project is currently under construction. This project is for a machine learning pipeline to generate tweets using advanced natural language processing models. The pipeline is designed to leverage AWS cloud services for scalability, performance, and reliability. My goal is to put my machine learning fundamentals and my AWS certification experience to be applied. 

## Goal

Our goal is to develop an end-to-end machine learning pipeline that enables A/B testing of different NLP models for generating tweets. This involves preprocessing data, training models, deploying models for inference, and dynamically comparing their performance to choose the best model.

## Machine Learning Models

- **LSTM Model**
- **GPT-2 Model**

## AWS Resources and Their Use

- **Amazon SageMaker**: For training ML models and managing A/B testing between LSTM and GPT-2 models.
- **Amazon S3**: Serves as the primary data lake for storing tweet datasets and model artifacts.
- **AWS Lambda and Amazon API Gateway**: These services  handle requests to the ML models for inference and to manage the API interface for the application.
- **AWS AppSync**: Provides a managed GraphQL service for seamless frontend-backend integration.
- **Amazon QuickSight**: Visualization
- **Amazon S3 with AWS Glue**

## Project Structure

The project consists of multiple components, including Jupyter notebooks for model training and data preprocessing, a CDK-based infrastructure as code for deploying AWS resources, and configuration files.

- `GPT2_model.ipynb` and `LSTM_model.ipynb`: Jupyter notebooks containing the code for training the GPT-2 and LSTM models respectively.
- `Tweet Exploration and Data Preprocessing.ipynb`: A notebook dedicated to data exploration and preprocessing tasks.
- `tweets.csv`: The dataset used for training the models.
- `ml-pipeline/`: The directory containing the AWS CDK application for infrastructure setup, including stack definitions for deploying the necessary AWS resources.

## Functionality and ML Pipeline

The pipeline begins with tweet data preprocessing, followed by model training. Once models are trained, they are deployed to Amazon SageMaker, where A/B testing is conducted to evaluate performance. The pipeline leverages AppSync for frontend interactions, API Gateway for managing requests, and QuickSight for visualization.

## Under Construction

Please note that this project is in active development. 

Stay tuned for updates and enhancements!
