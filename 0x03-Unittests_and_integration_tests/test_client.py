#!/usr/bin/env python3
""" """
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
class TestGithubOrgClient(unittest.TestCase):
    """ Tests the `GithubOrgClient` class """
    @parameterized.expand([
        ("goggle", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json"
    )

    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """ Tests the `org` method. """
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
