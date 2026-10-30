from pathlib import Path
import json
from topics import items
starts=[0,4,13,24,34];durations=[4,9,11,10,8]
def tc(ms):
 h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000);return f'{h:02}:{m:02}:{s:02},{ms:03}'
for item in items:
 sections=[];caps=[]
 for q,(phrases,start,d) in enumerate(zip(item.pop('lines'),starts,durations)):
  phrases=[part for p in phrases for part in ([p] if len(p.split())<=8 else [' '.join(p.split()[:len(p.split())//2]),' '.join(p.split()[len(p.split())//2:])])]
  window=3.3 if q==0 else d-.7;at=.12 if q==0 else .25;words=sum(len(p.split()) for p in phrases);beats=[]
  for phrase in phrases:
   pd=window*len(phrase.split())/words;beats.append(dict(text=phrase,at=at,duration=pd));caps.append(dict(text=phrase,startMs=round((start+at)*1000),endMs=round((start+at+pd)*1000),timestampMs=None,confidence=None));at+=pd
  sections.append(dict(id=q,start=start,duration=d,frames=d*30,text=' '.join(phrases),speechText=' '.join(phrases),beats=beats))
 item.update(sections=sections,captions=caps,duration=42,frames=1260,voiceStatus='none_user_will_dub',timing='Script-based editorial mouth and caption cues, not recorded audio lip sync',illustration='Original conceptual illustration; not study footage or exact CAD/data')
 Path(f'out/{item["slug"]}-dubbing.txt').write_text(item['title']+'\n\n'+'\n\n'.join(f'{s["start"]:02}–{s["start"]+s["duration"]:02} detik\n{s["text"]}' for s in sections)+'\n')
 Path(f'out/{item["slug"]}.srt').write_text('\n\n'.join(f'{i+1}\n{tc(c["startMs"])} --> {tc(c["endMs"])}\n{c["text"]}' for i,c in enumerate(caps))+'\n')
Path('public/batch.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
print([(i['id'],sum(len(s['text'].split()) for s in i['sections'])) for i in items])
