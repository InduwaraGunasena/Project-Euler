import numpy as np

triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


# don't forget to follow as below to input your triangle
#     triangle = """  <------quotes starting alone
#     12
#     78 14
#     96 02 47
#     52 41 22 99
#     ..............
#     ................
#     47 88 10 36 47 91 23
#     """             <-----quotes finishing alone


def convert_to_list(Triangle):
    list = []
    state = 0
    number = ""
    for i in range(len(Triangle)):
        if Triangle[i] != "\n" and triangle[i] != " ":
            number += Triangle[i]
            state += 1
            if state == 2:
                state = 0
                list.append(int(number))
                number = ""
    return list


def all_the_paths_list(list):
    rows = int((2 * len(list) + 0.25) ** (0.5) - 0.5)
    new_list = np.zeros((2 ** (rows - 1), rows))
    for i in range(2 ** (rows - 1)):
        new_list[i][0] = list[0]

    step = len(new_list)
    for t in range(1, rows):
        step = step / 2
        round = 0
        last_t_row = t - 1
        for u in range(len(new_list)):
            index = list.index(new_list[u][last_t_row])
            if round < step:
                new_list[u][t] = list[t + index]
                round += 1
            else:
                new_list[u][t] = list[t + 1 + index]
                round += 1
                if round == step * 2:
                    round = 0

    return new_list


def position_list(list):
    positions = []
    for i in range(len(list)):
        positions.append(i)
    return positions


def real_paths_list(positions_list, real_list):
    # The formula of triangle numbers is T(n) = n(n+1)/2
    # Here n = the row what you need & T = all indexes of the n'th traiangle
    rows = int((2 * len(real_list) + 0.25) ** (0.5) - 0.5)   # So I made a new formula using above formula to find row
    new_last_list = np.zeros((2 ** (rows - 1), rows))

    for i in range(len(positions_list)):
        for j in range(len(positions_list[i])):
            new_last_list[i, j] =  real_list[int(positions_list[i][j])]

    return new_last_list


def maximum_path(list):
    list2 = []
    for i in range(len(list)):
        total = int(sum(list[i]))
        list2.append(total)

    print("maximum sum of paths = ", max(list2))
    print("maximum sum of path's route =", end= " ")
    for k in range(len(list2)):
        if list2[k] == max(list2):
            print(list[k], end= " , ")


list1 = convert_to_list(triangle)
#print(list1)
list2 = position_list(list1)
list3 = all_the_paths_list(list2)
list4 = real_paths_list(list3, list1)
#print(list4)
maximum_path(list4)


"""

###################################################   SECOND PROGRAMME   ###################################################
def convert_to_list(Triangle):
    full_list = []
    list = []
    state = 0
    number = ""
    for i in Triangle:
        if i.isnumeric() == True:
            number += i
            state += 1
            if state == 2:
                state = 0
                list.append(int(number))
                number = ""
        else:
            if i == '\n' and list != []:
                full_list.append(list)
                list = []

    return full_list

def maximum_numbers_in_rows(list):
    # The formula of triangle numbers is T(n) = n(n+1)/2
    # Here n = the row what you need & T = all indexes of the n'th traiangle

    rows = int((2 * len(list) + 0.25) ** (0.5) - 0.5)   # So I made a new formula using above formula.

    # I decided to choose maximum numbers which are greater than the average number of a row.
    # I made a full list using lists of maximum numbers of each row in ascending order.
    row_max_numbers_positions = []

    for line_num in range(1,rows+1):
        start_index = 0 # This is the first index number of any row. It is varying in different lines.
        for i in range(1, line_num + 1):
            start_index += i

        sum = 0 # The sum of indexes in a row.
        for h in range(line_num):
            sum += list[start_index + h]
        max = sum // line_num # The average number of the row

        maximums_list = [] # I add all the indexes of greater than average number of the row in this list
        for g in range(start_index, start_index + line_num + 1):
            if list[g] > max:
                maximums_list.append(list[g])
        row_max_numbers_positions.append(maximums_list)
        # I added to this list that shows all the maximum numbers in any row separated by its row
    return row_max_numbers_positions

"""
