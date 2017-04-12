# -*- coding: utf-8 -*-

import numpy as np
import cv2

def ReadRaw(filepath, t, width, height):
    data = np.fromfile(filepath, t)
    return data.reshape((height, width))
    
def ReadRawToInt32(filepath, t, width, height):
    data = np.fromfile(filepath, t)
    data[data>2147483647] = 2147483647
    data[data<0] = 0
    dataint32 = data.astype(np.int32)
    return dataint32.reshape((height, width))

def HOB200C(src):
    w = src.shape[1]
    hob_l = src[:,12:128+12].mean(1).reshape(-1,1)
    hob_r = src[:,w-12-128:w-12].mean(1).reshape(-1,1)
    return src - ((hob_l + hob_r) / 2).astype(np.int32)

def Stagger(src, flag):
    h = src.shape[0]
    w = src.shape[1]
    
    #masking
    mask_odd = 1 - np.arange(h).reshape(h,1) % 2
    mask_even = np.arange(h).reshape(h,1) % 2
    mat_odd = src * mask_odd
    mat_even = src * mask_even
    
    #Stagger
    spacer = np.zeros(h).reshape(h,1)
    if flag in {'R', 'r'}:
        mat_even = np.hstack((spacer, mat_even))
        mat_even = np.delete(mat_even, w, 1)
    elif flag in {'L', 'l'}:
        mat_even = np.hstack((mat_even, spacer))
        mat_even = np.delete(mat_even, 0, 1)
    return mat_odd + mat_even
    
def Demosaic(src, flag, RGain, BGain):
    #Clip
    src[src>65535] = 65535
    src[src<0] = 0
    mat16 = src.astype(np.uint16)
    
    #Demosaic
    if flag in {'GR', 'gr'}:
        pic = cv2.cvtColor(mat16, cv2.COLOR_BAYER_GR2BGR)
    elif flag in {'RG', 'rg'}:
        pic = cv2.cvtColor(mat16, cv2.COLOR_BAYER_RG2BGR)
    elif flag in {'GB', 'gb'}:
        pic = cv2.cvtColor(mat16, cv2.COLOR_BAYER_GB2BGR)
    elif flag in {'BG', 'bg'}:
        pic = cv2.cvtColor(mat16, cv2.COLOR_BAYER_BG2BGR)
    
    #Gain
    gain = np.array([ BGain,  1,  RGain]).reshape(1,1,3)
    pic = pic * gain
    pic[pic>255] = 255
    return pic.astype(np.uint8)

def Mono(src):
    #Clip
    src[src>255] = 255
    src[src<0] = 0
    return src.astype(np.uint8)

def Show(pic):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def SaveBMP(pic, filepath):
    cv2.imwrite(filepath, pic)
 
if __name__ == "__main__":
    print("run cvmodule")
