# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

RUN apt-get update -y

RUN apt-get install libpq-dev -y

RUN pip install --upgrade pip

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY ./app /app

# Set environment variables
ENV PYTHONUNBUFFERED=1

EXPOSE 5050

# Command to run the FastAPI application
CMD ["python","main.py"]
