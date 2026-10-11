#!/usr/bin/env python3
import argparse
import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def classification(status):
    if status == 403:
        return 'access_denied'
    if status == 404:
        return 'not_found'
    if status == 429:
        return 'rate_limited'
    return 'ok' if status < 400 else 'http_error'


def check_source(source, opener=urllib.request.urlopen):
    result = {'id': source['id'], 'url': source['url']}
    req = urllib.request.Request(source['url'], headers={
        'User-Agent': 'Copilot-M365-Ops-Skill-source-check/0.1'})
    try:
        with opener(req, timeout=20) as response:
            status = getattr(response, "status", 200)
            result.update(status=status, final_url=response.geturl(),
                          classification=classification(status))
    except urllib.error.HTTPError as exc:
        result.update(status=exc.code, classification=classification(exc.code), detail=str(exc))
    except (urllib.error.URLError, TimeoutError) as exc:
        result.update(status=None, classification='network_error', detail=str(exc))
    return result


def main():
    parser = argparse.ArgumentParser(description='HTTP access only; not content verification or freshness')
    parser.add_argument('--report', type=Path, help='Optional JSON reachability report')
    args = parser.parse_args()
    data = json.loads((ROOT / 'sources/sources.json').read_text(encoding='utf-8'))
    results = [check_source(source) for source in data['sources']]
    for result in results:
        ok = result['classification'] == 'ok'
        status = f"HTTP {result['status']}" if result['status'] else result.get('detail', '')
        print(f"{'OK' if ok else 'FAIL'} {result['id']}: {status} ({result['classification']})")
    if args.report:
        args.report.write_text(json.dumps({
            'checked_at': datetime.now(timezone.utc).isoformat(),
            'meaning': 'HTTP access only; not content verification or freshness',
            'results': results,
        }, indent=2) + '\n', encoding='utf-8')
    return 1 if any(r['classification'] != 'ok' for r in results) else 0


if __name__ == '__main__':
    raise SystemExit(main())
