"""Render the evidence-backed v1.1 logical view as native draw.io cells and SVG.
Does not generate or modify the architecture model or records.
"""
from pathlib import Path
import xml.etree.ElementTree as E
import json,textwrap
P=Path(__file__).resolve().parents[1]; W,H=2780,1980
model=json.loads((P/'architecture-model.json').read_text()); refs={r['id']:r for r in model['relationships']}
mx=E.Element('mxfile',host='app.diagrams.net',type='device',version='24.7.17')
d=E.SubElement(mx,'diagram',id='vantage-logical-v01',name='Consolidated layered architecture')
gm=E.SubElement(d,'mxGraphModel',grid='1',gridSize='10',page='1',pageScale='1',pageWidth=str(W),pageHeight=str(H),math='0',shadow='0')
root=E.SubElement(gm,'root');E.SubElement(root,'mxCell',id='0');E.SubElement(root,'mxCell',id='1',parent='0')
N={}; edges=[]
styles={'box':('#ffffff','#7188a2'),'band':('#edf3fa','#bacbdd'),'support':('#f5f7fa','#b7c4d2'),'future':('#fff8e8','#b79345'),'conflict':('#fff0ea','#bc7b67'),'title':('#ffffff','#ffffff')}
def box(i,label,x,y,w,h,kind='box',fs=17,bold=False,parent='1',heading=False):
 fill,stroke=styles[kind]; style=f'rounded=0;whiteSpace=wrap;html=0;fillColor={fill};strokeColor={stroke};fontColor=#17324f;fontSize={fs};spacing=12;align=left;verticalAlign={"top" if heading else "middle"};'
 if bold:style+='fontStyle=1;'
 if kind in ['future','conflict']:style+='dashed=1;'
 if heading:style+='container=1;collapsible=0;recursiveResize=0;'
 ce=E.SubElement(root,'mxCell',id=i,value=label,style=style,vertex='1',parent=parent)
 xx=x-N[parent]['x'] if parent in N else x; yy=y-N[parent]['y'] if parent in N else y
 E.SubElement(ce,'mxGeometry',x=str(xx),y=str(yy),width=str(w),height=str(h),attrib={'as':'geometry'})
 N[i]=dict(id=i,label=label,x=x,y=y,w=w,h=h,kind=kind,fs=fs,bold=bold,parent=parent,heading=heading)
def band(i,label,x,y,w,h):box(i,label,x,y,w,h,'band',22,True,heading=True)
def edge(i,a,b,label='',points=None,kind='data',sa='right',ta='left',evidence=None):
 xy={'right':(1,.5),'left':(0,.5),'top':(.5,0),'topright':(.8,0),'bottom':(.5,1)};ax,ay=xy[sa];bx,by=xy[ta]
 col='#af8a42' if kind=='future' else '#5e7692'
 st=f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=block;endFill=1;strokeColor={col};fontColor=#45617d;fontSize=13;labelBackgroundColor=#ffffff;exitX={ax};exitY={ay};entryX={bx};entryY={by};'
 if kind!='data':st+='dashed=1;dashPattern='+('2 4;' if kind=='config' else '7 4;')
 ce=E.SubElement(root,'mxCell',id=i,value=label,style=st,edge='1',parent='1',source=a,target=b)
 ge=E.SubElement(ce,'mxGeometry',relative='1',attrib={'as':'geometry'})
 if points:
  ar=E.SubElement(ge,'Array',attrib={'as':'points'})
  for x,y in points:E.SubElement(ar,'mxPoint',x=str(x),y=str(y))
 edges.append(dict(id=i,a=a,b=b,label=label,points=points or [],kind=kind,sa=sa,ta=ta,evidence=evidence or i))
box('title','VANTAGE Intelligence | Consolidated layered architecture',40,20,2700,55,'title',34,True)
box('subtitle','v1.1 • 08 Oct 2026 • Logical design review baseline • Source-supported does not mean deployed or production-approved',40,80,2700,35,'title',18)
# Explicit companion capability; not a newly invented primary layer.
band('G01','Signal Management  [M05 / P05]',40,150,520,1110)
box('C53','Signal Management UI\nManage catalog; view signals [M05.5]',70,220,460,95,parent='G01')
box('C13','Signal Catalog\nApplicable signal definitions [M04 / M05]',70,355,460,85,parent='G01')
for i,txt,y in [('C67','Signal Taxonomy\nDomain → Group → Signal [P01 / P05]',480),('C64','Entity Dictionary\nProducts, fees, benefits, credit concepts [P05]',570),('C65','Curated Examples\nPositive / Negative [P02 / P05]',660),('C66','Regulatory / Policy Mappings\nReference metadata; not a policy service [P05]',750)]:box(i,txt,70,y,450,65,fs=15,parent='G01')
box('C52','Signal Definitions / schema\nDetection method • criteria • thresholds\nUnified deterministic / semantic / LLM definition\nExact schema still under agreement [M05 / P01–P02]',70,875,460,125,fs=16,parent='G01')
box('schema-note','Planning fields [P01–P02]\nsignal_id / name / description / domain / group\ndetection_method / detection_config\napplicable_products / applicable_speakers\nentity_refs / example_refs / requirement_refs\nregulatory_refs / severity / version / status\nTypes, requiredness and lifecycle rules: OPEN',70,1030,460,200,'support',15,parent='G01')
edge('R83','C53','C13','manage',sa='bottom',ta='top',kind='config')
for rid,i in [('R77','C67'),('R75','C64'),('R74','C65'),('R76','C66')]:
 y=N[i]['y']+N[i]['h']/2;edge(rid,i,'C52',points=[(545,y),(545,850),(300,850)],sa='right',ta='top',kind='config')
edge('R88','C52','C13',points=[(55,937),(55,397)],sa='left',ta='left',kind='config')
# Sources and future adapter role.
band('sources','Conversation sources / adapters',620,150,1600,170)
box('C02','Transcript Emulator\nSeparate module/service [U06]\nConcurrent streams requested [M05]',650,215,440,80,fs=17,parent='sources')
box('C01','Genesys Cloud\nFuture live source [A02 / M05]\nOAuth in reference; live setup TBD',1140,215,410,80,'future',16,parent='sources')
box('C58','Future Genesys / outreach adapters\nProvider contracts not established [M05.4]',1610,215,570,80,'future',16,parent='sources')
edge('R90','C01','C58',kind='future')
# Streaming concern and native service container, with editable responsibility children.
band('L01','Interaction Streaming  [A01 / M05]',620,355,1600,285)
box('C57','Default WebSocket adapter\nInitial adapter construct\nPackaging within Ingestor: OPEN',650,435,295,120,fs=17,parent='L01')
box('C56','Ingestor service / Call Ingestor  [M05.2–4 / P05]',995,425,1180,175,'box',20,True,parent='L01',heading=True)
box('C68','Session management\ncall_id = session / correlation ID\nIndependent calls [M05.4]',1020,490,345,85,fs=15,parent='C56')
box('C05','Normalize Transcript Event\nSpeaker / timestamp [P05]\nCleanup rules remain open',1410,490,345,85,fs=15,parent='C56')
box('C69','Segmentation / buffering\nWindowing → mini-batches\nSize / ordering rules: OPEN',1800,490,345,85,fs=15,parent='C56')
edge('R65','C02','C57','',points=[(870,340),(797,340)],sa='bottom',ta='top')
edge('R66','C57','C56')
# Support context adjacent to ingress; physical topology deliberately not assigned.
box('C47','Context Cache  [M04 / P05]\nIn-memory, same conversation only\nRecent utterance window + identified signals\nBounded hot-path context; TTL / owner OPEN',2290,425,450,140,'support',16)
edge('R68','C56','C47','maintain context')
box('context-note','Storage distinction\nKeep recent detection context separate from the larger conversation log.\nNo unlimited-history dependency or mandatory entity enrichment inferred.',2290,605,450,135,'support',16)
# Detection area: configured routing, not implied invocation of every strategy.
band('L02','Real-time Signal Detection  [A01 / M02 / M05]',620,700,1600,525)
box('C54','Call-metadata applicability\nSelect catalog signals for this call\nBefore detection [M04]',650,770,320,95,fs=17,parent='L02')
box('C59','Detector service / Signal Detector\nConfigured method; not automatic all-path execution\nScheduling and fallback policy: OPEN [M05 / P05]',1040,770,700,95,fs=17,parent='L02')
edge('R92','C56','C54','utterance / metadata',points=[(1585,675),(810,675)],sa='bottom',ta='top')
edge('R62','C13','C54','catalog eligibility',points=[(595,397),(595,817)],kind='config')
edge('R91','C54','C59')
edge('R70','C52','C59','signal configuration',points=[(580,937),(580,665),(1390,665)],sa='right',ta='top',kind='config')
edge('R69','C47','C59','conversation context',points=[(2275,495),(2275,760),(1800,760),(1800,817)],sa='left',ta='right')
box('C39','Deterministic Detector [A05]',650,1000,330,160,fs=16,bold=True,parent='L02',heading=True)
for ci,ct,cx,cy in [('C14','Rules',670,1060),('C15','Regex',825,1060),('C16','Fuzzy',670,1110),('C17','Entity rules',825,1110)]:box(ci,ct,cx,cy,135,35,fs=14,parent='C39')
box('semantic','Semantic strategy [M02 / M05]\nTop-K + reranker retained; thresholds unspecified',1020,940,640,265,'support',16,True,parent='L02',heading=True)
box('C18','Embedding\nUtterance vector',1040,1010,170,65,fs=15,parent='semantic')
box('C19','Vector Search\nSimilarity retrieval',1240,1010,180,65,fs=14,parent='semantic')
box('C35','Top-K candidates\nK not selected',1450,1010,185,65,fs=15,parent='semantic')
box('C36','Reranker\nBGE label in S02\nExact model OPEN',1240,1110,180,75,fs=15,parent='semantic')
box('C60','LLM-based detection\nCandidate + requirement + context\nModel / endpoint / invocation policy OPEN\nDistinct from later generation\n[M05.3 / P04 / P05]',1730,1000,450,160,fs=16,parent='L02')
edge('R71','C59','C39',points=[(1390,895),(815,895)],sa='bottom',ta='top')
edge('R72','C59','C18',points=[(1390,910),(1125,910)],sa='bottom',ta='top')
edge('R73','C59','C60',points=[(1390,925),(1955,925)],sa='bottom',ta='top')
edge('R26','C18','C19');edge('R45','C19','C35')
edge('R46','C35','C36',points=[(1542,1147)],sa='bottom',ta='right')
# Output and shared resolution reference.
band('output','Signal evidence, resolution and output  [A05 / A09 / P05]',620,1265,1600,320)
box('C21','Signal Evidence\n[A05 / A06]',1040,1340,285,75,fs=17,parent='output')
box('C22','Signal Resolution\nThreshold-based acceptance [U07]',1400,1330,285,95,fs=16,parent='output')
box('C23','Detected Signal\nSignal ID • domain/group • evidence\nConfidence • entities • regulatory mapping\nReference result fields [P05]',1760,1320,420,110,fs=16,parent='output')
edge('R21-R24','C39','C21','evidence',points=[(815,1377)],sa='bottom',ta='left',evidence='R21,R22,R23,R24')
edge('R30','C21','C22');edge('R31','C22','C23')
edge('R47','C36','C22','semantic result',points=[(1330,1240),(1542,1240)],sa='bottom',ta='top')
edge('R93','C60','C22','LLM result',points=[(1955,1295),(1628,1295)],sa='bottom',ta='topright')
box('C24','Signal Events\nPOC output [A09]',650,1485,310,70,fs=17,parent='output')
box('C25','Real-Time Signal Workbench\nEvidence + latency display [A10]',1040,1485,490,70,fs=17,parent='output')
edge('R32','C22','C24',points=[(1542,1460),(805,1460)],sa='bottom',ta='top');edge('R33','C24','C25')
box('transport-note','Delivery mechanism: SSE / WebSocket proposed in S03\nFinal event contract / publication transport remain OPEN',1610,1485,570,70,'support',15,parent='output')
# Supporting stores/platforms are not a deployment boundary.
box('C61','Vector DB  [M05.8 / P05]\nPostgreSQL / “p vector” as reported\nSignal examples + semantic representations\nExact instance / extension / readiness OPEN',2290,885,450,135,'support',16)
edge('R79','C19','C61','Top-K retrieval',points=[(1330,1090),(1685,1090),(1685,880),(2240,880),(2240,952)],sa='bottom',ta='left')
edge('R78','C65','C61','',points=[(610,692),(610,125),(2760,125),(2760,840),(2515,840)],sa='right',ta='top',kind='config')
box('C63','BigQuery — Utterance & Call Log\nREFERENCE OPTION ONLY [P05 / U06]\nPersist utterances and detected results\nNot selected prototype storage',2290,1265,450,135,'future',16)
edge('R80','C56','C63','utterances: reference option',points=[(2250,512),(2250,1245),(2515,1245)],sa='right',ta='top',kind='future')
edge('R81','C23','C63','results',kind='future')
box('C62','GKE — “sales profit” environment\nProvisioning reportedly started [M05.8]\nDeployment map / readiness unverified',2290,1450,450,100,'support',16)
box('C70','Common Git repository / monorepo\nModules + architecture together [M05.9]\nNo repo URL or module paths supplied',2290,1590,450,100,'support',16)
box('C44','End-to-end logging / tracing [M05 / A08]\nAll stages; event history and latency\nP50 / P95 / P99; backend unspecified\nDeterministic internal target ≤100–150 ms\nPOC target only; end-to-end SLA TBD',2290,1730,450,160,'support',16)
# Remaining concerns remain explicitly later; not conflated with detection LLM.
band('L03','Contextual Generation — later [A01]',620,1670,720,180)
box('C27','Selective deeper context / generation\nWhen detected signal warrants it\nImplementation not defined',660,1730,640,90,fs=17,parent='L03')
band('L04','Activation — later [A01 / A10]',1400,1670,820,180)
box('C28','Activation\nSignal / recommendation delivery',1440,1730,345,90,fs=16,parent='L04')
box('C29','Downstream Consumers\nBoundary / contract OPEN',1835,1730,345,90,fs=16,parent='L04')
edge('R35','C23','C27','selective',points=[(2205,1375),(2205,1635),(980,1635)],sa='right',ta='top')
edge('R36','C27','C28','eventual [A10]');edge('R37','C28','C29')
# Review notes retain excluded/deferred items rather than inserting speculative hot-path nodes.
box('C55','Composite Signals [M05.6]\nPrior signal + new signal → third signal\nRule / window / lifecycle definition still open',40,1300,520,110,'future',17)
box('scaling-note','Earlier scaling reference retained [A04]\nInternal Transcript Stream → partitions → workers\nConversation-keyed processing; counts illustrative\nNot a mandated broker in the current prototype',40,1450,520,130,'support',16)
box('legend','Solid: source-supported logical flow   ··· Dotted: configuration   – – Amber: future / proposed / reference\nBoxes are logical responsibilities unless explicitly named services; no GKE pod, trust boundary, or data-store hosting inferred.\nAll 70 inventory records have a disposition in diagram-coverage.md. Full source and relationship IDs remain in the records.',40,1900,2700,75,'title',15)
# Draw.io source.
E.indent(mx); out=P/'diagrams/VANTAGE_Intelligence_Layered_Architecture.drawio'; E.ElementTree(mx).write(out,encoding='utf-8',xml_declaration=True)
# Exact-geometry companion preview. Connectors first, then boxes. Band backgrounds behind both.
svg=E.Element('svg',xmlns='http://www.w3.org/2000/svg',width=str(W),height=str(H),viewBox=f'0 0 {W} {H}')
def se(tag,**kw):return E.SubElement(svg,tag,{k.replace('_','-'):str(v) for k,v in kw.items()})
se('rect',x=0,y=0,width=W,height=H,fill='white');defs=E.SubElement(svg,'defs')
for name,col in [('arrow','#5e7692'),('future-arrow','#af8a42')]:
 mark=E.SubElement(defs,'marker',id=name,markerWidth='8',markerHeight='8',refX='7',refY='4',orient='auto');E.SubElement(mark,'path',d='M0,0 L8,4 L0,8 Z',fill=col)
def rect(n):
 f,s=styles[n['kind']];a=dict(x=n['x'],y=n['y'],width=n['w'],height=n['h'],fill=f,stroke=s)
 if n['kind'] in ['future','conflict']:a['stroke_dasharray']='7 4'
 se('rect',**a)
for n in N.values():
 if n['heading']:rect(n)
def anchor(n,s):return {'left':(n['x'],n['y']+n['h']/2),'right':(n['x']+n['w'],n['y']+n['h']/2),'top':(n['x']+n['w']/2,n['y']),'topright':(n['x']+n['w']*.8,n['y']),'bottom':(n['x']+n['w']/2,n['y']+n['h'])}[s]
for e in edges:
 a=anchor(N[e['a']],e['sa']);b=anchor(N[e['b']],e['ta']);pts=[a]+e['points']+[b]
 if len(pts)==2 and a[0]!=b[0] and a[1]!=b[1]:pts=[a,((a[0]+b[0])/2,a[1]),((a[0]+b[0])/2,b[1]),b]
 kw=dict(points=' '.join(f'{x},{y}' for x,y in pts),fill='none',stroke='#af8a42' if e['kind']=='future' else '#5e7692',stroke_width=1.6,marker_end='url(#future-arrow)' if e['kind']=='future' else 'url(#arrow)')
 if e['kind']!='data':kw['stroke_dasharray']='2 4' if e['kind']=='config' else '7 4'
 se('polyline',**kw)
 if e['label']:
  a,b=max(zip(pts,pts[1:]),key=lambda z:abs(z[0][0]-z[1][0])+abs(z[0][1]-z[1][1]));t=se('text',x=(a[0]+b[0])/2,y=(a[1]+b[1])/2-7,font_family='Arial',font_size=13,fill='#45617d',text_anchor='middle');t.text=e['label']
fits=[]
for n in N.values():
 if not n['heading']:rect(n)
 lines=[];chars=max(12,int((n['w']-26)/(n['fs']*.52)))
 for par in n['label'].split('\n'):lines+=textwrap.wrap(par,width=chars,break_long_words=False) or ['']
 lh=n['fs']*1.25;y=n['y']+n['fs']+12 if n['heading'] else n['y']+(n['h']-len(lines)*lh)/2+n['fs']
 for line in lines:
  t=se('text',x=n['x']+13,y=round(y,1),fill='#17324f',font_family='Arial',font_size=n['fs'],font_weight='bold' if n['bold'] else 'normal');t.text=line;y+=lh
 if len(lines)*lh>n['h']-10:fits.append(n['id'])
assert not fits,('Text exceeds box',fits)
E.ElementTree(svg).write(P/'diagrams/VANTAGE_Intelligence_Layered_Architecture.preview.svg',encoding='utf-8',xml_declaration=True)
# Validate source references and geometry.
cells=list(root);ids={c.get('id') for c in cells};assert len(ids)==len(cells)
for e in edges:
 assert e['a'] in ids and e['b'] in ids
 for r in e['evidence'].split(','):assert r in refs,(e['id'],r)
assert len(E.parse(out).findall('.//diagram'))==1
for n in N.values():
 if n['parent'] in N:
  q=N[n['parent']];assert n['x']>=q['x'] and n['y']>=q['y'] and n['x']+n['w']<=q['x']+q['w'] and n['y']+n['h']<=q['y']+q['h'],n['id']
# Sibling boxes must not overlap; nesting is intentional.
collisions=[];ns=list(N.values())
for j,a in enumerate(ns):
 for b in ns[j+1:]:
  if a['parent']!=b['parent']:continue
  if min(a['x']+a['w'],b['x']+b['w'])>max(a['x'],b['x']) and min(a['y']+a['h'],b['y']+b['h'])>max(a['y'],b['y']):collisions.append((a['id'],b['id']))
assert not collisions,collisions
(P/'diagrams/layout-v1.1.json').write_text(json.dumps(dict(width=W,height=H,nodes=N,edges=edges),indent=2))
print(f'Generated native editable page: {len(N)} vertices / {len(edges)} connectors. XML, source refs, text fit, nesting and peer overlap checks passed.')
