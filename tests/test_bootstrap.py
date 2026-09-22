from __future__ import annotations
import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class BootstrapTests(unittest.TestCase):
 def test_arm_to_thumb_transition(self):
  r=json.loads((ROOT/"analysis"/"sapphire-jp-bootstrap.json").read_text());t=r["transition"];self.assertEqual(r["instruction_count"],12);self.assertEqual((t["instruction_address"],t["literal_address"]),(0x080000FC,0x08000244));self.assertEqual((t["raw_target"],t["target_address"],t["target_state"]),(0x0800024D,0x0800024C,"thumb"))
 def test_manifest_hash(self):
  m=json.loads((ROOT/"manifests"/"bootstrap.json").read_text());o=m["outputs"][0];self.assertEqual(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest(),o["sha256"])
if __name__=="__main__":unittest.main()
