

# LeetCode. Yandex Task List. 146. LRU Cache

'''

146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4



Constraints:

    1 <= capacity <= 3000
    0 <= key <= 104
    0 <= value <= 105
    At most 2 * 105 calls will be made to get and put.

Accepted
891,892
Submissions
2,329,315


Related Topics
Hash Table, Linked List, Design, Doubly-Linked List

Similar Questions
LFU Cache
Hard
Design In-Memory File System
Hard
Design Compressed String Iterator
Easy
Design Most Recently Used Queue
Medium

'''


import math
import time
import collections
from typing import List, Dict
import numpy as np
import random as rnd
import itertools as it
from collections import defaultdict, Counter
import re
from functools import reduce
from functools import lru_cache
from bisect import bisect, bisect_left


class ListNode:
    def __init__(self, key=-1, val=-1, prevRef=None, nextRef=None):
        self.key = key
        self.val = val
        self.prev = prevRef
        self.next = nextRef


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = ListNode()  # initializing head and tail nodes
        self.head.next = self.tail  # setting up Doubly Linked List through head->tail
        self.tail.prev = self.head  # setting up Doubly Linked List through head<-tail

    def addToHead(self, node: ListNode) -> None:
        if node is not None:
            # add node at its position
            node.prev = self.head
            node.next = self.head.next
            # let other nodes know new node has been added at its position
            self.head.next.prev = node
            self.head.next = node

    def popNode(self, node: ListNode) -> None:
        # get prev and next nodes for provided node
        node_next = node.next
        node_prev = node.prev
        # change pointers of prev and next nodes to actually delete given node
        node_prev.next = node_next
        node_next.prev = node_prev

    def popFromTail(self, lruHash: Dict[int, ListNode]) -> int:
        # delete node from tail, it is the least recently used one
        node = self.tail.prev
        self.popNode(node)
        # once the node is deleted from tail, we don't need it in hashmap, so delete
        lruHash.pop(node.key)
        '''
        node_prev = node.prev
        # change pointers to actually delete tail's node
        self.tail.prev = node_prev
        node_prev.next = self.tail
        '''

    def moveToHead(self, node: ListNode, lruHash: Dict[int, ListNode]) -> None:
        # delete previously present node/node with old value and add new node
        # this moves node to head
        current_node = lruHash[node.key]
        self.popNode(current_node)
        self.addToHead(node)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # tells us the capacity of LRU, we need to keep
        self.lruHash = {}  # stores key: node pair to easily access nodes
        self.doublyLinkedList = DoublyLinkedList()

    def get(self, key: int) -> int:
        # key is present in LRU then move it to head bcoz recently used and return value, don't return key
        if key in self.lruHash:
            node = self.lruHash[key]
            self.doublyLinkedList.moveToHead(node, self.lruHash)
            return self.lruHash[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # we will have to either update or insert new key, value pair to
        # Doubly Linked List and LRU cache, here named lruHash
        node = ListNode(key, value)
        if key in self.lruHash:
            # to update value, we should move node to head
            # bcoz it is a recently used node
            self.doublyLinkedList.moveToHead(node, self.lruHash)
            self.lruHash[key] = node
        else:
            # to insert key, value, we can simply add node to head
            # which in return would also signify recently used node
            self.doublyLinkedList.addToHead(node)
            self.lruHash[key] = node
            # at any point of time, we add an extra node, we can pop Least Recently Used from tail of Doubly Linked List and LRU_hash so it doen't give any ambiguity later
            if len(self.lruHash) > self.capacity:
                self.doublyLinkedList.popFromTail(self.lruHash)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


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
