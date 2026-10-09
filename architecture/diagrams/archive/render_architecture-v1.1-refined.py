"""Presentation-refined v1.1 diagram; no model changes."""
from pathlib import Path
import copy, hashlib, html, json, textwrap
import xml.etree.ElementTree as E

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'diagrams'
OUT.mkdir(exist_ok=True)
source = json.loads((ROOT / 'diagrams/layout-v1.1.json').read_text())
N = copy.deepcopy(source['nodes'])
edges = copy.deepcopy(source['edges'])
W, H = source['width'], source['height']
# Align acceptance artifacts and increase clearance around connector labels.
for i in ['C21', 'C22', 'C23']:
    N[i]['y'], N[i]['h'] = 1320, 110
N['C39']['y'] = N['C60']['y'] = 1010
# Route retrieval in the inter-strategy gutter, avoiding the strategy heading.
next(e for e in edges if e['id'] == 'R79')['points'] = [(1330,1090),(1685,1090),(1685,975),(2240,975),(2240,952)]
next(e for e in edges if e['id'] == 'R93')['points'] = [(1955,1255),(1628,1255)]
# Match relocated result-row midpoints.
next(e for e in edges if e['id'] == 'R21-R24')['points'] = [(815,1375)]
next(e for e in edges if e['id'] == 'R88')['points'] = [(55,937),(55,397)]

bands = {'G01','sources','L01','L02','output','L03','L04'}
navy, teal, ink = '#193954', '#126C70', '#17324F'

def palette(n):
    if n['id'] == 'C22': return '#E1F3EF', teal
    if n['kind'] == 'future': return '#FFFAED', '#B38A36'
    if n['kind'] == 'conflict': return '#FFF0EA', '#BC7B67'
    if n['kind'] == 'title': return '#FFFFFF', '#FFFFFF'
    if n['id'] in bands: return '#F3F7FB', '#C3D2E1'
    if n['kind'] == 'support': return '#F7F9FC', '#C3D2E1'
    return '#FFFFFF', '#9AAFBE'

def heading_color(i):
    return teal if i in {'G01','L02','output'} else navy

def lines(n):
    width = max(12,int((n['w']-28)/(n['fs']*.55)))
    return [line for p in n['label'].split('\n') for line in (textwrap.wrap(p,width=width,break_long_words=False) or [''])]

def anchor(n,s):
    return {'left':(n['x'],n['y']+n['h']/2),'right':(n['x']+n['w'],n['y']+n['h']/2),'top':(n['x']+n['w']/2,n['y']),'topright':(n['x']+n['w']*.8,n['y']),'bottom':(n['x']+n['w']/2,n['y']+n['h'])}[s]

def route(e):
    a,b=anchor(N[e['a']],e['sa']),anchor(N[e['b']],e['ta'])
    pts=[a]+e['points']+[b]
    if len(pts)==2 and a[0]!=b[0] and a[1]!=b[1]:
        pts=[a,((a[0]+b[0])/2,a[1]),((a[0]+b[0])/2,b[1]),b]
    return pts

mx=E.Element('mxfile',host='app.diagrams.net',type='device')
d=E.SubElement(mx,'diagram',id='vantage-logical-v01',name='Consolidated layered architecture')
gm=E.SubElement(d,'mxGraphModel',grid='1',gridSize='10',page='1',pageScale='1',pageWidth=str(W),pageHeight=str(H),math='0',shadow='0')
r=E.SubElement(gm,'root');E.SubElement(r,'mxCell',id='0');E.SubElement(r,'mxCell',id='1',parent='0')
for n in N.values():
    fill,stroke=palette(n)
    value=n['label']
    style=f'rounded=0;whiteSpace=wrap;html=0;fillColor={fill};strokeColor={stroke};fontColor={ink};fontFamily=Arial;fontSize={n["fs"]};spacing=12;align=left;verticalAlign={"top" if n["heading"] else "middle"};'
    if n['id'] in bands:
        style+=f'shape=swimlane;horizontal=1;startSize=50;fillColor={heading_color(n["id"])};swimlaneFillColor={fill};fontColor=#FFFFFF;'
    if n['bold']: style+='fontStyle=1;'
    if n['kind'] in {'future','conflict'}: style+='dashed=1;dashPattern=7 4;'
    if n['heading']: style+='container=1;collapsible=0;recursiveResize=0;'
    if n['id']=='C22': style+='strokeWidth=2.5;fontStyle=1;'
    if not n['heading'] and n['kind']!='title' and n['id']!='C22':
        parts=value.split('\n')
        value='<b>'+html.escape(parts[0])+'</b>'+''.join('<br>'+html.escape(p) for p in parts[1:])
        style=style.replace('html=0','html=1')
    cell=E.SubElement(r,'mxCell',id=n['id'],value=value,style=style,vertex='1',parent=n['parent'])
    p=N.get(n['parent'],{'x':0,'y':0})
    E.SubElement(cell,'mxGeometry',x=str(n['x']-p['x']),y=str(n['y']-p['y']),width=str(n['w']),height=str(n['h']),attrib={'as':'geometry'})
xy={'right':(1,.5),'left':(0,.5),'top':(.5,0),'topright':(.8,0),'bottom':(.5,1)}
for e in edges:
    ax,ay=xy[e['sa']]; bx,by=xy[e['ta']]
    col='#B38A36' if e['kind']=='future' else '#52728B'
    st=f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=block;endFill=1;strokeColor={col};strokeWidth=1.8;fontColor=#35556E;fontFamily=Arial;fontSize=13;labelBackgroundColor=#FFFFFF;labelBorderColor=none;jumpStyle=arc;jumpSize=8;exitX={ax};exitY={ay};entryX={bx};entryY={by};'
    if e['kind']!='data': st+='dashed=1;dashPattern='+('2 4;' if e['kind']=='config' else '7 4;')
    c=E.SubElement(r,'mxCell',id=e['id'],value=e['label'],style=st,edge='1',parent='1',source=e['a'],target=e['b'])
    ge=E.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
    if e['points']:
        ar=E.SubElement(ge,'Array',attrib={'as':'points'})
        for x,y in e['points']:E.SubElement(ar,'mxPoint',x=str(x),y=str(y))
E.indent(mx)
E.ElementTree(mx).write(OUT/'VANTAGE_Intelligence_Layered_Architecture.drawio',encoding='utf-8',xml_declaration=True)

svg=E.Element('svg',xmlns='http://www.w3.org/2000/svg',width=str(W),height=str(H),viewBox=f'0 0 {W} {H}')
def se(tag,**kw):return E.SubElement(svg,tag,{k.replace('_','-'):str(v) for k,v in kw.items()})
se('rect',x=0,y=0,width=W,height=H,fill='white')
defs=E.SubElement(svg,'defs')
for name,col in [('arrow','#52728B'),('future','#B38A36')]:
    m=E.SubElement(defs,'marker',id=name,markerWidth='8',markerHeight='8',refX='7',refY='4',orient='auto')
    E.SubElement(m,'path',d='M0,0 L8,4 L0,8 Z',fill=col)
def rect(n):
    f,s=palette(n)
    kw=dict(x=n['x'],y=n['y'],width=n['w'],height=n['h'],fill=f,stroke=s,stroke_width=2.5 if n['id']=='C22' else 1)
    if n['kind'] in {'future','conflict'}:kw['stroke_dasharray']='7 4'
    se('rect',**kw)
    if n['id'] in bands:se('rect',x=n['x'],y=n['y'],width=n['w'],height=50,fill=heading_color(n['id']))
for n in N.values():
    if n['heading']:rect(n)
labels=[]
for e in edges:
    pts=route(e)
    kw=dict(points=' '.join(f'{x},{y}' for x,y in pts),fill='none',stroke='#B38A36' if e['kind']=='future' else '#52728B',stroke_width=1.8,marker_end='url(#future)' if e['kind']=='future' else 'url(#arrow)')
    if e['kind']!='data':kw['stroke_dasharray']='2 4' if e['kind']=='config' else '7 4'
    se('polyline',**kw)
    if e['label']:
        a,b=max(zip(pts,pts[1:]),key=lambda z:abs(z[0][0]-z[1][0])+abs(z[0][1]-z[1][1]))
        labels.append(((a[0]+b[0])/2,(a[1]+b[1])/2-8,e['label']))
for n in N.values():
    if not n['heading']:rect(n)
    ls=lines(n); lh=n['fs']*1.25
    assert len(ls)*lh<=n['h']-10, n['id']
    y=n['y']+n['fs']+12 if n['heading'] else n['y']+(n['h']-len(ls)*lh)/2+n['fs']
    first_count=len(textwrap.wrap(n['label'].split('\n')[0],width=max(12,int((n['w']-28)/(n['fs']*.55))),break_long_words=False))
    for idx,line in enumerate(ls):
        bold=n['bold'] or (idx<first_count and n['kind']!='title') or n['id']=='C22'
        t=se('text',x=n['x']+13,y=round(y,1),fill='#FFFFFF' if n['id'] in bands else ink,font_family='Arial',font_size=n['fs'],font_weight='bold' if bold else 'normal')
        t.text=line;y+=lh
for x,y,label in labels:
    width=len(label)*6.7+10
    se('rect',x=x-width/2,y=y-13,width=width,height=18,fill='white',rx=3)
    se('text',x=x,y=y,font_family='Arial',font_size=13,fill='#35556E',text_anchor='middle').text=label
E.ElementTree(svg).write(OUT/'VANTAGE_Intelligence_Layered_Architecture.preview.svg',encoding='utf-8',xml_declaration=True)

# Verify semantics against baseline XML rather than only against layout input.
from html.parser import HTMLParser
class Plain(HTMLParser):
    def __init__(self):super().__init__();self.s=''
    def handle_starttag(self,tag,attrs):
        if tag=='br':self.s+='\n'
    def handle_data(self,data):self.s+=data

def semantics(path):
    cells=E.parse(path).findall('.//mxCell'); out={}
    for c in cells:
        if c.get('vertex')!='1' and c.get('edge')!='1':continue
        value=c.get('value','')
        if 'html=1;' in c.get('style',''):
            p=Plain();p.feed(value);value=p.s
        out[c.get('id')]=(value,c.get('parent'),c.get('vertex'),c.get('edge'),c.get('source'),c.get('target'))
    return out
baseline=ROOT/'diagrams/archive/VANTAGE_Intelligence_Layered_Architecture.v1.1.drawio'
assert semantics(baseline)==semantics(OUT/'VANTAGE_Intelligence_Layered_Architecture.drawio'),'Semantic difference'
ns=list(N.values())
for i,a in enumerate(ns):
    if a['parent'] in N:
        p=N[a['parent']]
        assert p['x']<=a['x'] and p['y']<=a['y'] and a['x']+a['w']<=p['x']+p['w'] and a['y']+a['h']<=p['y']+p['h']
    for b in ns[i+1:]:
        if a['parent']==b['parent']:
            assert not(min(a['x']+a['w'],b['x']+b['w'])>max(a['x'],b['x']) and min(a['y']+a['h'],b['y']+b['h'])>max(a['y'],b['y'])),(a['id'],b['id'])
report={'baseline_sha256':hashlib.sha256(baseline.read_bytes()).hexdigest(),'vertices':len(N),'edges':len(edges),'checks':['Exact node/edge IDs, decoded labels, parents and endpoints match baseline','All diagram text retained','XML parsing','Text-height fit','Child containment','No sibling-box overlap'],'native_diagrams_net_render_verified':False}
(OUT/'layout-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
