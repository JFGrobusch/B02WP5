#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To use:
**"commands" refers to min max match functions    
    
    
    1. insert function in funcx(x)
        make sure you only have x as an undefined variable
        any other parameters (d, rho, etc.) should be given in numerical form
        see below for example
        
    2. Choose a zoom level and coordinate fineness. These must be an integer.
        Use low values for testing and higher values for final numbers    
    
    3. Save the document with a unique name.
        The commands are function specific, meaning you need a seperate document for every function
        Pick a descriptive name, e.g. math_mmoi or math_thickness
        You'll want to save the document in the same directory where you store your other python scripts
        This way python can find and import the commands easily
        
    4. In the main document, import the commands under a local name
        This allows you to use them for different functions
        e.x. import RangeMin from math_mmoi as minMass
        In the above example, math_mmoi is the name under which the mathbasics.py script was saved
        and minMass is the given local name.
        
    5. If you have any questions, let me know!    


Function descriptions:
    
    Use only RangeMin(start, end), RangeMax(start, end), and RangeMatch(start, end, value), the other functions are local
    
    RangeMin
        Find the x coordinate minimum function value on a range
    
    RangeMax
        Find the x coordinate of the maximum function value on a range
        
    RangeMatch
        Find the x coordinate where the function matches a given value.
            Estimate the range. Be generous!
            The commands are very good at zooming in, but they dont zoom in...
            So overshooting by orders of magnitude is okay (but try to avoid it)


Final note: the computer is blind; if there are multiple solutions, it will give only 1.
    

@author: jangrobusch
"""

########################    insert equation here #######################


def funcx(x):
    a = 1
    b = 2
    #insert specific func x
    y = a*x - b
    return(y)

zoomlevels = 4 #higher = more precise but slower
coordfineness = 64 #higher = more precise but slower

########################    insert equation here #######################


########## basic

def xcoords(start, end):   
    #fineness 50
    f = coordfineness
    xl = []
    r = (end-start)/(f-1)
    for i in range(f): xl.append(i*r+start)
    return(xl)

def ycoords(xcoords):
    yl = []
    for i in xcoords: yl.append(funcx(i))
    return(yl)

######### min: use RangeMin to get the x value of the minima
    
def intMin(start, end):
    #finds the interval over which the minimum occurs
    xc = xcoords(start, end)
    yc = ycoords(xc)
    ymin = min(yc)
    min_index = yc.index(ymin)
    if min_index == 0:
        x1 = xc[0]
    else:   x1 = xc[min_index-1]    
    if min_index == len(xc)-1:
        x2 = xc[-1]
    else:   x2 = xc[min_index+1]     
    xrange = [x1, x2]
    return(xrange)
    

def RangeMin(start, end):
    zl = zoomlevels
    #finds the minimum point of a function on a range
    #zoom levels 10
    xrange = intMin(start, end)
    for i in range(zl):
        xrange = intMin(xrange[0], xrange[1])                    
    xc = xcoords(xrange[0], xrange[1])
    yc = ycoords(xc)
    min_index = yc.index(min(yc))
    x = xc[min_index]               
        
    return(x)

######### max: use RangeMax to get the x value of the maxima
    
def intMax(start, end):
    #finds the interval over which the minimum occurs
    xc = xcoords(start, end)
    yc = ycoords(xc)
    ymax = max(yc)
    max_index = yc.index(ymax)
    if max_index == 0:
        x1 = xc[0]
    else:   x1 = xc[max_index-1]    
    if max_index == len(xc)-1:
        x2 = xc[-1]
    else:   x2 = xc[max_index+1]     
    xrange = [x1, x2]
    return(xrange)
    

def RangeMax(start, end):
    zl = coordfineness
    #finds the minimum point of a function on a range
    #zoom levels 10
    xrange = intMax(start, end)
    for i in range(zl):
        xrange = intMax(xrange[0], xrange[1])                    
    xc = xcoords(xrange[0], xrange[1])
    yc = ycoords(xc)
    max_index = yc.index(max(yc))
    x = xc[max_index]               
        
    return(x)

######## value: use RangeValue to get the x value where func(x) = y

def MinDiffIndex(yc, value):
    difflist = []
    for i in yc: difflist.append(abs(i-value))
    return(difflist.index(min(difflist)))
    

def intMatch(start, end, value):
    #finds the interval over which the minimum occurs
    xc = xcoords(start, end)
    yc = ycoords(xc)
    bestindex = MinDiffIndex(yc, value)
    if bestindex == 0:
        x1 = xc[0]
    else:   x1 = xc[bestindex-1]    
    if bestindex == len(xc)-1:
        x2 = xc[-1]
    else:   x2 = xc[bestindex+1]     
    xrange = [x1, x2]
    return(xrange)
    

def RangeMatch(start, end, value):
    zl = coordfineness
    #finds the minimum point of a function on a range
    #zoom levels 10
    xrange = intMatch(start, end, value)
    for i in range(zl):
        xrange = intMatch(xrange[0], xrange[1], value)                    
    xc = xcoords(xrange[0], xrange[1])
    yc = ycoords(xc)
    bestindex = MinDiffIndex(yc, value)
    x = xc[bestindex]                       
    return(x)

########################################################################
    #author Jan Grobusch