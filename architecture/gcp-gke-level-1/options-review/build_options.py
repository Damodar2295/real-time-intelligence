from diagram_renderer import View, OUT, ET, TEAL
from pathlib import Path
import json
base=OUT.parent/'v4'
g=json.loads((base/'graph-v4.json').read_text())
v=View('Technical Level 1 | Options Review',3760,2060)
v.nodes=g['nodes'];v.edges=g['edges']
v.nodes['page-title']['title']='VANTAGE Intelligence | Technical Level 1 | Options Review'
v.nodes['page-subtitle']['body']='13 October 2026 • Proposed evaluation view • V4 preserved • No implementation or technology approval\nPage 1: retained Pub/Sub candidate topology. Page 2: handoff and windowing alternatives. Select one path per test configuration.'
v.nodes['gcp']['title']='LUMI | Internal Google Cloud Platform'
v.nodes['queue'].update(title='Pub/Sub • Candidate A',body='Current handoff proposal\nAlternatives on page 2',status_label='EVALUATE')
v.nodes['worker'].update(body='Concurrent calls • context\nWorker windowing retained',fs=19)
v.nodes['ingress']['body']='Source adaptation / event framing\nCall / session identity'
v.nodes['notes'].update(title='DECISIONS TO VALIDATE',body='Lumi service approval OPEN.\nOrdering / loss / recovery OPEN.\nWindow placement: see page 2.\nRuntime borders are not trust zones.',fs=19)
v.nodes['provider'].update(body='Audio / transcript contract OPEN\nProvider transcript coexistence OPEN',fs=18)
v.nodes['resolver']['body']='Evidence + threshold baseline\nThreshold policy under review'
v.nodes['telemetry']['body']='Latency • queue age • quality • cost\nInstrumentation required; not verified'
for k in ['state','sql','model','stt']:
 v.nodes[k]['status_label']='LUMI APPROVAL OPEN'
v.nodes['legend']['body']='Solid: baseline logical flow • Amber dashed: proposed integration • Dotted: configuration • Dash-dot: telemetry • Purple: test input\nPage 1 retains V4 endpoints; alternatives are on page 2, not concurrent deployed brokers. Product access, trust controls and state ownership remain OPEN.'
mx=ET.Element('mxfile',host='app.diagrams.net',type='device')
reports=[v.export(mx,'vantage-options-overview')]
w=View('Handoff & Windowing | Alternatives',2400,1680)
w.header('13 October 2026 • Evaluation choices, not approved topology • Both sources use the same selected processing path\nChoose one handoff per configuration. No dual publishing, source-specific broker, or automatic fallback implied.')
w.band('source-zone','SOURCE ADAPTERS',40,180,480,470)
w.box('live','Genesys source','Provider transcript events OR\naudio → acquisition → STT\nContract / coexistence OPEN',65,250,430,175,'external','source-zone',fs=21)
w.box('emulator','Transcript emulator','Separate TEST source\nSame transcript contract',65,465,430,130,'test','source-zone',fs=21)
w.box('ingress-option','Transcript ingress','Connection / source adaptation\nEvent framing • call identity\nPreserve revision / finality',600,335,410,200,'normal',fs=21)
w.band('handoff-options','HANDOFF ALTERNATIVES • CHOOSE ONE',1100,180,590,590)
w.box('candidate-a','A • Cloud Pub/Sub','Current proposal\nLumi approval + latency validation',1130,255,530,130,'future','handoff-options',fs=21)
w.nodes['candidate-a']['icon']='pubsub.svg'
w.box('candidate-b','B • Redis Streams','Proposed alternative\nHosting / Lumi approval OPEN\nConsumer and recovery policy OPEN',1130,420,530,175,'future','handoff-options',fs=21)
w.nodes['candidate-b']['icon']='neutral-service.svg'
w.box('choice-note','','A and B are mutually exclusive test choices.\nRedis messaging is distinct from context cache;\nshared instance not assumed.',1130,630,530,100,'title','handoff-options',fs=19)
w.box('processing','Conversation processing','Concurrent calls • bounded context\nPer-call ordering / ownership OPEN\nWindowing location: compare below',1810,335,540,200,'normal',fs=21)
w.box('detection','Existing detection & output','Selective methods → evidence resolution\nAcceptance / completion rules OPEN\nPublication and later activation retained',1810,620,540,160,'decision',fs=21)
w.link('live','ingress-option','Transcript updates','future',pts=[(550,337.5),(550,400)],refs='ADD-01')
w.link('emulator','ingress-option','Test input','test',pts=[(560,530),(560,480)],refs='V4 edge-4')
w.link('ingress-option','handoff-options','Selected handoff','future',refs='ADD-04')
w.link('handoff-options','processing','Selected consumer path','future',refs='ADD-04')
w.link('processing','detection','','data','bottom','top')
w.band('local-option','C • COLOCATED PROTOTYPE OPTION',40,850,720,350)
w.box('local-inner','Ingress → bounded local queue → processing','Inside one application process\nNot a shared cross-instance broker\nRestart loss, overload and call placement OPEN',65,925,670,210,'future','local-option',fs=22)
w.band('window-options','WINDOW ASSEMBLY • SEPARATE DECISION',800,850,850,350)
w.box('window-a','Retain V4: workers assemble windows','Ingress frames transcript events before handoff.',825,920,800,95,'normal','window-options',fs=21)
w.box('window-b','Team proposal: ingress assembles windows','Adds call-window state to ingress; evaluate lifecycle and delay.\nTransport framing is not detection microbatching.',825,1035,800,140,'future','window-options',fs=20)
w.band('gates','EVALUATION GATES',1690,850,660,350)
w.box('gate-list','','Actual payload and transcript revisions\nFreshness versus loss / recovery by scenario\nCall isolation • P95/P99 • quality • cost\nLumi service access and operating owner\nSame workload; document guarantee differences',1715,925,610,230,'title','gates',fs=21)
w.band('platform','LUMI & STORAGE • NO NEW PRODUCT APPROVAL',40,1250,2310,270)
w.box('platform-note','','Confirm Pub/Sub / Redis / model access and supported versions with Lumi. GKE remains target; no Cloud Run migration implied.\nChoose stores separately for call context, catalog/versioning, vectors, and accepted evidence. PostgreSQL direction retained provisionally.\nHistory writer, threshold policy, acceptable loss and security ownership remain decisions. No zero-latency or lossless guarantee.',70,1320,2250,165,'title','platform',fs=22)
w.box('legend','READING GUIDE','Amber dashed cards/links = proposed alternatives • Purple = test source • Containers describe choices, not deployed security zones.\nPage 1 preserves baseline dependencies; this page expands decision options without selecting technologies or changing V4.',40,1550,2310,105,'title',fs=21)
reports.append(w.export(mx,'vantage-options-evaluation'))
ET.indent(mx)
ET.ElementTree(mx).write(OUT/'vantage-technical-level-1-options-review.drawio',encoding='utf-8',xml_declaration=True)
(OUT/'validation.json').write_text(json.dumps({'pages':reports,'v4_modified':False,'native_editor_import':'NOT TESTED'},indent=2))
print(reports)
