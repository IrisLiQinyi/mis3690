from datetime import datetime

now = datetime.today()
print(now)

# def days_until_birthday(birthday):
#     """How long until my next birthday?"""
#     today = datetime.today()
#     next_bir = datetime(today.year,birthday.month,birthday,day)
#     days.day = next_bir - today
#     return days


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    if b2.date == b1.date:
        if daytime(now.year - b2.year) == (now.year - b1.year) * 2:
            print('The older person is twice as old as the younger one')
        else:
            print('not double')
b1 = datetime(2017, 12, 25)
b2 = datetime(2016, 12, 25)
print(b2.date)
# print('Double Day', end=' ')
print(double_day(b1, b2))
  


def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week
    today = datetime.today

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1997, 10, 24)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2017, 12, 25)
    b2 = datetime(2016, 12, 25)
    print('Double Day', end=' ')
    print(double_day(b1, b2))


# def main():
#     datetime_exercises()


# if __name__ == '__main__':
#     datetime_exercises()
