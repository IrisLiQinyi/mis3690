# b"toto\xfe\775"
# int("3f",16)
# repr(10.6)

import random

class_roster = {'Jonathan Beltran': 0, 'Allison Fernandez': 1, 'Siddhanth Goyal': 0,
 'Jingyu He': 0, 'Defne Ikiz': 0, 
'Zirui Jiao': 0, 'Pranjal Joshi': 0, 'Dong Hyun Kim': 0, 'Ha Min Ko': 0,
 'Kyle Lawson': 0, 'Christine Lee': 1, 'Connie Li': 1,
                'Qinyi Li': 0, 'Matthew Michalke': 0, 'Ho Wang Alastair Ng': 1, 'Jonghyun Park': 0, 
                'Alden Pexton': 2, 'Shriya Rathi': 2, 'Waylon Ryan': 1, 'Christian Thompson': 3, 
                'Angela Tsung': 2, 'Aaron Wendell': 0, 'Sarah Zazyczny': 0, 'Shiyue (Shirley) Zong': 0}
c = class_roster.values()
min_times = min(c)

pool = []
for i in class_roster:
    if class_roster[i] == min_times:
        pool.append(i)

random_name = random.choice(pool)
class_roster['Qinyi Li'] +=1

print(class_roster)