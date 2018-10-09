# names = ['Defne', 'Jack', 'Angela']
# scores = [95,75,85]
# # Dictionary: a better way to represent key:value relationship
# #Association of a key and a value is called a key-value pair or an item
# grades = dict()
# print(grades)

# grades['Defne'] = 90 
# print(grades)
# grades['Jack'] = 75
# print (grades)
# grades = {'Defne': 90, 'Jack': 75, 'Angela': 85}
# print (grades)
# print(grades['Jack'])

# print(len(grades))
# 'Jack' in grades #only check the keys
# 90 in grades.values() #check the values

def histogram(s):
    # d = dict()
    # for c in s:
    #     if c not in d:
    #         d[c] = 1
    #     else:
    #         d[c] += 1
    # return d


# number_of_e = h.get('e', 0)
# number_of_a = h.get('a', 0)
# print(number_of_e)
# print(number_of_a)

    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
   

h = histogram('Bookkeeper')
print(h)

#Looping and dictionaries
def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('Massachusetts')
print_hist(h)

for key in sorted(h):
    print(key, h[key])
#reverse lookup
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError() #raise causes an exception
h = histogram('Massachusetts')
key = reverse_lookup(h,4)
print (key)

#Dictionaries and lists
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val]=[key]
        else:
            inverse[val].append(key)
    return inverse
hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)

# t = [1,2,3]
# d = dict()
# d[t] = 'oops'

#fibonacci
def fibonacci(n):
    pass
    if n == 0:
        fibonacci[n]=0 
        return fibonacci[n]
    else:
        fibonacci[n] = 1

#global variables
global_va = 5
def func1():
    # global global_va
    global_va = 40
def func2():
    print (global_va)

func1()
func2()
#exercise 3/1
f = open('words.txt')
def function_word():
    func = dict()
    for i in f:
        word = i.strip()
        func[word]=word
    return func
function_word()

# exercise 3/2
def has_duplicates(n):
    dictionary = {}
    for i in n:
        dictionary[i] = 1 + dictionary.get(i,0)
        if dictionary[i] > 1:
            return True
    return False
# l1 = [1,2,3,3,4,5,5]
l1 = [1,2,3]
print(has_duplicates(l1))