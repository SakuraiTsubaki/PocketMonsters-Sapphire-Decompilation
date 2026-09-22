from __future__ import annotations
import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ThumbEntryCfgTests(unittest.TestCase):
 def test_reachable_cfg(self):
  r=json.loads((ROOT/"analysis"/"sapphire-jp-thumb-entry-cfg.json").read_text());self.assertEqual((r["start_address"],r["scan_limit_address"]),(0x0800024C,0x0800424C));self.assertEqual((r["instruction_halfwords"],len(r["edges"]),len(r["calls"])),(107,18,21));self.assertFalse(r["return_observed"])
 def test_manifest_hash(self):
  m=json.loads((ROOT/"manifests"/"thumb-entry-cfg.json").read_text());o=m["outputs"][0];self.assertEqual(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest(),o["sha256"])
if __name__=="__main__":unittest.main()

