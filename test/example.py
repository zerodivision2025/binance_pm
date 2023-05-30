from binance_pm.binance_pm import BinancePm

if __name__ == '__main__':
    client = BinancePm('', '')
    # print(client.request_balance())
    # print(client.request_account())
    # print(client.request_max_borrowable('BTC'))
    # print(client.request_max_withdraw('BTC'))
    # print(client.request_um_positions())
    # print(client.request_cm_positions())

    print(client.request_um_open_orders())
