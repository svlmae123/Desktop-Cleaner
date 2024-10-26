import os 
import shutil

def clean_desktop():

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    folders = ["Images", "Documents", "Videos", "Others"]

    for folder in folders:
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        if os.path.isfile(item_path):
            if item.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                shutil.move(item_path, os.path.join(desktop_path, "Images", item))
            elif item.lower().endswith(('.pdf', '.doc', '.docx', '.txt')):
                shutil.move(item_path, os.path.join(desktop_path, "Documents", item))
            elif item.lower().endswith(('.mp4', '.avi', '.mov')):
                shutil.move(item_path, os.path.join(desktop_path, "Videos", item))
            else:
                shutil.move(item_path, os.path.join(desktop_path, "Others", item))
                
clean_desktop()
