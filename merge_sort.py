def merge_sort(my_list):
    n = len(my_list)
    if n <= 1:
        return my_list

    # Find the middle point and divide the list into two halves
    mid = n // 2  # Use integer division
    left = merge_sort(my_list[:mid])  # Recursively sort the left half
    right = merge_sort(my_list[mid:])  # Recursively sort the right half

    # Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    i = 0  # Pointer for the left half
    j = 0  # Pointer for the right half
    merged = []  # This will store the sorted list

    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # If there are remaining elements in left or right, append them
    merged.extend(left[i:])  # Append remaining elements in left
    merged.extend(right[j:])  # Append remaining elements in right

    return merged



my_list = [5, 2, 4, 7, 1, 3, 2, 6]

print("Given array is:")
for num in my_list:
    print(f"{num}", end=" ")

# Call merge_sort to sort the list
sorted_list = merge_sort(my_list)
print("\n\nSorted array is:")
for num in sorted_list:
    print(f"{num}", end=" ")

