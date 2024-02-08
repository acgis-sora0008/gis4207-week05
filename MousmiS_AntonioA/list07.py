import os
import arcpy
import sys


root_folder = r'..\..\..\data'

def list_feature_classes(workspace):
    arcpy.env.workspace = workspace
    feature_classes = arcpy.ListFeatureClasses()
    for fc in feature_classes:
        print(os.path.abspath(fc))

def list_workspaces(root_folder):
    if not os.path.exists(root_folder):
        print(f"The specified root folder '{root_folder}' does not exist.")
        return

    for root, _, _ in os.walk(root_folder):
        workspaces = arcpy.ListWorkspaces("", "ALL", root)
        for workspace in workspaces:
            print(os.path.abspath(workspace))
            list_feature_classes(workspace)
def main():
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python script.py <root_folder>")
        else:
            root_folder = sys.argv[1]
            list_workspaces(root_folder)
        
main()     