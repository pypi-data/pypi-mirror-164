from dnsdist_console import Console
from dnsdist_console import Statistics
import unittest

import dns.resolver

                           
my_resolver = dns.resolver.Resolver(configure=False)
my_resolver.nameservers = ['127.0.0.1']

r = my_resolver.resolve('www.github.com', 'a')
try:
    r = my_resolver.resolve('12345678', 'a')
except dns.resolver.NXDOMAIN:
    pass

class TestStatistic(unittest.TestCase):
    def setUp(self):
        self.console = Console(host="127.0.0.1", port=5199,
                               key="GQpEpQoIuzA6kzgwDokX9JcXPXFvO1Emg1wAXToJ0ag=")

    def tearDown(self):
        self.console.disconnect()
        
    def test_get_global(self):
        """get global stats"""
        s = Statistics(console=self.console)
        self.assertEqual(s["global"]["queries"], "2")

    def test_get_topqueries(self):
        """get top queries"""
        s = Statistics(console=self.console)
        self.assertEqual(s["top-queries"][0]["hits"], "1")

    def test_get_nxdomain(self):
        """get nxdomain"""
        s = Statistics(console=self.console)
        self.assertEqual(s["top-nxdomain"][0]["hits"], "1")

    def test_get_topclients(self):
        """get top clients"""
        s = Statistics(console=self.console)
        self.assertEqual(s["top-clients"][0]["hits"], "2")