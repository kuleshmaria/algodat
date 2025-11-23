"""
Implementation of Merge Sort in Python
Complexity: O(n*log(n))
"""

def _merge_sort(arr, left, right, comparator):
    if left == right:
        return [arr[left]]

    # divide
    mid = left + int((right-left)/2)
    l_arr = _merge_sort(arr, left, mid, comparator)
    r_arr = _merge_sort(arr, mid+1, right, comparator)

    # merge
    merged_arr = []
    li, ri = 0, 0
    m, n = len(l_arr), len(r_arr)
    while li < m and ri < n:
        if comparator(l_arr[li], r_arr[ri]):
            merged_arr.append(l_arr[li])
            li += 1
        else:
            merged_arr.append(r_arr[ri])
            ri += 1
    while li < m:
        merged_arr.append(l_arr[li])
        li += 1
    while ri < n:
        merged_arr.append(r_arr[ri])
        ri += 1

    return merged_arr

def merge_sort(arr, comparator = lambda x, y: x < y):
    n = len(arr)
    if n == 0:
        return []
    return _merge_sort(arr, 0, n - 1, comparator)

if __name__ == "__main__":
    unsorted_arr = [5, 3, 1, 2, 18]
    sorted_arr = merge_sort(unsorted_arr)
    print(sorted_arr)
