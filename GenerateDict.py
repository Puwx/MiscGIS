import os
import csv
import arcpy

def getFieldInfo(fc):
    fieldsOI = [f for f in dir(arcpy.ListFields(fc)[0]) if not f.startswith('_')]
    return [{prop:getattr(fieldObj,prop) for prop in fieldsOI} for fieldObj in arcpy.ListFields(fc)]

if __name__ == "__main__":
    inFile = arcpy.GetParameterAsText(0)
    outFolder = arcpy.GetParameterAsText(1)
    os.chdir(outFolder)
    baseName = os.path.basename(inFile).replace('.shp','')
    
    fieldInfo = getFieldInfo(inFile)
    with open(baseName+'_FieldInfo.csv','w') as outText:
        fields = list(fieldInfo[0].keys())
        dictWriter = csv.DictWriter(outText,fieldnames=fields,lineterminator='\n')
        dictWriter.writeheader()
        for field in fieldInfo:
            dictWriter.writerow(field)
    arcpy.AddMessage('Script completed.')
        
