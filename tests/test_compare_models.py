import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from evaluate_context import measure
class PairedBenchmarkContractTests(unittest.TestCase):
 def test_identical_context_predictions_have_identical_metrics(self):
  gold=json.loads((ROOT/"evaluation/fixtures/context_truth.json").read_text())
  pred=json.loads((ROOT/"evaluation/fixtures/context_predictions.json").read_text())
  a,b=measure(gold,pred),measure(gold,pred)
  self.assertEqual(a["field_metrics"],b["field_metrics"])
  self.assertEqual(a["missed_human_review"],b["missed_human_review"])
if __name__=="__main__": unittest.main()
