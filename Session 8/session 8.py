team = "New England Patriots"
# len(team)
letter = team[1]
print(letter)

# print(team[0])
# print(team[8])
# last = team[len(team)-1]
# print(last)
# last = team[-1] #-1 means the last one
# print(last)


# index = 0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index = index + 1

# for letter in team:
#     print(letter)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter =='O' or letter == 'Q':
#         print(letter+"u"+suffix)
#     else:
#         print(letter+suffix)

team = 'New England Patriots'
print(team[0:11])
team[0:4]
team[::2]
team[0:20:2]
team[::-2]

team='New England Patrios'
new_team=team[:12] + 'Seahawks'
print (new_team)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index +1
    return -1
print(find(team,'a'))

def find(word, letter):
    index = 0
    for i in range(len(team)):
        if team[i] == 'a':
            print (i)

for i, letter in enumerate(team):
    print(i,letter)


def count(s,l):
    index = 0
    for each in s:
        if each == 'l':
            index = index + 1
    return index
print(count(team,'a'))

team.split('e')

team.strip()

##3&4