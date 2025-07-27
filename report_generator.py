import time
from datetime import datetime, timedelta
from event_collector import event_buffer
from collections import Counter
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_report():
    while True:
        time.sleep(60)
        cutoff = datetime.utcnow() - timedelta(minutes=5)
        recent_events = [e for e in event_buffer if e['parsed_time'] >= cutoff]

        if not recent_events:
            logging.info("⚠️ No events in the last 5 minutes.")
            continue

        domain_counter = Counter()
        user_counter = Counter()

        for event in recent_events:
            domain_counter[event['meta']['domain']] += 1
            user_counter[event['user']] += 1

        top_domains = domain_counter.most_common(5)
        top_users = user_counter.most_common(5)

        print("\n📰 Report for Last 5 Minutes")
        print("📌 Top 5 Domains:")
        for domain, count in top_domains:
            print(f"   - {domain}: {count} edits")

        print("👤 Top 5 Users:")
        for user, count in top_users:
            print(f"   - {user}: {count} edits")
        print("-" * 40)

if __name__ == "__main__":
    logging.info("📊 Starting 5-minute rolling report generator...")
    generate_report()
