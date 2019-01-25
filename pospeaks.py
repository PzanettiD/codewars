def pick_peaks(arr):
    #your code here
    pos = []
    peaks = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i + 1]:
            pos.append(i)
            peaks.append(arr[i])
        if arr[i] > arr[i - 1] and arr[i] == arr[i + 1]:
            a = 0
            while True:
                if arr[i + 1 + a] == arr[len(arr) - 1]: 
                    break 
                if arr[i + 1 + a] == arr[i]:
                    a += 1
                if arr[i + 1 + a] < arr[i]:
                    pos.append(i)
                    peaks.append(arr[i])
                    break
                elif arr[i + 1 + a] > arr[i]:
                    break
        
    return {"pos": pos, "peaks": peaks}

print(pick_peaks([20, 5, 2, 11, 8, 6, 8, 11, 19, 16, 18, 17, -5, 9, 9, 6, 8, 0]))