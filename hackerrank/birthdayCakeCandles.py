def birthdayCakeCandles(candles):
    candles.sort(reverse=True)
    return candles.count(candles[0])

print(birthdayCakeCandles([3,2,1,3]))