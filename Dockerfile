# Use Alpine Linux as the base image
FROM alpine:latest

# Update the package repository and install Python and pip
RUN apk --no-cache add python3 py3-pip

# Install the paho-mqttm, requests, python_dotenv libraries
RUN pip3 install paho-mqtt
RUN pip3 install requests
RUN pip3 install python_dotenv

# Copy your Python script (mqtt-2-http.py) into the container
COPY mqtt-2-http.py /app/mqtt-2-http.py

# Set the working directory
WORKDIR /app

# Run your Python script when the container starts
CMD ["python3", "mqtt-2-http.py"]