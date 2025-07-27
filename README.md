# 📊 Wikipedia Watching

This project listens to live edit events from Wikipedia using their EventStream API and generates a summary report every 5 minutes showing how many edits occurred per domain (e.g., en.wikipedia.org, fr.wikipedia.org) and how many were made by logged-in vs anonymous users.

---

## 📁 Project Structure

WikipediaWatching/
│
├── event_collector.py # Collects real-time events and triggers report
├── report_generator.py # Generates domain-wise edit reports
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Requirements

- Python 3.8 or above
- Internet connection (to access the Wikipedia EventStream)

---

## 📦 Setup Instructions

1. **Clone or Download the Project Folder**
   - You can manually create a folder named `WikipediaWatching` and paste all files inside it.
   - Alternatively, use Git to clone (optional if you don't know Git):
   
     git clone https://github.com/your-username/WikipediaWatching.git
     cd WikipediaWatching
     ```

2. **Create and Activate a Virtual Environment**  
   *(Recommended but optional)*

   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

## Install Required Packages

pip install -r requirements.txt

## ▶️ How to Run the Project
Just run the main file event_collector.py — it will automatically handle event collection and report generation.

python event_collector.py
Leave it running. It will:

Continuously collect real-time edit events.

Every 1 minute, update the event buffer.

Every 5 minutes, generate a domain-based report in your terminal.

🐍 Python Dependencies
Listed in requirements.txt:

requests
sseclient-py
Install with:
pip install -r requirements.txt
