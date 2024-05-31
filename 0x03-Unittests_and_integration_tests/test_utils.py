#!/usr/bin/env python3
"""test_utils module"""
import unittest
from parameterized import parameterized
from utils import *
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test case for nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test the method if it returns the expected output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """raises KeyError for path in nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """test the method if it returns the expected output"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for test_memoize method"""

    def test_memoize(self):
        """test memoize function"""
        class TestClass:
            """Test Class"""

            def a_method(self):
                """returns an integer"""
                return 42

            @memoize
            def a_property(self):
                """returns property of object"""
                return self.a_method()
        obj_test = TestClass()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            result1 = obj_test.a_property
            result2 = obj_test.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
