import arcpy
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
workspace = os.path.join(script_dir, '..\..\..\..\data\SanFrancisco")
arcpy.env.workspace = workspace
feature_classes = arcpy.ListFeatureClasses()
for fc in feature_classes:
    print(fc)