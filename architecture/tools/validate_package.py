"""Read-only structural, provenance and documentation checks for the V1 package."""
from pathlib import Path
import ast
import json
import re
import struct
import subprocess
import xml.etree.ElementTree as ET
from render_architecture import View

ROOT=Path(__file__).resolve().parents[2]
V1=ROOT/'architecture/v1'
errors=[]
def check(ok,message):
    if not ok:errors.append(message)
manifest=json.loads((ROOT/'architecture/review/baseline-provenance.json').read_text())
level1=json.loads((V1/'graph-level-1.json').read_text())
graphs={'level-1-architecture':level1}
graphs.update(json.loads((V1/'component-graphs.json').read_text()))
expected=['level-1-architecture','component-views/01-real-time-ingestion','component-views/02-intelligence-processing','component-views/03-intelligence-delivery','integration-views/04-component-interactions','integration-views/05-high-level-flows']
check(list(graphs)==expected,'Wrong diagram inventory')
check(set(level1['nodes'])==set(manifest['source_nodes']),'Level 1 component set changed')
for key,n in level1['nodes'].items():
    check(n['parent']==manifest['source_nodes'][key]['parent'],'Level 1 ownership changed: '+key)
    check(n['title']==manifest['source_nodes'][key]['title'],'Level 1 title changed: '+key)
check([{k:e[k] for k in ['id','a','b']} for e in level1['edges']]==manifest['source_interfaces'],'Level 1 topology changed')
# Check entire baseline graph, allowing only two presentation metadata updates.
source=json.loads(subprocess.check_output(['git','show',manifest['source_commit']+':architecture/gcp-gke-level-1/v4/graph-v4.json'],cwd=ROOT))
for key,n in source['nodes'].items():
    if key not in ['page-subtitle','legend']:check(n==level1['nodes'][key],'Unrelated Level 1 change: '+key)
check(source['edges']==level1['edges'],'Level 1 interface properties changed')
check(level1['nodes']['page-title']['title']=='Vantage Real Time Intelligence','Incorrect heading')
check(level1['nodes']['queue']['title']=='Redis Streams','Incorrect ingress')
check(level1['nodes']['model']['title']=='SafeChain Integration','Incorrect LLM integration')
reports=[]
for slug,g in graphs.items():
    size=g.get('size',[3760,2115]);v=View(g.get('name','Level 1'),*size);v.nodes=g['nodes'];v.edges=g['edges']
    try:v.validate()
    except AssertionError as exc:errors.append('Geometry/text fit: '+slug+' '+str(exc))
    check(size[0]/size[1]==16/9,'Not 16:9: '+slug)
    path=V1/(slug+'.drawio');tree=ET.parse(path);cells=list(tree.iter('mxCell'));ids={c.get('id'):c for c in cells}
    check(len(ids)==len(cells),'Duplicate IDs: '+slug)
    for key,n in g['nodes'].items():
        check(key in ids and ids[key].get('vertex')=='1','Missing editable component '+slug+'/'+key)
    for e in g['edges']:
        c=ids.get(e['id']);check(c is not None,'Missing connector '+slug+'/'+e['id'])
        if c is not None:check(c.get('source')==e['a'] and c.get('target')==e['b'],'Endpoint mismatch '+slug+'/'+e['id'])
    for c in cells:
        if c.get('edge')=='1':check(c.get('source') in ids and c.get('target') in ids,'Dangling edge '+slug)
        check(not any(t in c.get('value','') for t in ['V4','Pub/Sub','Vertex AI','StreamingPull','gateway alternative']),'Outdated diagram text '+slug)
    svg=ET.parse(V1/(slug+'.svg')).getroot();check(float(svg.get('width'))==size[0] and float(svg.get('height'))==size[1],'SVG size mismatch')
    png=(V1/(slug+'.png')).read_bytes();check(png[:8]==b'\x89PNG\r\n\x1a\n','Not PNG')
    check(struct.unpack('>II',png[16:24])==tuple(size),'PNG size mismatch '+slug)
    for n in g['nodes'].values():
        if n.get('icon'):check((V1/'icons'/n['icon']).is_file(),'Missing icon '+n['icon'])
    reports.append({'view':slug,'editable_vertices':len(g['nodes']),'interfaces':len(g['edges']),'size':size})
readme=(ROOT/'README.md').read_text()
check(re.findall(r'^## (\d+)\.',readme,re.M)==[str(i) for i in range(1,21)],'README section order')
check('![Vantage Real Time Intelligence' in readme.split('## 3.')[0],'Level 1 not immediately after overview')
check(len(re.findall(r'!\[.*?\]\(architecture/v1/.*?\.png\)',readme))==6,'README must embed six views')
check('SafeChain Integration provides the enterprise-secured interface for LLM invocation within Vantage Real Time Intelligence.' in readme,'Required SafeChain statement missing')
for e in level1['edges']:check('`'+e['id']+'`' in readme,'Missing interface documentation '+e['id'])
check(not (ROOT/'architecture/gcp-gke-level-1/v4').exists(),'Competing active V4 directory')
check(len(list(ROOT.rglob('*.drawio')))==6,'Unexpected diagram count')
check(len(list(ROOT.rglob('README.md')))==1,'Competing README')
for p in ROOT.rglob('*'):
    if '.git' in p.parts or not p.is_file():continue
    check(p.suffix.lower() not in ['.jpg','.jpeg','.pyc'],'Excluded artifact '+str(p))
    if p.suffix=='.md':
        for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if not link.startswith(('http://','https://','#')):check((p.parent/link.split('#')[0]).exists(),'Broken link '+link)
    if p.suffix=='.py':ast.parse(p.read_text())
result={'package_checks':'FAIL' if errors else 'PASS','errors':errors,'baseline_component_count':len(level1['nodes']),'baseline_interfaces':len(level1['edges']),'views':reports,'runtime_tests':'NOT AVAILABLE — architecture-only repository','native_editor_open':'See recorded validation.json for browser import result','production_approval':'NOT ESTABLISHED; open contracts retained'}
print(json.dumps(result,indent=2))
raise SystemExit(1 if errors else 0)
