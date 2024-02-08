import os
import arcpy
import sys

root_folder = r'..\..\..\data'
for rf in os.walk(root_folder):
    print(rf)

def list_workspaces(root_folder):
    if not os.path.exists(root_folder):
        print(f"The specified root folder '{root_folder}' does not exist.")
        return

    for root, directories, files in os.walk(root_folder):
        for dirpath, dirnames, filenames in os.walk(root_folder):
            print(f"Directory Path: {dirpath}")
            print(f"Sub-directories: {dirnames}")
            print(f"Files: {filenames}")
            for workspace in arcpy.ListWorkspaces("", "ALL", root):
                print(os.path.abspath(workspace))

        


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_folder>")
    else:
        root_folder = sys.argv[1]
        list_workspaces(root_folder)