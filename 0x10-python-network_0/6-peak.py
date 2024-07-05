#!/usr/bin/python3
"""script to find peak in list of ints, interview prep
"""

"""
    THOUGHT PROCESS
        it's not sorted; sorting would take n(log(n))
            -> not worth sorting
        looping through and keeping track of max (brute force)
            -> O(n)

        possibly looping from each end reducing to 1/2 run time
            -> still O(n)
"""


def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    max_k = None
    for ele in list_of_integers:
        if max_k is None or max_k < ele:
            max_k = ele
    return max_k
