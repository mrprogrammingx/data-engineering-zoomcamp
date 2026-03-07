# Use an official Python runtime as a parent image
FROM python:3.13

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .
COPY run.sh /run.sh

# Ensure the script is executable inside the container
RUN chmod +x /run.sh

# Expose the Flask port
EXPOSE 5000

# Define the command to run the application
ENTRYPOINT ["/run.sh"]