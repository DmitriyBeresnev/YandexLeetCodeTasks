

# LeetCode. Yandex Task List. 22. Generate Parentheses

'''

22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]



Constraints:

    1 <= n <= 8

Accepted
885,720
Submissions
1,297,090


Related Topics
String, Dynamic Programming, Backtracking

Similar Questions
Letter Combinations of a Phone Number
Medium
Valid Parentheses
Easy

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
    def backtrack(self, parenthesisList: List[str], curStrCombination: str, left: int, right: int) -> None:
        if left > right:
            return
        if left == 0 and right == 0:
            parenthesisList.append(curStrCombination)
        if left > 0:
            self.backtrack(parenthesisList, curStrCombination + "(", left-1, right)
        if right > 0:
            self.backtrack(parenthesisList, curStrCombination + ")", left, right-1)

    def generateParenthesis(self, n: int) -> List[str]:
        parenthesisList = list()
        self.backtrack(parenthesisList, "", n, n)
        return parenthesisList


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
