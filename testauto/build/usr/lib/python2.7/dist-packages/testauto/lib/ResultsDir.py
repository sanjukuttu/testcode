#!/usr/bin/python
'''
'''
###############################################################################

import os, logging, thread
 
###############################################################################

class ResultsDir():
    '''
    A wrapper object for the directory that contains the results bundle 
    '''
    def __init__(self, station, test_name, test_starttime, subresults_dir=None):
        '''
        Initialise stuff
        '''
