
import sys

def main():
    """Checks that there is a commmand line argument. If it is then, it ensures called feature class exists. If it does exist, calls the list_feat_class()"""
    global arcpy 
    from arcpy import env

    if len(sys.argv) != 2:
        print ("Usage: list02.py <FeatureClassName>")
        sys.exit()

    env.workspace = sys.argv[1]
    import arcpy

    if not arcpy.Exists(env.workspace):
        print (f'{env.workspace}, "does not exist"')
        sys.exit()
    list_feat_class(env.workspace)

def list_feat_class(work_space):
    """Prints the requested characteristics of the feature class"""
    work_space = arcpy.ListFeatureClasses()
    for classes in work_space:
        print(classes)


if __name__ == "__main__":
    main()


