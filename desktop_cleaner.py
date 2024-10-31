import os
import shutil
import tkinter as tk
from tkinter import messagebox, simpledialog
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='desktop_cleaner.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clean_desktop(file_types):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folders = ["Images", "Documents", "Videos", "Others"]

    for folder in folders:
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        if os.path.isfile(item_path):
            moved = False
            for folder, types in file_types.items():
                if item.lower().endswith(types):
                    target_path = os.path.join(desktop_path, folder, item)
                    try:
                        shutil.move(item_path, target_path)
                        logging.info(f"Moved '{item}' to '{folder}' folder")
                    except Exception as e:
                        logging.error(f"Failed to move '{item}' to '{folder}' folder: {e}")
                    moved = True
                    break
            if not moved:
                target_path = os.path.join(desktop_path, "Others", item)
                try:
                    shutil.move(item_path, target_path)
                    logging.info(f"Moved '{item}' to 'Others' folder")
                except Exception as e:
                    logging.error(f"Failed to move '{item}' to 'Others' folder: {e}")

def get_file_types():
    file_types = {
        "Images": ('.png', '.jpg', '.jpeg', '.gif'),
        "Documents": ('.pdf', '.doc', '.docx', '.txt'),
        "Videos": ('.mp4', '.avi', '.mov'),
    }

    for folder in file_types.keys():
        user_input = simpledialog.askstring("Customize File Types",
                                             f"Enter file types for {folder} (comma-separated):",
                                             initialvalue=', '.join(file_types[folder]))
        if user_input:
            file_types[folder] = tuple(ext.strip() for ext in user_input.split(','))
    
    return file_types

def run_cleanup():
    file_types = get_file_types()
    clean_desktop(file_types)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messagebox.showinfo("Cleanup Complete", f"Your desktop has been cleaned!\nCompleted on: {timestamp}")

# Create the main application window
root = tk.Tk()
root.title("Desktop Cleaner")
root.geometry("400x200")
root.configure(bg="#f0f0f0")  # Light gray background

# Add a frame for better organization
frame = tk.Frame(root, bg="#ffffff", bd=5, relief=tk.RAISED)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

title_label = tk.Label(frame, text="Desktop Cleaner", font=("Helvetica", 18, "bold"), bg="#ffffff")
title_label.pack(pady=10)

cleanup_button = tk.Button(frame, text="Clean Desktop", command=run_cleanup, font=("Helvetica", 14), bg="#4CAF50", fg="white")
cleanup_button.pack(pady=20, padx=20)

# Start the GUI event loop
root.mainloop()
