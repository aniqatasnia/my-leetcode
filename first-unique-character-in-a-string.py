class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        
        return -1
# I feel like there's another way to do it, though...like with a seen queue and/or two pointers...It was listed under queues in the Roblox problems list and I can't tell if this implements that queue solution or not.
