# -*- coding: utf-8 -*-

import os
import numpy as np
from module import cvmodule as cis

#Set value

filepath = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Documents\\001.btn"
savefilepath = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Documents\\out.bmp"

offset = -700
bitshift = 5
RGain = 1.5
BGain = 3
#read raw data

matint = cis.ReadRaw(filepath, np.int16, 7872, 4348)


#digital processing

matint = matint + int(offset)                #offset
matint = matint >> int(bitshift)             #bitshift
matint = cis.Stagger(matint,"R")                     #Stagger
#matint = matint[49:49+1096, 160:160+1936]                 #Trim                       

#Demosaic and Color Gain

image = cis.Demosaic(matint, 'GR', RGain, BGain)   

#show image

cis.Show(image)
cis.SaveBMP(image, savefilepath)