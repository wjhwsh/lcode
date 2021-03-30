class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            storedIndex = left
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[storedIndex], nums[i] = nums[i], nums[storedIndex]
                    storedIndex += 1
            nums[storedIndex], nums[right] = nums[right], nums[storedIndex]
            return storedIndex
            
        
        def select(left, right, k_smallest):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            if pivot_index == k_smallest:
                return nums[pivot_index]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)
            
        
        return select(0, len(nums) -1 , len(nums) - k)
    
    
    
