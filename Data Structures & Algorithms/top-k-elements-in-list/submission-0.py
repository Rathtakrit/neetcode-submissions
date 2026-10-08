class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        freq = [[] for i in range(0,len(nums)+1,1)]
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for n,c in count.items():
            freq[c].append(n)

        results = []
        for i in range(len(freq)-1,0,-1) :
            for j in freq[i]:
                results.append(j)
                if len(results) == k:
                    return results