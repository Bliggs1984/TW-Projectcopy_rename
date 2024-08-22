import sys
import os
import shutil
import tkinter as tk
from tkinter import filedialog

def find_project_folders(root_folder):
    project_folders = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if "01 PROJECTS" in dirnames:
            project_folders.append({
                'project': os.path.basename(dirpath),
                'folder': os.path.join(dirpath, "01 PROJECTS")
            })
    return project_folders

def copy_and_rename(source_file, project_folders):
    filename = os.path.basename(source_file)
    file_extension = os.path.splitext(filename)[1]
    
    for project in project_folders:
        new_filename = f"{project['project']}{file_extension}"
        dest_path = os.path.join(project['folder'], new_filename)
        shutil.copy2(source_file, dest_path)
        print(f"Copied and renamed {filename} to {dest_path}")

def select_root_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Select the root folder containing project folders")
    root.destroy()
    return folder_path

try:
    print("Script started.")
    
    # Prompt user to select root folder
    root_folder = select_root_folder()

    if not root_folder:
        print("No folder selected. Exiting.")
        sys.exit(1)

    print(f"Selected root folder: {root_folder}")

    # Find all "01 PROJECTS" folders
    project_folders = find_project_folders(root_folder)

    if not project_folders:
        print("No '01 PROJECTS' folders found.")
        sys.exit(1)

    print(f"Found {len(project_folders)} '01 PROJECTS' folders.")

    # Get the list of files dragged onto the script
    files = sys.argv[1:]

    if not files:
        print("No files were dragged onto the script.")
        sys.exit(1)

    print(f"Files to process: {files}")

    # Process each file
    for file in files:
        copy_and_rename(file, project_folders)

    print("Script completed successfully.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
    import traceback
    traceback.print_exc()

input("Press Enter to exit...")