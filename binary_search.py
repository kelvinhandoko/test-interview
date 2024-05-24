# binary search algo with recursion
# Time complexity: O(log n)
# Space complexity: O(log n)

def binary_search(arr, item):
    arr.sort()
    half = len(arr) // 2
    if arr[half] == item:
        return half
    elif arr[half] > item:
        return binary_search(arr[:half], item)
    else:
        return half + binary_search(arr[half:], item)


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

# binary search algo without recursion
# Time complexity: O(log n)
# Space complexity: O(1)
# def binary_search(arr, item):
#     arr.sort()
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
