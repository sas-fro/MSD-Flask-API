import unittest

import datastorage
import json
import os

class TestDataStorage(unittest.TestCase):


    def setUp(self):
        self.ds = datastorage.DataStorage()
        self.ds.experiments.clear()
        self.ds.patients.clear()
        self.ds.data.clear()


    def test_create_patient(self):
        result = self.ds.create_patient("P11")
        self.assertTrue(result >= 0)


    def test_create_experiment(self):
        result = self.ds.create_experiment("E1")
        self.assertTrue(result >= 0)


    def test_get_patients(self):
        self.ds.create_patient("P1")
        self.ds.create_patient("P2")
        self.ds.create_patient("P3")
        self.assertEqual(len(self.ds.get_patients()), 3)


    def test_get_experiments(self):
        self.ds.create_experiment("E1")
        self.ds.create_experiment("E2")
        self.ds.create_experiment("E3")
        self.assertEqual(len(self.ds.get_experiments()), 3)


    def test_store(self):
        # Store data
        data = json.loads('{"some_data": "a"}')
        self.ds.store('unit_test_store_test', data)
        # Read data
        with open(os.getcwd() + '\\unit_test_store_test.json') as f:
            read_data = json.load(f)
        
        self.assertEqual(read_data, data)


if __name__ == '__main__':
    unittest.main()