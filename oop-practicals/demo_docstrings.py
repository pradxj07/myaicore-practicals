def calc_profit(cost, saleprice):
    # sale price - cost
    """ Accepts cost and saleprice as parameters and returns profit """
    profit = saleprice-cost
    return profit

test = calc_profit(100,400)
print(f"profit is {test}")
help(calc_profit)
# print(calc_profit)
print(calc_profit.__doc__())