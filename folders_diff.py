#Search folder contents - compare differences in parent folders and inner folders
import os
import pandas as pd
import numpy as np


def f_dif(f1,f2):
    """Find differences between two folders
    f1, f2:
      - folder paths
    Returns a tuple of 2 elements:
      - a list with differences between parent folders;
      - a dictionary with differences inside each subfolder.
    """

    if os.path.exists(f1):        
        fnames1 = os.listdir(f1) 
    if os.path.exists(f2):        
        fnames2 = os.listdir(f2) 

    #exists in f1 but not in f2
    dif1 = list(set(fnames1) - set(fnames2))
    #exists in f2 but not in f1
    dif2 = list(set(fnames2) - set(fnames1))

    #exists in one but not in the other
    dif3 = list(set(fnames1).symmetric_difference(fnames2))
    #print(dif3)

    #exists in both
    equ3 = list(set(fnames1).intersection(fnames2))

    #Check differences inside each subfolder that exists on both
    dif4 = {}
    for i in equ3:
        path1 = f1 + i  
        if os.path.exists(path1): 
            try:
                f1f = os.listdir(path1) 
            except:
                f1f = []
        path2 = f2 + i  
        if os.path.exists(path2): 
            try:
                f2f = os.listdir(path2) 
            except:
                f2f = []                
        if ((len(f1f) != 0) and (len(f2f) != 0)):  #if it is a directory
            dif4[i] = (list(set(f1f).symmetric_difference(f2f)))
    #print(dif4)

    return(dif3,dif4)

#Define Folder Paths
f_1 = "C:/Users/XXXXXX/FolderA/" #Folder 1
f_2 = "C:/Users/XXXXXX/FolderB/" #Folder 2

#Call function
res = f_dif(f_1,f_2)

#Print Results
print("Exists in one parent folder but not in the other")
print(res[0])
print("Differences inside each subfolder")
print(res[1])
