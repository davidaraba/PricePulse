import schedule
import time
import subprocess

def run_main():
    subprocess.run(["python3", "main.py"])  

# Schedule the job
schedule.every(30).seconds.do(run_main) 

while True:
    schedule.run_pending()
    time.sleep(60)