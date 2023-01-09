#!/usr/bin/python3
""" function that returns a tuple with the length of a string and its first character"""
def multiple_returns(sentence):
    len_sen = len(sentence)

    if (len_sen == 0):
        new_tuple = (len_sen, None)
    else:
        new_tuple = (len_sen, sentence[0])

    return (new_tuple)
