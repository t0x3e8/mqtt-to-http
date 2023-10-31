import paho.mqtt.client as mqtt
import requests
import logging
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

MQTT_BROKER_ADDRESS = os.getenv("MQTT_BROKER_ADDRESS")
MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC")
DEST_URL = os.getenv("DEST_URL")

# Set up logging
logging.basicConfig(level=logging.INFO)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected to MQTT Broker with result code " + str(rc))
        client.subscribe(MQTT_TOPIC)  # Subscribe to the MQTT topic of interest
    else:
        logging.error("Connection to MQTT Broker failed with result code " + str(rc))

def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    logging.info("Received message: " + message)

    if "ON" in message:
        try:
            # Make the HTTP POST request using requests
            data = {"message": message}
            response = requests.post(DEST_URL, data=data)

            if response.status_code == 200:
                logging.info("HTTP POST request successful.")
            else:
                logging.error(f"HTTP POST request failed with status code {response.status_code}")
        except Exception as e:
            logging.error("Error making HTTP POST request: " + str(e))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER_ADDRESS, MQTT_BROKER_PORT, 60)

client.loop_forever()
