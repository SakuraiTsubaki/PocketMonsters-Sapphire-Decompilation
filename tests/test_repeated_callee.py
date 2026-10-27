import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]


class RepeatedCalleeTests(unittest.TestCase):
    def test_origin_frontier_matches_global_callback_map(self):
        frontier = json.loads((ROOT / "analysis/sapphire-jp-repeated-callee.json").read_text())
        address_map = json.loads((ROOT / "analysis/axp-j-rev0-retail-main-callbacks-map.json").read_text())
        update = address_map["functions"][0]
        self.assertEqual(int(update["address"], 16), frontier["start_address"])
        self.assertEqual(frontier["start_offset"], 840)
        self.assertTrue(frontier["raw_halfwords_omitted"])
        self.assertTrue(all("halfword" not in item for item in frontier["instructions"]))
        source = (ROOT / update["source"]).read_text()
        for function in address_map["functions"]:
            self.assertIn(function["name"] + "(", source)
        self.assertFalse(address_map["raw_rom_bytes_included"])

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/repeated-callee.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(
                hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                output["sha256"],
            )


if __name__ == "__main__":
    unittest.main()
