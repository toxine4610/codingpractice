

import numpy as np

def weightCorrects(correct):

    # default np.pi only has 18 digits, we need to generate 10,000 digits of pi.
    # one potential solution is to use the symbolic math toolbox.

    from mpmath import mp
    mp.dps = 10000 # add one because we will be removing the decimal place
    

    xs = str(np.sqrt(mp.pi))
    # remove the decimal place
    pi_digits = [ x for x in xs if x != '.' ]

    print(pi_digits[:5])

    num = 0 
    den = 0

    for i in range( len(correct) ):
        correct_this_index = correct[i] * int(pi_digits[i])
        num += (correct_this_index)
        den += int( pi_digits[i] )
    return float(num/den)


correct = [1,0,1,1,0]
print( weightCorrects(correct))

