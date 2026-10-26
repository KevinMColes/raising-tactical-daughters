from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,hashlib,fitz
r=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.images=[];self.h1=0;self.canonical=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id'])
  if t=='h1':self.h1+=1
  if t=='a':self.links.append(a.get('href',''))
  if t=='img':self.images.append(a)
  if t=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
files=['index.html','our-story/index.html','raising-her-ready/index.html','community/index.html','speaking/index.html']
for f in files:
 t=(r/f).read_text();p=Page();p.feed(t)
 assert p.h1==1,(f,'H1 count');assert len(p.ids)==len(set(p.ids)),(f,'duplicate IDs')
 route='/' if f=='index.html' else '/'+f.removesuffix('index.html')
 assert p.canonical==['https://raisingtacticaldaughters.com'+route]
 json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',t,re.S).group(1))
 for href in p.links:
  u=urlsplit(href)
  if u.scheme:assert u.scheme=='https',(f,href);continue
  target=r/u.path.lstrip('/') if u.path else r/f
  if target.is_dir():target=target/'index.html'
  assert target.is_file(),(f,'broken local link',href)
  if u.fragment:
   q=Page();q.feed(target.read_text());assert u.fragment in q.ids,(f,'missing fragment',href)
 for img in p.images:
  assert (r/img['src'].lstrip('/')).is_file(),(f,'missing image')
  assert img.get('alt') and img.get('width') and img.get('height'),(f,'image accessibility')
 assert 'Kevin Coles' not in t,(f,'missing middle initial')
 print('PASS',f)
t=(r/'raising-her-ready/index.html').read_text()
assert t.count('class="guide-stage"')==7
for phrase in ['THE FIRST', 'PLACEHOLDER']:assert phrase not in t
assert 'https://calendly.com/kevinmcoles/speaking' in (r/'speaking/index.html').read_text()
p=r/'downloads/raising-her-ready-field-guide.pdf';assert len(fitz.open(p))==22
assert hashlib.sha256(p.read_bytes()).hexdigest()=='1b890b5f68a20f165a3e470db8e14f56f70919bcdb2d2abf785afdc076be5c81'
assert (r/'CNAME').read_text().strip()=='raisingtacticaldaughters.com'
print('PASS guide sections, original redesigned PDF, Calendly, and domain')
