#!/usr/bin/env python3
"""test_client module"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Test Github Organisation Client class"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
        ])
    @patch('client.get_json')
    def test_org(self, org_name: str,
                 response: Dict, mock_get_json) -> None:
        """Test org if the method return expected result"""
        mock_get_json.return_value = response

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, response)
        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org_name))

if __name__ == "__main__":
    unittest.main()
