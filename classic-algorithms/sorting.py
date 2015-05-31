def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) / 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp

n = [9, 18, 3, 49, 2, 45, 74, 23, 10, 68]
print "Original: " + " ".join(map(str, n))
merge_sort(n)
print "Sorted by Merge Sort: " + " ".join(map(str, n))

n = [73, 34, 1, 29, 15, 21, 59, 8, 37, 92]
print "Original: " + " ".join(map(str, n))
bubble_sort(n)
print "Sorted by Bubble Sort: " + " ".join(map(str, n))