class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum) # because over here you check if either the 
            # before or  after was bigger or not, whether it's implicit (by the current maxSub 
            # value) or explicit (by comparing curSum to maxSub), so then you've addressed 
            # even the situation where you've subtracted from the sum and it still might be 
            # used to make a subarray with a sum bigger than the currently held maximum sum
            # subarray with future contiguous numbers

        return maxSub
