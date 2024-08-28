from bisstats.http_request import Client
import re

c = Client('FAKE_API_KEY')
matcher = re.compile(f'{c.BASE_URL}/*')

GET_END_POINTS = dict(
    get_data='/data/{context}/{agencyID}/{resourceID}/{version}/{key}',
)

PARAM_END_POINTS = dict(
)

COMPLEX_ENDPOINTS = dict(
)

def test_get_data():
    """
    https://stats.bis.org/api/v2/data/dataflow/BIS/WS_TC/2.0/Q.5R.H.A.M.770.A

    agencyID and resourceID are taken from a page like https://data.bis.org/topics/TOTAL_CREDIT/BIS,WS_TC,2.0/Q.5R.H.A.M.770.A
    """
    result = c.get_data('dataflow', 'BIS', 'WS_TC', '2.0', 'Q.5R.H.A.M.770.A')
    assert len(result)
    print(result)

if __name__ == '__main__':
    result = c.get_data('dataflow', 'BIS', 'WS_TC', '2.0', 'Q.5R.H.A.M.770.A')
    print(result)
    print(result['data'])
