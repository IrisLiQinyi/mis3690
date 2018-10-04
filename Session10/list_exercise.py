AFC_east = ['New England Patriots', 'Bafflo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42,123]
empty = []
print (AFC_east, numbers, empty)
print ('Bafflo Bills' in AFC_east)
# ['spam',2.0, 5, [10,20]]
AFC_east[3] = 'New York Giants'
print (AFC_east)

#Traversing a list
for team in AFC_east:
    print(team)
numbers = [2,0,1,6,9]
for i in range(len(numbers)):
    numbers[i]=numbers[i]*2

print(numbers)

my_list = ['spam', 1, ['New England Patriots',\
                         'Buffalo Bills', 'Miami Dolphins',\
                         'New York Giants'],\
                         [1, 2, 3]]
print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

[0] *4
t = ['a', 'b', 'c', 'd', 'e', 'f']
# t[1:3] = ['x','y']
# print(t)
# print(t[1:3])
# print(t[3:6])
print(t[::2])
print(t[1::2]) #first : where to start 2nd : where to end 3rd: step
t.append('z') #Add an item to the end of the list add a list as an element 
print(t)
t.extend('e') #combine two list together
print(t)
t.sort(key=None, reverse=False)
print(t)

t[1] = ['g','h']
print(t)

# def nested_sum(t):
#     """Computes the total of all numbers in a list of lists.
#     t: list of list of numbers
#     returns: number
#     Expected output:
#     >>> t = [[1, 2], [3], [4, 5, 6]]
#     >>> nested_sum(t)
#     21
#     """
    


# def cumsum(t):
#     """Computes the cumulative sum of the numbers in t.
#     t: list of numbers
#     returns: list of numbers
#     Expected output:
#     >>> t = [1, 2, 3]
#     >>> cumsum(t)
#     [1, 3, 6]
#     """
#     total = 0
#     res = []
#     for x in t:
#         total += x
#         res.append(total)
#     return res
# t = [1,2,3]
# print(cumsum(t))

# def middle(t):
#     """Returns all but the first and last elements of t.
#     t: list
#     returns: new list
#     Expected output:
#     >>> t = [1, 2, 3, 4]
#     >>> middle(t)
#     [2, 3]
#     """
    
#     return t[1:-1]
# t = [1,2,3,4]
# print(middle(t), "The memoty address of middlet is:" id(middle(t)))
# print (t)

# def chop(t):
#     """Removes the first and last elements of t.
#     t: list
#     returns: None
#     Expected output:
#     >>> t = [1, 2, 3, 4]
#     >>> chop(t)
#     >>> t
#     [2, 3]
#     """
#     del t[0]
#     del t[-1]
# t = [1,2,3,4,5,6]    
# chop(t)
# print(t)
# def is_sorted(t):
#     """Checks whether a list is sorted.
#     t: list
#     returns: boolean
#     Expected output:
#     >>> is_sorted([1, 2, 2])
#     True
#     >>> is_sorted(['b', 'a'])
#     False
#     """
#     a = 0
    
#     if t[a]<t[a+1] or t[a]==t[a+1]:
#             return True
#     else:
#             return False
# t = ['b','a']
# print (is_sorted(t))

# a = [1,33,5,6,7,90]
# a.sort() # sort a internally
# a
# sorted(a)# print out the sorted a but won't change a 

# def is_anagram(word1, word2):
#     """Checks whether two words are anagrams
#     Two words are anagrams if you can rearrange the letters from one to 
    # spell the other.
    # word1: string or list
    # word2: string or list
    # returns: boolean
    # Expected output:
    # >>> is_anagram('stop', 'pots')
    # True
    # >>> is_anagram('different', 'letters')
    # False
    # >>> is_anagram([1, 2, 2], [2, 1, 2])
    # Ture
    # """
    # return sorted(word1) == sorted(word2)
    # a = 0
    # if len(word1) == len(word2):
    #     return False
    # else:
    #     if word1[a] == word2[-1-a]:
    #         return True
    #     else: 
    #         return False
# print(is_anagram('apple','elpap'))

# def has_duplicates(s):
#     """Returns True if any element appears more than once in a sequence.
#     s: string or list
#     returns: bool
#     output:
#     >>> print(has_duplicates('cba'))
#     False
#     >>> print(has_duplicates('abba'))
#     True
#     """
#     for i in s:
#         if s.count(i)>1:
#             return True
#     return False
# print(has_duplicates('abba'))

def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    
    for i in range(len(s)-1): #compare two elements use range
        if s[i] == s[i+1]:
            return True
    return False
print(has_adjacent_duplicates('abbc'))

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    # print(nested_sum(t))

    # t = [1, 2, 3]
    # print(cumsum(t))

    # t = [1, 2, 3, 4]
    # print(middle(t))
    # chop(t)
    # print(t)

    # print(is_sorted([1, 2, 2]))
    # print(is_sorted(['b', 'a']))

    # print(is_anagram('stop', 'pots'))
    # print(is_anagram('different', 'letters'))
    # print(is_anagram([1, 2, 2], [2, 1, 2]))

    # print(has_duplicates('cba'))
    # print(has_duplicates('abba'))


if __name__ == '__main__':
    main()


