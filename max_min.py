def max_min(k, arr):
    arr.sort()
    min_unfair = arr[-1]
    for i in range(len(arr) - k + 1):
        unfair = arr[i + k - 1] - arr[i]
        if unfair < min_unfair:
            min_unfair = unfair
    return min_unfair
