def countNicePairs(self, nums):
    from collections import Counter
    freqs=Counter( num - int(str(num)[::-1]) for num in nums)
    return sum( (freq *(freq-1)//2 ) for freq in freqs.values()) % (10**9+7)