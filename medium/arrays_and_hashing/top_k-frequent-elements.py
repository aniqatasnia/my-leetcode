# Bucket Sort algorithm 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # Dictionary of frequencies of each number in nums
        freq = [[] for i in range(len(nums) + 1)] # Frequency of each num as the index and the number(s) with that frequency (so a list) as the values to go through the top k most frequent values later
        res = []
        for n in nums:
            count[n] += 1

        for n, c in count.items(): # Populating freq from count
            freq[c].append(n)

        for c in range(len(freq) - 1, 0, -1): # Getting top k most frequent numbers in nums
            for n in freq[c]:
                res.append(n)
                if len(res) == k:
                    
                    return res

        # Question that came up while solving (and answered):
        # Why wasn't freq = [[]] * len(nums) the same as freq = [[] for i in range(len(nums) + 1)]?
