import glob
import os


def list_files_in_directory(directory):
    # Ensure the directory path ends with a slash
    if not directory.endswith('/'):
        directory += '/'

    # Use glob to list all files in the directory
    files = glob.glob(directory + '*')

    if files:
        print(f"Files in '{directory}':")
        for file in files:
            if os.path.isfile(file):
                print(os.path.basename(file))
    else:
        print(f"No files found in '{directory}'.")


if __name__ == "__main__":
    # Get the directory from the user
    directory = input("Enter the directory path: ")
    list_files_in_directory(directory)
