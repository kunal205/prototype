from pathlib import Path
import json
root=Path(__file__).parent
p=root/'build.py';s=p.read_text(encoding='utf-8')
s=s.replace("TOKENS={'Light'", "from journey_catalog import revise, FLOW\nSCREENS=revise(SCREENS)\n\nTOKENS={'Light'",1)
s=s.replace("['Home','Stories','Connect','Shop']","['Home','Stories','Community','Shop']")
s=s.replace("shell=shell.replace('__BOOK_DATA__',json.dumps(book_data))", "shell=shell.replace('__BOOK_DATA__',json.dumps(book_data))\n    shell=shell.replace('__JOURNEY_CSS__',(ROOT/'journey.css').read_text(encoding='utf-8')).replace('__JOURNEY_JS__',(ROOT/'journey.js').read_text(encoding='utf-8').replace('__FLOW_DATA__',json.dumps(FLOW)))\n    (ROOT/'activity-catalog.json').write_text(json.dumps(FLOW,indent=2),encoding='utf-8')")
p.write_text(s,encoding='utf-8')
p=root/'prototype-template.html';s=p.read_text(encoding='utf-8')
s=s.replace('</head>','<style>__JOURNEY_CSS__</style></head>',1)
s=s.replace("['community','community','Connect']","['community','community','Community']")
start=s.index('let touchStart=null,pinchStart=0;')
end=s.index("$('#wire').onclick",start)
s=s[:start]+s[end:]
s=s.replace('window.LL={screens,books,st,go,render,theme};', '__JOURNEY_JS__\nwindow.LL={screens,books,st,go,render,theme,flow,saved,completeActivity};')
s=s.replace(":'home',{initial:true});",":'welcome',{initial:true});")
s=s.replace('Product → request → review ↗','Playing kits → demo payment ↗')
s=s.replace('Pick an activity, move through its steps, and watch your plant grow. Skip and Continue respond immediately.','Choose an activity and try Guidance or Individual mode. Completion grows your plant, then leads to optional feedback and your growth chart.')
s=s.replace('Illustrative content and progress. Forms save only in this browser session. Video and server submissions are represented; nothing is sent.','Sample content. Progress, feedback, wishlist and demo submissions save on this device. Login, admin approval and payments are simulated. YouTube playback needs internet.')
p.write_text(s,encoding='utf-8')
(root/'youtube-videos.json').write_text(json.dumps([dict(title='Watch together · Video 1',url='https://www.youtube.com/watch?v=r_kmNk3bcPQ'),dict(title='Watch together · Video 2',url='https://www.youtube.com/watch?v=NDFqrbv6hkg')],indent=2),encoding='utf-8')
