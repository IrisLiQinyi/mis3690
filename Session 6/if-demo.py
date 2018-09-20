# age = input('please enter your age: ')
# if int(age) > 6:
#     print('teenager')
# elif age > 18: #else if can have as many as we want
#     print ('adult')
# else:
#     print('kid')

# x = 6
# y = 4
# if x == y:
#     print('x and y are euqual')
# else:
#     if x < y:
#         print ('x is less than y')
#     else:
#         print ('x is greater than y')

#Exercise 1
# weight = input ('weight: ')
# height = input ('height: ')
# BMI = 703 * float(weight) / float(height) ** 2
# if BMI < 18.5:
#     print('Underweight')
# elif BMI < 25:
#     print('Normal Weight')
# elif BMI < 30:
#     print('Overweight')
# else:
#     print('Obesity')

#2
# varA = input('variable A: ')
# varB = input('variable B: ')
# def compare(varA, varB):
#     if isinstance(varA, str) or isinstance(varB, str):
#         print('string involved')
#     else: 
#         if int(varA) > int(varB):
#             print ('Bigger')
#         elif int(varA) < int(varB):
#             print ('smaller')
#         else:
#             print('equal')
# a = 'hello'
# b = 3
# c = 6
# compare(a,b)
# def cigar_party(cigars, is_weekend):
#   if is_weekend and cigars >= 40:
#     return True
#   else:
#     if 40 <= int(cigars) <= 60:
#       return True
#     else:
#       return False
# print(cigar_party(30, True))

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)

# countdown(7)

# def print_n(s,n):
#     if n <= 0:
#         return
#     print(s)
#     print_n(s,n-1)
    
# print_n(hello,3)

# def print_n(s,n):
#   if n <=0:
#     return
#   print(s)
#   print_n(s,n-1)

# print_n("OMG",3)

