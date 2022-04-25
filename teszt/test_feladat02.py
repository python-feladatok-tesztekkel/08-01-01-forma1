from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import main

class TestOOP2(TestCase):
    def test_feladat02(self):
        aktualis = main.feladat02()
        elvart = 289
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg a legnagyobb sebességet!")
