![Build](https://github.com/regoawt/pyrozza/actions/workflows/cicd.yml/badge.svg)
# pyrozza
A Python wrapper for the UK Police API

## Usage
Instantiate the client:
```python
client = pyrozza.Client()
```

Currently, the following methods are available:
```python
client.street_level_crimes(
        lat: float = None,
        lon: float = None,
        poly: List[tuple] = None,
        date: str = None,
    )
client.street_level_outcomes(
        lat: float = None,
        lon: float = None,
        poly: List[tuple] = None,
        location_id: int = None,
        date: str = None
    )

client.crime_categories(date: str = None)
```

For the geo-related kwargs, only one of the following must be provided:
- `lat` AND `lon`
- `poly`
- `location_id`