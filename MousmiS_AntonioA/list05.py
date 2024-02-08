import sys
import os

root_folder = r'..\..\..\data'
for rf in os.walk(root_folder):
    print(rf)
    
def main():
    global root_folder
    """Main function to list all folders and sub-folders under the provided root folder."""
    if len(sys.argv) != 2:
        print("Usage: python list05.py <root_folder>")
        sys.exit()

    root_folder = sys.argv[1]
    if not os.path.exists(root_folder):
        print(f"{root_folder} does not exist.")
        sys.exit()
        
    list_folders(root_folder)     
    

def list_folders(root_folder):
    """Lists all folders and sub-folders under the provided root folder."""
    print("Folders and Sub-folders:")
    for dirpath, dirnames, filenames in os.walk(root_folder):
        print(f"Directory Path: {dirpath}")
        print(f"Sub-directories: {dirnames}")
        print(f"Files: {filenames}")
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))
       

if __name__ == "__main__":
    main()