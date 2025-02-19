import sys
import os

# Add the current directory to the system path to ensure the data_fetching_fakestore_api module can be found
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import functions from the correct file (data_fetching_fakestore_api.py)
from data_fetching_fakestore_api import fetch_data_from_api, save_data_to_json

import pytest
import json
from unittest.mock import Mock
import requests

# Sample URL for the Fake Store API
url = "https://fakestoreapi.com/products"


@pytest.fixture
def mock_api_response(mocker):
    # Mocking the response of requests.get
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = [
        {"id": 1, "title": "Product 1", "price": 50.0},
        {"id": 2, "title": "Product 2", "price": 60.0}
    ]
    return mock_response


def test_fetch_data_from_api(mock_api_response):
    """
    Test the function fetch_data_from_api to ensure it correctly fetches and returns data.
    """
    data = fetch_data_from_api(url)
    assert data is not None, "API should return data"
    assert isinstance(data, list), "Returned data should be in list format"
    assert len(data) > 0, "Data should not be empty"
    assert "id" in data[0], "Each product should have an 'id' field"
    assert "title" in data[0], "Each product should have a 'title' field"


def test_fetch_data_from_api_http_error(mocker):
    """
    Test the function fetch_data_from_api for HTTP error handling.
    """
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.status_code = 404  # Simulating 404 Not Found
    mock_response.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("HTTP error occurred")
    
    data = fetch_data_from_api(url)
    assert data is None, "Data should be None when there's an HTTP error"


def test_save_data_to_json(mock_api_response):
    """
    Test the function save_data_to_json to ensure data is written to a JSON file correctly.
    """
    data = fetch_data_from_api(url)
    filename = "test_products.json"
    save_data_to_json(data, filename)

    # Check if file is created
    with open(filename, 'r') as file:
        saved_data = json.load(file)
        assert saved_data == data, "Saved data should match the fetched data"


def test_save_empty_data_to_json():
    """
    Test the save_data_to_json function when no data is available.
    """
    empty_data = []
    filename = "empty_products.json"
    save_data_to_json(empty_data, filename)

    # Check if the file is created with empty data
    with open(filename, 'r') as file:
        saved_data = json.load(file)
        assert saved_data == empty_data, "Saved data should be empty"
