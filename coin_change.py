def coin_change(lst, amount):
    if amount == 0:
        return 0
    if len(lst) == 1 and amount % lst[0] != 0:
        return -1
    if amount in lst:
        return 1
    lst.sort(reverse = True)
    for i in range(0, len(lst)):
        coin = lst[i] 
        c = 1
        while(coin < amount):
            coin *= 2
            if coin == amount:
                return c + 1
            c += 1
            if amount - coin in lst:
                return c + 1
        
print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1], 0))
print(coin_change([1, 2, 3, 5], 14))  
