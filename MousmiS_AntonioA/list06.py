import os
import sys

def main():
    global arcpy; os; sys
    global root_folder


    if len(sys.argv) != 2:
        print('Usage: list06.py <root folder> ')
        sys.exit()
    import arcpy

    root_folder = sys.argv[1]
    if not os.path.exists(root_folder):
        print(f"{root_folder} does not exist.")
        sys.exit()

    list_workspaces(root_folder)



def list_workspaces(root_folder):
    if not os.path.exists(root_folder):
        print(f"The specified root folder '{root_folder}' does not exist.")
        return

    for root, directories, files in os.walk(root_folder):
        for dirpath, dirnames, filenames in os.walk(root_folder):
            print(f"Directory Path: {dirpath}")
            print(f"Sub-directories: {dirnames}")
            print(f"Files: {filenames}")
            workspaces = arcpy.ListWorkspaces("", "ALL")
            if workspaces is not None:
                for workspace in workspaces:
                    print(os.path.abspath(workspace))
            else:
                print("No workspaces found.")


        


if __name__ == "__main__":
    main()