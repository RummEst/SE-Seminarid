import os
import time

def create_project_folder():
    # Ask for the project name
    project_name = input("Enter the project name (leave empty for timestamp): ").strip()

    # Use current timestamp if project name is empty
    if not project_name:
        project_name = time.strftime("%Y%m%d_%H%M%S")

    # Create the project directory
    try:
        os.makedirs(project_name)
        print(f"Folder '{project_name}' created.")
    except FileExistsError:
        print(f"Folder '{project_name}' already exists.")
        return

    # List of files to create
    files_to_create = ["script.js", "styles.css", "index.html", f"{project_name}.html"]

    # Create each file in the project directory
    for file_name in files_to_create:
        file_path = os.path.join(project_name, file_name)
        with open(file_path, 'w') as file:
            pass  # Create an empty file
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_project_folder()
