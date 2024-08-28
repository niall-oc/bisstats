from bisstats.http_request import Client
import pytest
import requests_mock
import re

c = Client('FAKE_API_KEY')
matcher = re.compile(f'{c.BASE_URL}/*')

GET_END_POINTS = dict(
)

PARAM_END_POINTS = dict(
)

COMPLEX_ENDPOINTS = dict(
)
