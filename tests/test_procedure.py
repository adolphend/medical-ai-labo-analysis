import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from interpret_procedure import interpret
class ProcedureTests(unittest.TestCase):
 def setUp(self): self.obj=json.loads((ROOT/"pipeline/example-procedure.json").read_text())
 def test_order_and_blocking(self):
  result=interpret(self.obj)
  self.assertEqual(result["steps"][0]["step"],"clinical_intake")
  self.assertEqual(next(x for x in result["steps"] if x["step"]=="finding_model")["state"],"blocked")
  self.assertEqual(result["models_executed"],0)
 def test_cycle(self):
  self.obj["steps"][0]["depends_on"]=["follow_up"]
  with self.assertRaisesRegex(ValueError,"cycle"): interpret(self.obj)
 def test_clinician_gate(self):
  next(x for x in self.obj["steps"] if x["id"]=="management")["approval_required"]=False
  with self.assertRaisesRegex(ValueError,"approval"): interpret(self.obj)
if __name__=="__main__":unittest.main()
