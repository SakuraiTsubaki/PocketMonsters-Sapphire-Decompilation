import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]


class SeedRngWithRtcReconstructionTests(unittest.TestCase):
    def test_all_catalog_releases(self):
        catalog = json.loads((ROOT / "analysis/global-release-catalog.json").read_text(encoding="utf-8"))
        summary = json.loads((ROOT / "analysis/seed-rng-with-rtc-summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(summary["origin_reference"], catalog["releases"][0]["id"])
        for release in catalog["releases"]:
            release_id = release["id"]
            mapping = json.loads((ROOT / f"analysis/{release_id}-seed-rng-with-rtc-map.json").read_text(encoding="utf-8"))
            cfg = json.loads((ROOT / f"analysis/{release_id}-seed-rng-with-rtc-cfg.json").read_text(encoding="utf-8"))
            self.assertEqual(mapping["target"]["sha256"], release["sha256"])
            self.assertEqual([call["name"] for call in mapping["calls"]], ["RtcGetMinuteCount", "SeedRng"])
            self.assertEqual(mapping["function"]["rom_code_range"]["length"], 24)
            self.assertEqual(mapping["behavior"]["mask_literal"], "0x0000FFFF")
            self.assertTrue(cfg["raw_halfwords_omitted"])
            self.assertFalse(mapping["raw_rom_bytes_included"])

    def test_source_and_manifest(self):
        source = (ROOT / "src/seed_rng_with_rtc.c").read_text(encoding="utf-8")
        self.assertIn("(seed >> 16) ^ (seed & 0xFFFF)", source)
        manifest = json.loads((ROOT / "manifests/seed-rng-with-rtc-reconstruction.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])


if __name__ == "__main__":
    unittest.main()

