import arcpy
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
workspace = os.path.join(script_dir, "..", "..", "..", "..", "data", "Week05_Data", "SanFrancisco")
arcpy.env.workspace = workspace

def desc_feature_class(workspace):
    desc = arcpy.da.Describe(workspace)
    print(f'{"BaseName":13} {desc["baseName"]}\n{"CatalogPath":13} {desc["catalogPath"]}\n{"DataType":13} {desc["dataType"]}')
    
    
if len(sys.argv) !=2:
    print("Usage: list02 <FeatureClassName>")    
    sys.exit()
    
else:
    class_arg = sys.argv[1]
    desc_feature_class(workspace)