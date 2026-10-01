import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_map_and_source(self):
  m=json.loads((ROOT/'analysis/sapphire-jp-key-input-map.json').read_text());s=(ROOT/'src/key_input.c').read_text();self.assertEqual(m['target']['release'],'AXPJ-rev0');self.assertEqual(m['rom_code_range']['sha256'],'6f57c651796485bd14d6e53f08bed93660ec1b6496557070b7c643211a8ec0ba')
  for token in ('InitKeys(','ReadKeys(','gMain.keyRepeatCounter--','gMain.newKeys |= A_BUTTON'):self.assertIn(token,s)
  self.assertFalse(m['rom_code_range']['raw_bytes_published'])
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/key-input-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()
