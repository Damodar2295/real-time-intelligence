"""Read-only validation of the preserved V4 architecture review package."""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
manifest = json.loads((ROOT / 'architecture/review/v4-preservation.json').read_text())
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

for name, digest in manifest['v4_files'].items():
    path = ROOT / name
    check(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest,
          'V4 preservation mismatch: ' + name)

v4 = ROOT / 'architecture/gcp-gke-level-1/v4'
graph = json.loads((v4 / 'graph-v4.json').read_text())
tree = ET.parse(v4 / 'vantage-gcp-gke-technical-level-1-v4.drawio')
cells = list(tree.iter('mxCell'))
ids = {c.get('id'): c for c in cells}
check(len(ids) == len(cells), 'Duplicate draw.io IDs')
for edge in graph['edges']:
    cell = ids.get(edge['id'])
    check(cell is not None, 'Missing interface ' + edge['id'])
    if cell is not None:
        check(cell.get('source') == edge['a'] and cell.get('target') == edge['b'],
              'Endpoint mismatch ' + edge['id'])
for cell in cells:
    if cell.get('edge') == '1':
        check(cell.get('source') in ids and cell.get('target') in ids, 'Dangling connector')
for node_id in manifest['major_component_ids']:
    check(node_id in ids and ids[node_id].get('vertex') == '1', 'Missing editable shape ' + node_id)
ET.parse(v4 / 'vantage-gcp-gke-technical-level-1-v4.svg')
check(any('data:image/' in c.get('style', '') for c in cells), 'Missing embedded icons')
readme = (ROOT / 'README.md').read_text()
check(re.findall(r'^## (\d+)\.', readme, re.M) == [str(i) for i in range(1,23)], 'README section order')
check('## 2. Final Level 1 Architecture' in readme and
      '![Final VANTAGE' in readme.split('## 3.')[0], 'Missing early original diagram')
check('SafeChain is the mandatory' in readme, 'Missing mandatory SafeChain statement')
check('Redis Streams is the authoritative' in readme, 'Missing Redis requirement')
for identifier in manifest['major_component_ids'] + manifest['interface_ids']:
    check('`' + identifier + '`' in readme, 'Missing documented ID ' + identifier)
check(len(list(ROOT.rglob('README.md'))) == 1, 'Competing README files')
check(len(list(ROOT.rglob('*.drawio'))) == 1, 'Competing architecture diagrams')
for path in ROOT.rglob('*'):
    if '.git' in path.parts or not path.is_file():
        continue
    check(path.suffix.lower() not in ('.jpeg', '.jpg', '.pyc') and 'manager-review' not in path.parts,
          'Excluded asset: ' + str(path))
    if path.suffix == '.md':
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if not link.startswith(('https://', 'http://', '#')):
                check((path.parent / link.split('#')[0]).exists(), 'Broken link: ' + link)
report = {'package_checks': 'FAIL' if errors else 'PASS', 'errors': errors,
          'v4_preserved_files': len(manifest['v4_files']),
          'major_components': len(manifest['major_component_ids']),
          'interfaces': len(graph['edges']), 'xml_and_svg': 'PARSED',
          'architectural_alignment': 'BLOCKED — AR-01 Redis representation; AR-02 mandatory SafeChain representation',
          'native_drawio_import': 'NOT TESTED',
          'runtime_tests': 'NOT AVAILABLE — architecture tooling only'}
print(json.dumps(report, indent=2))
raise SystemExit(1 if errors else 0)
