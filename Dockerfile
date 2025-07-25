# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
#COPY requirements.txt .

# Install dependencies
COPY . .
RUN pip install --no-cache-dir -r app/requirements.txt

#COPY . .

RUN ls -al /app

RUN python3 app/init_soil_data_db.py && python3 app/init_users.py

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app/app.py"]
