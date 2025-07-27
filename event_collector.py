import logging
import threading
import time
import json
from datetime import datetime, timedelta
from collections import deque
from datetime import datetime
import sseclient

straem_url = 'https://stream.wikimedia.org/v2/stream/revision-create'

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
event_buffer = deque()

def consume_events():
    logging.info("📡 Starting Wikipedia event watcher...")
    try:
        client = sseclient.SSEClient(straem_url)
        for event in client:
            if event.event == 'message':
                try:
                    data = json.loads(event.data)
                    timestamp = datetime.strptime(data['meta']['dt'], '%Y-%m-%dT%H:%M:%SZ')
                    data['parsed_time'] = timestamp
                    event_buffer.append(data)

                    # Keep only events from the last 5 minutes
                    cutoff = datetime.utcnow() - timedelta(minutes=5)
                    while event_buffer and event_buffer[0]['parsed_time'] < cutoff:
                        event_buffer.popleft()

                except Exception as e:
                    logging.warning(f"⚠️ Could not parse event: {e}")
    except Exception as e:
        logging.error(f"❌ Error while consuming events: {e}")

if __name__ == "__main__":
    thread = threading.Thread(target=consume_events, daemon=True)
    thread.start()

    logging.info("✅ Event collector started. Leave this running...")
    while True:
        time.sleep(10)
