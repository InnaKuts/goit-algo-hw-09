import sys


def find_coins_greedy(amount: int, coins: list[int]) -> dict[int, int]:
    """
    :param amount: Amount to split
    :param coins: Sorted list of available coin values
    :return: Amount of each coins
    """
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount: int, coins: list[int]) -> dict[int, int]:
    """
    :param amount: Amount to split
    :param coins: Sorted list of available coin values
    :return: Amount of each coins
    """
    min_coins = [float('inf')] * (amount + 1)
    coin_used = [0] * (amount + 1)

    min_coins[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


def safe(fun):
    try:
        return fun()
    except:
        return None


def main():
    coins = [50, 25, 10, 5, 2, 1]
    amount = safe(lambda: int(sys.argv[1]))
    while not amount:
        amount = safe(lambda: int(input('Enter amount: ')))

    print(f'Greedy: {find_coins_greedy(amount, coins)}')
    print(f'Min:    {find_min_coins(amount, coins)}')


if __name__ == "__main__":
    main()
