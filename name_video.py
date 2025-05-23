import os
from datetime import datetime
from pathlib import Path

# Configuration
folder = Path("/Users/yiyuanhan/Library/CloudStorage/Box-Box/DBS Pain/Chronic Pain - Activa and Summit 2.0 - ePHI/PATIENT DATA - ePHI/RCS08/Video/")  # Change this to your video folder
rcs_id = "RCS08"                       # Set your RCSxx variable

# Get today's date string in YYMMDD
today = datetime.now().strftime("%y%m%d")

# Video file extensions to match
video_exts = {".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"}

# Gather today's video files and sort by creation time
videos_today = []
for file in folder.iterdir():
    if file.suffix.lower() in video_exts and file.is_file():
        # Use .stat().st_ctime for creation time (platform dependent)
        created = datetime.fromtimestamp(file.stat().st_ctime)
        if created.strftime("%y%m%d") == today:
            videos_today.append((file, created))

# Sort videos by creation time
videos_today.sort(key=lambda x: x[1])

# Rename videos according to your scheme
for idx, (file, created) in enumerate(videos_today, 1):
    no_str = f"{idx:02d}"
    new_name = f"{rcs_id}_{today}_{no_str}{file.suffix.lower()}"
    new_path = file.parent / new_name
    print(f"Renaming: {file.name} → {new_name}")
    file.rename(new_path)