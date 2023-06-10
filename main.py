from cs50 import SQL
import sys
import random

db = SQL('sqlite:///history.db')
R = '\033[0;31m'
W = '\033[0;37m'
G = '\033[0;32m'
B = '\033[0;34m'


def main():
    n = 6
    
    try:
        inp: int = int(input('1.Unit 1\n2.Unit 2\n3.Unit 3\n4.Unit 4\n5.The entire book (for men)'))

        if inp == 1:
            delete_multiple_lines(n)
            unit1()

        elif inp == 2:
            delete_multiple_lines(n)
            unit2()
        
        elif inp == 3:
            delete_multiple_lines(n)
            unit3()

        elif inp == 4:
            delete_multiple_lines(n)
            unit4()

        elif inp == 5:
            delete_multiple_lines(n)
            entire()

    except:
        print('There was an error')

def delete_multiple_lines(n=1):
    """Delete the last line in the STDOUT."""
    for _ in range(n):
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")

def unit1():
    n = 2

    try:

        inp: int = int(input('1.Chapter one\n'))

        if inp == 1:
            delete_multiple_lines(n)
            u1_lesson1()

    except:

        print('There was an error')

def unit2():
    n = 5

    try:

        inp: int = int(input('1.Chapter one\n2.Chapter two\n3.Chapter three\n4.Chapter four\n'))

        if inp == 1:
            delete_multiple_lines(n)
            u2_lesson1()

        elif inp == 2:
            delete_multiple_lines(n)
            u2_lesson2()

        elif inp == 3:
            delete_multiple_lines(n)
            u2_lesson3()

        elif inp == 4:
            delete_multiple_lines(n)
            u2_lesson4()

    except:

        print('There was an error')

def unit3():
    n = 4

    try:

        inp: int = int(input('1.Chapter one\n2.Chapter two\n3.Chapter three\n'))

        if inp == 1:
            delete_multiple_lines(n)
            u3_lesson1()

        elif inp == 2:
            delete_multiple_lines(n)
            u3_lesson2()

        elif inp == 3:
            delete_multiple_lines(n)
            u3_lesson3()

    except:

        print('There was an error')

def unit4():
    n = 4

    try:

        inp: int = int(input('1.Chapter one\n2.Chapter two\n3.Chapter three\n'))

        if inp == 1:
            delete_multiple_lines(n)
            u4_lesson1()

        elif inp == 2:
            delete_multiple_lines(n)
            u4_lesson2()

        elif inp == 3:
            delete_multiple_lines(n)
            u4_lesson3()

    except:

        print('There was an error')

def entire():
    
    lessons_list: list = ['u1_l1', 'u2_l1', 'u2_l2', 'u2_l3', 'u2_l4', 'u3_l1', 'u3_l2',
                          'u3_l3', 'u4_l1', 'u4_l2', 'u4_l3']
    
    lessons_dict: dict = {'u1_l1': 1, 'u2_l1': 9, 'u2_l2': 15, 'u2_l3': 18, 'u2_l4': 27,
                          'u3_l1': 39, 'u3_l2': 46, 'u3_l3': 51, 'u4_l1': 57,
                          'u4_l2': 60, 'u4_l3': 63}
    
    random.shuffle(lessons_list)

###########################

def u1_lesson1():
    
    start, end = 1, 85
    make_dict('u1_l1', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

###########################

def u2_lesson1():

    start, end = 1, 62
    make_dict('u2_l1', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

def u2_lesson2():

    start, end = 1, 31
    make_dict('u2_l2', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

def u2_lesson3():

    start, end = 1, 97
    make_dict('u2_l3', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

def u2_lesson4():

    start, end = 1, 126
    make_dict('u2_l4', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

###########################

def u3_lesson1():

    start, end = 1, 83
    make_dict('u3_l1', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

def u3_lesson2():

    start, end = 1, 46
    make_dict('u3_l2', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

def u3_lesson3():

    start, end = 1, 58
    make_dict('u3_l3', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

###########################

def u4_lesson1():

    start, end = 1, 27
    make_dict('u4_l1', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

def u4_lesson2():

    start, end = 1, 23
    make_dict('u4_l2', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

def u4_lesson3():

    start, end = 1, 26
    make_dict('u4_l3', start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    compare(start, end)

###########################

def make_dict(table: str , start: int, end: int) -> dict:

    row = db.execute('SELECT * FROM ? WHERE id >= ? AND id <= ?', table, start, end)

    global answers_dict

    answers_dict = dict()

    for i in row:

        answers_dict[i['id']] = i['answer']

def compare(start: int, end: int):
    
    global tottal_rate
    tottal_rate = list()

    global wrong_list
    wrong_list = list()

    for i in range(start, end + 1):

        if quiz_dict[i] == answers_dict[i]:

            tottal_rate.append(True)

        else:

            wrong_list.append(f'Q.{i}')
            tottal_rate.append(False)
    
    final_rate()

def final_rate():
    
    rate = tottal_rate.count(True) / len(tottal_rate) * 100

    analysis(rate, tottal_rate.count(True), len(tottal_rate))

def analysis(rate: int, count: int , len: int) -> None:
    
    print('|----------------|---------|-----------|---------------------|------')
    print(f'|  your rate is  |  {G}{round(rate, 2):5}{W}  |  {B}{count:2} / {len:2}{W}  |  your mistakes are  |')
    print('|----------------|---------|-----------|---------------------|------')
    print()
    print(f' {R}{wrong_list}{W}')



if __name__ == '__main__':
    main()