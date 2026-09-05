from pathlib import Path
p=Path(__file__).with_name('prototype-template.html')
s=p.read_text(encoding='utf-8')
def replace(old,new):
    global s
    assert old in s,old[:100]
    s=s.replace(old,new)
css='''
/* Home development bento */
.home .card:nth-child(2){background:var(--card);color:var(--text);border-color:var(--border)}
.home .card:nth-child(2):after{display:none}
.home .card:nth-child(2) p,.home .card:nth-child(2) .tag,.home .card:nth-child(2) .arrow{color:var(--muted)}
.bento-section{margin-top:12px}.bento-heading,.youtube-heading{font-size:20px;letter-spacing:-.6px;margin:0 0 14px;line-height:1.4}
.bento{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;grid-template-rows:144px 144px 164px}
.bento-tile{min-width:0;border:1px solid transparent;border-radius:22px;padding:16px;text-align:left;color:var(--text);position:relative;display:flex;flex-direction:column;align-items:flex-start;overflow:hidden}
.bento-tile:nth-child(1){grid-row:span 2;background:#ede3f7}.bento-tile:nth-child(2){background:#e2efe6}.bento-tile:nth-child(3){background:#f8e7d9}.bento-tile:nth-child(4){background:#f4e2ec}.bento-tile:nth-child(5){background:#ecebdd}
.bento-icon{width:30px;height:30px;margin-bottom:15px;color:var(--primary)}.bento-icon svg{width:100%;height:100%}
.bento-label{display:block;font-size:16px;font-weight:750;line-height:1.4;letter-spacing:-.3px;position:relative;z-index:1}.bento-label span{display:block}.bento-label .development{font-size:13px;font-weight:550;letter-spacing:0}
.bento-description{display:block;font-size:13px;color:var(--muted);line-height:1.6;margin-top:13px;max-width:125px}.bento-arrow{position:absolute;right:15px;bottom:12px;font-size:20px;color:var(--primary)}
.bento-orbit{width:94px;height:94px;margin-top:15px;align-self:center;color:var(--primary);opacity:.6}
.youtube-section{margin:12px 0}.youtube-sub{font-size:14px;color:var(--muted);line-height:1.7;margin:-6px 0 14px}
.youtube-link{display:flex;align-items:center;gap:13px;min-height:62px;padding:14px 16px;background:var(--card);border:1px solid var(--border);border-radius:16px;color:var(--text);text-decoration:none;margin-top:10px;font-size:14px;font-weight:650}.youtube-link>svg{width:25px;height:25px;color:var(--primary);flex-shrink:0}.youtube-link .external{margin-left:auto;color:var(--primary)}
.device[data-palette=Dark] .bento-tile:nth-child(1){background:#3b2d4f}.device[data-palette=Dark] .bento-tile:nth-child(2){background:#263c34}.device[data-palette=Dark] .bento-tile:nth-child(3){background:#49362d}.device[data-palette=Dark] .bento-tile:nth-child(4){background:#452d40}.device[data-palette=Dark] .bento-tile:nth-child(5){background:#3b3b2d}
.device[data-palette=Wireframe] .bento-tile{background:var(--soft);border-color:var(--border)}
.tablet .bento{grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:166px 166px}.tablet .bento-label{font-size:18px}.tablet .bento-label .development{font-size:14px}.tablet .bento-tile{padding:20px}.tablet .bento-orbit{margin-top:30px}
@media(max-width:740px){.tablet .bento{grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:144px 144px 164px}.tablet .bento-label{font-size:16px}.tablet .bento-tile{padding:16px}.tablet .bento-orbit{margin-top:15px}}
'''
replace('</head>','<style>'+css+'</style></head>')
replace("device.classList.toggle('reduced',reduced());","device.dataset.palette=st.wire?'Wireframe':st.theme==='System'?(osTheme.matches?'Dark':'Light'):st.theme;device.classList.toggle('reduced',reduced());")
replace("['categories','learn','Learn'],",'')
replace("C:'home',D:'categories'","C:'home',D:'home'")
icon='''function devIcon(name){const paths={brain:'<path d="M12 4v16M12 5C8-1 3 5 5 8c-5 2-3 8 0 8-1 5 5 7 7 3m0-14c4-6 9 0 7 3 5 2 3 8 0 8 1 5-5 7-7 3M5 8l3 2m11-2-3 2M5 16l3-2m11 2-3-2"/>',move:'<path d="m4 20 5-6 4 2 4-5M8 6l4 3 3-5m-3 5-3 5m4 2 6 4"/><circle cx="15" cy="3" r="2"/>',heart:'<path d="M20 5c-4-4-8 1-8 1S8 1 4 5c-5 5 8 15 8 15S25 10 20 5Z"/>',people:'<circle cx="8" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M2 21v-2a6 6 0 0 1 12 0v2m1-6a5 5 0 0 1 7 4v2"/>',spark:'<path d="m12 2 3 7 7 3-7 3-3 7-3-7-7-3 7-3Zm8 0v4m-2-2h4"/>'};return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths[name]}</svg>`;}
'''
replace('function item(it,i,s){',icon+'function item(it,i,s){')
branches='''if(type==='bento')return `<section class="bento-section" aria-labelledby="bento-heading"><h2 class="bento-heading" id="bento-heading">${esc(title)}</h2><div class="bento">${it.areas.map((area,n)=>`<button class="bento-tile" data-go="levels" data-development="${area.name}" aria-label="${area.name} development"><span class="bento-icon">${devIcon(area.icon)}</span><span class="bento-label"><span>${area.name}</span><span class="development">development</span></span>${n===0?`<span class="bento-description">${area.sub}</span><svg class="bento-orbit" viewBox="0 0 100 100" fill="none" aria-hidden="true"><circle cx="50" cy="50" r="30" stroke="currentColor" stroke-width="1.5"/><ellipse cx="50" cy="50" rx="43" ry="17" transform="rotate(-35 50 50)" stroke="currentColor" stroke-width="1.5"/><circle cx="50" cy="50" r="7" fill="currentColor"/><circle cx="22" cy="63" r="5" fill="currentColor"/><circle cx="75" cy="34" r="4" fill="currentColor"/></svg>`:''}<span class="bento-arrow" aria-hidden="true">↗</span></button>`).join('')}</div></section>`;
if(type==='youtube')return `<section class="youtube-section" aria-labelledby="youtube-heading"><h2 class="youtube-heading" id="youtube-heading">${esc(title)}</h2><p class="youtube-sub">Stories, little discoveries, and moments to share.</p>${[['Visit our channel',it.url],['Watch our videos',it.videos]].map(([label,url])=>`<a class="youtube-link" href="${esc(url)}" target="_blank" rel="noopener noreferrer" aria-label="${label} on YouTube (opens in a new tab)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="5"/><path d="m10 9 5 3-5 3Z" fill="currentColor" stroke="none"/></svg><span>${label}</span><span class="external" aria-hidden="true">↗</span></a>`).join('')}</section>`;
'''
replace("if(type==='art')return",branches+"if(type==='art')return")
replace("const next=build(s);","const shown=s.id==='levels'&&st.development?{...s,sub:st.development+' development'}:s;const next=build(shown);")
replace("if(b.dataset.go){let to=b.dataset.go;","if(b.dataset.go){if(b.dataset.development)st.development=b.dataset.development;let to=b.dataset.go;")
replace(".items>.card,.items>.row'",".items>.card,.items>.row,.bento-tile'")
p.write_text(s,encoding='utf-8')
print('Home prototype updated.')
