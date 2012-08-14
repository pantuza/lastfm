# -*- coding: utf-8 -*-
import sys
import os

# make the src directory public to the test classes
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(src_path)
