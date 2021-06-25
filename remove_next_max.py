if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_value=max(arr)
    arr.remove(max_value)
    for i in range(0,n):
        if max_value in arr:
                arr.remove(max_value)   
    next_max=max(arr)

    print(next_max)