import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\Abhishek\Pictures\Screenshots"
destination_dir = r"C:\Users\Abhishek\Desktop\Backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

schedule.every().day.at("18:57").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

print("Scheduled task started...")

while True:
    schedule.run_pending()
    time.sleep(60)
