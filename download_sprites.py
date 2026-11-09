import json, pathlib, urllib.request, hashlib
root=pathlib.Path(__file__).resolve().parent
entries=json.loads((root/'pokemon_catalog.json').read_text(encoding='utf-8'))['pokemon']
for p in entries:
 url=p['sprite']; target=root/'assets'/'sprites'/f"{p['dexNumber']}.png"
 target.parent.mkdir(parents=True,exist_ok=True)
 try:
  with urllib.request.urlopen(url,timeout=20) as r: content=r.read()
  if not content.startswith(b'\x89PNG\r\n\x1a\n'): raise ValueError('Arquivo não é PNG')
  target.write_bytes(content)
  print('OK',target.name,len(content),'bytes',hashlib.sha256(content).hexdigest())
 except Exception as e: print('FALHA',p['name'],e)
