import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MoveHandler(FileSystemEventHandler):
    # modify the on_modified method
    def on_modified(self, event):
        dirl = os.listdir(pathtowatch)
        for fname in dirl:
            fname1 = fname
            fname2 = fname

            source_folder = pathtowatch + "\\" + fname1
            destination_folder = destination + "\\" + fname2

            file_done = False
            file_size = -1
            while file_size != os.path.getsize(pathtowatch):
                file_size = os.path.getsize(destination)
                time.sleep(1)
            
            while not file_done:
                try:
                    os.rename(source_folder, destination_folder)
                    file_done = True
                except:
                    return True

pathtowatch = "/home/abdul/source"
destination = "/home/abdul/destination"

# creating event handler object.
event_handler = MoveHandler()

#observer
observer = Observer()
observer.schedule(event_handler, pathtowatch, recursive=True)
observer.start()

try:
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    observer.stop()
observer.join()
