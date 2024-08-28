import requests
import json


class Client:
    END_POINTS = dict(
        get_exchanges='/equity/metadata/exchanges',
        get_instruments='/equity/metadata/instruments',
        get_pies='/equity/pies',
        get_pie='/equity/pies/{id}',
        create_pie='/equity/pies',
        update_pie='/equity/pies{id}',
        delete_pie='/equity/pies/{id}',
        get_orders='/equity/orders/',
        get_order='/equity/orders/{id}',
        delete_order='/equity/orders/{id}',
        place_limit_order='/equity/orders/limit',
        place_market_order='/equity/orders/market',
        place_stop_order='/equity/orders/limit',
        place_stop_limit_order='/equity/orders/limit',
        get_account_cash='/equity/account/cash',
        get_account='/equity/account/info',
        get_positions='/equity/positions',
        get_position='/equity/orders/{ticker}',
        get_order_history='/equity/history/orders',
        get_dividends='/history/dividends',
        get_exports='/history/exports',
        get_transactions='/history/transactions',
        get_export='/history/exports'
    )

    def __init__(self, api_key, domain=None):
        """
        """
        self.API_KEY = api_key
        self.DOMAIN = domain or 'live.trading212.com'
        self.PATH = '/api/v0'
        self.BASE_URL = f'https://{self.DOMAIN}{self.PATH}'
        self.AUTH = {'Authorization': self.API_KEY}

    def _get(self, url: str, headers: dict, params: dict = None) -> dict:
        """
        """
        headers.update(self.AUTH)
        resp = requests.get(f'{self.BASE_URL}{url}', headers=headers, params=params)
        if resp.ok:
            return resp.json()
        else:
            raise Exception(f"{self.ERROR[resp.status_code]} - {resp.text}")

    def _delete(self, url: str, headers: dict, params: dict = None) -> dict:
        """
        """
        headers.update(self.AUTH)
        resp = requests.delete(f'{self.BASE_URL}{url}', headers=headers, params=params)
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(f"{self.ERROR[resp.status_code]} - {resp.text}")

    def _post(self, url: str, headers: dict, payload: dict) -> dict:
        """
        """
        headers.update(self.AUTH)
        resp = requests.post(f'{self.BASE_URL}{url}', headers=headers, json=payload)
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(f"HTTP {resp.status_code} - {resp.text}")

    def get_exchanges(self) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/exchanges
        """
        return self._get(self.END_POINTS['get_exchanges'], {})

    def get_instruments(self) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/instruments
        """
        return self._get(self.END_POINTS['get_instruments'], {})

    def get_pies(self) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/getAll
        """
        return self._get(self.END_POINTS['get_pies'], {})

    def get_pie(self, id: int) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/getDetailed
        """
        return self._get(self.END_POINTS['get_pie'].format(id=id), {})

    def create_pie(self, dividend_cash_action: str, end_date: str, goal: float, icon: str, instrument_shares: dict, name: str) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/create
        """
        payload = dict(
            dividendCashAction=dividend_cash_action,
            endData=end_date,
            goal=goal,
            icon=icon,
            instrumentShares=instrument_shares,
            name=name
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['create_pie'], headers, payload)

    def update_pie(self, id: int, dividend_cash_action: str, end_date: str, goal: float, icon: str, instrument_shares: dict, name: str) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/create
        """
        payload = dict(
            dividendCashAction=dividend_cash_action,
            endData=end_date,
            goal=goal,
            icon=icon,
            instrumentShares=instrument_shares,
            name=name
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['update_pie'].format(id=id), headers, payload)

    def delete_pie(self, id: int) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/delete
        """
        return self._delete(self.END_POINTS['delete_pie'].format(id=id), {})

    def get_orders(self) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/orders
        """
        return self._get(self.END_POINTS['get_orders'], {})

    def get_order(self, id: int) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/orders
        """
        return self._get(self.END_POINTS['get_order'].format(id=id), {})

    def delete_order(self, id: int) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/cancelOrder
        """
        return self._delete(self.END_POINTS['delete_order'].format(id=id), {})

    def place_limit_order(self, limit_price: float, quantity: float, ticker: str, time_validity: str) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/placeLimitOrder
        """
        payload = dict(
            limitPrice=limit_price,
            quantity=quantity,
            ticker=ticker,
            timeValidity=time_validity
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['place_limit_order'], headers, payload)

    def place_market_order(self, quantity: float, ticker: str) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/placeLimitOrder
        """
        payload = dict(
            quantity=quantity,
            ticker=ticker
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['place_market_order'], headers, payload)

    def place_stop_order(self, stop_price: float, quantity: float, ticker: str, time_validity: str) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/placeStopOrder
        """
        payload = dict(
            stopPrice=stop_price,
            quantity=quantity,
            ticker=ticker,
            timeValidity=time_validity
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['place_stop_order'], headers, payload)

    def place_stop_limit_order(self, limit_price: float, stop_price: float, quantity: float, ticker: str, time_validity: str) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/placeStopLimitOrder
        """
        payload = dict(
            limitPrice=limit_price,
            stopPrice=stop_price,
            quantity=quantity,
            ticker=ticker,
            timeValidity=time_validity
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['place_stop_limit_order'], headers, payload)

    def get_account_cash(self) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/accountCash
        """
        return self._get(self.END_POINTS['get_account_cash'], {})

    def get_account(self) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/account
        """
        return self._get(self.END_POINTS['get_account'], {})

    def get_positions(self) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/portfolio
        """
        return self._get(self.END_POINTS['get_positions'], {})

    def get_position(self, ticker: str) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/positionByTicker
        """
        return self._get(self.END_POINTS['get_position'].format(ticker=ticker), {})

    def get_order_history(self, cursor: int, ticker: str, limit: int) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/orders_1
        """
        query = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return self._get(self.END_POINTS['get_order_history'], {}, query)

    def get_dividends(self, cursor: int, ticker: str, limit: int) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/dividends
        """
        query = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return self._get(self.END_POINTS['get_dividends'], {}, query)

    def get_exports(self) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/getReports
        """
        return self._get(self.END_POINTS['get_exports'], {})

    def get_transactions(self, cursor: int, limit: int) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/transactions
        """
        query = {
            "cursor": cursor,
            "limit": limit
        }
        return self._get(self.END_POINTS['get_transactions'], {}, query)

    def get_export(self, data_included: dict, time_from: str, time_to: str) -> dict:
        """
        https://t212public-api-docs.redoc.ly/#operation/placeStopLimitOrder
        """
        payload = dict(
            dataIncluded=data_included,
            timeFrom=time_from,
            timeTo=time_to
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['get_export'], headers, payload)
