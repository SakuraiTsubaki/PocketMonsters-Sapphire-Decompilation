import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_map_and_source(self):
  m=json.loads((ROOT/'analysis/sapphire-jp-interrupt-init-map.json').read_text());s=(ROOT/'src/interrupt_init.c').read_text();self.assertEqual(m['target']['release'],'AXPJ-rev0');self.assertEqual(m['dma']['byte_count'],0x800);self.assertEqual(m['dma']['control'],'0x84000200');self.assertFalse(m['rom_code_and_literals']['raw_bytes_published'])
  for name in ('InitIntrHandlers','SetVBlankCallback','SetHBlankCallback','SetVCountCallback','SetSerialCallback'):self.assertIn(name+'(',s)
  for token in ('gIntrTable[i] = gIntrTableTemplate[i]','DMA3.control = DMA_ENABLE | DMA_32BIT','REG_DISPSTAT = DISPSTAT_VBLANK_INTR'):self.assertIn(token,s)
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/interrupt-init-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()
