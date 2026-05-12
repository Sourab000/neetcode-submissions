class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = []
        res = []

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for n,c in freq.items():
            count.append([c, n])

        count.sort(reverse = True)
        
        for i in range(k):
            res.append(count[i][1])
        
        return res

        
        
        