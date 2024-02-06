import sys

def main():
    """Checks that there is a commmand line argument. If it is then, it ensures called feature class exists. If it does exist, calls the desc_feature_class(fc)"""
    global arcpy 

    if len(sys.argv) != 2:
        print ("Usage: describe06.py <FeatureClassName>")
        sys.exit()

    fc = sys.argv[1]
    import arcpy
    if not arcpy.Exists(fc):
        print (f'{fc}, "does not exist"')
        sys.exit()
    desc_feature_class(fc)

def desc_feature_class(fc):
    """Prints the requested characteristics of the feature class"""

    desc = arcpy.da.Describe(fc)
    print(f'{"BaseName":13} {desc["baseName"]}\n{"CatalogPath":13} {desc["catalogPath"]}\n{"DataType":13} {desc["dataType"]}')
    fields = desc["fields"]
    print (fields)

    # for field in fields:
    #     print(f'{field:6}{})



if __name__ == "__main__":
    main()


