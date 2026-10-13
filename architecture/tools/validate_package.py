from pathlib import Path
import xml.etree.ElementTree as E
import json,re
root=Path(__file__).resolve().parents[2]
errors=[];reports=[]
for p in root.rglob('*.drawio'):
 tree=E.parse(p);pages=tree.findall('diagram')
 for page in pages:
  cells=list(page.iter('mxCell'));ids={c.get('id') for c in cells}
  assert len(ids)==len(cells),(p,'duplicate IDs')
  for c in cells:
   if c.get('edge')=='1':assert c.get('source') in ids and c.get('target') in ids,(p,c.get('id'))
 reports.append({'file':str(p.relative_to(root)),'pages':len(pages)})
for p in root.rglob('*.md'):
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not link.startswith(('https://','http://','#')) and not (p.parent/link.split('#')[0]).exists():errors.append(f'{p}: {link}')
for p in root.rglob('*'):
 if '.git' in p.parts:continue
 if p.is_file() and (p.suffix.lower() in ['.jpg','.jpeg','.pyc'] or 'manager-review' in p.parts):errors.append(str(p))
assert not errors,errors
print(json.dumps({'drawio':reports,'links':'PASS','excluded_assets':'PASS','native_editor_import':'NOT TESTED'},indent=2))
