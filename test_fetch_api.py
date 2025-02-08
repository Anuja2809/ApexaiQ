import pytest
from data_fetching_fakestore_api import APIClient

@pytest.fixture
def api_client():
    return APIClient("https://fakestoreapi.com/products")

def test_fetch_data(api_client):
    # Fetch data from the API
    data = api_client.fetch_data()
    
    # Validate that the response is a list
    assert isinstance(data, list), "Expected list but got different type"
    
    # Validate that the list is not empty
    assert len(data) > 0, "API returned empty list"
    
    # Validate that each item is a dictionary (expected JSON structure)
    assert isinstance(data[0], dict), "Expected dictionary in list but got different type"

    # Optional: Check the structure of the first item
    assert "id" in data[0], "Missing 'id' key in the first item"
    assert "title" in data[0], "Missing 'title' key in the first item"
