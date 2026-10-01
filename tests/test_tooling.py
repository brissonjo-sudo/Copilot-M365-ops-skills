import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ToolingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=ROOT.parent, prefix='tooling-test-')
        assert Path(self.temp.name).resolve().parent == ROOT.parent.resolve()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        self.source_path = self.repo / 'sources/sources.json'
        self.data = json.loads(self.source_path.read_text(encoding='utf-8'))

    def run_script(self, name, *args):
        self.source_path.write_text(json.dumps(self.data), encoding='utf-8')
        return subprocess.run([sys.executable, str(self.repo / 'scripts' / name), *args], capture_output=True, text=True)

    def fresh_sources(self):
        for source in self.data['sources']:
            source['last_verified'] = date.today().isoformat()

    def test_future_verification_blocks(self):
        self.fresh_sources()
        self.data['sources'][0]['last_verified'] = (date.today() + timedelta(days=1)).isoformat()
        self.assertNotEqual(self.run_script('check_freshness.py').returncode, 0)

    def test_warning_triggers_weekly_review_only(self):
        self.fresh_sources()
        next(s for s in self.data['sources'] if s['category'] == 'roadmap')['last_verified'] = (date.today() - timedelta(days=8)).isoformat()
        self.assertEqual(self.run_script('check_freshness.py').returncode, 0)
        self.assertNotEqual(self.run_script('check_freshness.py', '--review').returncode, 0)

    def test_critical_expiry_blocks_at_boundary(self):
        self.fresh_sources()
        self.data['sources'][0]['last_verified'] = (date.today() - timedelta(days=7)).isoformat()
        self.assertNotEqual(self.run_script('check_freshness.py').returncode, 0)

    def test_fresh_registry_passes(self):
        self.fresh_sources()
        self.assertEqual(self.run_script('check_freshness.py', '--review').returncode, 0)

    def test_execution_platform_rejected(self):
        path = self.repo / 'metadata.json'
        metadata = json.loads(path.read_text(encoding='utf-8'))
        metadata['platforms'] = ['Cowork', 'Copilot Studio']
        path.write_text(json.dumps(metadata), encoding='utf-8')
        self.assertNotEqual(self.run_script('validate_repo.py').returncode, 0)

    def test_broken_skill_companion_rejected(self):
        (self.repo / 'references/decision-tree.md').unlink()
        self.assertNotEqual(self.run_script('validate_repo.py').returncode, 0)

    def test_invalid_source_date_rejected(self):
        self.data['sources'][0]['last_verified'] = 'not-a-date'
        self.assertNotEqual(self.run_script('validate_repo.py').returncode, 0)


if __name__ == '__main__':
    unittest.main()
