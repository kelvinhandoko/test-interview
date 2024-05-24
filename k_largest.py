# k largest elements in an array
# Given an array of integers, find the k largest numbers in it.
#

# space complexity: O(1)
# time complexity: O(n log n)
def k_largest(arr, k):
    arr.sort()
    return arr[-k:]


# more efficient solution
# space complexity: O(k)
# time complexity: O(n log k)
def k_largest_heap(arr, k):
    from heapq import heappush, heappop
    heap = []
    for num in arr:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)
    return heap


print(k_largest([1, 23, 12, 9, 30, 2, 50], 1))  # [23, 30, 50]
