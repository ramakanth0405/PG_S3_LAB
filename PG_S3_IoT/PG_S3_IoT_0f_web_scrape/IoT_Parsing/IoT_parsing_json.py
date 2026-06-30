import json

raw_json_payload = '{"sensor_id": "DHT22_01", "metrics": {"temp": 26.4, "humidity": 55}}'

data = json.loads(raw_json_payload)

print(f"Device_ID: {data['sensor_id']}")
print(f"Current_Temperature: {data['metrics']['temp']} °C")

processed_data = {
    "gateway_id": "GW_MSc_01",
    "status": "ONLINE",
    "active_alerts": False
}

# Convert the dictionary into a raw text string for network transmission
string_to_send = json.dumps(processed_data)
print(f"Ready to transmit payload stream: {string_to_send}")