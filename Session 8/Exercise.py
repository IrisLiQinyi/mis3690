# team = 'New England Patriots'
# def find(word,letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1
# print(find(team,'E'))

# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'n':
#         count = count + 1
# print(count)

# team = 'New England Patriots'
# # new_team = team.upper()
# # print(new_team)
# index = team.find('a')
# print(index)

# name = 'dobd'
# print(name.find('b',1,3))

#Exercise 3
n = 'hey jude'
str.capitalize(n) #capitalize the first letter of the string

'hey nice to meet you'.split(' ') #split the string by space

'www.example.com'.strip('cmow.')
#whatever in the '' will be split

com = '#.....Section 3.2.1 Issue # 32#'
com.strip('.#!')

'New England Patriots'.replace('e','g')


####4/1

def receipt(x):
    new=0
    a=0
    for i in x:
        i=x[a]
        n=ord(i)-96
        a=a+1
        new=n+new
    return new
# print (receipt('bananas'))
# print(receipt('rice'))
print('total = ', receipt('bananas')+receipt('rice')+receipt('paprika')+receipt('potato chips'))
###########4/2
def receipt(x):
    new=0
    a=0
    for i in x:
        i=x[a]
        n=ord(i)-96
        a=a+1
        new=n+new
    return new
# print(receipt('bananas'))
# print(receipt('rice'))
print('total = ', receipt('bananas')+receipt('rice')+receipt('paprika')+receipt('potato chips'),'.00')
#######4/3
def receipt(x,y,z):
    new=0
    a=0
    highest=max(x,y,z,key=len)
    for i in (x,y,z):
        i=(x+y+z+h)[a]
        n=ord(i)-96
        a=a+1
        new=n+new
    return new

# print (receipt('bananas'))
# print(receipt('rice'))
# print('total = ', receipt('bananas')+receipt('rice')+receipt('paprika')+receipt('potato chips'))
