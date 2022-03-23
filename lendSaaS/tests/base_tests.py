import unittest
from unittest.mock import patch
from client import LendClient


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.lc = LendClient('api_key', 'client_name')
        

     