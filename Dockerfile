# syntax=docker/dockerfile:1

# Use an official Python runtime as a parent image
FROM python:3.12.1-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for PyAudio
RUN apt-get update && apt-get install -y \
    gcc \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variables for Uvicorn
ENV MODULE_NAME=server2
ENV VARIABLE_NAME=app

# Run the application
CMD ["uvicorn", "server2:app", "--host=0.0.0.0", "--port=8000"]