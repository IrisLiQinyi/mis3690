# def fabonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fabonacci(n-2) + fabonacci(n-1)
# print(fabonacci(3))

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n
print(factorial(6))
