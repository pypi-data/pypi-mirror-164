import pandas as pd
import unittest

from mssev import global_armss


class TestGlobalARMSS(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_csv('test/data.csv')

    def test_original(self):
        original_armss = global_armss(self.data, table='original')
        armss_delta = original_armss - self.data.gARMSS
        self.assertTrue((armss_delta.abs() < 0.001).all())
