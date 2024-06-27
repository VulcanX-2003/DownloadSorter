

import os
import shutil
import platform
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import sys

# Define file types
FILE_TYPES = {
    'Pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
    'Executables': ['.exe', '.bat', '.sh', '.msi'],
    'Music':[".mp3",".wma",".ogg",".wav"],
    'Videos':['.mp4'],
}

# Get OS-specific directories
def get_os_directories():
    downloads_folder = str(Path.home() / 'Downloads')
    pictures_folder = str(Path.home() / 'Pictures')
    documents_folder = str(Path.home() / 'Documents')
    music_folder = str(Path.home()/ 'Music')
    videos_folder = str(Path.home()/ 'Videos')
    

    return downloads_folder, pictures_folder, documents_folder, music_folder, videos_folder

# Event handler for file monitoring
class DownloadHandler(FileSystemEventHandler):
    def __init__(self, sorted_folders):
        self.sorted_folders = sorted_folders

    def on_modified(self, event):
        downloads_folder, pictures_folder, documents_folder,music_folder, videos_folder = self.sorted_folders

        for filename in os.listdir(downloads_folder):
            file_path = os.path.join(downloads_folder, filename)
            if os.path.isdir(file_path):
                continue

            _, file_extension = os.path.splitext(filename)
            destination_folder = None

            for category, extensions in FILE_TYPES.items():
                if file_extension.lower() in extensions:
                    if category == 'Pictures':
                        destination_folder = pictures_folder
                    elif category == 'Documents':
                        destination_folder = documents_folder
                    elif category == 'Music':
                        destination_folder = music_folder
                    elif category == 'Videos':
                        destination_folder = videos_folder
                    break

            if destination_folder:
                destination = os.path.join(destination_folder, filename)
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(destination):
                    destination = os.path.join(destination_folder, f"{base}_{counter}{ext}")
                    counter += 1

                shutil.move(file_path, destination)
                print(f"Moved {filename} to {destination_folder}")

def main():
    downloads_folder, pictures_folder, documents_folder, music_folder, videos_folder,  = get_os_directories()
    event_handler = DownloadHandler((downloads_folder, pictures_folder, documents_folder, music_folder, videos_folder))
    observer = Observer()
    observer.schedule(event_handler, path=downloads_folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
