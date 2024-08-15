grid_length = 50515093
C_0 = 30621295449583788  # The sum of hours which represented all the clocks within the grid at start
S_0 = 290797

time = 1000  # 10 ** 5

C_t = 0  # The sum of hours which represented all the clocks within the grid at 't' hour
previous_grids = []  # [ [ N_function of previous grid , element ],[],[],...]
previous_grid_hour = []  # if any new grid has many past hour values they are listed here.
clocks = 0

hour = 12
prev_hour = 12


def function_of_s(p):
    s_previous = S_0
    if p == 0:
        return S_0
    else:
        s_t = 0
        for i in range(0, p):
            s_t = s_previous ** 2 % grid_length
            s_previous = s_t
        return s_t


def clocks_range(num):
    n = []
    x_1 = x_2 = 0
    for i in range(0, 4, 2):
        x_1 = function_of_s(4 * num - (4 - i))
        x_2 = function_of_s(4 * num - (4 - (i + 1)))

        if x_2 > x_1:
            n.append(x_1)
            n.append(x_2)
        else:
            n.append(x_2)
            n.append(x_1)
    return n


def how_many_clocks_in_range(number):
    N_function = clocks_range(number)
    no_clocks = (N_function[1] - N_function[0] + 1) * (N_function[3] - N_function[2] + 1)
    return no_clocks


def is_this_range_has_any_previous_range(grid,hour,prev_hour):
    clocks_in_grid = 0
    C = C_0
    previous_grid_hour = []
    for t in range(len(previous_grids)):
        now = clocks_range(grid)
        previous = previous_grids[t][:4]
        if (now[0] > previous[0] and now[1] < previous[1]) and (now[2] > previous[2] and now[3] < previous[3]):
            # if new grid inside the previous grid
            clocks_in_grid = ((previous[1] - previous[0]) - (now[1] - now[0])) * ((previous[3] - previous[2]) - (now[3] - now[2]))
            previous_grid_hour.append((previous_grids[t][4]) * clocks_in_grid)
        elif (now[0] == previous[0] and now[1] == previous[1]) and (now[2] == previous[2] and now[3] == previous[3]):
            # if new grid exactly the same size to the previous grid
            clocks_in_grid = (previous[1] - previous[0]) * (previous[3] - previous[2])
            previous_grid_hour.append((previous_grids[t][4]) * clocks_in_grid)
        elif (now[1] <= previous[0] or now[0] >= previous[1]) and (now[3] <= previous[2] or now[2] >= previous[3]):
            # new grid is out of the previous grid
            continue
        else:
            if now[0] > previous[0]: # if new grid in the right side of the previous grid
                if previous[2] > now[2]: # if the new grid in the right side top corner
                    clocks_in_grid = ((now[1] - now[0]) - (now[1] - previous[1])) * ((now[3] - now[2]) - (previous[2] - previous[2]))
                elif previous[3] < now[3]:  # if the new grid in the right side bottom corner
                    clocks_in_grid = ((now[1] - now[0]) - (now[1] - previous[1])) * ((now[3] - now[2]) - (now[3] - previous[3]))
                else:# if the new grid in the right side and inside of the previous grid
                    clocks_in_grid = ((now[1] - now[0]) - (previous[1] - now[1])) * (now[3] - now[2] + 1)
            else:# if new grid in the left side of the previous grid
                if previous[2] > now[2]: # if the new grid in the left side top corner
                    clocks_in_grid = ((now[1] - now[0]) - (previous[0] - now[0])) * ((now[3] - now[2]) - (previous[2] - previous[2]))
                elif previous[3] < now[3]:  # if the new grid in the left side bottom corner
                    clocks_in_grid = ((now[1] - now[0]) - (previous[0] - now[0])) * ((now[3] - now[2]) - (now[3] - previous[3]))
                else:# if the new grid in the left side and inside of the previous grid
                    clocks_in_grid = ((now[1] - now[0]) - (previous[0] - now[0])) * (now[3] - now[2] + 1)
            previous_grid_hour.append((previous_grids[t][4]) * abs(clocks_in_grid))

    if len(previous_grid_hour) > 0:
        clocks = how_many_clocks_in_range(grid)
        C = C - sum(previous_grid_hour) + (clocks * hour)
        #print(previous_grid_hour)
        previous_grid_hour = []
    else:
        clocks = how_many_clocks_in_range(grid)
        C = C - clocks * prev_hour + clocks * hour

    return C


for r in range(0, time+1):
    if r == 0:
        C_t = C_0
    elif r == 1:
        hour += 1
        if hour == 13:
            hour = 1
            prev_hour = 12
        clocks = how_many_clocks_in_range(r)
        C_t = C_t - clocks * prev_hour + clocks * hour
        previous_grids.append(clocks_range(r) + [hour])  # update our previous_grids list to add with the range and hour what we add to that range
        prev_hour = hour
    else:
        hour += 1
        if hour == 13:
            hour = 1
            prev_hour = 12
        C_t = is_this_range_has_any_previous_range(r,hour,prev_hour)
        previous_grids.append(clocks_range(r)+ [hour])  # update our previous_grids list to add with the range and hour what we add to that range
        prev_hour = hour

print(f"answer of C({r}) = {C_t}")
#print(previous_grids)

#print(clocks_range(2))
