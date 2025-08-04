class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # Step 2: Push into max-heap using (-frequency, num)
        max_heap = []
        for num, freq in count.items():
            heapq.heappush(max_heap, (-freq, num))

        # Step 3: Pop k elements
        result = []
        for _ in range(k):
            freq, num = heapq.heappop(max_heap)
            result.append(num)

        return result