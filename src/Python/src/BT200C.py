# -*- coding: utf-8 -*-

import os
import numpy as np
from module import cvmodule as cis

#Set value

filepath = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Documents\\000.bin"
darkfilepath = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Documents\\ave.bin"
savefilepath = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Documents\\out.bmp"

offset = 0
bitshift = 5
colortype = 'C' # C or M
RGain = 1.4
BGain = 2.2


#read raw data

matint = cis.ReadRaw(filepath, np.int32, 2256, 1178)
darkmatint = cis.ReadRawToInt32(darkfilepath, np.float32, 2256, 1178)


#digital processing

matint = matint - darkmatint              #dark sub.
matint = cis.HOB200C(matint)                 #Horizontal noise correction
matint = matint + int(offset)                #offset
matint = matint >> int(bitshift)             #bitshift
matint = cis.Stagger(matint, "L")            #Stagger
matint = matint[49:49+1096, 160:160+1936]    #Trim                       

#Demosaic and Color Gain

if colortype == 'C':
    image = cis.Demosaic(matint, 'BG', RGain, BGain)   
elif colortype == 'M':
    image = cis.Mono(matint) 
  
#show image

cis.Show(image)
cis.SaveBMP(image, savefilepath)
