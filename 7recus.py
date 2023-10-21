#!/usr/bin/python3
def recursive_binary_search(arr, target, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start > end:
        return False

    mid = (start + end) // 2

    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, end)
    else:
        return recursive_binary_search(arr, target, start, mid - 1)

numbers = list(x for x in range(100))
target_number = int(input("Enter the number you want to search for: "))

result = recursive_binary_search(numbers, target_number)

if result:
    print(f"The number {target_number} was found in the list.")
else:
    print(f"The number {target_number} was not found in the list.")
