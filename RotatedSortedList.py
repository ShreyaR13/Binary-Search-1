"""
33. Search in a rotated sorted array
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such
that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
Time complexity O(log n)
Space complexity O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right  = len(nums) - 1

        while left <= right:
            mid = left + (right-left)//2

            if target == nums[mid]:
                return mid

            #if left is sorted
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # if right is sorted
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1