import arcpy
from arcpy import env
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
env.workspace = r'..\..\..\..\data\SanFrancisco'

feature_classes = arcpy.ListFeatureClasses()
for fc in feature_classes:
    print(fc)