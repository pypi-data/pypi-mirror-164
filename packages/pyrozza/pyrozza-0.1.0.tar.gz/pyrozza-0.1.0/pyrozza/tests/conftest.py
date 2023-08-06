import functools
from unittest.mock import patch

import pytest
from requests import Session


@pytest.fixture(scope="function", autouse=True)
def __mock_requests(request):
    """
    Fixture which mocks all usages of `requests.request`
    """
    patched_request = patch.object(Session, "request")
    mocked_request = patched_request.__enter__()

    request.cls.mocked_request = mocked_request
    request.addfinalizer(functools.partial(patched_request.__exit__, None, None, None))
