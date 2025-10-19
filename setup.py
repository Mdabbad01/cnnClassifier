from setuptools import setup, find_packages

setup(
    name="cnnClassifier",            # Project name
    version="0.1.0",                 # Version
    author="Md Abbad",               # Your name
    author_email="youremail@example.com",  # Your email
    description="A CNN image classification project",
    packages=find_packages(where="src"),  # Include all packages under src
    package_dir={"": "src"},              # Root directory for packages
    install_requires=[                    # Dependencies
        "tensorflow==2.12.0",
        "pandas",
        "dvc",
        "mlflow==2.2.2",
        "notebook",
        "numpy",
        "matplotlib",
        "seaborn",
        "python-box==6.0.2",
        "PyYAML",
        "tqdm",
        "environs==1.0.0",
        "joblib",
        "types-PyYAML",
        "scipy",
        "Flask",
        "Flask-Cors",
        "gdown",
    ],
    python_requires=">=3.8",         # Minimum Python version
)
