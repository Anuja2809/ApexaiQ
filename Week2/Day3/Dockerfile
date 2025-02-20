# Use official Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app files into the container
COPY . /app

# Install Flask inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to access the Flask app
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["python", "app.py"]
