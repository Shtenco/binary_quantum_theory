"""Regression checks for valid scientific negatives and completion consistency."""
import ast,contextlib,importlib.util,io,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class AuditStatusTests(unittest.TestCase):
 def test_no_go_is_valid_but_cannot_close(self):
  spec=importlib.util.spec_from_file_location('ledger',ROOT/'scripts/verify_theory_gates.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  data=json.loads((ROOT/'theory_gates.json').read_text())
  with tempfile.TemporaryDirectory() as d:
   path=Path(d)/'ledger.json';m.LEDGER=path
   for declared,expected in [(False,0),(True,1)]:
    data['core_theory_closed_declared']=declared;path.write_text(json.dumps(data));buf=io.StringIO()
    with contextlib.redirect_stdout(buf):code=m.main()
    result=json.loads(buf.getvalue());self.assertEqual(code,expected);self.assertFalse(result['structural_candidate_closed']);self.assertEqual(result['valid'],not declared)
 def test_all_nine_physical_conditions_required(self):
  def value(file,name):
   tree=ast.parse((ROOT/file).read_text())
   return next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets))
  actual=value('bcqg_bit_to_gravity_final.py','REQUIRED_PHYSICAL');expected=value('scripts/verify_physicalization_gates.py','EXPECTED_REQUIRED_PHYSICAL')
  self.assertEqual(actual,expected);self.assertEqual(len(actual),9)

if __name__=='__main__':unittest.main()
