import schedule
import time
import subprocess
from datetime import datetime

def run_main():
    print(f"\n=== Run at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    subprocess.run(["python3", "main.py"])

# Schedule the job to run every 6 hours
schedule.every(6).hours.do(run_main)

while True:
    schedule.run_pending()
    time.sleep(60)
