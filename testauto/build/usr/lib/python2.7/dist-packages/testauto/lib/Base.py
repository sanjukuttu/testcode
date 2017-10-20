#!/usr/bin/python
'''
'''
###############################################################################

import os, logging, shutil 

###############################################################################

class Script():
    '''
    This is the base class for all tests.
    '''
    def __init__(self, name, description):
        '''
        Initialise stuff
        '''

    def __del__(self):
        '''
        Perform post-test clean-up
        '''
        
    def start(self):
        '''
        Perform pre-test actions
        '''

    def run(self):
        '''
        Run the test.

        Just raise NotImplementedError here in the base class to replicate
        behaviour similar to a pure virtual function in C++.

        (The implementation of the run function is in the derived classes.)
        '''
        raise NotImplementedError

    def fetch_results(self):
        '''
        Fetches result
        '''
    # Accessors
