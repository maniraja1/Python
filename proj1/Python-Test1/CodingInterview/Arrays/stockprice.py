'''
Given daily stock price Find the max profit you can get by buying and selling stock
Consider selling price that occurs whenever you buy the stock
Below Algorith keeps a track of min price and keeps track of max profit
'''
def stockprice(a):
    min_price,max_profit = a[0],0
    for i in a:
        profit = i-min_price
        max_profit=max(max_profit,profit)
        min_price = min(i, min_price)
    print(max_profit)


s=[310,315,275,295,260,270,290,230,255,250]
stockprice(s)

def stockprice2(a):
    min_price,max_profit = a[0],0
    for i in a:
        profit = i-min_price
        max_profit=max(max_profit,profit)
        min_price = min(i, min_price)
    print(max_profit)