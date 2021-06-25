cube = lambda x: x*x*x
def fibonacci(n):
    fibonacciSeries = [0,1]
    if n>2:
        for i in range(2, n):
            nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
            fibonacciSeries.append(nextElement)
    return fibonacciSeries        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))