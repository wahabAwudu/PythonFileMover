import os
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MoveHandler(FileSystemEventHandler):
    # modify the on_modified method
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            source_folder = folder_to_track + "/" + filename
            dest_folder = folder_destination + "/" + filename
            os.rename(source_folder, dest_folder)

folder_to_track = "/mnt/c/Users/abdul/documents/source"
folder_destination = "/mnt/c/Users/abdul/documents/destination"

# creating event handler object.
event_handler = MoveHandler()

#observer
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
