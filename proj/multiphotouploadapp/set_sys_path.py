# -*- coding: utf-8 -*-
"""Sets sys.path for the library directories."""
import os
import sys

current_path = os.path.abspath(os.path.dirname(__file__))

# Add lib as primary libraries directory, with fallback to lib/dist
# and optionally to lib/dist.zip, loaded using zipimport.
sys.path[0:0] = [
    os.path.join(current_path,'fileupload'),
    '''
    os.path.join(current_path, 'lib','utilities'),
    os.path.join(current_path, 'lib','utilities','tipfy'),
    os.path.join(current_path, 'datamodels', 'continents'),
    os.path.join(current_path, 'datahandler'),
    os.path.join(current_path, 'datamodels'),
    '''
]
