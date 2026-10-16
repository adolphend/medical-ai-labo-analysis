import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from evaluate_predictions import evaluate

ROOT=Path(__file__).resolve().parents[1]
class BinaryEvaluationTests(unittest.TestCase):
    def test_fixture_metrics(self):
        r=evaluate(ROOT/"evaluation/fixtures/truth.csv",ROOT/"evaluation/fixtures/predictions.csv")
        self.assertEqual((r["tp"],r["tn"],r["fp"],r["fn"]),(2,2,1,1))
        self.assertAlmostEqual(r["accuracy"],4/6)
        self.assertAlmostEqual(r["sensitivity"],2/3)
        self.assertAlmostEqual(r["specificity"],2/3)
    def test_mismatched_cases_are_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"p.csv"
            p.write_text("case_id,score\nother,0.8\n")
            with self.assertRaises(ValueError):
                evaluate(ROOT/"evaluation/fixtures/truth.csv",p)
    def test_bad_threshold_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(ROOT/"evaluation/fixtures/truth.csv",ROOT/"evaluation/fixtures/predictions.csv",1.2)
if __name__=="__main__":
    unittest.main()
