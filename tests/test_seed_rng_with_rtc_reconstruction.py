import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_cfg_map_and_source(self):
  cfg=json.loads((ROOT/'analysis/sapphire-jp-seed-rng-with-rtc-cfg.json').read_text());m=json.loads((ROOT/'analysis/sapphire-jp-seed-rng-with-rtc-map.json').read_text());src=(ROOT/'src/seed_rng_with_rtc.c').read_text()
  self.assertEqual(cfg['source_sha256'],m['target']['sha256']);self.assertEqual(cfg['start_address'],int(m['function']['address'],16));self.assertEqual(cfg['range_end'],int(m['function']['range_end_exclusive'],16));self.assertTrue(cfg['return_observed']);self.assertTrue(cfg['raw_halfwords_omitted']);self.assertFalse(m['rom_code_range']['raw_bytes_published']);self.assertIn('void SeedRngWithRtc(void)',src)
 def test_behavior_and_calls(self):
  m=json.loads((ROOT/'analysis/sapphire-jp-seed-rng-with-rtc-map.json').read_text());src=(ROOT/'src/seed_rng_with_rtc.c').read_text();self.assertEqual([c['name'] for c in m['calls']],["RtcGetMinuteCount","SeedRng"])
  self.assertIn('(seed >> 16) ^ (seed & 0xFFFF)',src);self.assertEqual(m['behavior']['seed_width_bits'],16)
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/seed-rng-with-rtc-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()

