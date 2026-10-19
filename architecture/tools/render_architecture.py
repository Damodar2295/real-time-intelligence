"""Render the authoritative V1 graph and derived explanatory views; no runtime implementation."""
from pathlib import Path
import json, textwrap, html, re, base64
import xml.etree.ElementTree as ET

OUT=Path(__file__).resolve().parents[1]/'v1'
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
   if n.get('align')=='center':style+='align=center;'
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
     s('text',x=n['x']+n['w']/2 if n.get('align')=='center' else n['x']+(0 if n['kind']=='title' else (84 if n.get('icon') else 14)),text_anchor='middle' if n.get('align')=='center' else 'start',y=round(y,1),font_family='Arial',font_size=n['fs'],font_weight='bold' if bold else 'normal',fill='white' if n['band'] or n['kind']=='section' else INK).text=line;y+=lh
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
   if parent not in self.nodes:continue
   n=self.nodes[parent]
   for k,name in enumerate(names):
    data=base64.b64encode((OUT/'icons'/(name+'.svg')).read_bytes()).decode();x=n['w']-60*(len(names)-k)-10;y=(n['h']-40)/2
    c=ET.SubElement(root,'mxCell',id=parent+'-'+name+'-icon',value='',style='shape=image;imageAspect=1;aspect=fixed;image=data:image/svg+xml,'+data+';',vertex='1',parent=parent)
    ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width='40',height='40',attrib={'as':'geometry'})
    ET.SubElement(svg,'image',x=str(n['x']+x),y=str(n['y']+y),width='40',height='40',preserveAspectRatio='xMidYMid meet',href='data:image/svg+xml;base64,'+data)

def main():
 graphs={'level-1-architecture':json.loads((OUT/'graph-level-1.json').read_text())}
 graphs.update(json.loads((OUT/'component-graphs.json').read_text()))
 for slug,graph in graphs.items():
  v=View(graph.get('name','Vantage Real Time Intelligence — V1 Baseline Architecture'),*graph.get('size',[3760,2115]))
  v.nodes=graph['nodes'];v.edges=graph['edges']
  (OUT/slug).parent.mkdir(parents=True,exist_ok=True)
  mx=ET.Element('mxfile',host='app.diagrams.net',type='device')
  report=v.export(mx,slug)
  ET.indent(mx);ET.ElementTree(mx).write(OUT/(slug+'.drawio'),encoding='utf-8',xml_declaration=True)
  print(json.dumps(report))
if __name__=='__main__':main()
