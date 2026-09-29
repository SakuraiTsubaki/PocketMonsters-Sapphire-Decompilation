from __future__ import annotations
import hashlib,json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class EntrypointTests(unittest.TestCase):
 def test_entry_evidence_and_source_agree(self):
  r=json.loads((ROOT/"analysis"/"sapphire-jp-entrypoint.json").read_text(encoding="utf-8"));s=(ROOT/"src"/"rom_entry.s").read_text(encoding="utf-8");self.assertEqual(r["source_sha256"],"6a5ff7656531ab41d1ea9cd8f2d045ab6228405b43f3ee09ea3ff5077c0f60c9");self.assertEqual((r["instruction_word"],r["target_address"]),(0xEA000032,0x080000D0));self.assertEqual(int(re.search(r"\.word 0x([0-9a-f]+)",s).group(1),16),r["instruction_word"])
 def test_manifest_hashes_outputs(self):
  m=json.loads((ROOT/"manifests"/"entrypoint.json").read_text(encoding="utf-8"));
  for o in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest(),o["sha256"])
if __name__=="__main__":unittest.main()
