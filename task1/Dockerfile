FROM ubuntu:latest

# Update package list and upgrade installed packages
RUN apt-get update && apt-get upgrade -y

# Install Python3 and pip3
RUN apt-get install -y python3 python3-pip

# (Fix) Remove EXTERNALLY-MANAGED if pip install complains
RUN rm -f /usr/lib/python*/EXTERNALLY-MANAGED

# Install Flask via pip3 (not apt)
RUN pip3 install --no-cache-dir flask

# Set working directory
WORKDIR /app

# Copy our Flask app
COPY ./api.py /app/api.py

# Expose the app port inside the container (documentation purpose)
EXPOSE 5252

# Run the Flask app
CMD ["python3", "api.py"]
