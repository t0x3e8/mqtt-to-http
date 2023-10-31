# MQTT to HTTP

This repository contains a Python script that acts as a bridge, forwarding MQTT messages to an HTTP endpoint. Originally, it served as a bridge between MQTT and Ntfy, but it has since been expanded to support all HTTP endpoints. It's designed to be run within a Docker container.

## Usage
To use this script, follow these steps:
1. Clone the repository to your local machine:
```bash
git clone https://github.com/t0x3e8/mqtt-to-http.git
```
2. Create an `.env` file in the project directory with your configuration settings. Use the provided `.env.example` as a template and replace the placeholder values with your specific settings.
3. Build the Docker image:
```bash 
docker build -t mqtt-to-http .
```
4. Run the Docker container:
```bash
docker run -v /home/user/docker/mqtt-to-http/.env:/app/.env mqtt-to-http
```
*Replace /home/user/docker/mqtt-to-http/.env with the actual absolute path to your .env file.*

## Configuration
You can customize the following settings in the .env file:

* `MQTT_BROKER_ADDRESS`: The MQTT broker's address.
* `MQTT_BROKER_PORT`: The MQTT broker's port (e.g., 1883).
* `MQTT_TOPIC`: The MQTT topic you want to subscribe to.
* `DEST_URL`: The HTTP endpoint where MQTT messages will be forwarded.

## Dockerfile
The `Dockerfile` included in this repository sets up a lightweight Alpine Linux environment, installs Python, and installs the necessary Python libraries for the script to run. It also copies your Python script and `.env` file into the Docker container. To build and run the Docker container, follow the steps outlined in the "Usage" section above.

## License
This project is licensed under the MIT License.
