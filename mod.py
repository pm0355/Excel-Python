# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:52:53 2016

@author: pm0355a
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from types import *
import re
import itertools

def openXLSX(fn,sn):
    f = fn+".xlsx"
    xlsxfile = pd.ExcelFile(f)
    data = xlsxfile.parse(sn)
    df= pd.DataFrame(data)
    return xlsxfile, data, df
def colSelect(numCols,df):
    i=0
    col=[]    
    while(i<numCols):
        c=df[df.columns[i]]
        col.append(c)
        i+=1
    return col
def rowSelect(rowIndex, df):
    return df.iloc[[rowIndex]]
def newFile(alist, name, var):
    f=open(str(name)+".txt","w")
    for a in alist:
        f.write(a)
    f.close()
def newXLSX(cols, numrows, name, sname):
    columns=cols.split(",")
    numRows=numrows
    index=np.arange(numRows)
    dataframe = pd.DataFrame(columns=columns, index=index)
    writer = pd.ExcelWriter(name+'.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
    dataframe.to_excel(writer, sheet_name=sname)
# Close the Pandas Excel writer and output the Excel file.
    writer.save()

def minmax(data):
    'Computes the minimum and maximum values in one-pass using only 1.5*len(data) comparisons'
    it = iter(data)
    try:
        lo = hi = next(it)
    except StopIteration:
        raise ValueError('minmax() arg is an empty sequence')
    for x, y in itertools.izip_longest(it, it, fillvalue=lo):
        if x > y:
            x, y = y, x
        if x < lo:
            lo = x
        if y > hi:
            hi = y
    return lo, hi
