import arcpy

fc = (r'..\..\..\..\data\Canada\province.shp')

descfc = arcpy.Describe(fc)

descBaseName = descfc.BaseName
descCatPath = descfc.CatalogPath
descDataType = descfc.DataType

print (f"BaseName: {descBaseName}\nCatalogPath: {descCatPath}\nDataType: {descDataType}")