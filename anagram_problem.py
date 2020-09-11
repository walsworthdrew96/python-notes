#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the anagram function below.
def anagram(s):
    if len(s) % 2 == 1:
        return -1
    left = s[:int(len(s) / 2)]
    right = s[int(len(s) / 2):]
    left_chars = {}
    right_chars = {}
    for char in left:
        if char not in left_chars:
            left_chars[char] = 1
        else:
            left_chars[char] += 1
    for char in right:
        if char not in right_chars:
            right_chars[char] = 1
        else:
            right_chars[char] += 1
    print('left:', left)
    print('right:', right)
    print('left_chars:', left_chars)
    print('right_chars:', right_chars)
    char_change_count = 0
    for char, count in left_chars.items():
        print('left contains:  {1} {0}'.format(char, count))
        if char in right_chars:
            print('right contains: {1} {0}'.format(char, right_chars[char]))
        else:
            print('right contains: {1} {0}'.format(char, 0))
        if char not in right_chars:
            char_change_count += count
        else:
            if count - right_chars[char] > 0:
                char_change_count += count - right_chars[char]
        print('char_change_count:', char_change_count)
    return char_change_count


if __name__ == '__main__':
    f = open('anagram_test', 'r')
    for line in f.readlines():
        print('line.rstrip():', line.rstrip())
        print('result:', anagram(line.rstrip()))
        print('\n\n')
