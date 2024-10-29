# Test the Linear search all indices
def linear_search_all_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)  
    return indices if indices else -1  

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search_all_indices(test_list, 5)
print(f"Linear for All Indices : Indices of 5 are {result}")


def find_insertion_point(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left  # The insertion point

# Test the function
sorted_list = [1, 3, 4, 6, 8, 9]
target = 5
insertion_point = find_insertion_point(sorted_list, target)
print(f"Insertion Point for {target} is at index {insertion_point}")
print("Updated list:", sorted_list)


# Linear Search with Comparison Count
def linear_search(arr, target):
    comparisons = 0
    for i, num in enumerate(arr):
        comparisons += 1
        if num == target:
            return i, comparisons
    return -1, comparisons

# Binary Search (Iterative) with Comparison Count
def binary_search(arr, target):
    left, right, comparisons = 0, len(arr) - 1, 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# Binary Search (Recursive) with Comparison Count
def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons
    mid = (left + right) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons + 1)
    return binary_search_recursive(arr, target, left, mid - 1, comparisons + 1)

def main():
    test_list, target = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 6
    sorted_list = sorted(test_list)

    for search, name in [(linear_search, "Linear Search"),
                         (lambda arr, tgt: binary_search(arr, tgt), "Binary Search (Iterative)"),
                         (lambda arr, tgt: binary_search_recursive(arr, tgt, 0, len(arr) - 1), "Binary Search (Recursive)")]:
        index, comparisons = search(test_list if "Linear" in name else sorted_list, target)
        print(f"{name}: Index of {target} is {index}, Comparisons made: {comparisons}")


# Integrate jump search into main()
def main():
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    target = 6
    sorted_list = sorted(test_list) 

    # Call jump_search with the sorted list and target
    index, comparisons = jump_search(sorted_list, target)
    print(f"Jump Search: Index of {target} is {index}, Comparisons made: {comparisons}")

def jump_search(arr, target):
    n = len(arr)
    step = int(n ** 0.5)  
    prev = 0  
    comparisons = 0  # To keep track of comparisons made

    # Jump through the array to find the potential block
    while prev < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1, comparisons 

    # Linear search within the blocka
    while prev < n and arr[prev] < target:
        comparisons += 1
        prev += 1
        if prev == min(step, n):
            return -1, comparisons 

    comparisons += 1
    if prev < n and arr[prev] == target:
        return prev, comparisons  # Return index and comparison count

    return -1, comparisons  

if _name_ == "_main_":
    main()