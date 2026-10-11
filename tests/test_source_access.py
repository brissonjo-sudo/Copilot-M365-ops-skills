import importlib.util
import unittest
import urllib.error
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('source_access', Path(__file__).resolve().parents[1] / 'scripts/check_sources.py')
ACCESS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ACCESS)


class SourceAccessTests(unittest.TestCase):
    source = {'id': 'example', 'url': 'https://learn.microsoft.com/example'}

    def error(self, status):
        def opener(*args, **kwargs):
            raise urllib.error.HTTPError(self.source['url'], status, 'test', {}, None)
        return ACCESS.check_source(self.source, opener)

    def test_access_denial_is_not_staleness(self):
        result = self.error(403)
        self.assertEqual(result['classification'], 'access_denied')
        self.assertNotIn('last_verified', result)
        self.assertNotIn('stale', result)

    def test_not_found_rate_limit_and_server_error(self):
        for status, category in [(404, 'not_found'), (429, 'rate_limited'), (503, 'http_error')]:
            with self.subTest(status=status):
                self.assertEqual(self.error(status)['classification'], category)

    def test_timeout_is_network_error(self):
        def opener(*args, **kwargs):
            raise TimeoutError('test timeout')
        self.assertEqual(ACCESS.check_source(self.source, opener)['classification'], 'network_error')

    def test_success_preserves_final_url_without_refreshing_date(self):
        class Response:
            status = 200
            def geturl(self):
                return 'https://learn.microsoft.com/canonical'
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
        result = ACCESS.check_source(self.source, lambda *a, **k: Response())
        self.assertEqual(result['classification'], 'ok')
        self.assertEqual(result['final_url'], 'https://learn.microsoft.com/canonical')
        self.assertNotIn('last_verified', result)
