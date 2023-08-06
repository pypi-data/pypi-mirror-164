from unittest import TestCase
from unittest.mock import call

import pytest
from requests import HTTPError

from pyrozza.client import Client
from pyrozza.exceptions import PyrozzaError


class TestClient(TestCase):
    def setUp(self):
        self.pyrozza = Client()

    def test_valid_geo_params(self):
        # The values don't matter for this test
        valid_geo_kwargs = [{"lat": 12, "lon": 34}, {"poly": 56}, {"location_id": 78}]
        returned_params = [{"lat": 12, "lng": 34}, {"poly": 56}, {"location_id": 78}]
        for idx, valid_kwarg in enumerate(valid_geo_kwargs):
            assert self.pyrozza._get_geo_params(**valid_kwarg) == returned_params[idx]

    def test_invalid_geo_params(self):
        # The values don't matter for this test
        invalid_geo_kwargs = [
            {"lat": 12},
            {"lon": 34},
            {"lat": 56, "poly": 78},
            {"lon": 91, "location_id": 23},
        ]

        with pytest.raises(PyrozzaError) as exc:
            for valid_kwarg in invalid_geo_kwargs:
                assert self.pyrozza._get_geo_params(**valid_kwarg) == exc
                assert str(exc) == "Incorrect geo-related kwargs provided."

    def test_street_level_crimes(self):
        # Doesn't matter what the actual response is
        expected_return = {"test": "response"}
        self.mocked_request.return_value = self._mocked_response(200, expected_return)
        returned = self.pyrozza.street_level_crimes(lat=1, lon=2, date="2022-07")
        assert returned == expected_return
        self.mocked_request.assert_called_once_with(
            "GET",
            "https://data.police.uk/api/crimes-street/all-crime",
            params={"lat": 1, "lng": 2, "date": "2022-07"},
            allow_redirects=True,
        )

    def test_street_level_outcomes(self):
        # Doesn't matter what the actual response is
        expected_return = {"test": "response"}
        self.mocked_request.return_value = self._mocked_response(200, expected_return)
        returned = self.pyrozza.street_level_outcomes(location_id=3, date="2022-07")
        assert returned == expected_return
        self.mocked_request.assert_called_once_with(
            "GET",
            "https://data.police.uk/api/outcomes-at-location",
            params={"location_id": 3, "date": "2022-07"},
            allow_redirects=True,
        )

    def test_crime_categories(self):
        # Doesn't matter what the actual response is
        expected_return = {"test": "response"}
        self.mocked_request.return_value = self._mocked_response(200, expected_return)
        returned = self.pyrozza.crime_categories(date="2022-07")
        assert returned == expected_return
        self.mocked_request.assert_called_once_with(
            "GET",
            "https://data.police.uk/api/crime-categories",
            params={"date": "2022-07"},
            allow_redirects=True,
        )

    def _mocked_response(self, status, json, ok=True):
        class Response:
            def __init__(self, status, json, ok):
                self.status = status
                self._json = json
                self.ok = ok

            def json(self):
                return self._json

            def raise_for_status(self):
                if not self.ok:
                    raise HTTPError

        return Response(status, json, ok)
