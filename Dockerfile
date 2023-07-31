# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the container's working directory
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask app will run (change if needed)
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["python", "app.py"]
