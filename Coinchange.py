class Coinchange:
    def coinChange(self,total_Amount,coins):
        coins.sort()
        index = len(coins)-1
        x= []
        while True:
            coinValue = coins[index]
            if coinValue<=total_Amount:
                x.append(coinValue)
                total_Amount = total_Amount-coinValue

            if coinValue > total_Amount:
                index-=1
            if total_Amount ==0:
                break
        print(x)


Coin = Coinchange()
No_Denomination = int(input("Enter the number of coins: "))
coin = []
print("Enter the denominations")
for i in range(0,No_Denomination):
    y = int(input())
    coin.append(y)
total_amount = int(input("Enter the amount: "))
Coin.coinChange(total_amount,coin)


