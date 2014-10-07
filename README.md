Original Problem: Write program to rename files in the following manner:

icr_172595_A1 ==> icr172595.0

icr_172595_B1 ==> icr172595.1

icr_172596_C1 ==> icr172596.0

icr_172596_D1 ==> icr172596.1

icr_172597_E1 ==> icr172597.0

icr_172597_F1 ==> icr172597.1

...

Solution strategy:

    1. Eliminate the first underscore. 
    2. Replace the second underscore with a period.
    3. Replace the suffix with an incremental integer index starting from 0.


Revised problem:

    1. First underscore may not be present, or may be a space.
    2. Alphabetic prefix should be lowercased.

Revised solution strategy:

    1. Use regular expressions to extract [alphabetic prefix] [optional delimiter] [numerical ssn] [underscore] [microtray index]
    2. Construct: lowercase[alphabetic prefix] [numerical ssn] [underscore] [integer index]

