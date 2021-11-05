

# LeetCode. Yandex Task List. 20. Valid Parentheses

'''

20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true



Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

Accepted
1,741,221
Submissions
4,299,585


Related Topics
String, Stack

Similar Questions
Generate Parentheses
Medium
Longest Valid Parentheses
Hard
Remove Invalid Parentheses
Hard
Check If Word Is Valid After Substitutions
Medium


Hide Hint 1
An interesting property about a valid parenthesis expression is that a sub-expression of a valid expression should also be a valid expression. (Not every sub-expression) e.g.

{ { } [ ] [ [ [ ] ] ] } is VALID expression
          [ [ [ ] ] ]    is VALID sub-expression
  { } [ ]                is VALID sub-expression

Can we exploit this recursive structure somehow?

Hide Hint 2
What if whenever we encounter a matching pair of parenthesis in the expression, we simply remove it from the expression? This would keep on shortening the expression. e.g.

{ { ( { } ) } }
      |_|

{ { (      ) } }
    |______|

{ {          } }
  |__________|

{                }
|________________|

VALID EXPRESSION!


Hide Hint 3
The stack data structure can come in handy here in representing this recursive structure of the problem. We can't really process this from the inside out because we don't have an idea about the overall structure. But, the stack can help us process this recursively i.e. from outside to inwards.

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
    def stackPop(self, stack: list, expectedStackTop: str) -> bool:
        if len(stack) > 0:
            if stack[-1] == expectedStackTop:
                stack.pop()
                return True
        return False

    def isValid(self, s: str) -> bool:
        # optimization for inputs that don't have an even number of elements
        if len(s) % 2:
            return False
        symbolsList = list(s)
        roundBracketsStack = []
        bracesStack = []
        squareBrackets = []
        generalStack = []
        for s in symbolsList:
            if s == "(":
                roundBracketsStack.append(s)
                generalStack.append(s)
            if s == "{":
                bracesStack.append(s)
                generalStack.append(s)
            if s == "[":
                squareBrackets.append(s)
                generalStack.append(s)
            if s == ")":
                self.stackPop(roundBracketsStack, "(")
                if not self.stackPop(generalStack, "("):
                    generalStack.append(s)
            if s == "}":
                self.stackPop(bracesStack, "{")
                if not self.stackPop(generalStack, "{"):
                    generalStack.append(s)
            if s == "]":
                self.stackPop(squareBrackets, "[")
                if not self.stackPop(generalStack, "["):
                    generalStack.append(s)
        return not len(roundBracketsStack) and not len(bracesStack) and not len(squareBrackets) and not len(generalStack)


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
