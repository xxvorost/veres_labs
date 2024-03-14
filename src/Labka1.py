def mono(arr):
    if arr[0] > arr[len(arr) - 1]:
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                return False
    else:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
    return True