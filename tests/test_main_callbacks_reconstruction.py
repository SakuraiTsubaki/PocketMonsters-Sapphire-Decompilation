import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_map(self):
  m=json.loads((ROOT/'analysis/main-callbacks-map.json').read_text());self.assertEqual(m['target']['sha256'],'6a5ff7656531ab41d1ea9cd8f2d045ab6228405b43f3ee09ea3ff5077c0f60c9');self.assertEqual([f['name'] for f in m['functions']],['UpdateLinkAndCallCallbacks','InitMainCallbacks','CallCallbacks','SetMainCallback2']);self.assertTrue(all(len(f['bytes_sha256'])==64 for f in m['functions']))
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/main-callbacks-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
