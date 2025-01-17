import schedule
import time
from app import run_scraper

# Schedule scraper to run daily at 6:00 AM
schedule.every().day.at("06:00").do(run_scraper)

print("Scheduler started. Press Ctrl+C to exit.")

while True:
    schedule.run_pending()
    time.sleep(1)