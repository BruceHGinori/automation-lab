"""
Automation Lab
File Organizer
"""

from pathlib import Path


def main():
    print("=== Automation Lab ===")
    print("File Organizer")
    print()

    folder = input("Enter the folder path: ")

    folder_path = Path(folder)

    if folder_path.exists():
        print("\nFolder found!")
    else:
        print("\nFolder not found.")


if __name__ == "__main__":
    main()