# Use an official Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies from requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install gunicorn
RUN pip install --no-cache-dir gunicorn

# Copy the rest of the Django project files into the container
COPY . .

# Start the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "peers.wsgi:application"]
