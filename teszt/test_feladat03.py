from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import main

class TestOOP3(TestCase):
    def test_feladat03(self):
        aktualis = main.feladat03()
        elvart = 256
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg a legkisebb sebességet!")
