class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)
        heap = [(-val, key) for key, val in counter.items()]
        heapq.heapify(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



        