# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
