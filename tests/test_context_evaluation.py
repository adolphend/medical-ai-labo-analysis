import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from evaluate_context import measure
class ContextTests(unittest.TestCase):
 def setUp(self):
  self.gold=json.loads((ROOT/"evaluation/fixtures/context_truth.json").read_text())
  self.pred=json.loads((ROOT/"evaluation/fixtures/context_predictions.json").read_text())
 def test_detects_context_omissions(self):
  r=measure(self.gold,self.pred)
  self.assertEqual(r["n_cases"],2)
  self.assertEqual(r["field_metrics"]["facts"]["fn"],1)
  self.assertEqual(r["field_metrics"]["contraindication_flags"]["fn"],1)
  self.assertEqual(r["missed_human_review"],1)
 def test_unmatched_case_rejected(self):
  with self.assertRaises(ValueError): measure(self.gold,self.pred[:1])
 def test_untraceable_evidence(self):
  self.pred[0]["evidence_ids"]=["invented"]
  self.assertEqual(measure(self.gold,self.pred)["unsupported_evidence_ids"],1)
if __name__=="__main__":unittest.main()
