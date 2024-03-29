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

    def post_cm_position_mode(self, dual_side_position):
        url_path = '/papi/v1/cm/positionSide/dual'
        return self.sign_request('POST', url_path, {'dualSidePosition': dual_side_position})

    def request_um_user_trades(self, symbol, start_time=None, end_time=None, from_id=None, limit=None):
        url_path = '/papi/v1/um/userTrades'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'startTime': start_time, 'endTime': end_time, 'fromId': from_id, 'limit': limit})

    def request_cm_user_trades(self, symbol=None, pair=None, start_time=None, end_time=None, from_id=None, limit=None):
        url_path = '/papi/v1/cm/userTrades'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'pair': pair, 'startTime': start_time, 'endTime': end_time, 'fromId': from_id, 'limit': limit})

    def request_margin_user_trades(self, symbol=None, order_id=None, start_time=None, end_time=None, from_id=None, limit=None):
        url_path = '/papi/v1/margin/myTrades'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'orderId': order_id, 'startTime': start_time, 'endTime': end_time, 'fromId': from_id, 'limit': limit})

    def request_um_leverage_bracket(self, symbol=None):
        url_path = '/papi/v1/um/leverageBracket'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_cm_leverage_bracket(self, symbol=None):
        url_path = '/papi/v1/cm/leverageBracket'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_margin_force_orders(self, start_time=None, end_time=None, current=None, size=None):
        url_path = '/papi/v1/margin/forceOrders'
        return self.sign_request('GET', url_path, {'startTime': start_time, 'endTime': end_time, 'current': current, 'size': size})

    def request_um_force_orders(self, symbol=None, auto_close_type=None, start_time=None, end_time=None, limit=None):
        url_path = '/papi/v1/um/forceOrders'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'autoCloseType': auto_close_type, 'startTime': start_time, 'endTime': end_time, 'limit': limit})

    def request_cm_force_orders(self, symbol=None, auto_close_type=None, start_time=None, end_time=None, limit=None):
        url_path = '/papi/v1/cm/forceOrders'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'autoCloseType': auto_close_type, 'startTime': start_time, 'endTime': end_time, 'limit': limit})

    def request_um_api_trading_status(self, symbol=None):
        url_path = '/papi/v1/um/apiTradingStatus'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_um_commission_rate(self, symbol):
        url_path = '/papi/v1/um/commissionRate'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_cm_commission_rate(self, symbol):
        url_path = '/papi/v1/cm/commissionRate'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_margin_loan_hist(self, asset, tx_id=None, start_time=None, end_time=None, current=None, size=None, archived=None):
        url_path = '/papi/v1/margin/marginLoan'
        return self.sign_request('GET', url_path, {'asset': asset, 'txId': tx_id, 'startTime': start_time, 'endTime': end_time,
                                                   'current': current, 'size': size, 'archived': archived})

    def request_margin_repay_hist(self, asset, tx_id=None, start_time=None, end_time=None, current=None, size=None, archived=None):
        url_path = '/papi/v1/margin/repayLoan'
        return self.sign_request('GET', url_path, {'asset': asset, 'txId': tx_id, 'startTime': start_time, 'endTime': end_time,
                                                   'current': current, 'size': size, 'archived': archived})

    def request_margin_interest_hist(self, asset=None, start_time=None, end_time=None, current=None, size=None, archived=None):
        url_path = '/papi/v1/margin/marginInterestHistory'
        return self.sign_request('GET', url_path, {'asset': asset, 'startTime': start_time, 'endTime': end_time,
                                                   'current': current, 'size': size, 'archived': archived})

    def request_portfolio_interest_hist(self, asset=None, start_time=None, end_time=None, size=None):
        url_path = '/papi/v1/portfolio/interest-history'
        return self.sign_request('GET', url_path, {'asset': asset, 'startTime': start_time, 'endTime': end_time, 'size': size})

    def post_auto_collection(self):
        url_path = '/papi/v1/auto-collection'
        return self.sign_request('POST', url_path)

    def post_bnb_transfer(self, amount, transfer_side):
        url_path = '/papi/v1/bnb-transfer'
        return self.sign_request('POST', url_path, {'amount': amount, 'transferSide': transfer_side})

    def request_repay_futures_switch(self):
        url_path = '/papi/v1/repay-futures-switch'
        return self.sign_request('GET', url_path, )

    def post_repay_futures_switch(self, auto_repay):
        url_path = '/papi/v1/repay-futures-switch'
        return self.sign_request('POST', url_path, {'autoRepay': auto_repay})

    def post_repay_futures_negative_balance(self, ):
        url_path = '/papi/v1/repay-futures-negative-balance'
        return self.sign_request('POST', url_path, )

    def request_um_income_hist(self, symbol=None, income_type=None, start_time=None, end_time=None, limit=None):
        """TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE,
        CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT,
        COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE"""
        url_path = '/papi/v1/um/income'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'incomeType': income_type, 'startTime': start_time, 'endTime': end_time, 'limit': limit})

    def request_cm_income_hist(self, symbol=None, income_type=None, start_time=None, end_time=None, limit=None):
        """TRANSFER","WELCOME_BONUS", "FUNDING_FEE", "REALIZED_PNL", "COMMISSION", "INSURANCE_CLEAR", and "DELIVERED_SETTELMENT"""
        url_path = '/papi/v1/cm/income'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'incomeType': income_type, 'startTime': start_time, 'endTime': end_time, 'limit': limit})

    def place_um_order(self, symbol, side, type, position_side=None, time_in_force=None, quantity=None, reduce_only=None, price=None,
                       new_client_order_id=None, new_order_resp_type=None):
        url_path = '/papi/v1/um/order'
        return self.sign_request('POST', url_path, {'symbol': symbol, 'side': side, 'type': type,
                                                    'positionSide': position_side, 'timeInForce': time_in_force, 'quantity': quantity, 'reduceOnly': reduce_only,
                                                    'price': price, 'newClientOrderId': new_client_order_id, 'newOrderRespType': new_order_resp_type})

    def place_cm_order(self, symbol, side, type, position_side=None, time_in_force=None, quantity=None, reduce_only=None, price=None,
                       new_client_order_id=None, new_order_resp_type=None):
        url_path = '/papi/v1/cm/order'
        return self.sign_request('POST', url_path, {'symbol': symbol, 'side': side, 'type': type,
                                                    'positionSide': position_side, 'timeInForce': time_in_force, 'quantity': quantity, 'reduceOnly': reduce_only,
                                                    'price': price, 'newClientOrderId': new_client_order_id, 'newOrderRespType': new_order_resp_type})

    def place_margin_order(self, symbol, side, type, quantity=None, quote_order_qty=None, price=None, stop_price=None, new_client_order_id=None, new_order_resp_type=None,
                           iceberg_qty=None, side_effect_type=None, time_in_force=None):
        url_path = '/papi/v1/margin/order'
        return self.sign_request('POST', url_path, {'symbol': symbol, 'side': side, 'type': type,
                                                    'quantity': quantity, 'quoteOrderQty': quote_order_qty,
                                                    'price': price, 'stopPrice': stop_price, 'newClientOrderId': new_client_order_id, 'newOrderRespType': new_order_resp_type,
                                                    'icebergQty': iceberg_qty, 'sideEffectType': side_effect_type, 'timeInForce': time_in_force})

    def place_margin_oco_order(self, symbol, side, quantity, stop_price, list_client_order_id, limit_client_order_id, price=None, limit_iceberg_qty=None,
                               stop_client_order_id=None, stop_limit_price=None, stop_iceberg_qty=None, stop_limit_time_in_force=None,
                               new_order_resp_type=None, side_effect_type=None, time_in_force=None):
        url_path = '/papi/v1/margin/order/oco'
        return self.sign_request('POST', url_path, {'symbol': symbol, 'side': side, 'quantity': quantity, 'stopPrice': stop_price, 'price': price,
                                                    'listClientOrderId': list_client_order_id, 'limitClientOrderId': limit_client_order_id, 'limitIcebergQty': limit_iceberg_qty,
                                                    'stopClientOrderId': stop_client_order_id, 'stopLimitPrice': stop_limit_price, 'stopIcebergQty': stop_iceberg_qty, 'stopLimitTimeInForce': stop_limit_time_in_force,
                                                    'newOrderRespType': new_order_resp_type, 'sideEffectType': side_effect_type, 'timeInForce': time_in_force})

    def post_margin_loan(self, asset, amount):
        url_path = '/papi/v1/marginLoan'
        return self.sign_request('POST', url_path, {'asset': asset, 'amount': amount})

    def post_margin_repay(self, asset, amount):
        url_path = '/papi/v1/repayLoan'
        return self.sign_request('POST', url_path, {'asset': asset, 'amount': amount})

    def cancel_um_order(self, symbol, order_id=None, orig_client_order_id=None):
        url_path = '/papi/v1/um/order'
        return self.sign_request('DELETE', url_path, {'symbol': symbol, 'orderId': order_id, 'origClientOrderId': orig_client_order_id})

    def cancel_um_orders(self, symbol):
        url_path = '/papi/v1/um/allOpenOrders'
        return self.sign_request('DELETE', url_path, {'symbol': symbol})

    def cancel_cm_order(self, symbol, order_id=None, orig_client_order_id=None):
        url_path = '/papi/v1/cm/order'
        return self.sign_request('DELETE', url_path, {'symbol': symbol, 'orderId': order_id, 'origClientOrderId': orig_client_order_id})

    def cancel_cm_orders(self, symbol):
        url_path = '/papi/v1/cm/allOpenOrders'
        return self.sign_request('DELETE', url_path, {'symbol': symbol})

    def cancel_margin_order(self, symbol, order_id=None, orig_client_order_id=None, new_client_order_id=None):
        url_path = '/papi/v1/margin/order'
        return self.sign_request('DELETE', url_path, {'symbol': symbol, 'orderId': order_id, 'origClientOrderId': orig_client_order_id, 'newClientOrderId': new_client_order_id})

    def cancel_margin_orders(self, symbol):
        url_path = '/papi/v1/margin/allOpenOrders'
        return self.sign_request('DELETE', url_path, {'symbol': symbol})

    def cancel_margin_oco_order(self, symbol, order_list_id=None, list_client_order_id=None, new_client_order_id=None):
        url_path = '/papi/v1/margin/orderList'
        return self.sign_request('DELETE', url_path, {'symbol': symbol, 'orderListId': order_list_id, 'listClientOrderId': list_client_order_id, 'newClientOrderId': new_client_order_id})

    def request_margin_all_orders(self, symbol, order_id=None, start_time=None, end_time=None, limit=None):
        url_path = '/papi/v1/margin/allOrders'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'orderId': order_id, 'startTime': start_time, 'endTime': end_time, 'limit': limit})

    def request_margin_order(self, symbol, order_id=None, orig_client_order_id=None):
        url_path = '/papi/v1/margin/order'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'orderId': order_id, 'origClientOrderId': orig_client_order_id})

    def request_um_order(self, symbol, order_id=None, orig_client_order_id=None):
        url_path = '/papi/v1/um/order'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'orderId': order_id, 'origClientOrderId': orig_client_order_id})

    def request_um_open_order(self, symbol, order_id=None, orig_client_order_id=None):
        url_path = '/papi/v1/um/openOrder'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'orderId': order_id, 'origClientOrderId': orig_client_order_id})

    def request_um_open_orders(self, symbol=None):
        url_path = '/papi/v1/um/openOrders'
        return self.sign_request('GET', url_path, {'symbol': symbol})

    def request_um_all_orders(self, symbol, order_id=None, start_time=None, end_time=None, limit=None):
        url_path = '/papi/v1/um/allOrders'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'orderId': order_id, 'startTime': start_time, 'endTime': end_time, 'limit': limit})

    def request_cm_order(self, symbol, order_id=None, orig_client_order_id=None):
        url_path = '/papi/v1/cm/order'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'orderId': order_id, 'origClientOrderId': orig_client_order_id})

    def request_cm_open_order(self, symbol, order_id=None, orig_client_order_id=None):
        url_path = '/papi/v1/cm/openOrder'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'orderId': order_id, 'origClientOrderId': orig_client_order_id})

    def request_cm_open_orders(self, symbol=None, pair=None):
        url_path = '/papi/v1/cm/openOrders'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'pair': pair})

    def request_cm_all_orders(self, symbol, pair=None, order_id=None, start_time=None, end_time=None, limit=None):
        url_path = '/papi/v1/cm/allOrders'
        return self.sign_request('GET', url_path, {'symbol': symbol, 'pair': pair, 'orderId': order_id, 'startTime': start_time, 'endTime': end_time, 'limit': limit})

    def request_listen_key(self):
        url_path = '/papi/v1/listenKey'
        return self.sign_request('POST', url_path)

    def keepalive_listen_key(self):
        url_path = '/papi/v1/listenKey'
        return self.sign_request('PUT', url_path)

    def close_listen_key(self):
        url_path = '/papi/v1/listenKey'
        return self.sign_request('DELETE', url_path)
