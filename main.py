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
    
    # try:
        inp: int = int(input('1.Unit 1\n2.Unit 2\n3.Unit 3\n4.Unit 4\n5.The entire book (for men)\n'))

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

    # except:
    #     print('There was an error')

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
            lessons(85, 'u1_l1')

    except:

        print('There was an error')

def unit2():
    n = 5

    try:

        inp: int = int(input('1.Chapter one\n2.Chapter two\n3.Chapter three\n4.Chapter four\n'))

        if inp == 1:
            delete_multiple_lines(n)
            lessons(62, 'u2_l1')

        elif inp == 2:
            delete_multiple_lines(n)
            lessons(31, 'u2_l2')

        elif inp == 3:
            delete_multiple_lines(n)
            lessons(97, 'u2_l3')

        elif inp == 4:
            delete_multiple_lines(n)
            lessons(126, 'u2_l4')

    except:

        print('There was an error')

def unit3():
    n = 4

    try:

        inp: int = int(input('1.Chapter one\n2.Chapter two\n3.Chapter three\n'))

        if inp == 1:
            delete_multiple_lines(n)
            lessons(83, 'u3_l1')

        elif inp == 2:
            delete_multiple_lines(n)
            lessons(46, 'u3_l2')

        elif inp == 3:
            delete_multiple_lines(n)
            lessons(58, 'u3_l3')

    except:

        print('There was an error')

def unit4():
    n = 4

    try:

        inp: int = int(input('1.Chapter one\n2.Chapter two\n3.Chapter three\n'))

        if inp == 1:
            delete_multiple_lines(n)
            lessons(27, 'u4_l1')

        elif inp == 2:
            delete_multiple_lines(n)
            lessons(23, 'u4_l2')

        elif inp == 3:
            delete_multiple_lines(n)
            lessons(26, 'u4_l3')

    except:

        print('There was an error')

def entire():
    
    global entire_tottal_rate
    entire_tottal_rate = list()

    lessons_list: list = ['u1_l1', 'u2_l1', 'u2_l2', 'u2_l3', 'u2_l4', 'u3_l1', 'u3_l2',
                          'u3_l3', 'u4_l1', 'u4_l2', 'u4_l3']
    
    random.shuffle(lessons_list)

    i = 1

    while len(lessons_list) > 0:

        lessons_page_dict: dict = {'u1_l1': 1, 'u2_l1': 9, 'u2_l2': 15, 'u2_l3': 18,
                                'u2_l4': 27, 'u3_l1': 39, 'u3_l2': 46, 'u3_l3': 51,
                                'u4_l1': 57,'u4_l2': 60, 'u4_l3': 63}
        
        lessons_end_dict: dict = {'u1_l1': 85, 'u2_l1': 62, 'u2_l2': 31, 'u2_l3': 97,
                                'u2_l4': 126, 'u3_l1': 83, 'u3_l2': 46, 'u3_l3': 58,
                                'u4_l1': 27, 'u4_l2': 23, 'u4_l3': 26}

        print(f'{i}.Page number ({lessons_page_dict[lessons_list[0]]}) | Unit{lessons_list[0][1]} Chapter{lessons_list[0][4]}')

        lessons(lessons_end_dict[lessons_list[0]], lessons_list[0], False)

        lessons_list = lessons_list[1:]

        i += 1

    entire_analysis()

###########################

def lessons(end: int, lesson: str, able_to_compare=True):

    start, end = 1, end
    make_dict(lesson, start, end)

    global quiz_dict
    quiz_dict = dict()

    for i in range(start, end + 1):

        inp: str = input(f'{i}: ')

        quiz_dict[i] = inp

        if i % 12 == 0:

            delete_multiple_lines(12)

    delete_multiple_lines(end)

    if able_to_compare:
        compare(start, end)

    else:
        entire_compare(end)

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

###########################

def entire_compare(end: int):

    for i in range(1, end + 1):

        if quiz_dict[i] == answers_dict[i]:

            entire_tottal_rate.append(True)

        else:

            entire_tottal_rate.append(False)

def entire_analysis():
    
    count = entire_tottal_rate.count(True)

    entire_len = len(entire_tottal_rate)

    rate = count / entire_len * 100

    print('|----------------|---------|----------------------------------')
    print(f'|  your rate is  |  {G}{round(rate, 2):5}{W}  |  {B}{count:2} / {entire_len:2}{W}')
    print('|----------------|---------|----------------------------------')



if __name__ == '__main__':
    main()