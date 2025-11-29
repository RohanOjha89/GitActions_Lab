## GitActions ML Pipeline – CI/CD with GitHub Actions & Docker

This repository demonstrates a complete CI/CD pipeline for a simple Machine Learning workflow using GitHub Actions and Docker.
The project shows how to:
- Automate testing and validation (CI)
- Build and publish a Docker image (CD)
- Run an ML training pipeline inside a reproducible container
- Use development and main branches in a real DevOps workflow

### Project Overview
This project is a minimal ML workflow that:
- Loads the California Housing dataset
- Splits data into train/test
- Trains a Random Forest Regressor
- Evaluates using Mean Squared Error (MSE)
- Prints results to the console
All of this is packaged inside a Docker container, automatically built and pushed by GitHub Actions.

### Repository Structure
```bash
GitActions_Lab/
│
├── ml_pipeline.py                 # ML training pipeline
├── requirements.txt               # Dependencies
├── Dockerfile                     # Docker image definition
│
├── tests/
│   ├── test_pipeline_pytest.py    # Pytest-based test
│   ├── test_pipeline_unittest.py  # unittest-based test
│
└── .github/
    └── workflows/
        └── ci.yml                 # CI/CD pipeline (GitHub Actions)
```

### CI/CD Workflow
**Continuous Integration (CI)**
Runs on:
- Pushes to dev
- Pull Requests targeting main

It includes:
- Install Python & dependencies
- Run pytest tests
- Run unittest tests
- Run the ML pipeline (ml_pipeline.py) as a smoke test
This ensures that code changes are validated before they reach the main branch.

**Continuous Delivery (CD)**
Runs only on pushes to main.
After CI passes:
- GitHub Actions logs in to Docker Hub
- Builds the Docker image defined in Dockerfile
- Pushes it automatically to your Docker Hub repo
    -- **rohanojha89/gitactions-lab:latest**
This gives you a fully automated build-and-push pipeline.

### Docker Image: What It Contains
The Docker image includes:
- Python 3.11 runtime
- All dependencies (requirements.txt)
- Your ML pipeline (ml_pipeline.py)
- A default command to run the pipeline when the container starts
Anyone can run your entire ML pipeline without installing Python or any dependencies.

### Running the ML Pipeline via Docker
Anyone with Docker installed can execute the ML training script:
**Pull the image:**
    -- docker pull rohanojha89/gitactions-lab:latest
**Run it:**
    -- docker run --rm rohanojha89/gitactions-lab:latest

This will:
- Launch a fresh container
- Run ml_pipeline.py
- Train the Random Forest model
- Output the MSE score
No Python setup. No dependencies. No repo cloning.

### Secrets & CD Setup
The CD workflow expects two GitHub Actions secrets:
**DOCKERHUB_USERNAME**
**DOCKERHUB_TOKEN**
A Docker Hub Access Token with read/write permissions.