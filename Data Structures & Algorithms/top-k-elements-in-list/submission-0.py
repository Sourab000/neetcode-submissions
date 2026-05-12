class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            
            if n not in freq:
                freq[n] = 0
            freq[n] += 1

        res = sorted(freq.keys(), key = lambda x: freq[x], reverse = True)

        return res[:k]

        
        
        