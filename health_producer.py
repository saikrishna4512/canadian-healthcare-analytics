import asyncio
import json
import time
import random
import os
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

CONNECTION_STRING = os.environ.get("EVENT_HUB_CONNECTION_STRING")

EVENT_HUB_NAME = "health-data-stream"

async def send_health_data():
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STRING,
        eventhub_name=EVENT_HUB_NAME
    )

    async with producer:
        cities = ["Vancouver", "Toronto", "Calgary", "Winnipeg", "Halifax"]

        while True:
            event_data_batch = await producer.create_batch()

            health_record = {
                "city": random.choice(cities),
                "hospital_id": f"H{random.randint(1, 50):03d}",
                "wait_time_hours": round(random.uniform(1, 24), 2),
                "patients_waiting": random.randint(10, 200),
                "timestamp": time.time(),
                "source": "healthcare_simulation"
            }

            event_data_batch.add(EventData(json.dumps(health_record)))
            await producer.send_batch(event_data_batch)
            print(f"Sent: {health_record}")
            await asyncio.sleep(5)

asyncio.run(send_health_data())