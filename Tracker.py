import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Hp/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print("Hey{event.src_path} has been created")
    def on_deleted(self, event):
        print("Opps,Someone Deleated{event.src_path}!")  
    def on_modified(self, event):
        print("Someone{event.src_path}has been Modified")
    def on_moved(self, event):
        print("{event.src_path}has been moved")    

    event_handler = FileSystemEventHandler()

    observer = Observer()

    observer.schedule(event_handler, from_dir,recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(2)
            print("running...")

    except KeyboardInterrupt:
        print("stopped!")
        observer.stop()


