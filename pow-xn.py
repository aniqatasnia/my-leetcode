# # my solution (doesn't work for large inputs of n)
# recursion only I think maybe idk
# O(n!) I'm pretty sure
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#         else:
#             res = x * self.myPow(x, abs(n) - 1)
#             return res if n >= 0 else 1/res

# neetcode solution O(log n)
# recursion + memoization
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            res = helper(x, n // 2)
            res = res * res 
            return x * res if n % 2 else res
    
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
