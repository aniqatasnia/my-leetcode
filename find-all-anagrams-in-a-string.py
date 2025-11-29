class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window with two pointers
        if len(p) > len(s):
            return []
        pCount, sCount = {}, {}
        # first iteration of checking sCount anagram with pCount,just easier to do it that way
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1

        res = [0] if pCount == sCount else []
        l = 0

        # all iterations after first iteration, just easier to do it that way
        for r in range(len(p), len(s)):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            sCount[s[l]] -= 1 # remove the letter on the left (decrease its count by 1)

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l +=1
            if sCount == pCount:
                res.append(l)
        
        return res
