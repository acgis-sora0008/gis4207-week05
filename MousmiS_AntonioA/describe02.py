import arcpy

fc = (r'..\..\..\..\data\Canada\province.shp')

descfc = arcpy.Describe(fc)

descBaseName = descfc.BaseName
descCatPath = descfc.CatalogPath
descDataType = descfc.DataType

print (f'{"BaseName":13} {descBaseName}\n{"CatalogPath":13} {descCatPath}\n{"DataType":13} {descDataType}')