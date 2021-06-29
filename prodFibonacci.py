#Product of consecutive Fibonacci numbers

# def productFib(prod):
#     return

def productFib(prod):
    fibSequence = fib(prod)
    arr = []
    for i in range(1,len(fibSequence)):
        for x in range(1,len(fibSequence)):
         if i * x == prod:
            arr.append(i)
    return arr

def fib(n):
    fibonacciSeries =[0,1]
    if n > 2:
        for i in range(2,n+1):
                nextNumber = fibonacciSeries[i-1] + fibonacciSeries[i-2]
                fibonacciSeries.append(nextNumber)
    return fibonacciSeries
print(productFib(4895))
