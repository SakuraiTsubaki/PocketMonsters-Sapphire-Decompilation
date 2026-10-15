import hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1];COUNT=12
class T(unittest.TestCase):
 def test_catalog_evidence(self):
  s=json.loads((R/'analysis/rng-catalog-summary.json').read_text());c=json.loads((R/'analysis/global-release-catalog.json').read_text());self.assertEqual((s['release_count'],len(c['releases'])),(COUNT,COUNT));self.assertEqual(sum(x['origin_reference']for x in s['releases']),1)
  for x in s['releases']:
   m=json.loads((R/x['evidence']['map']).read_text());self.assertEqual(m['target']['sha256'],x['sha256']);self.assertEqual(m['variant'],'standard');self.assertEqual(m['algorithm'],s['algorithm'])
   for name,key in (('Random','random_cfg'),('SeedRng','seed_cfg')):
    cfg=json.loads((R/x['evidence'][key]).read_text());self.assertEqual(cfg['source_sha256'],x['sha256']);self.assertTrue(cfg['raw_halfwords_omitted']);self.assertEqual((len(cfg['returns']),cfg['calls']),(1,[]));self.assertEqual(cfg['range_start'],int(m['functions'][name]['address'],16));self.assertEqual(cfg['range_end'],int(m['functions'][name]['range_end_exclusive'],16))
 def test_manifest(self):
  m=json.loads((R/'manifests/rng-catalog-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
