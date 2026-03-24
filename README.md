# RCB Ticket Alert Bot

Dear RCB fans, we all know how frustrating it is to sit and refresh the page constantly, waiting for tickets to go live. This bot monitors ticket and merchandise pages for you and sends instant email alerts when tickets are available, so you don’t have to stay glued to your monitor!

---

## 🚀 Features

- Monitors multiple URLs
- Detects ticket availability changes
- Sends instant email alerts
- Runs continuously with minimal delay

---

## 🛠️ Requirements

- Python 3.8+
- Playwright
- Gmail account (with App Password)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rcb-ticket-alert-bot.git
cd rcb-ticket-alert-bot
````
2. Install dependencies
 ```bash
pip install playwright
playwright install
````

3.🔐 Gmail App Password Setup (IMPORTANT)

Google blocks normal passwords for scripts, so you need an App Password.

Steps to Generate App Password:
Go to your Google Account Security
 page.
Enable 2-Step Verification if not already enabled.
Scroll down to App Passwords and click it.
In Select App, choose Mail.
In Select Device, choose Other (Custom name) and enter e.g., "RCB Bot".
Click Generate.
Copy the 16-character password provided (this is what you use in the script).

⚙️ Configuration

Open the script (main.py) and update:

EMAIL = "your_email@gmail.com"
PASSWORD = "your_16_char_app_password"
TO_EMAILS = ["receiver1@gmail.com", "receiver2@gmail.com"]


4.▶️ Run the Script

```bash
python main.py
````

How It Works
Continuously checks ticket pages
Detects changes such as:
Removal of "Tickets not available"
Presence of booking-related keywords
Sends an email alert immediately when tickets appear
Stops automatically after detection
