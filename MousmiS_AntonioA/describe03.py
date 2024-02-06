import arcpy
import sys

def desc_feature_class(fc):
    
    desc = arcpy.da.Describe(fc)
    print(f'{"BaseName":13} {desc["baseName"]}\n{"CatalogPath":13} {desc["catalogPath"]}\n{"DataType":13} {desc["dataType"]}')


# fc = (r'..\..\..\..\data\Canada\province.shp')

if len(sys.argv) != 2:
    print ("Usage: describe03.py <FeatureClassName>")
    sys.exit()
else:
    feat_class_arg = sys.argv[1]
    desc_feature_class(feat_class_arg)

