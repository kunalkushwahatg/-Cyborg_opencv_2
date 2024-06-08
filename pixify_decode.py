import numpy as np
import cv2
import os
import sys
import time
import random

'''
Guidelines :- 1) You are not allowed to import libraries other than those already mentioned
              2) You are allowed to code only in the function given below . Code present anywhere else would be ignored by the code verifying exec.
              3) You must code in such a way that the code inside the function is robust for all test cases.
              4) The code verifying exectubale would iterate over the test cases and call this function with one test image at a time. 
'''

def decode(image):
    '''
    Description:- This function takes in image as the input (a numpy array) and returns the character embedded in the image
    For example : if yellow squares = 4 , red squares = 3 , number of shapes containing shapes = 5 . Then the correct character to be returned would be (4*2 + 3*1 + 5) which is p. 
    Note :- if the value comes out to be 32 then the function should return an empty single space " ".
    '''


    ############ Enter your Code Here #################
    character = " "
    k = 0
    for i in range(100, 601, 100):
        for j in range(100, 601, 100):
            if image[i,j][0] == 0 and image[i,j][1] >  254 and image[i,j][2] > 254:
                k += 2

            if tuple(image[i+30, j+30]) != (255, 255, 255) or tuple(image[i+30 , j+70]) != (255, 255, 255) or tuple(image[i+70, j+30]) != (255, 255, 255) or tuple(image[i+70, j+70]) != (255, 255, 255):
                if i<600 and j<600:
                    k += 1

            
            if image[i,j][0] == 0 and image[i,j][1] == 0 and image[i,j][2] > 254:
                k += 1

    if k <= 26:
        character = chr(k + 96)


    ###################################################
    return character

    