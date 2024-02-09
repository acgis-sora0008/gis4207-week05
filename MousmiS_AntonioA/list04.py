# import sys
# def main():
#     if len(sys.argv) !=2:
#         root_folder = "r'..\..\..\..\data"
#         print('Usage: list04.py <data>')
#         sys.exit()
        
#     elif not arcpy.Exists(root_folder):
#         print("Error: The provided root folder does not exists")
    
#     import arcpy
    
#     list_workspace(root_folder)
    
# def list_workspace(root_folder):
#     import arcpy
    
#     arcpy.env.workspace = arcpy.ListWorkspaces(workspace_type="ALL", include_private=True)
    
    
#     for ws in workspace:
#         print(ws)
        
        
        
# if __name__ == "__main__":
#     main()                       
        
# ###
#     List ws in given folder
#     delayed imports
#     display Usagae
#     use .exists
#     etc
# #######
    
import sys

def main():
    global arcpy 

    if len(sys.argv) != 2:
        print('Usage: list04.py <data>')
        sys.exit()
 
    root_folder = sys.argv[1]
    # workspace = sys.argv[2]
    import arcpy  
    

    list_workspace(root_folder)


def list_workspace(root_folder):
    """"Prints all workspaces in specified root folder"""
    workspaces = arcpy.ListWorkspaces(root_folder)
    if not workspaces:
        print(f'No workspaces found under {root_folder}')
    else:
        for workspace in workspaces:
            print(workspace)



if __name__ == "__main__":
    main()


