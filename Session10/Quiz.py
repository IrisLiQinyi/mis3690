# t = ['a', 'b', 'c', 'd', 'f', 'e']
# print(t[0:2])

# sorted(t)
# t
# t.sort()
# t
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
        # if c not in d:
        #     d[c] = 1
        # else:
        #     d[c] += 1
    return d
h = histogram('Bookkeeper')
print(h)

# number_of_e = h.get('e', 0)
# number_of_a = h.get('a', 0)
# print(number_of_e)
# print(number_of_a)
# a = h.get('a',0)

# a = [1, 2, 3]
# b = [1, 2, 3]
# b is a

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    global numFibCalls
    numFibCalls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


numFibCalls = 0
fibArg = 10

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0


print(fib_efficient(fibArg))
print('function calls', numFibCalls)