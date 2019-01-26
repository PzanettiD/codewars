# https://www.codewars.com/kata/scramblies/train/python
# If a portion of str1 characters can be rearranged to match str2, return True,
# otherwise returns false.
import collections

def scramble(s1, s2):
    # your code here
    if len(s1) < len(s2):
        return False
    s22 = collections.Counter(s2)
    s11 = collections.Counter(s1)
    for s in s2:
        if s22[s] > s11[s]:
            return False
    return True
