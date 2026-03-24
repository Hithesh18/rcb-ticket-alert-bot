from playwright.sync_api import sync_playwright
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = "from@gmail.com"
PASSWORD = "your_app_password"
TO_EMAILS = ["test2@gmail.com", "test1@gmail.com", "dummy@gmail.com", "test@gmail.com"]

URLS = [
    "https://shop.royalchallengers.com/ticket",
    "https://shop.royalchallengers.com/merchandise"
]

def send_email(subject, body):
    for to_email in TO_EMAILS:
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL, PASSWORD)
                server.sendmail(EMAIL, to_email, msg.as_string())
                print(f"Email sent to {to_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        viewport={'width': 1920, 'height': 1080}
    )
    page = context.new_page()

    print("Monitoring pages...")

    while True:
        for url in URLS:
            try:
                page.goto(url, wait_until="networkidle", timeout=60000)
                page.wait_for_selector("body", timeout=10000)
                time.sleep(2)

                page_text = page.inner_text("body")

                print(f"Checking {url}...")

                if "ticket" in url:
                    if "Tickets not available" not in page_text:
                        if len(page_text) > 200:
                            print(f"Change detected on {url}")
                            send_email("RCB TICKETS ALERT", f"Tickets may be available: {url}")
                            browser.close()
                            exit()
                        else:
                            print("Page too short, skipping")
                    else:
                        print("Tickets not available")

                elif "Book" in page_text or "TICKETS AVAILABLE" in page_text.upper():
                    print(f"Booking keyword found on {url}")
                    send_email("RCB TICKETS ALERT", f"Booking detected: {url}")
                    browser.close()
                    exit()

            except Exception:
                print(f"Error on {url}")

        print("Waiting 1 second...")
        time.sleep(1)
