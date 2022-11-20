weights = [1,2,3]
values=[6,10,12]

def knapsack(w,v,c):
    dp = [[0] * (c+1)] * (len(w) + 1)
    for i in range(len(w)):
        for j in range(1,c + 1):



print(knapsack(weights,values, 5))