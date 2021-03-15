def average(prev_avg, x, n):
    return ((prev_avg * n + x) // (n + 1))


# Prints average of a stream of numbers
def streamAvg(arr):
    n=len(arr)
    avg = 0
    for i in range(n):
        avg = average(avg, arr[i], i)
        print("Average of ", i + 1," numbers is ", avg)


arr=[99,95,97]
D=streamAvg(arr)
