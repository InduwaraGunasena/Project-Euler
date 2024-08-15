"""
# MY FIRST CODE IMPLEMENTATION

import copy
# must need to contain 1 for make any number
coins = [10, 5, 2, 1]

c = 13  # the amount you need to make from basic coins in coins list

def maker(coin_list, target, lis,n):
    d = target // coin_list[0]

    if len(coin_list) == 1: #  Base Case
        lis[0].append(d)
        n.append(lis[0])
        return
    else:
        if len(lis) == 0:
            for a in range(d, -1, -1):
                lis.append([a])
        else:
            lis = [copy.copy(lis[0]) for u in range(d+1)]
            b = d
            for q in range(len(lis)):
                lis[q].append(b)
                b -= 1

        for m in range(len(lis)):
            maker(coin_list[1:], target - (coin_list[0] * lis[m][-1]), [lis[m]], n)


ans = []
n = []
maker(coins, c, ans, n)
print(n)
print(len(n))

"""


"""
#OPTIMIZED CODE FOR LIST DOWN ALL THE POSSIBLE WAYS
coins = [10, 5, 2, 1]
target_amount = 13

def make_combinations(coin_list, target, current_combination, result):
    # if there is no rest amount to fill the target and the possible coin sequence has
    # all the coins in the list then add that sequence to the final answer result.
    if target == 0 and len(current_combination) == len(coins):
        result.append(current_combination[:])
        return
    # if that target cannot complete using rest of the coins or any other impossibilities, return/give up that situation
    elif target < 0 or len(coin_list) == 0 or len(current_combination) >= len(coins):
        return

    current_coin = coin_list[0]
    max_coins = target // current_coin

    for num_coins in range(max_coins, -1, -1):
        make_combinations(coin_list[1:], target - num_coins * current_coin, current_combination + [num_coins], result)

result = []
make_combinations(coins, target_amount, [], result)
print(result)
print(len(result))


"""

# OPTIMIZED CODE FOR CALCULATE THE NUMBER OF WAYS TO MAKE THAT VALUE USING GIVEN COIN LIST
def count_combinations(coins, target):
    # This method is using a special behavior of this problem nature.
    # You can identify this pattern by making a grid, given coins as the header and each row represents no. of ways to complete that value.
    # Example grid here for coins = [1p,2p,5p,10p]
    #          Target | 1p | 2p | 5p | 10p |
    #             1p  | 1  | 1  | 1  | 1   |   since only one way for make 1p (using 1*1p)
    #             2p  | 1  | 2  | 2  | 2   |   since only 2 ways for make 2p (using 2*1p and 1*2p)
    #             7p  | 1  | 4  | 6  | 6   |   since, only 1 way to make 7p by using only 1p,
    #                                                 4 ways to make 7p by using 1p and 2p(7*1p, 3*2p + 1*1p, 2*2p + 3*1p, 1*2p + 5*1p)
    #                                                 5 ways to make 7p by using 1p, 2p and 5p(7*1p, 3*2p + 1*1p, 2*2p + 3*1p, 1*2p + 5*1p(same as above), 1*5p + 1*2p, 1*5p + 2*1p)
    # So like wise this pattern goes straightforward for any value.


    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

coins = [1, 2, 5, 10]
target_amount = 13
result = count_combinations(coins, target_amount)
print(result)






