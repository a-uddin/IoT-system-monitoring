import json
import time
import datetime
import ssl
import psutil
import paho.mqtt.client as mqtt

# Load credentials and settings from config.json
with open("config.json") as f:
    config = json.load(f)

ENDPOINT = config["ENDPOINT"]
PORT = config["PORT"]
TOPIC = config["TOPIC"]
CLIENT_ID = config["CLIENT_ID"]
CA_PATH = config["CA_PATH"]
CERT_PATH = config["CERT_PATH"]
KEY_PATH = config["KEY_PATH"]


# === System Stats Function ===
def get_laptop_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()

    stats = {
         'device_id': CLIENT_ID,
        'cpu_percent': cpu_percent,
        'memory_used': round(memory.used / (1024 ** 3), 2),
        'memory_total': round(memory.total / (1024 ** 3), 2),
        'memory_percent': memory.percent,
        'disk_used': round(disk.used / (1024 ** 3), 2),
        'disk_total': round(disk.total / (1024 ** 3), 2),
        'disk_percent': disk.percent,
        'bytes_sent_MB': round(net.bytes_sent / (1024 ** 2), 2),
        'bytes_recv_MB': round(net.bytes_recv / (1024 ** 2), 2)
    }
    return stats

# === MQTT Setup ===
client = mqtt.Client(client_id=CLIENT_ID)
client.tls_set(ca_certs=CA_PATH,
               certfile=CERT_PATH,
               keyfile=KEY_PATH,
               tls_version=ssl.PROTOCOL_TLSv1_2)

client.connect(ENDPOINT, PORT)
client.loop_start()

# === Publish Stats Every 5 Seconds ===
try:
    while True:
        stats = get_laptop_stats()
        client.publish(TOPIC, json.dumps(stats))
        print("Published:", stats)
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped by user")
    client.loop_stop()
