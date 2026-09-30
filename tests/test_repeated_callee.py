import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RepeatedCalleeTests(unittest.TestCase):
 def test_manifest_and_publication_shape(self):
  m=json.loads((ROOT/"manifests/repeated-callee.json").read_text());
  for o in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest(),o["sha256"])
  p=ROOT/m["outputs"][0]["path"];r=json.loads(p.read_text())
  self.assertTrue(r["raw_halfwords_omitted"]);self.assertTrue(all("halfword" not in x for x in r["instructions"]));self.assertEqual(r["start_offset"],0x348)
 def test_c_reconstruction_matches_cfg(self):
  r=json.loads((ROOT/"analysis/sapphire-jp-repeated-callee.json").read_text());m=json.loads((ROOT/"analysis/main-callbacks-map.json").read_text());s=(ROOT/"src/main_callbacks.c").read_text();self.assertEqual(m["functions"][0]["address"],r["start_address"])
  for f in m["functions"]:self.assertIn(f["name"]+"(",s)
  self.assertEqual(m["proven_offsets"]["gMain.heldKeys"],0x2c);self.assertFalse(m["naming_basis"]["raw_rom_bytes_published"])
if __name__=="__main__":unittest.main()
