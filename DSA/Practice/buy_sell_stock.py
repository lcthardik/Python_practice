prices=[7,1,5,3,6,4]

low=min(prices)
i=prices.index(low)
high=max(prices[i:])
if high>low:
    print(high-low)
else:
    print(0)
