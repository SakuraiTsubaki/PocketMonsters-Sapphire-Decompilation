import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_map_and_ordered_behavior(self):
  m=json.loads((ROOT/'analysis/sapphire-jp-vblank-intr-map.json').read_text());s=(ROOT/'src/vblank_intr.c').read_text();self.assertEqual(m['target']['release'],'AXPJ-rev0');self.assertEqual(m['function']['address'],0x08000574);self.assertFalse(m['rom_code_range']['raw_bytes_published'])
  tokens=['if(!gLinkVSyncDisabled)','savedIme=REG_IME','m4aSoundVSync()','gMain.vblankCounter1++','gMain.vblankCallback()','gMain.vblankCounter2++','gPcmDmaCounter=gSoundInfo.pcmDmaCounter','m4aSoundMain()','Random()','INTR_CHECK|=INTR_FLAG_VBLANK']
  positions=[s.index(t) for t in tokens];self.assertEqual(positions,sorted(positions))
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/vblank-intr-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()
