import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RepeatedCalleeTests(unittest.TestCase):
 def test_manifest_and_publication_shape(self):
  m=json.loads((ROOT/"manifests/repeated-callee.json").read_text());o=m["outputs"][0];p=ROOT/o["path"]
  self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),o["sha256"]);r=json.loads(p.read_text())
  self.assertTrue(r["raw_halfwords_omitted"]);self.assertTrue(all("halfword" not in x for x in r["instructions"]));self.assertEqual(r["start_offset"],0x348)
if __name__=="__main__":unittest.main()
