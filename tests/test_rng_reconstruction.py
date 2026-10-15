import hashlib, json, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]
EXPECTED={"release":"AXPJ-rev0","sha":"6a5ff7656531ab41d1ea9cd8f2d045ab6228405b43f3ee09ea3ff5077c0f60c9","variant":"standard","random":"0x0803E130","seed":"0x0803E150","rng":"0x03004748"}
class Tests(unittest.TestCase):
 def test_evidence_and_cfgs(self):
  m=json.loads((ROOT/'analysis/sapphire-jp-rng-map.json').read_text());self.assertEqual(m['target'],{'release':EXPECTED['release'],'sha256':EXPECTED['sha']});self.assertEqual(m['variant'],EXPECTED['variant']);self.assertEqual(m['globals']['gRngValue'],EXPECTED['rng']);self.assertEqual(m['algorithm']['multiplier'],1103515245);self.assertEqual(m['algorithm']['increment'],24691)
  for name,slug,address in (('Random','random',EXPECTED['random']),('SeedRng','seed-rng',EXPECTED['seed'])):
   cfg=json.loads((ROOT/f'analysis/sapphire-jp-{slug}-cfg.json').read_text());self.assertEqual(cfg['source_sha256'],EXPECTED['sha']);self.assertTrue(cfg['raw_halfwords_omitted']);self.assertEqual((len(cfg['returns']),cfg['calls']),(1,[]));self.assertEqual(m['functions'][name]['address'],address);self.assertEqual(cfg['range_start'],int(address,16));self.assertEqual(cfg['range_end'],int(m['functions'][name]['range_end_exclusive'],16))
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/rng-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included']);[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
