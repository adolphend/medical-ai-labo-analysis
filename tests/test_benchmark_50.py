import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from benchmark_50_diseases import plan,validate_results
class FiftyDiseaseBenchmarkTests(unittest.TestCase):
 def test_plan(self):
  data=plan()
  self.assertEqual(data["number_of_diseases"],50)
  self.assertEqual(data["number_of_tasks"],250)
  self.assertTrue(all(s["status"]=="not_tested" for x in data["conditions"] for s in x["tasks"]))
 def test_invalid_result_is_rejected(self):
  with self.assertRaises(ValueError):validate_results({"results":[{"disease":"unknown","task":"foo"}]})
 def test_no_results(self):
  self.assertEqual(validate_results({"results":[]})["not_tested"],250)
if __name__=="__main__": unittest.main()
