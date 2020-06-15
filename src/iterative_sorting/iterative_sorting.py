# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for s in range(i+1, len(arr)):
            if arr[s] < arr[smallest_index]:
                smallest_index = s
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # loop through the array, and swap num at cur_index with the smallest comparative num
        # increment cur_index
        # repeat

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    for i in range(len(arr) - 1, 0):
        for j in i - 1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # create left index and right index (starting at 0 and 1)
    # compare the indexes, if the right is < the left, swap
    # increment left and right index each time
    # if no swapping occurs, return the array.
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):
#     if len(arr) == 0:
#         return arr

#     if maximum == -1:
#         maximum = max(arr)

#     buckets = [0 for _ in range(maximum+1)]

#     for x in arr:
#         if x < 0:
#             return "Negative numbers not allowed"
#         buckets [x] += 1
#     # We have the counts of over value in our input array.
#     # Loop through our buckets, starting at the smallest index
#     j = 0
#     for i in range(len(buckets)):
#         while buckets [i] > 0:
#             arr[j] = i
#             j += 1
#             buckets[i] -= 1
