#
# First Flask App Dockerfile
#
#

# Pull base image.
FROM centos:7.0.1406

# Build commands
# Use an official Python runtime as a parent image
FROM python:2.7-slim


# Set the working directory to /app
WORKDIR /opt/flask_blog

# Copy the current directory contents into the container at /app
ADD . /opt/flask_blog

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
