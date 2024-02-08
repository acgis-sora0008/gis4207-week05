import os
import arcpy
import sys

root_folder = r'..\..\..\data'

def list_feature_classes(root_folder, datatype, out_file_name):
    if not os.path.exists(root_folder):
        print(f"The specified root folder '{root_folder}' does not exist.")
        return

    if datatype not in ["Point", "Polyline", "Polygon"]:
        print("The second argument must be 'Point', 'Polyline', or 'Polygon'.")
        return

    with open(out_file_name, "w") as outfile:
        outfile.write(f"{datatype} feature classes in and below {root_folder}\n")

        for dirpath, dirnames, filenames in arcpy.da.Walk(root_folder, datatype):
            for filename in filenames:
                outfile.write(os.path.abspath(os.path.join(dirpath, filename)) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <root_folder> <Point|Polyline|Polygon> <out_file_name>")
    else:
        root_folder = sys.argv[1]
        datatype = sys.argv[2]
        out_file_name = sys.argv[3]
        list_feature_classes(root_folder, datatype, out_file_name)