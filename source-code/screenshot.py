import pyautogui
import time
import os
import hashlib
import schedule
from datetime import datetime

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Screenshot folder
save_folder = os.path.join(BASE_DIR, "Screenshots")
os.makedirs(save_folder, exist_ok=True)

# Logs folder
logs_folder = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_folder, exist_ok=True)

# Log file path
log_filename = f"upload_log_{datetime.today().strftime('%Y-%m-%d')}.txt"
log_path = os.path.join(logs_folder, log_filename)

#  Google Drive Authentication
gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)

#  Create or find date-based folder in Drive
def get_or_create_drive_folder(folder_name):
    query = f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    folder_list = drive.ListFile({'q': query}).GetList()

    if folder_list:
        return folder_list[0]['id']
    else:
        folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        return folder['id']

#  Compute SHA-256 hash
def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
    
# upload_log_file
def upload_log_file(log_path, folder_id):
    log_filename = os.path.basename(log_path)

    try:
        #  Search for existing log file in the folder
        query = f"'{folder_id}' in parents and title='{log_filename}' and trashed=false"
        existing_files = drive.ListFile({'q': query}).GetList()

        #  If found, delete it
        if existing_files:
            for file in existing_files:
                file.Delete()
            print(f" Existing log file replaced: {log_filename}")

        #  Upload fresh log file
        log_file = drive.CreateFile({'title': log_filename, 'parents': [{'id': folder_id}]})
        log_file.SetContentFile(log_path)
        log_file.Upload()
        print(f" Daily log file uploaded: {log_filename}")

    except Exception as e:
        print(f" Log upload failed: {e}")

#  Screenshot + Upload + Log
def take_screenshot():
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    filename = f"screenshot_{timestamp}.png"
    screenshot_path = os.path.join(save_folder, filename)

    # Capture screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    print(f" Screenshot saved: {screenshot_path}")

    # Hash the screenshot
    file_hash = hash_file(screenshot_path)

    # Create or find Drive folder for today
    global folder_id
    folder_name = datetime.today().strftime('%Y-%m-%d')
    folder_id = get_or_create_drive_folder(folder_name)

    # Upload to Drive
    try:
        upload_file = drive.CreateFile({'title': filename, 'parents': [{'id': folder_id}]})
        upload_file.SetContentFile(screenshot_path)
        upload_file.Upload()
        print(f" Uploaded to Drive folder '{folder_name}': {filename}")

        # Log the event
        with open(log_path, "a", encoding="utf-8") as log:
            log.write(f"{timestamp} | {filename} | SHA-256: {file_hash}\n")

    except Exception as e:
        print(f" Upload failed: {e}")



#  Schedule every 20 seconds
schedule.every(5).seconds.do(take_screenshot)

#  Run loop
try:
    print(" Screenshot logger started. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\n Logger stopped manually.")
    upload_log_file(log_path, folder_id)


