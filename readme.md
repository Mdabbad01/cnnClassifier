# CNN-Based Kidney CT Scan Classification

## Overview

This project implements an end-to-end deep learning pipeline for classifying kidney CT scan images into Normal and Tumor categories.

The system is designed using a modular architecture with clearly separated components for data ingestion, base model preparation, model training, evaluation, and prediction. Configuration files are used to manage parameters and ensure reproducibility.

## Architecture

The workflow follows a structured pipeline:

1. Data Ingestion  
2. Base Model Preparation  
3. Model Training  
4. Model Evaluation (integrated with MLflow)  
5. Model Serving through Flask API  

All core logic is organized inside a reusable Python package located in:

src/cnnClassifier/

## Dataset

The dataset consists of kidney CT scan images categorized into:

- Normal  
- Tumor  

Images are processed during ingestion and passed through the training pipeline.

## Key Features

- Modular component-based structure  
- YAML-driven configuration management  
- MLflow experiment tracking  
- DVC pipeline support  
- Structured logging and exception handling  
- Docker support  
- Flask-based prediction interface  

## Tech Stack

- Python  
- TensorFlow / Keras  
- MLflow  
- DVC  
- Flask  
- Docker  
- YAML configuration  

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the training pipeline:

python main.py

Start the Flask application:

python app.py

## Project Structure

├── src/
│   └── cnnClassifier/
├── config/
├── artifacts/
├── research/
├── app.py
├── main.py
├── Dockerfile
├── dvc.yaml
