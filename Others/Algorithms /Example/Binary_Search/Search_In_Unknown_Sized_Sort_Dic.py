"""
Description
Given a integer dictionary A of unknown size, where the numbers in the dictionary are sorted in ascending order, determine if a given target integer T is in the dictionary. Return the index of T in A, return -1 if T is not in A.

Assumptions

dictionary A is not null
dictionary.get(i) will return null(Java)/INT_MIN(C++)/None(Python) if index i is out of bounds
Examples

A = {1, 2, 5, 9, ......}, T = 5, return 2
A = {1, 2, 5, 9, 12, ......}, T = 7, return -1
# Definition for a unknown sized dictionary.
# class Dictionary(object):
#   def get(self, index):
#     pass
"""


Solution(object):
  def search(self, dic, target):
    """
    input: Dictionary dic, int target
    return: int
    """
    # write your solution here


    j = 0
    i = 1
    while dic.get(i) and dic.get(i) < target:
      i *= 2

    left = j
    right = i
    while left <= right:
      mid = (left + right) / 2:
        left = mid + 1
      elif not dic.get(mid) or dic.get(mid) > target:
        right = mid - 1
      else:
        return mid
    return -1
