import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('pilot_package', ROOT / 'scripts/build_pilot.py')
PACKAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGE)


class PilotPackageTests(unittest.TestCase):
    def test_reproducible_archive_and_extracted_companions(self):
        with tempfile.TemporaryDirectory() as temp:
            one = PACKAGE.build(ROOT, Path(temp) / 'one', 'baseline')
            two = PACKAGE.build(ROOT, Path(temp) / 'two', 'baseline')
            self.assertEqual(one['sha256'], two['sha256'])
            self.assertTrue(one['extraction_verified'])
            with zipfile.ZipFile(one['archive']) as z:
                names = z.namelist()
                self.assertIn('copilot-m365-ops/LICENSE', names)
                self.assertIn('copilot-m365-ops/references/billing.md', names)
                self.assertFalse(any('/.git/' in n or '/__pycache__/' in n or '/.env' in n for n in names))
                manifest = json.loads(z.read('copilot-m365-ops/PACKAGE-MANIFEST.json'))
                self.assertEqual(manifest['status'], 'validation incomplète')
                self.assertEqual(manifest['native_replays'], 'not_run')
