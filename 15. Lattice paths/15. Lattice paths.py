"""
This explanation is described by 2x2 grid.

Firstly I numbered that grid by following.
         1   2   3
         4   5   6
         7   8   9
Then I wrote all the routes I can go.
            1 >> 2 >> 3 >> 6 >> 9
            1 >> 2 >> 5 >> 6 >> 9
            1 >> 2 >> 5 >> 8 >> 9
            1 >> 4 >> 7 >> 8 >> 9
            1 >> 4 >> 5 >> 8 >> 9
            1 >> 4 >> 5 >> 6 >> 9
We have only one destination and only one stating point.There are accordingly 9 and 1.
So these points are known by them. So if we choose one number(N), then we have only 2 choices
to select another number(either N+1 or N+3).Therefore we have to do to calculate the routes by using
our knowledge of permutations and combinations.
                  4!     <----ways of find another number(this is marked the above grid by '>>' sign)
      answer =  ------
                2! . 2!  <----(Since we have 2 options(N+1 or N+3) and these each options are doubled)


"""

grid_size = 20
last_grid_num = (grid_size + 1) ** 2
indexes = (grid_size * 2)
total_methods = 1
same_methods = 1

for i in range(indexes - 1):
    total_methods *= (indexes - i)

num = int(indexes / 2)

for j in range(num):
    same_methods *= (num - j)
same_methods = (same_methods) ** 2

total = int(total_methods / same_methods)
print("answer = ", total)
