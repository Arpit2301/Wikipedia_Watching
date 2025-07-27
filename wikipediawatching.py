import sseclient
import logging
import json
import time
from datetime import datetime

# Use the misspelled variable name as per instruction
straem_url = "https://stream.wikimedia.org/v2/stream/revision-create"

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def consume_events(duration_seconds=60):
    start_time = time.time()
    events = []

    try:
        logging.info(f"⏳ Connecting to Wikipedia Event Stream for {duration_seconds} seconds...")

        # Connect directly using URL string (sseclient handles internals)
        client = sseclient.SSEClient(straem_url)

        for event in client:
            if time.time() - start_time > duration_seconds:
                break
            if event.event == "message":
                try:
                    data = json.loads(event.data)
                    events.append(data)
                    logging.info(f"📌 Title: {data.get('page_title')} | User: {data.get('user')} | Domain: {data.get('meta', {}).get('domain')}")
                except json.JSONDecodeError:
                    logging.warning("⚠️ Skipped invalid JSON event.")

    except Exception as e:
        logging.error(f"❌ Error while consuming events: {e}")

    return events

def generate_report(events):
    if not events:
        logging.warning("⚠️ No events to report.")
        return

    domain_count = {}
    user_count = {}

    for event in events:
        domain = event.get('meta', {}).get('domain', 'unknown')
        user = event.get('user', 'anonymous')

        domain_count[domain] = domain_count.get(domain, 0) + 1
        user_count[user] = user_count.get(user, 0) + 1

    logging.info("\n🧾 Summary Report")
    logging.info("-" * 30)
    logging.info("Top Domains:")
    for domain, count in sorted(domain_count.items(), key=lambda x: x[1], reverse=True):
        logging.info(f"{domain}: {count} changes")

    logging.info("\nTop Users:")
    for user, count in sorted(user_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        logging.info(f"{user}: {count} changes")

if __name__ == "__main__":
    logging.info("📡 Starting Wikipedia event watcher...")
    events = consume_events(duration_seconds=60)
    generate_report(events)
