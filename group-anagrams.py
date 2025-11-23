from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # default dict --> dict with values as a list
        
        for s in strs:
            count = [0] * 26 # letters a - z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        
        return list(result.values())

# alternative if you don't want to import defaultdict
# def groupAnagrams(strs):
#     result = {}
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord("a")] += 1
#         key = tuple(count)
#         if key in result:
#             result[key].append(s)
#         else:
#             result[key] = [s]
    
#     return list(result.values())
