# Use an official Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install --no-cache-dir gunicorn

# Copy the rest of the Django project files into the container
COPY . .

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

