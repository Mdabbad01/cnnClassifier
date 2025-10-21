# Use lightweight Python image
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy only requirements first (faster caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary project files
COPY app.py .
COPY src/ ./src/
COPY templates/ ./templates/
COPY artifacts/training/model.h5 ./artifacts/training/model.h5

# Expose port
EXPOSE 8080

# Run the Flask app
CMD ["python3", "app.py"]
