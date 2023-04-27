#!/usr/bin/python3
"""Function that finds the peak in a list of unsorted numbers"""


def find_peak(list_of_integers):
    """Check if the list is empty"""
    if len(list_of_integers) == 0:
        return None
    """Set the range to include the entire list"""
    low = 0
    r = len(list_of_integers) - 1
    """Perform a binary search to find a peak"""
    while low < r:
        m = (low + r) // 2
        """Check wether the middle is a peak"""
        if list_of_integers[m] > list_of_integers[m + 1]:
            """Narrow the range to the second half"""
            r = m
        else:
            low = m + 1
            return list_of_integers[low]
