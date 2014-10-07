#!/usr/bin/env python
# usage: ./renamer [data_directory]

import os, re, sys
from collections import defaultdict

if len(sys.argv) < 2:
    data_dir = "test" 
else:
    data_dir = sys.argv[1]

# regular expressions
pattern_bad = re.compile("^([a-zA-Z]+)([^0-9]*)([0-9]+)(_*)(\S+)$")
# pattern_good = re.compile("^[a-z]+[0-9]+\.\d+$")

# extract triples
quads = [] 
for f in os.listdir(data_dir): 
    match_bad = pattern_bad.search(f)
    prefix = match_bad.group(1).lower()
    delim1 = match_bad.group(2)
    ssn = match_bad.group(3)
    delim2 = match_bad.group(4)
    suffix = match_bad.group(5)
    quads.append((prefix,ssn,suffix,f))

# sort quads
quads.sort()

# renaming
tally = defaultdict(int)
for t in quads:
    prefix,ssn,suffix,original = t
    tally[(prefix,ssn)] += 1
    g = "{0}{1}.{2}".format(prefix.lower(),ssn,tally[(prefix,ssn)]-1)
    print "{0} ==> {1}".format(original, g)
    os.rename( os.path.join(data_dir, original), os.path.join(data_dir, g))
