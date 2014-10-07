#!/usr/bin/env python
# usage: ./renamer [data_directory]

import os, re

data_dir = "test" 

files = sorted(os.listdir(data_dir))
for a in files: 
    b = re.sub('_','',a, 1) 
    c = re.sub('_','.',b,1) 
    print "{0} ==> {1}".format(a,c) 

