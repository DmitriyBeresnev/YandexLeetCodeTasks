

# LeetCode. Yandex Task List. 283. Move Zeroes

'''

283. Move Zeroes
Easy

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]



Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
Accepted
1,335,695
Submissions
2,241,617


Related Topics
Array, Two Pointers

Similar Questions
Remove Element
Easy

Hide Hint 1
In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.

Hide Hint 2
A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

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
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nonZeroElementPos = 1
        if n == 1:
            return
        curNonZeroElementVal = nums[nonZeroElementPos]
        for i in range(0, n-1):
            if nonZeroElementPos < n:
                curNonZeroElementVal = nums[nonZeroElementPos]
            while curNonZeroElementVal == 0 and nonZeroElementPos < n and nonZeroElementPos != n-1:
                nonZeroElementPos += 1
                curNonZeroElementVal = nums[nonZeroElementPos]
            if nums[i] == 0:
                if i >= nonZeroElementPos:
                    nonZeroElementPos = i + 1
                if nonZeroElementPos < n:
                    curNonZeroElementVal = nums[nonZeroElementPos]
                while curNonZeroElementVal == 0 and nonZeroElementPos < n and nonZeroElementPos != n - 1:
                    nonZeroElementPos += 1
                    curNonZeroElementVal = nums[nonZeroElementPos]
                if nonZeroElementPos < n and nums[nonZeroElementPos] != 0:
                    temp = nums[i]
                    nums[i] = nums[nonZeroElementPos]
                    nums[nonZeroElementPos] = temp
                    nonZeroElementPos += 1


if __name__ == "__main__":
    #
    start = time.perf_counter()
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    print(solution.moveZeroes(nums = nums))
    print(nums)
    end = time.perf_counter()
    print(f"test 1: {end - start:10.6f} sec")
    #
    start2 = time.perf_counter()
    nums = [0, 0]
    print(solution.moveZeroes(nums = nums))
    print(nums)
    end2 = time.perf_counter()
    print(f"test 2: {end2 - start2:10.6f} sec")
    #
    start3 = time.perf_counter()
    nums = [1, 0, 0]
    print(solution.moveZeroes(nums = nums))
    print(nums)
    end3 = time.perf_counter()
    print(f"test 3: {end3 - start3:10.6f} sec")
    #
    start4 = time.perf_counter()
    nums = [4,2,4,0,0,3,0,5,1,0]
    print(solution.moveZeroes(nums = nums))
    print(nums)
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
