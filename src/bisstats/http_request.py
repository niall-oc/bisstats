import requests
import pandas as pd
from lxml import etree
from io import StringIO


class Client:
    END_POINTS = dict(
        get_data='/data/{context}/{agencyID}/{resourceID}/{version}/{key}',
    )

    def __init__(self, api_key, domain=None):
        """
        """
        self.API_KEY = api_key
        self.DOMAIN = domain or 'stats.bis.org'
        self.PATH = '/api/v2'
        self.BASE_URL = f'https://{self.DOMAIN}{self.PATH}'
        self.AUTH = {'Authorization': self.API_KEY}

    def _get(self, url: str, headers: dict, params: dict = None) -> dict:
        """
        """
        headers.update(self.AUTH)
        headers = {'Content-Type': 'application/json'}
        resp = requests.get(f'{self.BASE_URL}{url}', headers=headers, params=params)
        if resp.ok:
            root = etree.fromstring(resp.text.encode('ascii'))
            message_def_url = "{" + [m for m in root.attrib.values()[0].split(' ') if m.endswith('message')][0] + "}"
            metadata = root.find(message_def_url + 'DataSet/Series').attrib
            df = pd.DataFrame([i.attrib for i in root.findall(message_def_url + 'DataSet/Series/')])
            return {'meta': metadata, 'data': df}
        else:
            raise Exception(f"{resp.status_code} - {resp.text}")

    def _delete(self, url: str, headers: dict, params: dict = None) -> dict:
        """
        """
        headers.update(self.AUTH)
        headers = {'Content-Type': 'application/json'}
        resp = requests.delete(f'{self.BASE_URL}{url}', headers=headers, params=params)
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(f"{resp.status_code} - {resp.text}")

    def _post(self, url: str, headers: dict, payload: dict) -> dict:
        """
        """
        headers.update(self.AUTH)
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(f'{self.BASE_URL}{url}', headers=headers, json=payload)
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(f"HTTP {resp.status_code} - {resp.text}")

    def get_data(self, context, agencyID, resourceID, version, key,
                 c=None,
                 updatedAfter=None,
                 firstNObservations=None,
                 lastNObservations=None,
                 dimensionAtObservation=None) -> dict:
        """
        spec is /data/{context}/{agencyID}/{resourceID}/{version}/{key}
        example is https://stats.bis.org/api/v2/data/dataflow/BIS/WS_TC/2.0/Q.5R.H.A.M.770.A
        agencyID, resourceID and version are taken from a page like https://data.bis.org/topics/TOTAL_CREDIT/BIS,WS_TC,2.0/Q.5R.H.A.M.770.A
        """
        return self._get(self.END_POINTS['get_data'].format(context=context, agencyID=agencyID, resourceID=resourceID, version=version, key=key), {})
