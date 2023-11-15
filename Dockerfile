# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /


# Copy the current directory contents into the container at the working directory
COPY . .


# Define the command to run the application
CMD ["pytest", "test_sparse_recomemnder.py"]
