# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:21:27 2020

@author: Faraz
"""



#first param is input folder path

import subprocess, shlex
import sys,os,time
#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
#print( "The arguments are: " , str(sys.argv))


CONVERTER_PATH = "ODAFileConverter" 


#INPUT_FOLDER  =  '/home/farazahmed_95/converter_pkg'
#OUTPUT_FOLDER ='/home/farazahmed_95/converter_pkg'

INPUT_FOLDER  = sys.argv[1]
#OUTPUT_FOLDER = "E:\\FIVERR\\jasper_1977\\testdwg_laptop\\out" 
OUTPUT_FOLDER = sys.argv[2]

OUTVER = "ACAD2010"
OUTFORMAT = "DXF"
RECURSIVE = "0"
AUDIT = "1"

INPUTFILTER = sys.argv[3]
INPUTFILTER = 't1.dwg'

OUTPUT_DXF_NAME = INPUTFILTER[:-4]

kml_file_tmp = OUTPUT_FOLDER +"/"+ OUTPUT_DXF_NAME + '_tmp.kml'
#kml_file = OUTPUT_FOLDER +"\\"+ OUTPUT_DWF_NAME+ '.kml'

kml_file = OUTPUT_FOLDER +"/"+ OUTPUT_DXF_NAME + '.kml'
#kml_file = OUTPUT_FOLDER +"\\"+ OUTPUT_DWF_NAME+ '.kml'

# Command to run
cmd = [CONVERTER_PATH, INPUT_FOLDER, OUTPUT_FOLDER, OUTVER, OUTFORMAT, RECURSIVE, AUDIT, INPUTFILTER]
# Run
subprocess.run(cmd, shell=True)
subprocess.run(cmd, shell=False)

time.sleep(2)


#ogr_cmd = 'ogr2ogr -s_srs EPSG:28992 -t_srs EPSG:4326 -f KML new.kml t1.dxf'
ogr_cmd = 'ogr2ogr -s_srs EPSG:28992 -t_srs EPSG:4326 -f KML '
ogr_cmd +=    kml_file_tmp + ' ' + OUTPUT_DXF_NAME +'.dxf'
os.system(ogr_cmd)


'''
mycmd='"C:\\Program Files\\ODA\\ODAFileConverter_title 21.2.0\\ODAFileConverter.exe" "E:\\FIVERR\jasper_1977\\testdwg_laptop" "E:\\FIVERR\\jasper_1977\\testdwg_laptop\\out" "ACAD2010" "DXF" "0" "1" "EMN-01.dwg"'
subprocess.run(shlex.split(mycmd))



ogr_cmd = 'ogr2ogr -s_srs EPSG:28992 -t_srs EPSG:4326 -f KML new.kml t1.dxf'
os.system(ogr_cmd)

'''

'''

import os
os.system('ODAFileConverter "/home/farazahmed_95/converter_pkg" "/home/farazahmed_95/converter_pkg" "ACAD2010" "DXF" "0" "1" "*.dwg"')

ogr_cmd = 'ogr2ogr -s_srs EPSG:28992 -t_srs EPSG:4326 -f KML f.kml t1.dxf'
os.system(ogr_cmd)'''


################################################

from fastkml import kml
#kml_file = 'E:\FIVERR\jasper_1977\testdwg_laptop\out.kml'
with open(kml_file_tmp, 'rt', encoding="utf-8") as myfile:    
    doc = myfile.read().encode('utf-8')

k = kml.KML()
k.from_string(doc)

f= list(k.features())

d =f[0]
folder =list(d.features())[0]
features = list(folder.features())
#list((list(features[0].styles())[0]).styles())[0].to_string()
#list((list(features[0].styles())[0]).styles())[0].color = 'ff000000'

for f in features:
    #color for layer GEUL blue... 
    #color is written in reverse start FF is for #, then two chars for blue so,on 
    # next 2 chars for red then last 2 for green
    
    #Geul=Blue
    #GESTUURDE BORING=dark green
    #TUINBORING=light blue
    
    #Persing=light green  --no entry
    #Mantelbuis = green --no entry
    #Handhole= dark red--no entry
    #DP=red--no entry
    
    
    f_str = f.to_string().lower().lower()
    if '<SimpleData name="Layer">GEUL</SimpleData>'.lower() in f_str :
        list((list(f.styles())[0]).styles())[0].color = 'FFFF0000' 
    if '<SimpleData name="Layer">TUINBORING</SimpleData>'.lower() in f_str :
        list((list(f.styles())[0]).styles())[0].color = 'FFff8e6c'
    if '<SimpleData name="Layer">GESTUURDE BORING</SimpleData>' in f_str :
        list((list(f.styles())[0]).styles())[0].color = 'FF005500'
    
   
#f = open("E:\\FIVERR\\jasper_1977\\testdwg_laptop\\out\\python_converted.kml", "w")
f_file = open(kml_file, "w")        
f_file.write(k.to_string())
f_file.close()



