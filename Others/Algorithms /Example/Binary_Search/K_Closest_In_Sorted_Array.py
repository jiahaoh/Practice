"""
Description
Given a target integer T, a non-negative integer K and an integer array A sorted in ascending order, find the K closest numbers to T in A.

Assumptions

A is not null
K is guranteed to be >= 0 and K is guranteed to be <= A.length
Return

A size K integer array containing the K closest numbers(not indices) in A, sorted in ascending order by the difference between the number and T.
Examples

A = {1, 2, 3}, T = 2, K = 3, return {2, 1, 3} or {2, 3, 1}
A = {1, 4, 6, 8}, T = 3, K = 3, return {4, 1, 6}
"""

class Solution(object):
  def kClosest(self, array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    # write your solution here
    print array
    if not array:
      return -1
    elif k == 0:
      return []
    elif len(array) == 1:
      return array

    result = []
    left = 0
    right = len(array) - 1
    while left < right - 1:
      mid = (left + right) / 2
      if array[mid] > target:
        right = mid
      elif array[mid] < target:
        left = mid
      else:
        result.append(array[mid])
    result.append(array[left] if abs(array[left] - target) < abs(array[right] - target) else array[right])

    left = array.index(result[0]) - 1
    right = array.index(result[0]) + 1
    while len(result) < k and (left >= 0 or right < len(array)):
      if right >= len(array):
        result.append(array[left])
        left -= 1
      elif left < 0:
        result.append(array[right])
        right += 1
      else:
        print left,right
        if abs(array[left] - target) < abs(array[right] - target):
          result.append(array[left])
          left -= 1
        else:
          result.append(array[right])
          right += 1

    return result
                                    
