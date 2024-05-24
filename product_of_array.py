import functools
import time
import matplotlib.pyplot as plt


# Function with space complexity O(n) and time complexity O(n)
def product_of_array(nums):
    if len(nums) == 0:
        return []
    total = functools.reduce(lambda x, y: x * y, nums)
    return [total // x for x in nums]


# More efficient solution with space complexity O(1) and time complexity O(n)
def product_of_array_efficient(nums):
    n = len(nums)
    result = [1] * n
    product = 1
    for i in range(n):
        result[i] = product
        product *= nums[i]

    product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= product
        product *= nums[i]
    return result


# Measure the execution time for both functions
def measure_time(func, nums):
    start_time = time.time()
    func(nums)
    end_time = time.time()
    return end_time - start_time


# Input sizes to test
input_sizes = [10, 100, 400, 500, 600]

# Lists to store execution times
times_product_of_array = []
times_product_of_array_efficient = []

# Test the functions with various input sizes
for size in input_sizes:
    nums = list(range(1, size + 1))  # Generate a list of given size

    # Measure time for product_of_array
    time_taken = measure_time(product_of_array, nums)
    times_product_of_array.append(time_taken)

    # Measure time for product_of_array_efficient
    time_taken = measure_time(product_of_array_efficient, nums)
    times_product_of_array_efficient.append(time_taken)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, times_product_of_array, label='product_of_array', marker='o')
plt.plot(input_sizes, times_product_of_array_efficient, label='product_of_array_efficient', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time Comparison')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Use logarithmic scale for better visualization
plt.show()
