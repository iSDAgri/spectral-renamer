#!/usr/bin/env python
import os

num_digits = 8
prefix = 'icr'
output_dir = 'test'
num_files = 100
ssn_start = 172596 

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

ssn = ssn_start - 1
for i in xrange(0,num_files):
    if 0 == (i % 2) and i > 0: ssn += 1
    row = i % 8
    col = (i / 8) + 1
    microtray_code = chr(row + 65) + str(col)   

    if 0 == i % 3:
        delimiter = " "
    elif 1 == i % 3:
        delimiter = ""
    elif 2 == i % 3:
        delimiter = "_"

    if 0 == i % 2:
        prefix = prefix.upper()
    else:
        prefix = prefix.lower()

    fn = "{0}{1}{2}_{3}".format(prefix, delimiter, ssn, microtray_code)
    open(os.path.join(output_dir,fn),'a').close()

