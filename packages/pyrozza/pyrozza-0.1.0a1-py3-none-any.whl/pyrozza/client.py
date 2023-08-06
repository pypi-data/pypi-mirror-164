from typing import List

import requests

from pyrozza.exceptions import PyrozzaError


class Client:
    """
    Client to interface with UK Police API.
    """

    def __init__(self):
        self._domain = "https://data.police.uk/api/"
        self._session = requests.Session()

    # TODO: Validate date helper method

    def street_level_crimes(
        self,
        lat: float = None,
        lon: float = None,
        poly: List[tuple] = None,
        date: str = None,
    ):
        """
        Crimes at street-level; either within a 1 mile radius of a single
        point, or within a custom area.

        :param lat: Latitude of the requested crime area
        :param lon: Longitude of the requested crime area
        :param poly: The lat/lng pairs which define the boundary of the custom area
        :param date: (YYYY-MM) Month within which crime was committed
        """
        endpoint = "crimes-street/all-crime"
        params = self._get_geo_params(lat=lat, lon=lon, poly=poly)
        if date:  # pragma: no branch
            params.update({"date": date})
        return self._get(endpoint=endpoint, params=params)

    def street_level_outcomes(
        self,
        lat: float = None,
        lon: float = None,
        poly: List[tuple] = None,
        location_id: int = None,
        date: str = None,
    ):
        """
        Outcomes at street-level; either at a specific location, within a 1
        mile radius of a single point, or within a custom area.

        :param lat: Latitude of the requested crime area
        :param lon: Longitude of the requested crime area
        :param poly: The lat/lng pairs which define the boundary of the custom area
        :param location_id: Specific location street ID
        :param date: (YYYY-MM) Month within which outcome was determined
        """
        endpoint = "outcomes-at-location"
        params = self._get_geo_params(
            lat=lat, lon=lon, poly=poly, location_id=location_id
        )
        if date:  # pragma: no branch
            params.update({"date": date})
        return self._get(endpoint=endpoint, params=params)

    def crime_categories(self, date: str = None):
        """
        Valid list of categories for a given date.

        :param date: (YYYY-MM) Month to filter list of crime categories by
        """
        endpoint = "crime-categories"
        params = {"date": date}
        return self._get(endpoint=endpoint, params=params)

    def _get(self, endpoint: str, *args, **kwargs):
        resp = self._session.get(f"{self._domain}{endpoint}", *args, **kwargs)
        resp.raise_for_status()
        return resp.json()

    def _get_geo_params(self, **kwargs):
        """
        Checks that the combination of geo-related kwargs are valid and returns
         the querydict.
        """
        valid_geo_kwargs = {("lat", "lon"), ("poly",), ("location_id",)}
        geo_kwargs = tuple(
            [geo_arg for geo_arg in kwargs.keys() if kwargs[geo_arg] is not None]
        )
        if geo_kwargs in valid_geo_kwargs:
            params = {key: kwargs.get(key) for key in geo_kwargs}

            # Change `lon` key to `lng`
            if "lon" in params.keys():
                params["lng"] = params["lon"]
                del params["lon"]
            return params
        raise PyrozzaError("Incorrect geo-related kwargs provided.")
