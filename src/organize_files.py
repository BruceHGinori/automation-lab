"""
Automation Lab
File Organizer
"""

from pathlib import Path

def get_files(folder_path):
    files = []

    for item in folder_path.iterdir():
        if item.is_file():
            files.append(item)

    return files

def main():
    print("=== Automation Lab ===")
    print("File Organizer")
    print()

    folder = input("Enter the folder path: ")

    folder_path = Path(folder)

    if not folder_path.exists():
        print("\nPath not found.")
        return

    if not folder_path.is_dir():
        print("\nThe specified path is not a directory.")
        return

    print("\nFolder found!")
    print("\nContents:")

    files = get_files(folder_path)

    for file in files:
        print(file.name)


if __name__ == "__main__":
    main()