# Solution 1
class Solution1:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        
        return -1
# I feel like there's another way to do it, though...like with a seen queue and/or two pointers...
# It was listed under queues in the Roblox problems list and I can't tell if this implements that queue solution or not.

# Solution 2
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        unique = {}
        for c in s:
            if c not in seen:
                unique[c] = c
                seen[c] = c
            elif c in unique:
                unique.pop(c)

        for i, c in enumerate(s):
            if c in unique:
                
                return i
        
        return -1
    # Okay there was another way to do it (with a seen queue at least, but haven't tried pointers yet) but it was effectively the same as the hashmap solution.
    # Wait unless a queue has to be implemented as FIFO, I forgot shoot. 
    # But even then how would you look up/would looking up allow it to be as efficient or more efficient than dictionary hashmap solution?
    # You could also sort it, and then use a stack/queue, or even two pointers (sorting takes extra time complexity tho, O(nlogn))
