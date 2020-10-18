#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:56:57 2020

@author: Javi
"""
import agentframeworkfinal
import modelfinal
import os


"""
This file was created to check the functionality of the modelfinal.py script.
Checks that program still runs even when the initial paramameters that are 
inputted from the command line are not correct.
"""


#no input parameters
#os.system('python modelfinal.py')

#output
"""
Incorrect number of arguments inputted. Using default values.
Loading initial parameters...
Number of agents = 10
Number of iterations = 100
Neighbourhood = 20
Loading environment...
Initialising Agents...
"""

#non-integer initial parameters
#os.system('python modelfinal.py hello world goodbye')

#output
"""
Number of agents must be an integer. Using default values.
Number of iterations must be an integer. Using default values.
Neighbourhood must be an integer. Using default values.
Loading initial parameters...
Number of agents = 10
Number of iterations = 100
Neighbourhood = 20
Loading environment...
Initialising Agents...
"""

#too many args given
#os.system('python modelfinal.py 10 100 10 20 30 40 50')
#output
"""
Incorrect number of arguments inputted. Using default values.
Loading initial parameters...
Number of agents = 10
Number of iterations = 100
Neighbourhood = 20
Loading environment...
Initialising Agents...
"""


