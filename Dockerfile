# Use Python 3.10+ (for TensorFlow 2.18.0 support)
FROM python:3.10-slim-buster  

# Upgrade pip to the latest version
RUN pip install --upgrade pip  

# Install AWS CLI
RUN apt update -y && apt install awscli -y  

# Set working directory
WORKDIR /app  

# Copy project files
COPY . /app  

# Install all dependencies from requirements.txt  docker
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt  

# Run the application
CMD ["python3", "app.py"]
