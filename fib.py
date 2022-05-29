# def fib(n: int) -> int:
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

def fib(n: int) -> int:
    a = 0
    b = 1
    for i in range(n):
        a, b = b, (a + b)
    return a
    
#print("Fib[n]:", fib(205))
print("Fib[n]:", fib(205))
