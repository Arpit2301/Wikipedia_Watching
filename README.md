# 📡 Wikipedia Watching

This project connects to Wikipedia’s live event stream and watches for edit activity happening across different language domains (like English `en`, Hindi `hi`, French `fr`, etc.). It collects events every minute and generates user activity reports every 5 minutes.

---

## ✅ Project Overview

This tool performs two main tasks:

1. **Collects Wikipedia Edit Events**  
   - Every **1 minute**, it listens to Wikipedia’s live stream and stores recent edit events in a file.

2. **Generates Reports**  
   - Every **5 minutes**, it processes the collected events to generate a summary report.
   - The report shows **how many edits each user made**, grouped by domain.

You only need to run **one Python script**. Everything runs automatically in the background.

---

## 🗂 Folder & File Structure
WikipediaWatching/
├── event_collector.py       # Main file - runs the full program
├── report_generator.py      # (Used internally) Generates the user edit report
├── requirements.txt         # Python dependencies
├── README.md                # You're reading this :)
├── logs/                    # Stores log files (auto-created)
├── data/                    # Stores event and report JSON files (auto-created)

---

## ⚙️ Setup Instructions

### 1. Clone or Create Project Folder

You can name your folder `WikipediaWatching`.

### 2. Add These Files to It:
- `event_collector.py`
- `report_generator.py`
- `requirements.txt`
- `README.md` (this file)

### 3. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
4. Activate Virtual Environment
On Windows:

bash
Copy
Edit
venv\Scripts\activate
On Mac/Linux:

bash
Copy
Edit
source venv/bin/activate
5. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
▶️ How to Run the Program
Just run the main script:

bash
Copy
Edit
python event_collector.py
Let it run in the terminal. It will:

Fetch Wikipedia events every 1 minute

Generate a report every 5 minutes

You’ll see log messages in the terminal and in the logs/ folder.

📦 Output Files
All data is saved automatically in the data/ folder:

Raw Event Data:
Saved every 1 minute as:
events_YYYY-MM-DD_HH-MM.json

Report Data:
Saved every 5 minutes as:
report_YYYY-MM-DD_HH-MM.json
It contains:

Domain (en, hi, etc.)

Users and their edit count

## 👨‍💻 Author

Made with 💻 and ☕ by **Arpit Gupta**

- 🐙 GitHub: [github.com/Arpit2301](https://github.com/Arpit2301)  
- 💼 LinkedIn: [linkedin.com/in/arpit-gupta-081b68227](https://www.linkedin.com/in/arpit-gupta-081b68227)
