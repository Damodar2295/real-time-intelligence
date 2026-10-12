from pathlib import Path
import json,hashlib,base64,xml.etree.ElementTree as E
P=Path(__file__).resolve().parent
old=E.parse(P.parent/'v3/vantage-gcp-gke-technical-level-1-v3.drawio');new=E.parse(P/'vantage-gcp-gke-technical-level-1-v4.drawio')
o={c.get('id'):c for c in old.iter('mxCell')};n={c.get('id'):c for c in new.iter('mxCell')}
assert len(new.findall('diagram'))==1
assert set(o)<=set(n)
assert len(n)==len(list(new.iter('mxCell')))
old_edges={k:(v.get('source'),v.get('target')) for k,v in o.items() if v.get('edge')=='1'}
new_edges={k:(v.get('source'),v.get('target')) for k,v in n.items() if v.get('edge')=='1'}
assert old_edges==new_edges
for k,(a,b) in new_edges.items():
 assert a in n and b in n
 assert n[k].get('interfaceId')==k and n[k].get('sourceRefs')
 assert n[k].get('decisionStatus') and n[k].get('protocolStatus')
images=[]
for k,c in n.items():
 style=c.get('style','')
 if 'shape=image;' in style:
  raw=base64.b64decode(style.split('image=data:image/svg+xml,')[1].split(';')[0]);E.fromstring(raw)
  assert style==o[k].get('style');images.append(k)
  assert c.get('parent') in n
for k in ['stt','queue','state','sql','model','telemetry','controls']:assert n[k].get('parent')=='gcp'
assert n['worker'].get('parent')=='ingestion-zone' and n['coord'].get('parent')=='detection-zone'
for f,h in json.loads((P/'v3-baseline-hashes.json').read_text()).items():assert hashlib.sha256((P.parent/f).read_bytes()).hexdigest()==h,f
G=json.loads((P/'graph-v4.json').read_text());nodes=G['nodes']
assert all(n[k].get('componentId')==k for k in nodes)
# Check orthogonal edge paths against unrelated card interiors.
def anchor(v,s):return {'left':(v['x'],v['y']+v['h']/2),'right':(v['x']+v['w'],v['y']+v['h']/2),'top':(v['x']+v['w']/2,v['y']),'bottom':(v['x']+v['w']/2,v['y']+v['h']),'topright':(v['x']+v['w']*.8,v['y'])}[s]
for e in G['edges']:
 a=anchor(nodes[e['a']],e['sa']);b=anchor(nodes[e['b']],e['ta']);pts=[a]+[tuple(t) for t in e['pts']]+[b]
 if len(pts)==2 and a[0]!=b[0] and a[1]!=b[1]:pts=[a,((a[0]+b[0])/2,a[1]),((a[0]+b[0])/2,b[1]),b]
 out=[pts[0]]
 for p in pts[1:]:
  q=out[-1]
  if q[0]!=p[0] and q[1]!=p[1]:out.append((p[0],q[1]))
  out.append(p)
 for a,b in zip(out,out[1:]):
  for k,v in nodes.items():
   if k in (e['a'],e['b']) or v['band'] or v['kind'] in ('title','zone','section'):continue
   x,y,w,h=v['x'],v['y'],v['w'],v['h']
   hit=(a[0]==b[0] and x<a[0]<x+w and max(min(a[1],b[1]),y)<min(max(a[1],b[1]),y+h)) or (a[1]==b[1] and y<a[1]<y+h and max(min(a[0],b[0]),x)<min(max(a[0],b[0]),x+w))
   assert not hit,(e['id'],k)
report={'single_page':True,'baseline_vertices_preserved':len(nodes),'interfaces_preserved':len(new_edges),'embedded_icons_preserved':len(images),'stable_ids':True,'interface_traceability':True,'managed_services_outside_gke':True,'v3_bytes_unchanged':True,'no_connectors_through_unrelated_cards':True,'native_editor_import':'NOT TESTED','production_controls':'NOT VERIFIED'}
(P/'validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
