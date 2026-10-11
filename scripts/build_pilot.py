#!/usr/bin/env python3
"""Build and verify a deterministic pilot archive; never installs or publishes it."""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = ('SKILL.md', 'README.md', 'INSTALL_CHATGPT.md', 'LICENSE', 'VERSION', 'metadata.json')
DIRECTORIES = ('references', 'playbooks', 'examples', 'sources', 'docs', 'scripts', 'tests/evaluations')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def payload(root):
    paths = [root / name for name in ROOT_FILES]
    paths += [root / 'tests/README.md', root / 'tests/scenarios.json']
    for directory in DIRECTORIES:
        paths.extend(p for p in (root / directory).rglob('*') if p.is_file()
                     and '__pycache__' not in p.parts and p.suffix != '.pyc'
                     and 'superpowers' not in p.relative_to(root).parts)
    return {str(p.relative_to(root)).replace('\\', '/'): p.read_bytes() for p in sorted(set(paths))}


def build(root, output, source_revision):
    version = (root / 'VERSION').read_text(encoding='utf-8').strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('Invalid release version')
    content = payload(root)
    manifest = {
        'version': version, 'baseline_revision': source_revision,
        'status': 'validation incomplète', 'native_installation': 'not_confirmed',
        'native_replays': 'not_run',
        'files': {name: {'sha256': digest(data), 'bytes': len(data)} for name, data in sorted(content.items())},
    }
    content['PACKAGE-MANIFEST.json'] = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f'copilot-m365-ops-{version}.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(content.items()):
            info = zipfile.ZipInfo('copilot-m365-ops/' + name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    with tempfile.TemporaryDirectory(prefix='verify-pilot-') as temp:
        with zipfile.ZipFile(archive) as z:
            expected_names = {'copilot-m365-ops/' + name for name in content}
            if set(z.namelist()) != expected_names or len(z.namelist()) != len(expected_names):
                raise ValueError('Unexpected or duplicate archive entries')
            z.extractall(temp)
        installed = Path(temp) / 'copilot-m365-ops'
        for name, data in content.items():
            if (installed / name).read_bytes() != data:
                raise ValueError(f'Extracted payload mismatch: {name}')
        skill = (installed / 'SKILL.md').read_text(encoding='utf-8')
        for companion in re.findall(r'`((?:references|playbooks|sources)/[^`]+)`', skill):
            if not (installed / companion).is_file():
                raise ValueError(f'Missing companion: {companion}')
    (output / 'manifest.json').write_bytes(content['PACKAGE-MANIFEST.json'])
    sha = digest(archive.read_bytes())
    (output / 'SHA256SUMS').write_text(f'{sha}  {archive.name}\n', encoding='utf-8')
    return {'archive': str(archive), 'sha256': sha, 'payload_files': len(manifest['files']), 'extraction_verified': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'dist')
    parser.add_argument('--source-revision', help='Baseline commit; payload hashes identify uncommitted preparation edits')
    args = parser.parse_args()
    revision = args.source_revision or subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
    print(json.dumps(build(ROOT, args.output_dir, revision), ensure_ascii=False))


if __name__ == '__main__':
    main()
