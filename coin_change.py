# The Problem: bank array has certain types of coins infinitely. There is a certain amt to be formed. How many ways?
# Solution = comb(include) + comb(exclude)

# a - bank array, amt - maximum amt
def count(a, amt):
    ln = len(arr)
    # create the 2D dp array
    dp = [[0]*ln for x in range(amt+1)]
    # first row can be 1; i.e. if amt==0 there is 1 solution, don't include any coin
    dp[0]=[1]*ln
    # for a choice of the amt
    for curr_amt in range(1,amt+1):
    	# for (upto) each member of the bank array
        for n in range(ln):
        	# new guy coin
            curr_coin = a[n]
            # two choices:
            # pick the new guy coin; it will be zero if its not possible to pick that coin as it will exceed the limit
            x=dp[curr_amt-curr_coin][n] if curr_amt-curr_coin>=0 else 0
            # don't pick the new guy coin
            y=dp[curr_amt][n-1]# if n-1>=0 else 0
            # add all the combinations that come through both the choices
            dp[curr_amt][n] = x+y
    # after utilizing "all" of the bank array, how many ways to form the "whole" amount
    return dp[amt][ln-1]

arr = [1, 2, 3]
amt = 4
print(count(arr, amt))
