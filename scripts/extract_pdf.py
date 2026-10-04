import fitz,re,json,time
from pathlib import Path
import argparse
parser=argparse.ArgumentParser(description='Extract this EMV 3DS PDF into Markdown and PNG.')
parser.add_argument('pdf',type=Path);parser.add_argument('output',type=Path)
args=parser.parse_args();out=args.output
if out.exists() and any(out.iterdir()):raise SystemExit('Output must be a new or empty directory.')
for sub in ['en/pages','en/chapters','assets/images','data']:(out/sub).mkdir(parents=True,exist_ok=True)
doc=fitz.open(args.pdf);toc=doc.get_toc()
major=[t for t in toc if t[0]==1];images=[];pages=[];tablescount=0;start=time.time()
def clean(s):
 return s.replace('\u00ad','').replace('\uf0b7','•').strip()
def mdcell(s):
 return clean(s or '').replace('|','&#124;').replace('\n','<br>')
def tablemd(t):
 rows=t.extract()
 if not rows:return ''
 # Preserve all columns and every cell, including empty/merged cells.
 rows=[[mdcell(c) for c in row] for row in rows]
 return '\n'.join(['| '+' | '.join(rows[0])+' |','| '+' | '.join(['---']*len(rows[0]))+' |']+['| '+' | '.join(r)+' |' for r in rows[1:]])
for i,p in enumerate(doc,1):
 h=p.rect.height;w=p.rect.width;area=fitz.Rect(69,78,w-65,h-78)
 blocks=p.get_text('dict',clip=area)['blocks'];events=[];tableboxes=[];tabledata=[]
 special={46:(190,103,402,257),369:(226,166,605,490),370:(70,103,765,425)}
 figbox=fitz.Rect(special[i]) if i in special else None
 if i<398:
  found=p.find_tables(clip=area,strategy='lines_strict')
  for ti,t in enumerate(found.tables):
   if t.row_count<2 or t.col_count<2:continue
   if figbox and figbox.intersects(fitz.Rect(t.bbox)):continue
   tableboxes.append(fitz.Rect(t.bbox));tabledata.append({'bbox':list(t.bbox),'rows':t.extract()});events.append((t.bbox[1],t.bbox[0],tablemd(t)));tablescount+=1
 for b in blocks:
  if b['type']!=0:continue
  buf=[];bufpos=None
  for line in b['lines']:
   box=fitz.Rect(line['bbox'])
   if figbox and figbox.contains(box.tl):continue
   if any(r.contains(box.tl+fitz.Point(1,1)) or (r & box).get_area()/max(box.get_area(),1)>.65 for r in tableboxes):continue
   spans=line['spans'];text=clean(''.join(s['text'] for s in spans));
   if not text:continue
   size=max(s['size'] for s in spans);bold=any('Bold' in s['font'] for s in spans)
   if size>=15 or (bold and re.match(r'^(?:\d+(?:\.\d+)*|[A-D](?:\.\d+)*)\s+',text)):
    if buf:events.append((bufpos[0],bufpos[1],' '.join(buf)));buf=[]
    prefix='## ' if size>=18 else '### '
    events.append((box.y0,box.x0,prefix+text))
   else:
    if not buf:bufpos=(box.y0,box.x0)
    buf.append(text)
  if buf:
   s=' '.join(buf);s=re.sub(r'\s+([.,;:])',r'\1',s)
   if s.startswith('• '):s='- '+s[2:]
   events.append((bufpos[0],bufpos[1],s))
 infos=[{'bbox':list(figbox)}] if figbox else p.get_image_info()
 for j,info in enumerate(infos,1):
  r=fitz.Rect(info['bbox'])
  if r.width<20 or r.height<20:continue
  caption=''
  candidates=[]
  for b in blocks:
   if b['type']!=0:continue
   s=clean(' '.join(''.join(x['text'] for x in l['spans']) for l in b['lines']))
   if re.match(r'^Figure [0-9A-D]+\.\d+[: ]',s) and b['bbox'][3]<=r.y0+8:candidates.append((r.y0-b['bbox'][3],s))
  if candidates:caption=min(candidates)[1]
  match=re.match(r'^Figure ([0-9A-D]+\.\d+)[: ]',caption);ident='figure-'+match[1].replace('.','-') if match else f'page-{i:03}-image-{j:02}'
  name=ident+'.png'
  if (out/'assets/images'/name).exists():name=ident+f'-{j}.png'
  pix=p.get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=r,alpha=False);pix.save(out/'assets/images'/name)
  images.append({'page':i,'file':'assets/images/'+name,'caption_en':caption or f'Image on PDF page {i}','bbox':list(r),'width':pix.width,'height':pix.height})
  events.append((r.y0,r.x0,f'![{caption or "Image on PDF page "+str(i)}](../../assets/images/{name})'))
 events.sort(key=lambda e:(round(e[0]/3),e[1]))
 body='\n\n'.join(e[2] for e in events)
 title=f'PDF page {i}'
 nav=f'[Contents](../../index.md) · [Previous](./{i-1:03}.md)' if i>1 else '[Contents](../../index.md)'
 if i<len(doc):nav+=f' · [Next](./{i+1:03}.md)'
 md=f'---\nlayout: default\ntitle: "{title}"\nlang: en\n---\n\n# {title}\n\n> English source extraction. Translation status is shown on the home page. Tables are reconstructed from the PDF; this is not an official EMVCo edition.\n\n{nav}\n\n{body}\n\n---\n\n{nav}\n'
 (out/f'en/pages/{i:03}.md').write_text(md)
 pages.append({'page':i,'width':w,'height':h,'body':body,'tables':tabledata})
 if i%50==0:print(f'{i}/410 pages extracted; {len(images)} images; {tablescount} tables',flush=True)
json.dump(pages,open(out/'data/source-pages.json','w'),ensure_ascii=False,indent=2)
json.dump(images,open(out/'data/images.json','w'),ensure_ascii=False,indent=2)
json.dump(toc,open(out/'data/source-toc.json','w'),ensure_ascii=False,indent=2)
# Group source pages into chapter files; each page has a stable anchor.
chapters=[('front','Front matter',1,16),('01','Introduction',17,34),('02','EMV 3-D Secure Overview',35,48),('03','Authentication Flow Requirements',49,93),('04','User Interface Templates, Requirements and Guidelines',94,144),('05','Message Handling Requirements',145,171),('06','Security Requirements',172,184),('a','3-D Secure Data Elements',185,376),('b','Message Format',377,393),('c','Generate ECC Key Pair',394,395),('d','Approved Transport Layer Security Versions',396,397),('requirements','Requirements index',398,410)]
for ident,title,a,b in chapters:
 chunks=[]
 for n in range(a,b+1):
  body=pages[n-1]['body'];body=body.replace('../../assets/images/','../../assets/images/')
  chunks.append(f'<a id="page-{n}"></a>\n\n## PDF page {n}\n\n'+body)
 text=f'---\nlayout: default\ntitle: "{title}"\nlang: en\n---\n\n# {title}\n\n[Home](../../index.md)\n\n'+ '\n\n---\n\n'.join(chunks)
 (out/f'en/chapters/{ident}.md').write_text(text)
json.dump(chapters,open(out/'data/chapters.json','w'),ensure_ascii=False,indent=2)
print(json.dumps({'pages':len(pages),'images':len(images),'tables':tablescount,'seconds':round(time.time()-start,1)}))
