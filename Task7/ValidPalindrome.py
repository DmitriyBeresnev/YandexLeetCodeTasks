

# LeetCode. Yandex Task List. 125. Valid Palindrome

'''

125. Valid Palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.



Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

Accepted
1,013,294
Submissions
2,541,172


Related Topics
Two Pointers, String

Similar Questions
Palindrome Linked List
Easy
Valid Palindrome II
Easy
Maximum Product of the Length of Two Palindromic Subsequences
Medium

'''


import math
import time
import collections
from typing import List
import numpy as np
import random as rnd
import itertools as it
from collections import defaultdict, Counter
import re
from functools import reduce
from functools import lru_cache
from bisect import bisect, bisect_left


class Solution:
    def isPalindrome(self, s: str) -> bool:
        symbolsList = list(s.replace(" ", ""))
        delList = list()
        for symbol in symbolsList:
            if ((ord(symbol) < 65 or ord(symbol) > 90) and (ord(symbol) < 97 or ord(symbol) > 122) and (ord(symbol) < 48 or ord(symbol) > 57)):
                #symbolsList.remove(symbol)
                delList.append(symbol)
        for symbol in delList:
            symbolsList.remove(symbol)
        for i, symbol in enumerate(symbolsList):
            if symbol.isupper():
                symbolsList[i] = symbol.lower()
        # print(symbolsList)
        half = int(len(symbolsList) / 2)
        if len(symbolsList) % 2 == 0:
            left = "".join(symbolsList[:half])
            right = "".join(symbolsList[half:])
            if hash(left[::-1]) == hash(right):
                return True
            else:
                return False
        else:
            left = "".join(symbolsList[:half])
            right = "".join(symbolsList[half+1:])
            if hash(left[::-1]) == hash(right):
                return True
            else:
                return False


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    print(solution.twoSum(nums = [2 ,7 ,11 ,15], target = 9))
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    print(solution.twoSum(nums = [3 ,2 ,4], target = 6))
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    print(solution.twoSum(nums = [3 ,3], target = 6))
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    print(solution.isIsomorphic("badc", "baba"))
    end4 = time.perf_counter()
    print(f"test 4: {end4 - start4:10.6f} sec")
    #
    start5 = time.perf_counter()
    print(solution.isIsomorphic("abab", "baba"))
    end5 = time.perf_counter()
    print(f"test 5: {end5 - start5:10.6f} sec")
    #
    start6 = time.perf_counter()
    print(solution.firstMissingPositive([1, 1]))
    end6 = time.perf_counter()
    print(f"test 6: {end6 - start6:10.6f} sec")
