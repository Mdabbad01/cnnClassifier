🧠 CNN Image Classifier

A deep learning project to build, train, and deploy a Convolutional Neural Network (CNN) for image classification.
This project is modular, production-ready, and includes experiment tracking, data versioning, and deployment setup.

🚀 Features

✅ End-to-end CNN pipeline
✅ Modular Python package structure (src/cnnClassifier/)
✅ YAML-based configuration system
✅ Logging and exception handling
✅ Experiment tracking with MLflow
✅ Data versioning using DVC
✅ Flask API for model prediction
✅ Ready for deployment on AWS / Render / GCP

📁 Project Structure
cnnClassifier/
│
├── .github/workflows/        <- CI/CD workflows
├── config/                   <- Config files (YAML)
├── research/                 <- Jupyter notebooks / experiments
├── logs/                     <- Log files
├── src/cnnClassifier/        <- Main package
│   ├── __init__.py
│   ├── components/           <- Model components (data loader, model trainer)
│   ├── config/               <- Config management scripts
│   ├── constants/            <- Project constants
│   ├── entity/               <- Data entities for type safety
│   ├── pipeline/             <- Training/inference pipelines
│   ├── utils/                <- Utility functions (common.py, etc.)
│   └── ...
│
├── templates/                <- HTML templates for Flask app
├── main.py                   <- Entry point
├── setup.py                  <- Package setup file
├── requirements.txt           <- Dependencies
├── config.yaml               <- Main configuration file
├── dvc.yaml                   <- DVC pipeline configuration
└── README.md