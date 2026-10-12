"""Editable GCP/GKE technical proposal mapped from VANTAGE v1.2."""
from pathlib import Path
import json, textwrap, html, re, base64
import xml.etree.ElementTree as ET

OUT=Path(__file__).resolve().parent
NAVY='#002663'; TEAL='#006FCF'; INK='#002663'; GRAY='#3872A5'
COLORS={'normal':('#FFFFFF','#A5BAC8'),'support':('#EAF4FF','#B7C9D3'),'future':('#FFFFFF','#B29145'),'test':('#F1EBFA','#9879B9'),'decision':('#EAF4FF','#006FCF'),'external':('#EEF3F8','#839CAE'),'section':('#006FCF','#006FCF'),'zone':('#F4F9FF','#83ADD3')}
class View:
 def __init__(self,name,w,h):self.name=name;self.w=w;self.h=h;self.nodes={};self.edges=[]
 def box(self,i,title,body,x,y,w,h,kind='normal',parent='1',refs='',fs=18):
  self.nodes[i]=dict(id=i,title=title,body=body,x=x,y=y,w=w,h=h,kind=kind,parent=parent,refs=refs,fs=fs,band=False)
 def band(self,i,title,x,y,w,h,parent='1',color=NAVY):
  self.nodes[i]=dict(id=i,title=title,body='',x=x,y=y,w=w,h=h,kind='support',parent=parent,refs='',fs=21,band=True,color=color)
 def link(self,a,b,label='',kind='data',sa='right',ta='left',pts=None,refs=''):
  self.edges.append(dict(id='edge-'+str(len(self.edges)+1),a=a,b=b,label=label,kind=kind,sa=sa,ta=ta,pts=pts or [],refs=refs))
 def header(self,subtitle):
  self.box('page-title','VANTAGE Intelligence | '+self.name,'',40,15,self.w-80,55,kind='title',fs=30)
  self.box('page-subtitle','',subtitle,40,78,self.w-80,66,kind='title',fs=20)
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
  width=max(10,int((n['w']-28-(70 if n.get('icon') else 0))/(n['fs']*.55)))
  title=textwrap.wrap(n['title'],width=width,break_long_words=False)
  body=[l for p in n['body'].split('\n') for l in textwrap.wrap(p,width=width,break_long_words=False)] if n['body'] else []
  return title,body
 def validate(self):
  for n in self.nodes.values():
   assert n['x']>=0 and n['y']>=0 and n['x']+n['w']<=self.w and n['y']+n['h']<=self.h,n['id']
   t,b=self.lines(n);assert (len(t)+len(b))*n['fs']*1.22+(8 if t and b else 0)<=n['h']-(8 if n['kind']=='title' else 16),(self.name,n['id'],t,b)
   if n['parent']!='1':
    p=self.nodes[n['parent']];assert p['x']<=n['x'] and p['y']+(0 if p['kind']=='zone' else 42)<=n['y'] and n['x']+n['w']<=p['x']+p['w'] and n['y']+n['h']<=p['y']+p['h'],n['id']
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
  for name,col in [('arrow',GRAY),('future','#AA8539'),('test','#8A5DB0')]:
   m=ET.SubElement(defs,'marker',id=name,markerWidth='8',markerHeight='8',refX='7',refY='4',orient='auto');ET.SubElement(m,'path',d='M0,0 L8,4 L0,8 Z',fill=col)
  def rect(n):
   if n['kind']=='title':return
   fill,stroke=COLORS[n['kind']]
   fill=n.get('zone_fill',fill)
   attrs=dict(x=n['x'],y=n['y'],width=n['w'],height=n['h'],fill=fill,stroke=stroke,stroke_width=2 if n['kind']=='decision' else 1)
   if n['kind']=='future':attrs['stroke_dasharray']='7 4'
   if n['kind']=='zone':attrs.update(stroke_dasharray='2 5',stroke_width=2)
   s('rect',**attrs)
   if n['band']:s('rect',x=n['x'],y=n['y'],width=n['w'],height=44,fill=n['color'])
  for n in self.nodes.values():
   fill,stroke=COLORS.get(n['kind'],('#FFFFFF','#FFFFFF'))
   fill=n.get('zone_fill',fill)
   style=f'rounded=0;whiteSpace=wrap;html=1;fontFamily=Arial;fontSize={n["fs"]};fontColor={INK};fillColor={fill};strokeColor={stroke};spacing=14;align=left;verticalAlign=middle;'
   value=('<b>'+html.escape(n['title'])+'</b>' if n['title'] else '')+('<br>' if n['title'] and n['body'] else '')+html.escape(n['body']).replace('\n','<br>')
   if n['band']:
    value=html.escape(n['title']);style+=f'shape=swimlane;startSize=44;horizontal=1;fillColor={n["color"]};swimlaneFillColor={fill};fontColor=#FFFFFF;fontStyle=1;container=1;collapsible=0;recursiveResize=0;'
   if n.get('icon'):style+='spacingLeft=84;'
   if n['kind']=='zone':style+='dashed=1;dashPattern=2 5;strokeWidth=2;container=1;collapsible=0;recursiveResize=0;'
   if n['kind']=='section':style+='fontColor=#FFFFFF;fontStyle=1;'
   if n['kind']=='future':style+='dashed=1;dashPattern=7 4;'
   if n['kind']=='title':style+='strokeColor=none;fillColor=none;spacing=0;'
   if n['kind']=='decision':style+='strokeWidth=2;'
   c=ET.SubElement(root,'mxCell',id=n['id'],value=value,style=style,vertex='1',parent=n['parent'],sourceRefs=n['refs'],componentId=n['id'],decisionStatus=n.get('decision_status','NOTATION'),deploymentStatus='NOT VERIFIED')
   parent=self.nodes.get(n['parent'],{'x':0,'y':0});ET.SubElement(c,'mxGeometry',x=str(n['x']-parent['x']),y=str(n['y']-parent['y']),width=str(n['w']),height=str(n['h']),attrib={'as':'geometry'})
   if n['band'] or n['kind']=='zone':rect(n)
  for e in self.edges:
   pts=self.points(e);future=e['kind']=='future';col='#8A5DB0' if e['kind']=='test' else ('#AA8539' if future else GRAY)
   attrs=dict(points=' '.join(f'{x},{y}' for x,y in pts),fill='none',stroke=col,stroke_width=1.8,marker_end='url(#test)' if e['kind']=='test' else ('url(#future)' if future else 'url(#arrow)'))
   if e['kind'] not in ('data','test'):attrs['stroke_dasharray']='7 4' if future else ('9 3 2 3' if e['kind']=='telemetry' else '2 4')
   s('polyline',**attrs)
   style=f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=block;endFill=1;strokeColor={col};strokeWidth=1.8;fontFamily=Arial;fontSize=17;labelBackgroundColor=#FFFFFF;fontColor={INK};jumpStyle=arc;jumpSize=8;'
   anchors={'left':(0,.5),'right':(1,.5),'top':(.5,0),'bottom':(.5,1),'topright':(.8,0)}
   ax,ay=anchors[e['sa']];bx,by=anchors[e['ta']];style+=f'exitX={ax};exitY={ay};entryX={bx};entryY={by};'
   if e['kind'] not in ('data','test'):style+='dashed=1;dashPattern='+('7 4;' if future else ('9 3 2 3;' if e['kind']=='telemetry' else '2 4;'))
   c=ET.SubElement(root,'mxCell',id=e['id'],value=e['label'],style=style,edge='1',parent='1',source=e['a'],target=e['b'],sourceRefs=e['refs'],interfaceId=e['id'],decisionStatus=e.get('decision_status','OPEN'),protocolStatus=e.get('protocol_status','OPEN'))
   ge=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
   if e.get('label_pos'):
    length=sum(abs(b[0]-a[0])+abs(b[1]-a[1]) for a,b in zip(pts,pts[1:]));remain=length/2
    for a,b in zip(pts,pts[1:]):
     seg=abs(b[0]-a[0])+abs(b[1]-a[1])
     if seg and remain<=seg:
      mid=(a[0]+(b[0]-a[0])*remain/seg,a[1]+(b[1]-a[1])*remain/seg);break
     remain-=seg
    ET.SubElement(ge,'mxPoint',x=str(e['label_pos'][0]-mid[0]),y=str(e['label_pos'][1]-mid[1]-5),attrib={'as':'offset'})
   if len(pts)>2:
    ar=ET.SubElement(ge,'Array',attrib={'as':'points'})
    for x,y in pts[1:-1]:ET.SubElement(ar,'mxPoint',x=str(x),y=str(y))
  for n in self.nodes.values():
   if not n['band'] and n['kind']!='zone':rect(n)
   t,b=self.lines(n);lh=n['fs']*1.22;total=(len(t)+len(b))*lh+(8 if t and b else 0)
   y=n['y']+29 if n['band'] else n['y']+(n['h']-total)/2+n['fs']
   for bold,ls in [(True,t),(False,b)]:
    for line in ls:
     s('text',x=n['x']+(0 if n['kind']=='title' else (84 if n.get('icon') else 14)),y=round(y,1),font_family='Arial',font_size=n['fs'],font_weight='bold' if bold else 'normal',fill='white' if n['band'] or n['kind']=='section' else INK).text=line;y+=lh
    if bold and t and b:y+=8
  for e in self.edges:
   if e['label']:
    pts=self.points(e);a,b=max(zip(pts,pts[1:]),key=lambda z:abs(z[0][0]-z[1][0])+abs(z[0][1]-z[1][1]));x=(a[0]+b[0])/2;y=(a[1]+b[1])/2-8;w=len(e['label'])*8.5+14

    if e.get('label_pos'):x,y=e['label_pos']
    s('rect',x=x-w/2,y=y-14,width=w,height=23,fill='white')
    s('text',x=x,y=y,text_anchor='middle',font_family='Arial',font_size=17,fill=INK).text=e['label']
  self.add_status(root,svg)
  self.add_icons(root,svg)
  ET.ElementTree(svg).write(OUT/(slug+'.svg'),encoding='utf-8',xml_declaration=True)
  return {'page':self.name,'vertices':len(self.nodes),'connectors':len(self.edges),'size':[self.w,self.h]}



 def add_status(self,root,svg):
  for n in self.nodes.values():
   if not n.get('status_label'):continue
   label=n['status_label'];x=n['w']-170;y=3
   cell=ET.SubElement(root,'mxCell',id=n['id']+'-status',value=label,style='text;html=0;strokeColor=none;fillColor=none;align=right;fontFamily=Arial;fontSize=12;fontColor=#61798A;spacing=0;',vertex='1',parent=n['id'])
   ET.SubElement(cell,'mxGeometry',x=str(x),y=str(y),width='160',height='17',attrib={'as':'geometry'})
   ET.SubElement(svg,'text',x=str(n['x']+n['w']-10),y=str(n['y']+15),attrib={'text-anchor':'end','font-family':'Arial','font-size':'12','fill':'#61798A'}).text=label

 def add_icons(self,root,svg):
  for n in self.nodes.values():
   if not n.get('icon'):continue
   raw=(OUT/'icons'/n['icon']).read_bytes()
   data=base64.b64encode(raw).decode()
   x,y=14,(n['h']-52)/2
   size=52
   if n['band']:y=4;x=14;size=36
   cell=ET.SubElement(root,'mxCell',id=n['id']+'-icon',value='',style='shape=image;imageAspect=1;aspect=fixed;image=data:image/svg+xml,'+data+';',vertex='1',parent=n['id'])
   ET.SubElement(cell,'mxGeometry',x=str(x),y=str(y),width=str(size),height=str(size),attrib={'as':'geometry'})
   ET.SubElement(svg,'image',x=str(n['x']+x),y=str(n['y']+y),width=str(size),height=str(size),preserveAspectRatio='xMidYMid meet',href='data:image/svg+xml;base64,'+data)


  for parent,names in [('telemetry',['cloud_monitoring','trace']),('controls',['identity_and_access_management'])]:
   n=self.nodes[parent]
   for k,name in enumerate(names):
    data=base64.b64encode((OUT/'icons'/(name+'.svg')).read_bytes()).decode();x=n['w']-60*(len(names)-k)-10;y=(n['h']-40)/2
    c=ET.SubElement(root,'mxCell',id=parent+'-'+name+'-icon',value='',style='shape=image;imageAspect=1;aspect=fixed;image=data:image/svg+xml,'+data+';',vertex='1',parent=parent)
    ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width='40',height='40',attrib={'as':'geometry'})
    ET.SubElement(svg,'image',x=str(n['x']+x),y=str(n['y']+y),width='40',height='40',preserveAspectRatio='xMidYMid meet',href='data:image/svg+xml;base64,'+data)

# Neutral symbols identify capabilities, never vendors or selected runtimes.
neutral={
 'service':'<rect x="8" y="8" width="48" height="48" rx="5"/><path d="M18 23h28M18 32h20M18 41h28"/>',
 'audio':'<path d="M9 28v10m8-20v30m8-38v46m8-34v22m8-30v36m8-24v12m8-18v24"/>',
 'screen':'<rect x="5" y="10" width="54" height="37" rx="3"/><path d="M32 47v9M19 56h26M13 36l10-10 9 5 17-14"/>',
 'shield':'<path d="M32 5l23 9v18c0 13-23 26-23 26S9 45 9 32V14zM21 31l8 8 15-17"/>',
 'cloud':'<path d="M16 47a12 12 0 010-24 17 17 0 0133-1 13 13 0 011 25z"/>',
 'check':'<circle cx="32" cy="32" r="25"/><path d="M17 32l10 10 21-23"/>',
 'branch':'<path d="M8 32h17V12h24M25 32h24M25 32v20h24"/><circle cx="53" cy="12" r="4"/><circle cx="53" cy="32" r="4"/><circle cx="53" cy="52" r="4"/>',
 'search':'<circle cx="26" cy="26" r="17"/><path d="M39 39l18 18M17 26h18M26 17v18"/>'}
for name,body in neutral.items():
 (OUT/'icons'/('neutral-'+name+'.svg')).write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><g fill="none" stroke="#006FCF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'+body+'</g></svg>')
v=View('Enterprise Technical Level 1 | V4',3760,2100)
v.header('Status: DRAFT — EARB review  |  Target: GCP / GKE  |  Owner: UNASSIGNED  |  Review date: 12 October 2026\nBaseline: latest local V3 + logical model v1.2  |  Target confirmation does not indicate deployment or production approval')
v.band('gcp','GOOGLE CLOUD  |  Confirmed target platform',420,160,2840,1760)
v.band('gke','GKE APPLICATION RUNTIME  |  Confirmed target; workload boundaries proposed',455,580,2770,1000,'gcp',TEAL)
v.box('managed-label','MANAGED CLOUD SERVICES','Outside GKE • Proposed selections',465,215,1100,70,'title','gcp',fs=20)
def card(i,t,b,x,y,w=410,h=150,kind='future',parent='gke',icon='neutral-service.svg',refs=''):
 v.box(i,t,b,x,y,w,h,kind,parent,refs,20);v.nodes[i]['icon']=icon
card('genesys','Genesys Cloud','Live call source\nAudio interface OPEN',35,670,340,150,'external','1','neutral-cloud.svg','C01')
card('test','Transcript emulator','Separate TEST service\nConcurrent call streams',35,930,340,150,'test','1','neutral-service.svg','C02')
v.box('provider','Provider integration','Authentication • format • reconnect\nContracts OPEN',35,1220,340,140,'support',fs=20)
card('stt','Speech-to-Text','Streaming recognition\ngRPC / TLS • PROPOSED',490,300,435,160,parent='gcp',icon='speech-to-text.svg',refs='C72')
card('queue','Cloud Pub/Sub','Transcript topic + subscription\nCall ordering semantics OPEN',1040,300,435,160,parent='gcp',icon='pubsub.svg',refs='C74')
card('state','Memorystore for Redis','Bounded same-call context\nPrior signals • lifecycle OPEN',1640,300,435,160,parent='gcp',icon='memorystore.svg',refs='C47')
card('sql','Cloud SQL · PostgreSQL','pgvector • catalog • results\nHosting and storage PROPOSED',2210,300,435,160,parent='gcp',icon='cloud_sql.svg',refs='C61')
card('model','Vertex AI endpoint','LLM inference • PROPOSED\nEnterprise gateway alternative',2770,300,435,160,parent='gcp',icon='vertexai.svg',refs='C60')
card('bridge','Audio acquisition','Genesys stream / STT client\nTranscript event output',490,670,380,150,refs='C71',icon='neutral-audio.svg')
card('ingress','Transcript ingress','Source adaptation\nCall / session identity',490,930,380,150,refs='C57,C73')
card('worker','Ingestion worker pool','Normalize • sessions\nSegmentation / microbatches',1010,930,410,150,refs='C08,C56')
card('coord','Detector coordination','Catalog applicability\nSelect configured method(s)',1530,930,410,150,refs='C54,C59',icon='neutral-branch.svg')
card('rules','Deterministic detection','Rules • regex • fuzzy\nEntity checks',2050,690,420,150,refs='C39')
card('semantic','Semantic detection','Embed → top-K → rerank\nModel / hosting OPEN',2050,930,420,150,refs='C18,C19,C36',icon='neutral-search.svg')
card('llm','LLM detection adapter','Candidate + requirement\nConversation context',2050,1170,420,150,refs='C60')
card('resolver','Shared Signal Resolution','Threshold-based acceptance\nCalibration / combination OPEN',2670,930,505,165,kind='decision',refs='C22',icon='neutral-check.svg')
card('publisher','Signal publication API','Accepted signal events\nDelivery + persistence proposed',2670,1240,505,145,refs='C24,C40')
card('management','Signal Management UI / API','Catalog • definitions • curated examples\nActivation / versioning workflow OPEN',1010,1375,870,130,refs='C53,C13,C52',icon='neutral-screen.svg')
card('later','Contextual generation / activation','LATER • selective follow-on',2670,1440,505,110,refs='C27,C28',icon='neutral-branch.svg')
card('workbench','Signal workbench','Evidence + latency display\nHosting / access OPEN',3310,1240,410,145,'external','1','neutral-screen.svg','C25')
card('consumers','Downstream consumers','LATER integration\nDelivery contract OPEN',3310,1480,410,140,'future','1','neutral-screen.svg','C29')
v.box('status','DECISION STATUS','CONFIRMED = agreed target / behavior\nPROPOSED = implementation recommendation\nOPEN = unresolved contract / owner\nNo deployed infrastructure asserted',3310,300,410,220,'support',fs=20)
v.box('notes','PERSISTENCE & MODELS','Existing PostgreSQL remains an option.\nFull-call storage is OPEN.\nBigQuery is reference-only.\nEmbedding / reranker hosting is OPEN.',3310,650,410,200,'support',fs=20)
# Shared support: the same aggregate capabilities as the previous view, with separate product icons.
card('telemetry','Cloud Observability','Logging • Monitoring • Trace\nApplication instrumentation required',490,1710,740,150,'future','gcp','cloud_logging.svg','C44')
card('controls','Identity, secrets & network controls','Workload Identity / IAM • Secret Manager\nPrivate connectivity and network policy',1320,1710,1020,150,'future','gcp','secret_manager.svg')
v.box('governance','ENTERPRISE GOVERNANCE','Access • retention • privacy • audit\nOwnership and policies OPEN',2430,1710,745,150,'support','gcp',fs=21)
# Preserve all 25 previous view relationships. Coordinates only change presentation.
v.link('genesys','bridge','Audio • interface OPEN','future',refs='R94')
v.link('bridge','stt','gRPC / TLS + results','future','top','bottom',[(680,515),(707.5,515)],'R95')
v.link('bridge','ingress','Transcript events','data','bottom','top',refs='R96')
v.link('test','ingress','WebSocket','test',refs='R65')
v.link('ingress','queue','Publish API / TLS','future','right','bottom',[(940,1005),(940,515),(1257.5,515)],'R98')
v.link('queue','worker','StreamingPull / ack','future','bottom','top',[(1257.5,550),(1215,550)],'R99')
v.link('worker','coord','Microbatch • gRPC proposed','data',refs='R92')
v.link('worker','state','Redis / TLS','future','top','bottom',[(1215,880),(1480,880),(1480,490),(1857.5,490)],'R68')
v.link('state','coord','Same-call context','future','bottom','top',[(1857.5,525),(1735,525)],'R69')
for dst,y in [('rules',765),('semantic',1005),('llm',1245)]:
 v.link('coord',dst,'','data','right','left',[(1995,1005),(1995,y)],'R71,R72,R73')
for src,y in [('rules',765),('semantic',1005),('llm',1245)]:
 v.link(src,'resolver','','data','right','left',[(2545,y),(2545,1012.5)],'R30,R47,R93')
v.link('llm','model','HTTPS inference','future','right','bottom',[(2605,1245),(2605,550),(2987.5,550)],'R73')
v.link('semantic','sql','Vector search • SQL / TLS','future','top','bottom',[(2260,885),(2505,885),(2505,500),(2427.5,500)],'R79')
v.link('management','coord','Catalog configuration','config','top','bottom',[(1445,1140),(1735,1140)],'R62,R70')
v.link('management','sql','Catalog • SQL / TLS','future','right','left',[(1910,1440),(1910,1360),(1965,1360),(1965,480),(2165,480),(2165,380)],'PROPOSED catalog store')
v.link('resolver','publisher','Accepted signals','data','bottom','top',refs='R32')
v.link('publisher','workbench','SSE / WebSocket over HTTPS','future',refs='R33,R40')
v.link('publisher','sql','Persist result • proposed','future','right','top',[(3245,1312.5),(3245,280),(2427.5,280)],'PROPOSED storage mapping')
v.link('resolver','later','Selective follow-on','future','bottom','left',[(2635,1095),(2635,1495)],'R35')
v.link('later','consumers','Delivery contract OPEN','future',refs='R36,R37')
v.link('gke','telemetry','Logs / metrics / traces','config','bottom','top',[(1840,1640),(860,1640)],'C44')
# Concise descriptive zone labels; no legacy source-reference numbers.
for i,t,x,y,w in [('ingestion','1  INTERACTION INGESTION',490,625,380),('detection','2  DETECTION & ORCHESTRATION',2050,625,420),('resolution','3  RESOLUTION & OUTPUT',2670,625,505)]:
 v.box('label-'+i,t,'',x,y,w,42,'section','gke',fs=20)
v.box('legend','CONNECTIONS & SCOPE','Solid blue: documented processing   •   Amber dashed: proposed interface   •   Dotted blue: configuration / telemetry   •   Purple: test input\nGCP / GKE are confirmed targets. Dashed component borders indicate proposed implementation. Workload groups do not imply separate Kubernetes Deployments.',40,1950,3680,110,'title',fs=22)
v.nodes['gke']['icon']='google_kubernetes_engine.svg'
# Titles shorter for legibility; full unresolved details remain in the decision notes.
for e in v.edges:
 if e['label']=='Microbatch • gRPC proposed':e['label_pos']=(1475,915)
 if e['label']=='SSE / WebSocket over HTTPS':e['label_pos']=(3260,1220)
 if e['label']=='Delivery contract OPEN':e['label_pos']=(3260,1430)
 if e['label']=='Selective follow-on':e['label_pos']=(2615,1415)
 if e['label']=='gRPC / TLS + results':e['label_pos']=(700,510)
 if e['label']=='Publish API / TLS':e['label_pos']=(985,710)
 if e['label']=='StreamingPull / ack':e['label_pos']=(1295,800)
 if e['label']=='Redis / TLS':e['label_pos']=(1510,730)
 if e['label']=='Same-call context':e['label_pos']=(1735,825)
 if e['label']=='Vector search • SQL / TLS':e['label_pos']=(2460,870)
 if e['label']=='HTTPS inference':e['label_pos']=(2605,520)
 if e['label']=='Catalog • SQL / TLS':e['label_pos']=(1950,1380)
 if e['label']=='Persist result • proposed':e['label_pos']=(3020,275)
# Visual process containers: grouping only, not additional service boundaries.
for ident,x,w,h,tint,members in [
 ('ingestion-zone',475,975,730,'#F4F9FF',['bridge','ingress','worker','label-ingestion']),
 ('detection-zone',1510,990,730,'#F0F6FC',['coord','rules','semantic','llm','label-detection']),
 ('resolution-zone',2655,535,940,'#F4F7FA',['resolver','publisher','later','label-resolution'])]:
 v.box(ident,'','',x,625,w,h,'zone','gke')
 v.nodes[ident]['zone_fill']=tint
 for member in members:v.nodes[member]['parent']=ident
v.nodes['label-ingestion'].update(x=490,w=945)
v.nodes['label-detection'].update(x=1525,w=960)
# Background containers precede their editable children in both exports.
first=['gcp','gke','ingestion-zone','detection-zone','resolution-zone']
v.nodes={**{k:v.nodes[k] for k in first},**{k:n for k,n in v.nodes.items() if k not in first}}
# V4 review refinements: preserve stable IDs/endpoints; no new processing links.
confirmed=['genesys','test','workbench','resolver']
for n in v.nodes.values():
 if n.get('icon') and not n['band']:
  n['decision_status']='CONFIRMED behavior; implementation OPEN' if n['id'] in confirmed else 'PROPOSED implementation'
  n['status_label']='CONFIRMED ROLE' if n['id'] in confirmed else 'PROPOSED'
for k in ['gcp','gke']:v.nodes[k]['decision_status']='CONFIRMED target; deployment NOT VERIFIED'
for k in ['provider','governance']:v.nodes[k]['decision_status']='OPEN ownership / controls'
v.nodes['state']['body']='Bounded same-call context\nHistory writer / recovery OPEN'
v.nodes['coord']['body']='Select applicable method(s)\nScheduling / completion OPEN'
v.nodes['status']['body']='CONFIRMED: agreed target / role\nPROPOSED: implementation choice\nOPEN: contract / owner undecided\nDeployment is NOT VERIFIED'
v.nodes['notes']['title']='DATA & TRUST BOUNDARIES'
v.nodes['notes']['body']='Runtime boxes are not trust zones.\nIngress / access policy OPEN.\nFull-call storage OPEN.\nBigQuery is reference-only.'
v.nodes['legend']['body']='Solid blue: documented data flow   •   Amber dashed: proposed integration   •   Dotted blue: configuration / control   •   Dash-dot blue: telemetry   •   Purple: test input\nShaded process groups are visual only. Security boundaries and control inheritance are OPEN. Stable component / interface IDs are embedded and listed in the V4 matrix.'
refs={10:'R71',11:'R72',12:'R73',13:'R50,R30',14:'R47',15:'R93',16:'C60',19:'C13,C52,C53',21:'R33,R51',22:'R34',25:'C44'}
for e in v.edges:
 num=int(e['id'].split('-')[1])
 if num in refs:e['refs']=refs[num]
 e['decision_status']='PROPOSED interface' if e['kind']=='future' else 'CONFIRMED logical relationship'
 e['protocol_status']='PROPOSED' if num in [2,5,6,7,8,16,17,19,21,22] else ('DOCUMENTED WebSocket' if num==4 else 'OPEN / not specified')
 if num==25:e['kind']='telemetry';e['decision_status']='CONFIRMED telemetry requirement; product PROPOSED'
# Remove 40px of unused vertical gap above the GKE runtime.
def compact(y):return y if y<=470 else (y-40 if y>=540 else 470+(y-470)*30/70)
for n in v.nodes.values():
 bottom=compact(n['y']+n['h']);n['y']=compact(n['y']);n['h']=bottom-n['y']
for e in v.edges:
 e['pts']=[(x,compact(y)) for x,y in e['pts']]
 if e.get('label_pos'):e['label_pos']=(e['label_pos'][0],compact(e['label_pos'][1]))
v.h-=40
mx=ET.Element('mxfile',host='app.diagrams.net',type='device')
report=v.export(mx,'vantage-gcp-gke-technical-level-1-v4')
ET.indent(mx);ET.ElementTree(mx).write(OUT/'vantage-gcp-gke-technical-level-1-v4.drawio',encoding='utf-8',xml_declaration=True)
(OUT/'graph-v4.json').write_text(json.dumps({'nodes':v.nodes,'edges':v.edges},indent=2)+'\n')
(OUT/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(report)
