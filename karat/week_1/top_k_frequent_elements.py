#https://leetcode.com/problems/top-k-frequent-elements/description/


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    lookup = defaultdict(int)
    result = []
    tmp = set()

    for num in nums:
        lookup[num] += 1
    values = lookup.values()

    max_heap = [-1 * val for val in values]
    heapq.heapify(max_heap)

    for i in range(k):
        tmp.add(-1 * heapq.heappop(max_heap))

    for key, val in lookup.items():
        if val in tmp:
            result.append(key)
    return result


"""
Time Complexity -> O(n)
Space Complexity -> O(n)
"""