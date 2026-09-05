from pathlib import Path
import urllib.request,re,base64
root=Path(__file__).parent
url='https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap'
req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
css=urllib.request.urlopen(req,timeout=20).read().decode()
for fonturl in set(re.findall(r'url\((https:[^)]+)\)',css)):
    data=urllib.request.urlopen(fonturl,timeout=20).read()
    mime='font/woff2' if '.woff2' in fonturl else 'font/ttf'
    css=css.replace(fonturl,'data:'+mime+';base64,'+base64.b64encode(data).decode())
(root/'embedded-font.css').write_text(css,encoding='utf-8')
print('Embedded font saved',len(css))
