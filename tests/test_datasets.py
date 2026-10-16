import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from check_datasets import validate_registry
ROOT=Path(__file__).resolve().parents[1]
class DatasetTests(unittest.TestCase):
    def test_registry_metadata(self):
        registry=json.loads((ROOT/"evaluation/dataset-registry.json").read_text())
        self.assertEqual(validate_registry(registry),8)
    def test_unapproved_is_blocked(self):
        registry=json.loads((ROOT/"evaluation/dataset-registry.json").read_text())
        with self.assertRaises(ValueError):
            validate_registry(registry,"chexpert")
if __name__=="__main__":
    unittest.main()
