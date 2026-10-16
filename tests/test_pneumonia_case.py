import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from medgemma_pneumonia_case import parse_class
class TestLabelParser(unittest.TestCase):
 def test_single_normal(self):self.assertEqual(parse_class("NORMAL"),"normal")
 def test_single_pneumonia(self):self.assertEqual(parse_class("PNEUMONIA"),"pneumonia")
 def test_unknown_abstains(self):self.assertIsNone(parse_class("UNKNOWN"))
 def test_conflicting_abstains(self):self.assertIsNone(parse_class("normal or pneumonia"))
 def test_no_partial_match(self):self.assertIsNone(parse_class("abnormality"))
if __name__=="__main__":unittest.main()
