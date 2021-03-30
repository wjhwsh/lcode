class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)
        return res
    
    def twoSum(self, nums, i, res):
        seen = set()
        j = i + 1
        while j < len(nums):
            target = - (nums[i] + nums[j])
            if target in seen:
                res.append([nums[i], nums[j], target])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
            
