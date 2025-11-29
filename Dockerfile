# Use official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your ML pipeline script
COPY ml_pipeline.py .

# Default command: run your ML pipeline
CMD ["python", "ml_pipeline.py"]