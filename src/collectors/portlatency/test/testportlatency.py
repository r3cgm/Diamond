#!/usr/bin/python
# coding=utf-8
################################################################################

from test import CollectorTestCase
from test import get_collector_config

class TestPortLatencyCollector(CollectorTestCase):
    def setUp(self):
        config = get_collector_config('PortLatencyCollector', {})

        self.collector = PortlatencyCollector(config, None)

    def test_import(self):
        self.assertTrue(PortLatencyCollector)
