import numpy as np
import cv2
from __main__ import *
import matplotlib.pyplot as plt
import imutils
import os
import random


from som import*
from som2 import*

from prb1 import*
from prb2 import*
from prb3 import*


flag = False
prgRun = True



def main(prgRun):

    problem=3

    if problem==1:
        prb1main()
    if problem==2:
        prb2main()
    if problem==3:
        prb3main()


    prgRun = False
    return prgRun



if __name__ == '__main__':
    prgRun = True
    while prgRun == True:
        prgRun = main(prgRun)

    cv2.destroyAllWindows()
