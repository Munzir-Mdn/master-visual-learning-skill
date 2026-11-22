from pathlib import Path
import json,re,unittest
ROOT=Path(__file__).resolve().parents[1]
class TestMVLS(unittest.TestCase):
 def test_structure(self):
  self.assertTrue((ROOT/'SKILL.md').is_file())
  self.assertEqual(len(list((ROOT/'modules').glob('M*.md'))),9)
 def test_config(self):
  c=json.loads((ROOT/'config/defaults.json').read_text(encoding='utf-8'))
  self.assertEqual(c['version'],'1.0.0')
  self.assertTrue(c['generation_requires_approval'])
  self.assertFalse(c['quiz_auto'])
  self.assertFalse(c['feynman_auto'])
 def test_decisions(self):
  s=(ROOT/'docs/decisions.md').read_text(encoding='utf-8')
  decisions=re.findall(r'^\d+\. \*\*.*?\*\* — Choice \*\*([ABC])\*\*\.',s,re.M)
  self.assertEqual(len(decisions),28)
  for n in (3,9,14): self.assertEqual(decisions[n-1],'A')
  self.assertTrue(all(x=='C' for i,x in enumerate(decisions,1) if i not in (3,9,14)))
 def test_module_links(self):
  s=(ROOT/'SKILL.md').read_text(encoding='utf-8')
  for p in re.findall(r'\]\((modules/[^)]+)\)',s): self.assertTrue((ROOT/p).exists(),p)
 def test_security_gates(self):
  s=(ROOT/'SKILL.md').read_text(encoding='utf-8').lower()
  for term in ('explicit approval','untrusted input','do not add feynman','minimal source attribution','not verified'):
   self.assertIn(term,s)
if __name__=='__main__': unittest.main()
