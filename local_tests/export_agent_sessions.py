"""Export real visible Codex messages for this coursework's Custom source."""

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(os.environ.get(
    'CODEX_HOME', Path.home() / '.codex')) / 'sessions'
DESTINATION = ROOT / '.agent-sessions/source/codex-visible'
LEGACY_SESSION_IDS = {'01a1b01b-3cf1-7e50-b715-142a0570d8e0'}
EXPECTED_REPO = 'https://github.com/Orion333333/aim-2627-cpp-cw-20906982'
MAX_BYTES = 50 * 1024 * 1024
CONTEXT_PREFIXES = (
    '# AGENTS.md instructions',
    '<environment_context>',
    '<external_codex_apps_open_page>',
    '<external_codex_apps_selected_page_part_',
)
HOOK_MARKER = '# coursework-visible-export-v1'
HOOK_TEXT = '''
# coursework-visible-export-v1
import subprocess
import sys
from pathlib import Path

root = subprocess.check_output(
    ['git', 'rev-parse', '--show-toplevel'], text=True).strip()
exporter = Path(root) / 'local_tests/export_agent_sessions.py'
sys.exit(subprocess.call([sys.executable, '-B', str(exporter)]))
'''


def belongs_here(metadata):
    if not isinstance(metadata, dict):
        return False
    if metadata.get('id') in LEGACY_SESSION_IDS:
        return True
    cwd = metadata.get('cwd')
    return (isinstance(cwd, str) and Path(cwd).is_absolute()
            and Path(cwd).resolve() == ROOT.resolve())


def check_repository():
    origin = subprocess.check_output(
        ['git', '-C', str(ROOT), 'remote', 'get-url', 'origin'],
        text=True).strip().rstrip('/')
    if origin.startswith('git@github.com:'):
        origin = origin.replace('git@github.com:', 'https://github.com/', 1)
    if origin.removesuffix('.git').casefold() != EXPECTED_REPO.casefold():
        raise RuntimeError('The export script belongs to another repository')


def write_atomically(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, suffix='.tmp',
                                         delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def visible_messages(raw):
    records = []
    excluded = {}
    for number, line in enumerate(raw.splitlines(), 1):
        try:
            record = json.loads(line)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(record, dict):
            continue
        payload = record.get('payload', {})
        if not isinstance(payload, dict):
            continue
        role = payload.get('role')
        channel = payload.get('channel')
        phase = payload.get('phase')
        allowed = (
            record.get('type') == 'response_item'
            and payload.get('type') == 'message'
            and role in ('user', 'assistant')
            and channel in (None, 'final', 'commentary')
            and phase not in ('analysis', 'reasoning', 'summary')
        )
        if not allowed:
            key = role or payload.get('type') or record.get('type', 'unknown')
            if not isinstance(key, str):
                key = 'unknown'
            excluded[key] = excluded.get(key, 0) + 1
            continue
        content = []
        for item in payload.get('content') or []:
            if not isinstance(item, dict):
                continue
            if item.get('type') not in ('input_text', 'output_text', 'text'):
                continue
            text = item.get('text')
            if not isinstance(text, str):
                continue
            if role == 'user' and text.lstrip().startswith(CONTEXT_PREFIXES):
                continue
            content.append({'type': item.get('type'), 'text': text})
        if content:
            records.append({
                'timestamp': record.get('timestamp'),
                'source_line': number,
                'role': role,
                'channel': channel,
                'content': content,
            })
    return records, excluded


def export_sessions():
    check_repository()
    DESTINATION.mkdir(parents=True, exist_ok=True)
    inventory = []
    for path in sorted(SOURCE.glob('*/*/*/rollout-*.jsonl')):
        if path.is_symlink() or not path.is_file():
            continue
        with path.open('rb') as stream:
            header = stream.readline(65537)
        try:
            first = json.loads(header)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(first, dict):
            continue
        metadata = first.get('payload', {})
        if first.get('type') != 'session_meta' or not belongs_here(metadata):
            continue
        if path.stat().st_size > MAX_BYTES:
            raise RuntimeError(f'Selected session exceeds 50 MiB: {path.name}')
        with path.open('rb') as stream:
            raw = stream.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise RuntimeError(
                f'Selected session grew beyond 50 MiB: {path.name}')
        messages, excluded = visible_messages(raw)
        if not messages:
            continue
        relative = path.relative_to(SOURCE).with_suffix('.visible.jsonl')
        destination = DESTINATION / relative
        destination.resolve().relative_to(DESTINATION.resolve())
        export_header = {
            'cwd': str(ROOT.resolve()),
            'source_agent': 'codex',
            'session_id': metadata.get('id'),
            'original_session_cwd': metadata.get('cwd'),
            'original_session_path': str(path),
            'export_policy': 'visible user/assistant text only, version 1',
            'association': 'this coursework chat or exact repository cwd',
        }
        data = '\n'.join(json.dumps(record, ensure_ascii=False)
                         for record in [export_header, *messages]) + '\n'
        write_atomically(destination, data.encode('utf-8'))
        inventory.append({
            'source': str(path),
            'source_sha256': hashlib.sha256(raw).hexdigest(),
            'export': relative.as_posix(),
            'export_sha256': hashlib.sha256(data.encode('utf-8')).hexdigest(),
            'visible_messages': len(messages),
            'excluded_records': excluded,
        })
    if not inventory:
        raise RuntimeError('No verified coursework session found')
    manifest = {
        'cwd': str(ROOT.resolve()),
        'coverage': 'text projection; original rollouts remain unchanged',
        'excluded': ['system/developer context', 'reasoning', 'tools',
                     'workspace-only context', 'non-text attachments'],
        'sources': inventory,
    }
    manifest_data = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
    write_atomically(DESTINATION / 'manifest.json',
                     manifest_data.encode('utf-8'))
    total = sum(item['visible_messages'] for item in inventory)
    print(f'Exported {total} visible messages from '
          f'{len(inventory)} verified rollout files')


def install_hook():
    hook_path = subprocess.check_output(
        ['git', '-C', str(ROOT), 'rev-parse', '--git-path',
         'hooks/pre-commit'], text=True).strip()
    active = Path(hook_path)
    if not active.is_absolute():
        active = ROOT / active
    if (not active.exists()
            or '# File generated by pre-commit' not in
            active.read_text(encoding='utf-8')):
        raise RuntimeError('Install the pre-commit framework hook first')
    legacy = active.with_name('pre-commit.legacy')
    if (legacy.exists()
            and HOOK_MARKER not in legacy.read_text(encoding='utf-8')):
        raise RuntimeError(
            'An existing legacy hook must be preserved manually')
    interpreter = Path(sys.executable).as_posix()
    hook_text = f'#! "{interpreter}"\n' + HOOK_TEXT.lstrip('\n')
    legacy.write_bytes(hook_text.encode('utf-8'))
    legacy.chmod(0o755)
    print('Installed repository-local export hook before framework checks')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--install-hook', action='store_true')
    arguments = parser.parse_args()
    export_sessions()
    if arguments.install_hook:
        install_hook()


if __name__ == '__main__':
    main()
