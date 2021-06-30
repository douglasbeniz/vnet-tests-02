"""
An example of a test module in pytest
"""

from vnet_tests_02 import join

def test_join_use_case() -> None:
    """Function result when parameters are properly received as use case specification"""
    assert join([1, 2, 3], ", ") == "1, 2, 3"

def test_join_edge_case_signle_item() -> None:
	"""Edge case situation when only one item is received in the input list"""
	assert join([1], ", ") == "1"

def test_join_edge_case_empty_delimiter() -> None:
	"""Edge case situation when delimiter is an empty string"""
	assert join([1, 2, 3], "") == "123"
