class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # hashmap containing array of arrays of anagrams (strings in strs) we want to return
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1 # storing the frequency of letters in s in an array mapping its indices to letters in the alphabet
            key = tuple(count) # can't use arrays as keys for dicts in python
            res[key].append(s) # add this string to the final dictionary to return of arrays of arrays of anagrams

        return list(res.values()) # convert values of dict (tuple of arrays of anagrams) in result dict to a list and return it 
