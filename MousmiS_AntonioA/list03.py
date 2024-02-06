
import sys

def main():
    """Checks that there is a commmand line argument. If it is then, it ensures called feature class exists. If it does exist, calls the list_feat_class()"""
    global arcpy 
    from arcpy import env

    if len(sys.argv) != 3:
        print("Usage: list02.py <Workspace> <FeatureType>")
        sys.exit()

    workspace = sys.argv[1]
    feature_type = sys.argv[2]

    env.workspace = workspace

    valid_feature_type = ['Annotation', 'Arc', 'Dimension', 'Edge', 'Junction', 'Label', 'Line', 'Multipatch', 'Multipoint', 'Node', 'Point', 'Polygon', 'Polyline', 'Region', 'Route', 'Tic', 'All']
    if not feature_type in valid_feature_type:
        print (f'{feature_type}, "is not valid"')
        sys.exit()

    import arcpy
    if not arcpy.Exists(workspace):
        print (f'{workspace}, "does not exist"')
        sys.exit()


    list_feat_class(workspace, feature_type)


def list_feat_class(workspace, shape_type):
    """Prints the requested characteristics of the feature class."""
    feature_classes = [fc for fc in arcpy.ListFeatureClasses() if arcpy.Describe(fc).shapeType.lower() == shape_type.lower()]
    
    if not feature_classes:
        print(f'No feature classes with ShapeType {shape_type} found in {workspace}')
    else:
        for fc in feature_classes:
            print(fc)


if __name__ == "__main__":
    main()


