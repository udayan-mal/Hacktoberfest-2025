def largest(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

def largest_using_sort(arr):
    arr.sort()
    return arr[-1]

if __name__ == "__main__":
    arr = [10, 324, 45, 90, 9808]
    print(largest(arr))
    print(largest_using_sort(arr))
