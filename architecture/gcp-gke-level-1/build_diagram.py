"""Editable GCP/GKE technical proposal mapped from VANTAGE v1.2."""
from pathlib import Path
import json, textwrap, html, re
import xml.etree.ElementTree as ET

OUT=Path(__file__).resolve().parent
NAVY='#173D56'; TEAL='#086F75'; INK='#18394E'; GRAY='#61798A'
COLORS={'normal':('#FFFFFF','#A5BAC8'),'support':('#F4F8FA','#B7C9D3'),'future':('#FFF9EC','#B29145'),'test':('#F1EBFA','#9879B9'),'decision':('#E3F4F0','#267F76'),'external':('#EEF3F8','#839CAE')}
class View:
 def __init__(self,name,w,h):self.name=name;self.w=w;self.h=h;self.nodes={};self.edges=[]
 def box(self,i,title,body,x,y,w,h,kind='normal',parent='1',refs='',fs=18):
  self.nodes[i]=dict(id=i,title=title,body=body,x=x,y=y,w=w,h=h,kind=kind,parent=parent,refs=refs,fs=fs,band=False)
 def band(self,i,title,x,y,w,h,parent='1',color=NAVY):
  self.nodes[i]=dict(id=i,title=title,body='',x=x,y=y,w=w,h=h,kind='support',parent=parent,refs='',fs=21,band=True,color=color)
 def link(self,a,b,label='',kind='data',sa='right',ta='left',pts=None,refs=''):
  self.edges.append(dict(id='edge-'+str(len(self.edges)+1),a=a,b=b,label=label,kind=kind,sa=sa,ta=ta,pts=pts or [],refs=refs))
 def header(self,subtitle):
  self.box('page-title','VANTAGE Intelligence | '+self.name,'',40,20,self.w-80,75,kind='title',fs=30)
  self.box('page-subtitle','',subtitle,40,98,self.w-80,35,kind='title',fs=17)
 def footer(self,y):
  self.box('legend','READING GUIDE','Solid arrow: logical data / event flow    ··· Dotted: configuration    – – Amber: proposed or later path    Purple: test source',40,y,self.w-80,65,kind='title',fs=16)
  self.box('scope','', 'Logical boundaries, not deployment or trust zones. Configured strategies are selective; timing and combination rules remain open.',40,y+65,self.w-80,30,kind='title',fs=16)
 def anchor(self,n,s):
  return {'left':(n['x'],n['y']+n['h']/2),'right':(n['x']+n['w'],n['y']+n['h']/2),'top':(n['x']+n['w']/2,n['y']),'bottom':(n['x']+n['w']/2,n['y']+n['h']),'topright':(n['x']+n['w']*.8,n['y'])}[s]
 def points(self,e):
  a=self.anchor(self.nodes[e['a']],e['sa']);b=self.anchor(self.nodes[e['b']],e['ta']);pts=[a]+e['pts']+[b]
  if len(pts)==2 and a[0]!=b[0] and a[1]!=b[1]:pts=[a,((a[0]+b[0])/2,a[1]),((a[0]+b[0])/2,b[1]),b]
  # Ensure orthogonal geometry even where endpoint positions differ from waypoints.
  out=[pts[0]]
  for p in pts[1:]:
   q=out[-1]
   if q[0]!=p[0] and q[1]!=p[1]:out.append((p[0],q[1]))
   out.append(p)
  return out
 def lines(self,n):
  width=max(10,int((n['w']-28)/(n['fs']*.55)))
  title=textwrap.wrap(n['title'],width=width,break_long_words=False)
  body=[l for p in n['body'].split('\n') for l in textwrap.wrap(p,width=width,break_long_words=False)] if n['body'] else []
  return title,body
 def validate(self):
  for n in self.nodes.values():
   assert n['x']>=0 and n['y']>=0 and n['x']+n['w']<=self.w and n['y']+n['h']<=self.h,n['id']
   t,b=self.lines(n);assert (len(t)+len(b))*n['fs']*1.22+(8 if t and b else 0)<=n['h']-(8 if n['kind']=='title' else 16),(self.name,n['id'],t,b)
   if n['parent']!='1':
    p=self.nodes[n['parent']];assert p['x']<=n['x'] and p['y']+42<=n['y'] and n['x']+n['w']<=p['x']+p['w'] and n['y']+n['h']<=p['y']+p['h'],n['id']
  ns=list(self.nodes.values())
  for k,a in enumerate(ns):
   for b in ns[k+1:]:
    if a['parent']==b['parent']:
     assert not(min(a['x']+a['w'],b['x']+b['w'])>max(a['x'],b['x']) and min(a['y']+a['h'],b['y']+b['h'])>max(a['y'],b['y'])),(a['id'],b['id'])
  for e in self.edges:assert e['a'] in self.nodes and e['b'] in self.nodes
 def export(self,mx,slug):
  self.validate()
  d=ET.SubElement(mx,'diagram',id=slug,name=self.name)
  gm=ET.SubElement(d,'mxGraphModel',grid='1',gridSize='10',page='1',pageScale='1',pageWidth=str(self.w),pageHeight=str(self.h),math='0',shadow='0')
  root=ET.SubElement(gm,'root');ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
  svg=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',width=str(self.w),height=str(self.h),viewBox=f'0 0 {self.w} {self.h}')
  def s(tag,**attrs):return ET.SubElement(svg,tag,{k.replace('_','-'):str(v) for k,v in attrs.items()})
  s('rect',x=0,y=0,width=self.w,height=self.h,fill='white')
  defs=ET.SubElement(svg,'defs')
  for name,col in [('arrow',GRAY),('future','#AA8539')]:
   m=ET.SubElement(defs,'marker',id=name,markerWidth='8',markerHeight='8',refX='7',refY='4',orient='auto');ET.SubElement(m,'path',d='M0,0 L8,4 L0,8 Z',fill=col)
  def rect(n):
   if n['kind']=='title':return
   fill,stroke=COLORS[n['kind']]
   attrs=dict(x=n['x'],y=n['y'],width=n['w'],height=n['h'],fill=fill,stroke=stroke,stroke_width=2 if n['kind']=='decision' else 1)
   if n['kind']=='future':attrs['stroke_dasharray']='7 4'
   s('rect',**attrs)
   if n['band']:s('rect',x=n['x'],y=n['y'],width=n['w'],height=44,fill=n['color'])
  for n in self.nodes.values():
   fill,stroke=COLORS.get(n['kind'],('#FFFFFF','#FFFFFF'))
   style=f'rounded=0;whiteSpace=wrap;html=1;fontFamily=Arial;fontSize={n["fs"]};fontColor={INK};fillColor={fill};strokeColor={stroke};spacing=14;align=left;verticalAlign=middle;'
   value=('<b>'+html.escape(n['title'])+'</b>' if n['title'] else '')+('<br>' if n['title'] and n['body'] else '')+html.escape(n['body']).replace('\n','<br>')
   if n['band']:
    value=html.escape(n['title']);style+=f'shape=swimlane;startSize=44;horizontal=1;fillColor={n["color"]};swimlaneFillColor={fill};fontColor=#FFFFFF;fontStyle=1;container=1;collapsible=0;recursiveResize=0;'
   if n['kind']=='future':style+='dashed=1;dashPattern=7 4;'
   if n['kind']=='title':style+='strokeColor=none;fillColor=none;spacing=0;'
   if n['kind']=='decision':style+='strokeWidth=2;'
   c=ET.SubElement(root,'mxCell',id=n['id'],value=value,style=style,vertex='1',parent=n['parent'],sourceRefs=n['refs'])
   parent=self.nodes.get(n['parent'],{'x':0,'y':0});ET.SubElement(c,'mxGeometry',x=str(n['x']-parent['x']),y=str(n['y']-parent['y']),width=str(n['w']),height=str(n['h']),attrib={'as':'geometry'})
   if n['band']:rect(n)
  for e in self.edges:
   pts=self.points(e);future=e['kind']=='future';col='#AA8539' if future else GRAY
   attrs=dict(points=' '.join(f'{x},{y}' for x,y in pts),fill='none',stroke=col,stroke_width=1.8,marker_end='url(#future)' if future else 'url(#arrow)')
   if e['kind']!='data':attrs['stroke_dasharray']='7 4' if future else '2 4'
   s('polyline',**attrs)
   style=f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=block;endFill=1;strokeColor={col};strokeWidth=1.8;fontFamily=Arial;fontSize=14;labelBackgroundColor=#FFFFFF;fontColor={INK};jumpStyle=arc;jumpSize=8;'
   anchors={'left':(0,.5),'right':(1,.5),'top':(.5,0),'bottom':(.5,1),'topright':(.8,0)}
   ax,ay=anchors[e['sa']];bx,by=anchors[e['ta']];style+=f'exitX={ax};exitY={ay};entryX={bx};entryY={by};'
   if e['kind']!='data':style+='dashed=1;dashPattern='+('7 4;' if future else '2 4;')
   c=ET.SubElement(root,'mxCell',id=e['id'],value=e['label'],style=style,edge='1',parent='1',source=e['a'],target=e['b'],sourceRefs=e['refs'])
   ge=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
   if e.get('label_pos'):ET.SubElement(ge,'mxPoint',x='0',y='-65',attrib={'as':'offset'})
   if len(pts)>2:
    ar=ET.SubElement(ge,'Array',attrib={'as':'points'})
    for x,y in pts[1:-1]:ET.SubElement(ar,'mxPoint',x=str(x),y=str(y))
  for n in self.nodes.values():
   if not n['band']:rect(n)
   t,b=self.lines(n);lh=n['fs']*1.22;total=(len(t)+len(b))*lh+(8 if t and b else 0)
   y=n['y']+29 if n['band'] else n['y']+(n['h']-total)/2+n['fs']
   for bold,ls in [(True,t),(False,b)]:
    for line in ls:
     s('text',x=n['x']+(0 if n['kind']=='title' else 14),y=round(y,1),font_family='Arial',font_size=n['fs'],font_weight='bold' if bold else 'normal',fill='white' if n['band'] else INK).text=line;y+=lh
    if bold and t and b:y+=8
  for e in self.edges:
   if e['label']:
    pts=self.points(e);a,b=max(zip(pts,pts[1:]),key=lambda z:abs(z[0][0]-z[1][0])+abs(z[0][1]-z[1][1]));x=(a[0]+b[0])/2;y=(a[1]+b[1])/2-8;w=len(e['label'])*7.1+10

    if e.get('label_pos'):x,y=e['label_pos']
    s('rect',x=x-w/2,y=y-14,width=w,height=20,fill='white')
    s('text',x=x,y=y,text_anchor='middle',font_family='Arial',font_size=14,fill=INK).text=e['label']
  ET.ElementTree(svg).write(OUT/(slug+'.svg'),encoding='utf-8',xml_declaration=True)
  return {'page':self.name,'vertices':len(self.nodes),'connectors':len(self.edges),'size':[self.w,self.h]}

v=View('GCP / GKE Technical Level 1',3000,1810)
v.header('Implementation proposal • 12 October 2026 • Existing detection behavior preserved; technology choices require approval')
v.band('gcp','GOOGLE CLOUD | TARGET PLATFORM — CONFIRMED',400,150,2100,1510)
v.band('gke','GKE | TARGET RUNTIME — CONFIRMED; WORKLOAD SPLIT PROPOSED',430,470,1550,990,'gcp',TEAL)
v.box('genesys','Genesys Cloud','Enterprise call source\nLive audio interface OPEN',40,240,310,125,'external',refs='C01',fs=20)
v.box('test','Transcript emulator','Separate TEST service\nWebSocket transcript input',40,485,310,130,'test',refs='C02',fs=21)
v.box('provider','Provider integration','Authentication, audio format\nand reconnect contract OPEN\nNo audio-native bypass selected',40,730,310,200,'support',fs=18)
v.box('stt','Cloud Speech-to-Text','PROPOSED managed STT\nStreaming recognition / gRPC\nLanguage and accuracy evaluation',470,245,480,150,'future','gcp','C72',20)
v.box('queue','Pub/Sub topic + subscription','PROPOSED transcript queue\nPublish / StreamingPull + acknowledgment\nCall ordering key proposal; semantics OPEN',1040,245,650,150,'future','gcp','C74',20)
v.box('platform','Cloud service access','PROPOSED: private service access where supported\nWorkload identity + least-privilege IAM\nProject / network / region selection OPEN',1780,245,680,150,'support','gcp',fs=20)
v.box('bridge','Audio acquisition adapter','PROPOSED GKE workload\nGenesys stream ↔ STT client\nEmit transcript events',460,550,380,125,'future','gke','C71',19)
v.box('ingress','Transcript ingress service','PROPOSED GKE workload\nSource adaptation + call/session ID\nPublish transcript events',900,550,410,125,'future','gke','C57,C73',19)
v.box('worker','Ingestion worker pool','PROPOSED GKE replicas / autoscaling\nConsume / normalize / session windows\nIndependent calls; ordering and recovery OPEN',1370,550,570,125,'future','gke','C08,C56',19)
v.box('coord','Detector coordination service','PROPOSED GKE service boundary • Select applicable catalog signals and invoke configured method(s)\nNo mandatory all-path execution; scheduling and fallback OPEN',460,760,1480,100,'future','gke','C54,C59',20)
v.box('rules','Deterministic engine','PROPOSED GKE module/service\nRules • regex • fuzzy • entity checks',460,920,430,125,'future','gke','C39',20)
v.box('semantic','Semantic engine','PROPOSED GKE workload\nEmbedding → vector top-K → reranker\nModel / compute sizing OPEN',950,920,460,125,'future','gke','C18,C19,C36',19)
v.box('llm','LLM detection adapter','PROPOSED GKE workload\nCandidate + requirement + context\nPrompt / model / endpoint OPEN',1470,920,470,125,'future','gke','C60',19)
v.box('resolver','Shared Signal Resolution','CONFIRMED acceptance role; GKE packaging PROPOSED\nThreshold-based acceptance for all invoked methods\nScore calibration / combination / finality OPEN',690,1150,760,125,'decision','gke','C22',19)
v.box('publisher','Signal publication API','PROPOSED GKE workload\nAccepted signal events\nSSE / WebSocket over HTTPS proposed',1530,1150,410,115,'future','gke','C24,C40',18)
v.box('management','Signal Management UI / API','PROPOSED GKE packaging • Catalog / definitions / curated examples\nVersion activation and embedding population workflow OPEN',460,1320,870,100,'future','gke','C53,C13,C52',19)
v.box('later','Contextual generation / activation','LATER • workload placement PROPOSED\nSelective follow-on; distinct from detection',1390,1320,550,100,'future','gke','C27,C28',19)
v.box('state','Memorystore for Redis','PROPOSED managed context store\nBounded utterances + prior signals\nPer-call ownership / TTL / recovery OPEN',2020,530,450,155,'future','gcp','C47',19)
v.box('sql','Cloud SQL for PostgreSQL','PROPOSED hosting + pgvector\nCatalog / examples / accepted records\nExisting approved PostgreSQL alternative',2020,750,450,155,'future','gcp','C61',19)
v.box('model','Vertex AI endpoint','PROPOSED model integration\nAlternative: enterprise model gateway\nModel and approval OPEN',2020,970,450,155,'future','gcp','C60',19)
v.box('telemetry','Cloud Observability','PROPOSED Logging / Monitoring / Trace\nGKE + application instrumentation\nCall/event trace and stage latency\nAccess, retention and sampling OPEN',2020,1215,450,210,'future','gcp','C44',19)
v.box('controls','PROPOSED SHARED CONTROLS | Apply across GKE workloads and cloud-service access','Workload Identity Federation for GKE + IAM  •  Secret Manager API / CSI integration  •  Private connectivity / network policy\nSignal version governance, data retention, privacy and audit: enterprise/application ownership OPEN',430,1510,2040,115,'support','gcp',fs=21)
v.box('workbench','Real-time signal workbench','Confirmed consumer capability\nUI hosting / access boundary OPEN\nEvidence and latency display',2570,1140,390,150,'external',refs='C25',fs=20)
v.box('consumers','Downstream consumers','LATER integration\nContracts and hosting OPEN',2570,1370,390,110,'future',refs='C29',fs=20)
v.box('persist-note','Persistence boundary','Cloud SQL result storage: PROPOSED\nFull-call retention / destination OPEN\nBigQuery remains a reference option',2570,780,390,185,'support',refs='C63',fs=19)
v.box('review-note','Decision status','CONFIRMED: target or agreed behavior\nPROPOSED: recommended implementation\nOPEN: contract / ownership undecided\nNo deployed infrastructure asserted',2570,245,390,250,'support',fs=19)
v.link('genesys','bridge','audio • interface OPEN','future','right','left',[(380,302.5),(380,607.5)],'R94')
v.link('bridge','stt','gRPC / TLS request + results','future','top','bottom',[(650,435),(710,435)],'R95')
v.link('bridge','ingress','transcript events','data',refs='R96')
v.link('test','ingress','WebSocket','data','right','top',[(365,550),(365,440),(1105,440)],'R65')
v.link('ingress','queue','publish API / TLS','future','top','bottom',[(1105,425),(1365,425)],'R98')
v.link('queue','worker','StreamingPull / TLS','future','bottom','top',[(1740,395),(1740,445),(1655,445)],'R99')
v.link('worker','coord','microbatch • gRPC proposed','data','bottom','topright',[(1655,720),(1644,720)],'R92')
v.link('worker','state','Redis / TLS','future',refs='R68')
v.link('state','coord','context','future','left','right',[(1990,607.5),(1990,810)],'R69')
for dst,x in [('rules',675),('semantic',1180),('llm',1705)]:v.link('coord',dst,'','data','bottom','top',[(1200,890),(x,890)],'R71,R72,R73')
for src,x in [('rules',675),('semantic',1180),('llm',1705)]:v.link(src,'resolver','','data','bottom','top',[(x,1100),(1070,1100)],'R30,R47,R93')
v.link('llm','model','HTTPS inference','future',refs='R73')
v.link('semantic','sql','SQL / TLS + vector search','future','right','left',[(1435,982.5),(1435,900),(2000,900),(2000,827.5)],'R79')
v.link('management','coord','catalog configuration','config','left','left',[(445,1370),(445,810)],'R62,R70')
v.link('management','sql','SQL / TLS','future','right','left',[(1350,1370),(1350,1440),(1995,1440),(1995,827.5)],'PROPOSED catalog store')
v.link('resolver','publisher','accepted events',refs='R32')
v.link('publisher','workbench','SSE / WebSocket over HTTPS','future','right','top',[(2005,1207.5),(2005,1170),(2535,1170),(2535,1110),(2765,1110)],'R33,R40')
v.link('publisher','sql','persist result • proposed','future','right','bottom',[(1987,1207.5),(1987,1140),(2490,1140),(2490,935),(2245,935)],'PROPOSED storage mapping')
v.link('resolver','later','selective','future','bottom','top',[(1070,1295),(1665,1295)],'R35')
v.link('later','consumers','delivery contract OPEN','future','bottom','bottom',[(1665,1475),(2765,1475)],'R36,R37')
v.link('gke','telemetry','workload logs / metrics / traces','config','bottom','bottom',[(1205,1490),(2245,1490)],'C44')
v.edges[1]['label_pos']=(680,420)
v.box('legend','CONNECTIONS & SCOPE','Solid: retained logical processing flow   ··· Dotted: configuration / telemetry   – – Amber: proposed service interface or later flow   Purple: test input\nAll new workload boundaries, cloud products and protocols shown as PROPOSED need enterprise approval. Managed services are outside the GKE boundary.',40,1680,2920,105,'title',fs=21)
mx=ET.Element('mxfile',host='app.diagrams.net',type='device')
report=v.export(mx,'vantage-gcp-gke-technical-level-1')
ET.indent(mx);ET.ElementTree(mx).write(OUT/'vantage-gcp-gke-technical-level-1.drawio',encoding='utf-8',xml_declaration=True)
(OUT/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(report)
