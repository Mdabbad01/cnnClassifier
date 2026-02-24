CNN-Based Kidney CT Scan Classification
Overview

This project implements an end-to-end deep learning pipeline for classifying kidney CT scan images into Normal and Tumor categories. The system is built using a modular MLOps-oriented architecture with configuration-driven components and experiment tracking.

Architecture

The project follows a structured pipeline approach:

Data Ingestion

Base Model Preparation

Model Training

Model Evaluation with MLflow

Model Serving via Flask API

The implementation is organized under a reusable Python package (src/cnnClassifier) with clearly separated components and configuration management.

Dataset

The dataset contains kidney CT scan images categorized into:

Normal

Tumor

Images are processed during the ingestion stage and used for model training and evaluation.

Key Features

Modular component-based architecture

YAML-driven configuration

MLflow experiment tracking

DVC pipeline integration

Logging and exception handling

Docker support

Flask-based prediction API

Tech Stack

Python

TensorFlow / Keras

MLflow

DVC

Flask

Docker

YAML configuration

How to Run

Install dependencies

Configure parameters in config.yaml and params.yaml

Execute pipeline through main.py

Run Flask app using app.py
