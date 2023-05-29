from binance_pm import BinanceAPI


class BinancePm(BinanceAPI):
    def __init__(self, api_key, api_secret):
        base_url = 'https://papi.binance.com'
        super(BinancePm, self).__init__(api_key, api_secret, base_url)

    def request_balance(self, asset=None):
        url_path = '/papi/v1/balance'
        return self.sign_request('GET', url_path, {'asset': asset})
