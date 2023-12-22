    
def buyChoco(self, prices, money):

    min_1=min(prices)
    prices.remove(min_1)

    min_2=min(prices)
    prices.remove(min_2)

    if (min_1+min_2) <= money:
        return money-( min_1+min_2)
    else:
        return money