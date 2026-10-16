import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from medgemma_disease_pipeline import build,audit
class MedGemmaDiseasePipelineTests(unittest.TestCase):
 def test_fifty_conditions_and_all_stages(self):
  p=build();s=audit(p)
  self.assertEqual(s["checked_diseases"],50)
  self.assertEqual(s["checked_stages"],450)
  self.assertEqual(s["unmeasured_stages"],450)
 def test_clinical_approval_is_not_bypassed(self):
  p=build();p["conditions"][0]["stages"][7]["human_signoff"]=False
  with self.assertRaises(ValueError):audit(p)
 def test_claimed_evaluation_requires_provenance(self):
  p=build();p["conditions"][0]["stages"][0]["evaluation"]["status"]="passed"
  with self.assertRaises(ValueError):audit(p)
if __name__=="__main__": unittest.main()
