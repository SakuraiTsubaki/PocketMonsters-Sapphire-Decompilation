from __future__ import annotations
import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location("verify_target",ROOT/"tools"/"verify_target.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def fixture():
 d=bytearray(0x200);d[0xA0:0xAC]=b"POKEMON SAPP";d[0xAC:0xB0]=b"AXPJ";d[0xB0:0xB2]=b"01";d[0xB2]=0x96;d[0xBC]=0;d[0xBD]=(-sum(d[0xA0:0xBD])-0x19)&0xFF;return bytes(d)
class VerifyTargetTests(unittest.TestCase):
 def target(self,o,rev=0):return {"size":len(fixture()),"hashes":[{"algorithm":"sha1","value":o["sha1"]},{"algorithm":"sha256","value":o["sha256"]}],"header":{"title":"POKEMON SAPP","game_code":"AXPJ","maker_code":"01","software_version":rev,"header_checksum":o["header"]["header_checksum"]}}
 def test_matching_identity(self):
  o=m.inspect_bytes(fixture());self.assertTrue(all(m.compare_identity(o,self.target(o)).values()))
 def test_wrong_revision_is_rejected(self):
  o=m.inspect_bytes(fixture());self.assertFalse(m.compare_identity(o,self.target(o,1))["header_software_version"])
 def test_short_input_is_rejected(self):
  with self.assertRaisesRegex(ValueError,"too small"):m.inspect_bytes(bytes(0xBF))
if __name__=="__main__":unittest.main()
