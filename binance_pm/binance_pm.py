from binance_pm import BinanceAPI


class BinancePm(BinanceAPI):
    def __init__(self, api_key, api_secret):
        base_url = 'https://papi.binance.com'
        super(BinancePm, self).__init__(api_key, api_secret, base_url)

    def request_balance(self, asset=None):
        url_path = '/papi/v1/balance'
        return self.sign_request('GET', url_path, {'asset': asset})

    def request_account(self):
        url_path = '/papi/v1/account'
        return self.sign_request('GET', url_path)

    def request_max_borrowable(self, asset):
        url_path = '/papi/v1/margin/maxBorrowable'
        return self.sign_request('GET', url_path, {'asset': asset})

    def request_max_withdraw(self, asset):
        url_path = '/papi/v1/margin/maxWithdraw'
        return self.sign_request('GET', url_path, {'asset': asset})

    def request_um_positions(self, symbol=None):
        url_path = '/papi/v1/um/positionRisk'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_cm_positions(self, margin_asset=None, pair=None):
        url_path = '/papi/v1/cm/positionRisk'
        return self.sign_request('GET', url_path, {'marginAsset': margin_asset, 'pair': pair})

    def post_um_leverage(self, symbol, leverage):
        url_path = '/papi/v1/um/leverage'
        return self.sign_request('POST', url_path, {'symbol': symbol, 'leverage': leverage})

    def post_cm_leverage(self, symbol, leverage):
        url_path = '/papi/v1/cm/leverage'
        return self.sign_request('POST', url_path, {'symbol': symbol, 'leverage': leverage})

    def request_um_position_mode(self):
        url_path = '/papi/v1/um/positionSide/dual'
        return self.sign_request('GET', url_path)

    def request_cm_position_mode(self):
        url_path = '/papi/v1/cm/positionSide/dual'
        return self.sign_request('GET', url_path)

    def post_um_position_mode(self, dual_side_position):
        url_path = '/papi/v1/um/positionSide/dual'
        return self.sign_request('POST', url_path, {'dualSidePosition': dual_side_position})

    def request_um_position_mode(self, symbol, startTime=None, endTime=None, fromId=None, limit=None):
        url_path = '/papi/v1/um/userTrades'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'startTime': startTime, 'endTime': endTime, 'fromId': fromId, 'limit': limit})

    def request_cm_position_mode(self, symbol=None, pair=None, startTime=None, endTime=None, fromId=None, limit=None):
        url_path = '/papi/v1/cm/userTrades'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'pair': pair, 'startTime': startTime, 'endTime': endTime, 'fromId': fromId, 'limit': limit})

    def request_um_leverage_bracket(self, symbol=None):
        url_path = '/papi/v1/um/leverageBracket'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_cm_leverage_bracket(self, symbol=None):
        url_path = '/papi/v1/cm/leverageBracket'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_margin_force_orders(self, startTime=None, endTime=None, current=None, size=None):
        url_path = '/papi/v1/margin/forceOrders'
        return self.sign_request('GET', url_path, {'startTime': startTime, 'endTime': endTime, 'current': current, 'size': size})

    def request_um_force_orders(self, symbol=None, autoCloseType=None, startTime=None, endTime=None, limit=None):
        url_path = '/papi/v1/um/forceOrders'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'autoCloseType': autoCloseType, 'startTime': startTime, 'endTime': endTime, 'limit': limit})

    def request_cm_force_orders(self, symbol=None, autoCloseType=None, startTime=None, endTime=None, limit=None):
        url_path = '/papi/v1/cm/forceOrders'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'autoCloseType': autoCloseType, 'startTime': startTime, 'endTime': endTime, 'limit': limit})

    def request_um_api_trading_status(self, symbol=None):
        url_path = '/papi/v1/um/apiTradingStatus'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_um_commission_rate(self, symbol):
        url_path = '/papi/v1/um/commissionRate'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_cm_commission_rate(self, symbol):
        url_path = '/papi/v1/cm/commissionRate'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_margin_loan_hist(self, asset, txId=None, startTime=None, endTime=None, current=None, size=None, archived=None):
        url_path = '/papi/v1/margin/marginLoan'
        return self.sign_request('GET', url_path, {'asset': asset, 'txId': txId, 'startTime': startTime, 'endTime': endTime,
                                                   'current': current, 'size': size, 'archived': archived})

    def request_margin_repay_hist(self, asset, txId=None, startTime=None, endTime=None, current=None, size=None, archived=None):
        url_path = '/papi/v1/margin/repayLoan'
        return self.sign_request('GET', url_path, {'asset': asset, 'txId': txId, 'startTime': startTime, 'endTime': endTime,
                                                   'current': current, 'size': size, 'archived': archived})

    def request_margin_interest_hist(self, asset, startTime=None, endTime=None, current=None, size=None, archived=None):
        url_path = '/papi/v1/margin/marginInterestHistory'
        return self.sign_request('GET', url_path, {'asset': asset, 'startTime': startTime, 'endTime': endTime,
                                                   'current': current, 'size': size, 'archived': archived})

    def request_portfolio_interest_hist(self, asset, startTime=None, endTime=None, size=None):
        url_path = '/papi/v1/portfolio/interest-history'
        return self.sign_request('GET', url_path, {'asset': asset, 'startTime': startTime, 'endTime': endTime, 'size': size})

    def post_auto_collection(self):
        url_path = '/papi/v1/auto-collection'
        return self.sign_request('POST', url_path)

    def post_bnb_transfer(self, amount, transferSide):
        url_path = '/papi/v1/bnb-transfer'
        return self.sign_request('POST', url_path, {'amount': amount, 'transferSide': transferSide})
