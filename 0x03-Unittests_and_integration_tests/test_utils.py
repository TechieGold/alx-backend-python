#!/usr/bin/env python3

"""unittest module
"""

import unittest
from parameterized import parameterized
from typing import Dict, Union, Tuple
from utils import (
    access_nested_map
)


class TestAccessNestedMap(unittest.TestCase):
    """ Tests the `access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nexted_map(self, nested_map: Dict,
                               path: Tuple[str],
                               expected_result: Union[Dict, int],
                               ) -> None:
        """ Tests `access_nested_map` 's output"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
