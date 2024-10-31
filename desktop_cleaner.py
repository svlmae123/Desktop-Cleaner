import os
import shutil
import tkinter as tk
from tkinter import messagebox, simpledialog

def clean_desktop(file_types):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folders = ["Images", "Documents", "Videos", "Others"]

    # Create folders if they don't exist
    for folder in folders:
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files based on the user's custom file types
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        if os.path.isfile(item_path):
            moved = False
            for folder, types in file_types.items():
                if item.lower().endswith(types):
                    shutil.move(item_path, os.path.join(desktop_path, folder, item))
                    moved = True
                    break
            # If the file type does not match any folder, move it to 'Others'
            if not moved:
                shutil.move(item_path, os.path.join(desktop_path, "Others", item))

def get_file_types():
    file_types = {
        "Images": ('.png', '.jpg', '.jpeg', '.gif'),
        "Documents": ('.pdf', '.doc', '.docx', '.txt'),
        "Videos": ('.mp4', '.avi', '.mov'),
    }

    # Allow users to customize file types
    for folder in file_types.keys():
        user_input = simpledialog.askstring("Customize File Types",
                                             f"Enter file types for {folder} (comma-separated):",
                                             initialvalue=', '.join(file_types[folder]))
        if user_input:
            # Update the file types for the folder
            file_types[folder] = tuple(ext.strip() for ext in user_input.split(','))
    
    return file_types

# GUI code starts here
def run_cleanup():
    file_types = get_file_types()  # Get custom file types from the user
    clean_desktop(file_types)  # Call your existing cleanup function
    messagebox.showinfo("Cleanup Complete", "Your desktop has been cleaned!")

# Create the main application window
root = tk.Tk()
root.title("Desktop Cleaner")
root.geometry("300x150")  # Set the size of the window

# Add a button to run the cleanup
cleanup_button = tk.Button(root, text="Clean Desktop", command=run_cleanup)
cleanup_button.pack(pady=20)  # Add some padding for better layout

# Start the GUI event loop
root.mainloop()
