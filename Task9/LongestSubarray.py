

# LeetCode. Yandex Task List. 1493. Longest Subarray of 1's After Deleting One Element

'''

1493. Longest Subarray of 1's After Deleting One Element
Medium

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4

Example 5:

Input: nums = [0,0,0]
Output: 0



Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.

Accepted
30,851
Submissions
51,601


Related Topics
Math, Dynamic Programming, Sliding Window

Similar Questions
-

Hide Hint 1
Maintain a sliding window where there is at most one zero on it.



Intuition
There are only 3 cases that we need to take care of:
(1) only zeros in nums
(2) only ones in nums
(3) others

Complexity
Time O(N)
Space O(N)

Solution

def longestSubarray(self, nums: List[int]) -> int:
	# We get the group's key and length first, e.g. [0,1,1,1,0,1,1,0,1] -> [[0 , 1], [1, 3], [0, 1], [1, 2], [0, 1], [1, 1]]
	groupby = [ [k, len(list(i))] for k, i in itertools.groupby(nums)]


	if len(groupby) == 1:
		# case(1) only zeros in nums
		if groupby[0][0] == 0:
			return 0
		# case(2) only ones in nums
		elif groupby[0][0] == 1:
			return groupby[0][1] - 1
	else:
		# case(3) others
		res = max([times for i,times in groupby if i==1])
		for i in range(1, len(groupby)-1):
			# if both sides have ones and are separated by only 1 zero
			if groupby[i][0] == 0 and groupby[i][1] == 1:
				res = max(res, groupby[i-1][1] + groupby[i+1][1])
		return res

Similar Sliding Window Problems
1156. Swap For Longest Repeated Character Substring

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
    def longestSubarray(self, nums: List[int]) -> int:
        subArrSizesList = list()
        firstSubArrSize = 0
        secondSubArrSize = 0
        n = len(nums)
        if nums.count(0) == 0:
            return n-1
        for i in range(0, n):
            if nums[i] != 0:
                firstSubArrSize += 1
            elif nums[i] == 0:
                for j in range(i+1, n):
                    if nums[j] != 0:
                        secondSubArrSize += 1
                    else:
                        break
                subArrSizesList.append(firstSubArrSize + secondSubArrSize)
                firstSubArrSize = 0
                secondSubArrSize = 0
        return max(subArrSizesList)


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
