# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:31:37 2019

@author: CSLW1
"""
import numpy
from PyQt5.QtWidgets import QFileDialog
import linecache

title = 'Hazard Reclass - Select Hazard .asc grid'
path = "C:\Modelling"
filter = "ASC (*.asc)"

qfd = QFileDialog()
#qfd.setFileMode(QFileDialog.ExistingFiles)

def Reclass(inputGrid):  

    loop = 0
    count = 0
    inputGridTxt = inputGrid[0]
    
    for x in inputGridTxt:
        saveGrid = x.strip(".asc")
        saveGrid = saveGrid + "_HazardReclass.asc"
        gridArray = numpy.loadtxt(x, skiprows=6)


        header1 = linecache.getline(x,1)
        header2 = linecache.getline(x,2)
        header3 = linecache.getline(x,3)
        header4 = linecache.getline(x,4)
        header5 = linecache.getline(x,5)
        header6 = linecache.getline(x,6)

        header = (header1 + header2 + header3 + header4 + header5 + header6)



        #=============================================================================
        for a in gridArray:
            for i, item in enumerate(a):
                loop = loop + 1
                if item > -900 and item < 0.75:
                    a[i] += 100
                    count = count + 1
                elif item >= 0.75 and item < 1.25:
                    a[i] += 200
                    count = count + 1
                elif item >= 1.25 and item < 2.00:
                    a[i] += 300
                    count = count + 1
                elif item >= 2.00:
                    a[i] += 400
                    count = count + 1
                else:
                    continue

        #=============================================================================

        header=str(header)

        with open (saveGrid, "w") as f:
            f.write(header)
            numpy.savetxt(f, gridArray, fmt="%1.4f")

inputGrid = QFileDialog.getOpenFileNames(qfd, title, path, filter)
runReclass = Reclass(inputGrid)