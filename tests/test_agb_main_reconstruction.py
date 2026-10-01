import hashlib,json,re,unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]

class AgbMainReconstructionTests(unittest.TestCase):
 def setUp(self):
  self.cfg=json.loads((ROOT/'analysis/sapphire-jp-thumb-entry-cfg.json').read_text())
  self.map=json.loads((ROOT/'analysis/sapphire-jp-agb-main-map.json').read_text())
  self.source=(ROOT/'src/main_loop.c').read_text()
 def test_every_mapped_call_is_in_verified_cfg(self):
  cfg_calls={(x['source'],x['target']) for x in self.cfg['calls']}
  mapped={(x['address'],x['target']) for x in self.map['direct_calls']}
  self.assertEqual(mapped,cfg_calls)
 def test_nonreturning_loop_boundary_is_verified(self):
  function=self.map['function']
  self.assertTrue(function['nonreturning'])
  self.assertFalse(self.cfg['return_observed'])
  edge=function['loop_back_edge']
  self.assertIn({'source':edge['source'],'target':edge['target'],'kind':'branch'},self.cfg['edges'])
 def test_repeated_callback_dispatch_is_preserved(self):
  calls=[x for x in self.map['direct_calls'] if x['name']=='UpdateLinkAndCallCallbacks']
  self.assertEqual([x['address'] for x in calls],[134218460,134218510,134218542])
  self.assertEqual(self.source.count('UpdateLinkAndCallCallbacks();'),3)
  self.assertIn('LinkRecvPostprocess();',self.source)
 def test_source_contains_reset_soft_reset_and_frame_tail(self):
  for token in ('RegisterRamReset(RESET_ALL)','B_START_SELECT','DoSoftReset();','PlayTimeCounter_Update();','MapMusicMain();','WaitForVBlank();','for (;;)'):
   self.assertIn(token,self.source)
  self.assertNotRegex(self.source,re.compile(r'0x[0-9a-fA-F]{8}.*(?:instruction|halfword)'))
 def test_manifest_hashes_every_output(self):
  manifest=json.loads((ROOT/'manifests/agb-main-reconstruction.json').read_text())
  for output in manifest['outputs']:
   self.assertEqual(hashlib.sha256((ROOT/output['path']).read_bytes()).hexdigest(),output['sha256'])

if __name__=='__main__':unittest.main()


