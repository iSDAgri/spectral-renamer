#!/usr/bin/env python
# usage: ./renamer [data_directory]

import os, re
from collections import defaultdict

data_dir = "test" 

tally = defaultdict(int)
files = sorted(os.listdir(data_dir))
for a in files: 
    b = re.sub('_','',a, 1) 
    c = re.sub('_','.',b,1) 
    prefix = c.split('.')[0]
    tally[prefix] += 1 
    d =  prefix + "." + str(tally[prefix]-1)
    print "{0} ==> {1}".format(a,d) 
    os.rename( os.path.join(data_dir, a), os.path.join(data_dir,  d))
