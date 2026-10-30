
import os
import shutil

path = os.path.expanduser("~/Downloads")

folders = ["Images", "Documents", "Videos", "Audio", "Others"]

for folder in folders:
    os.makedirs(os.path.join(path, folder), exist_ok=True)

for file in os.listdir(path):
    source = os.path.join(path, file)

    if os.path.isfile(source):
        ext = os.path.splitext(file)[1].lower()

        if ext in [".jpg", ".jpeg", ".png"]:
            folder = "Images"
        elif ext in [".pdf", ".txt", ".docx"]:
            folder = "Documents"
        elif ext in [".mp4", ".mkv"]:
            folder = "Videos"
        elif ext in [".mp3", ".wav"]:
            folder = "Audio"
        else:
            folder = "Others"

        destination = os.path.join(path, folder, file)
        shutil.move(source, destination)

print("Downloads organizetion operation was successfully complited !")
