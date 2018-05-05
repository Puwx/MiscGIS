import arcpy,os,sys
def workspace(name):
    arcpy.env.workspace = name
    arcpy.env.overwriteOutput = True
    return arcpy.env.workspace
inputfc = arcpy.GetParameterAsText(0)
outputloc = arcpy.GetParameterAsText(1)
path,fc = os.path.split(inputfc)
workspace(outputloc)

describe = arcpy.Describe(inputfc)
spacial_ref = describe.spatialReference
# Centroid = SHAPE@XY

pointtemp = arcpy.CreateFeatureclass_management(outputloc,fc+"_ZXZYZZ","POINT","","","",spacial_ref)

if describe.shapeType != "Polygon":
    arcpy.AddError("This feature is not a polygon and therefore isn't compatible with the tool!")
    raise SystemExit(0)

xy = []
with arcpy.da.SearchCursor(inputfc,"SHAPE@XY","",spacial_ref) as cursor:
    for row in cursor:
        xy.append(row)

del cursor,row

with arcpy.da.InsertCursor(pointtemp,"SHAPE@XY") as inscursor:
    for row in xy:
        inscursor.insertRow(row)

pointfc = arcpy.SpatialJoin_analysis(pointtemp,inputfc,os.path.join(outputloc,fc+"_Point"),"JOIN_ONE_TO_ONE","","","CLOSEST")

arcpy.Delete_management(pointtemp)

del inscursor,row














