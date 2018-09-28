fin = open("words.txt")


# counter = 0
# for line in fin:
#     word = line.strip()
#     counter += 1
# print(counter)


# def read_long_words():
#     """
#     prints only the words with more than 20 characters
#     """
    
#     for line in fin:
#         word = line.strip()
#         if len(word) > 20:
#             print (word)
      






# def has_no_e(word):
#     """
#     returns True if the given word doesn’t have the letter “e” in it.
#     """
#     for letter in word:
#         if letter == 'e' or letter == 'E':
#             return False
#     return True





# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('Epslon'))

def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for i in word:
        if i in forbidden:
            return False
    return True


print(avoids('Babson', 'ab'))
print(avoids('College', 'ab'))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for i in word:
        if i not in available:
            return False
        return True



print(uses_only('Babson', 'aBbsonxyz'))
print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for i in required:
        if i not in word:
            return False
    return True

print(uses_all('Babson', 'abs'))
print(uses_all('college', 'abs'))


# def is_abecedarian(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     a = word[0]
#     for i in word:
#         if i < a:
#             return False
#         a = c
#     return True

        


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))

def is_abecedarian(word):
    # n = 0
    # a = word[n]
    # b = word[n+1]
    # while n < len(word):
    #     if a > b:
    #         return False
    #         n =+1
    # return True
    if word[0] > word[1]:
        return False 
    return is_abecedarian(word[1:])
    

print(is_abecedarian('abs'))
print(is_abecedarian('college'))

