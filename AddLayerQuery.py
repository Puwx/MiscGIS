"""
This script is meant to be run as an ArcGIS toolbox script tool and its purpose is to apply a definition query to a
layer based off of the current selection that is applied to the layer.
  The script tool only requires 1 parameter: Input feature layer - TYPE = Feature Layer
To use this tool:
  1. Select the features of interest from you feature layer
  2. Open the AddLayerQuery tool from your toolbox
  3. Select the feature layer from the dropdown
  4. The script will append your select to the existing query (if it exists) or completely add a new one
"""


import arcpy

def getVals(fc):
    return ','.join([str(row[0]) for row in arcpy.da.SearchCursor(fc,'OID@')])

if __name__=='__main__':
    fc = arcpy.GetParameterAsText(0)
    values = getVals(fc)

    mxd = arcpy.mapping.MapDocument('current')
    lyr = arcpy.mapping.ListLayers(mxd,wildcard=fc)[0]
    
    if len(lyr.definitionQuery) > 0:
        outQuery = '{} AND OBJECTID IN ({})'.format(lyr.definitionQuery,values)
    else:
        outQuery = 'OBJECTID IN ({})'.format(values)
    lyr.definitionQuery = outQuery
    
    arcpy.RefreshActiveView();arcpy.RefreshTOC()
    
