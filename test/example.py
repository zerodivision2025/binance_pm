from binance_pm.binance_pm import BinancePm

if __name__ == '__main__':
    client = BinancePm('', '')
    print(client.request_balance())
