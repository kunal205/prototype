/* Connected journey, using the sample content approved for this prototype. */
const flow=__FLOW_DATA__;
const STORE='little-legacy-prototype-v3';
let saved={completions:[],wishlist:[],community:[],orders:[],child:'Maya'};
try{const data=JSON.parse(localStorage.getItem(STORE)||'null');if(data&&Array.isArray(data.completions))saved={...saved,...data};}catch{}
function persist(){try{localStorage.setItem(STORE,JSON.stringify(saved));}catch{announce('Storage is unavailable. Your changes remain available during this session.');}}
Object.assign(st,{child:saved.child,development:'Cognitive',level:1,activityId:flow.activities[0].id,mode:'Guidance',run:null,rating:null,wishlistOnly:false,filtersOpen:true,pages:{},kitId:'discovery',communityText:'',attachment:null,shownGrowth:null});
const activity=()=>flow.activities.find(a=>a.id===st.activityId)||flow.activities[0];
const kit=()=>flow.kits.find(k=>k.id===st.kitId)||flow.kits[0];
const completed=()=>saved.completions.filter(c=>c.child===st.child);
const currentCompletion=()=>saved.completions.find(c=>c.id===st.run?.completionId);
const actCard=a=>({type:'card',title:a.title,sub:`${a.seconds/60} minutes · ${a.description}`,tag:`${a.category.toUpperCase()} · LEVEL ${a.level}`,to:'@activity-'+a.id});
const noteItem=title=>({type:'note',title});
const actionItem=(label,to,secondary=false)=>({label,to,secondary});
const rowItem=(title,to,sub='')=>({type:'row',title,to,sub});
const uid=()=>crypto.randomUUID?crypto.randomUUID():Date.now()+'-'+Math.random();
st.perspectives={};

function perspectiveSvg(book,page,view=0){
 const frames=['0 0 360 330','80 80 210 193','10 95 210 193'];
 return storyScene(book,page).replace('viewBox="0 0 360 330"',`viewBox="${frames[view]}"`).replace('Sample story illustration,',`${['Full view','Closer view','Alternate view'][view]} of sample story illustration,`);
}
function storyPageImage(book,page,readerId){
 const selected=st.perspectives[readerId+'-'+page]||0;
 return `<div class="story-image-frame" data-image-page="${page}"><div class="story-main-image">${perspectiveSvg(book,page,selected)}</div><div class="perspective-stack" role="group" aria-label="Alternate views of image ${page+1}" ${(st.pages[readerId]||0)!==page?'hidden':''}>${['Full view','Closer view','Alternate view'].map((label,v)=>`<button type="button" class="perspective-thumb" data-perspective="${v}" data-perspective-page="${page}" data-perspective-book="${book.id}" aria-label="${label} of image ${page+1}" aria-pressed="${selected===v}">${perspectiveSvg(book,page,v)}<span class="a11y-only">${label}</span></button>`).join('')}<span class="perspective-count" aria-hidden="true">3 views</span></div></div>`;
}

function scene(category,variant=0){
 const colors=['#DCD2EE','#D4E9DC','#F5DCCB','#EED6E4','#E5E3C7'];
 const ci=Math.max(0,['Cognitive','Physical','Emotional','Social','Creative'].indexOf(category));
 const motif=[`<rect x="70" y="100" width="70" height="70" rx="16" fill="#8665B1"/><circle cx="203" cy="130" r="40" fill="#E8A06F"/><path d="m280 92 40 75h-80Z" fill="#6F9E83"/>`,
 `<path d="M65 163Q120 83 177 149T305 117" stroke="#6F9E83" stroke-width="12" fill="none" stroke-linecap="round"/><circle cx="167" cy="75" r="26" fill="#8665B1"/><circle cx="284" cy="161" r="26" fill="#E8A06F"/>`,
 `<path d="M180 164s-87-47-64-82c24-35 64 2 64 2s40-37 64-2c23 35-64 82-64 82Z" fill="#B984A4"/><path d="M164 107q16 24 32 0" stroke="#fff" stroke-width="5" fill="none"/>`,
 `<circle cx="126" cy="87" r="26" fill="#8665B1"/><circle cx="236" cy="87" r="26" fill="#6F9E83"/><path d="M87 168q0-85 78 0m32 0q0-85 78 0" stroke="#B984A4" stroke-width="13" stroke-linecap="round" fill="none"/>`,
 `<path d="m93 163 22-87 27 16-45 74Z" fill="#8665B1"/><path d="m211 58 12 35 36 2-28 24 9 36-30-20-31 20 10-36-28-24 37-2Z" fill="#E8A06F"/><circle cx="280" cy="163" r="22" fill="#6F9E83"/>`][ci];
 return `<svg viewBox="0 0 360 220" role="img" aria-label="Sample ${esc(category)} illustration ${variant+1}"><rect width="360" height="220" rx="24" fill="${colors[ci]}"/><circle cx="${65+variant*60}" cy="43" r="18" fill="#fff" opacity=".5"/><path d="M0 199q90-45 180-2t180-15v38H0Z" fill="#fff" opacity=".3"/><g transform="translate(${variant*4-4} ${variant*3})">${motif}</g><circle cx="310" cy="42" r="5" fill="#fff"/><circle cx="45" cy="99" r="4" fill="#fff"/></svg>`;
}
function storyScene(book,page){
 const skies=['#E8DEF3','#DCECE4','#E8E5F1'],sun=['#EFB974','#E4B5B9','#BBB3D7'];
 return `<svg viewBox="0 0 360 330" role="img" aria-label="Sample story illustration, page ${page+1} of 3"><rect width="360" height="330" rx="22" fill="${skies[page]}"/><circle cx="${75+page*93}" cy="70" r="30" fill="${sun[page]}"/><path d="M0 235Q90 165 180 225T360 196V330H0Z" fill="#99B9A1"/><path d="M0 278Q170 185 360 270V330H0Z" fill="#739A81"/><path d="M181 269V${173-page*29}" stroke="#4C785C" stroke-width="8" stroke-linecap="round"/><path d="M179 226c-50 0-66-20-63-50 45 0 63 17 63 50Z" fill="#496F54"/><path d="M184 199c0-41 22-59 53-55 0 34-17 55-53 55Z" fill="#5A8966"/>${page>0?'<path d="M185 246c43 0 58-19 55-44-37 0-55 16-55 44Z" fill="#3D694D"/>':''}${page===2?'<circle cx="181" cy="112" r="26" fill="#E7A8B4"/><circle cx="181" cy="112" r="10" fill="#F3D58C"/>':''}<path d="M36 123q13-13 26 0m0 0q13-13 26 0" fill="none" stroke="#8D7C9C" stroke-width="3"/><text x="20" y="310" font-size="10" fill="#fff" font-family="sans-serif">SAMPLE STORY ART · ${esc(book.category.toUpperCase())}</text></svg>`;
}
function plantSvg(stage){
 const top=170-stage*21,minY=Math.min(0,top-30);
 return `<svg viewBox="0 ${minY} 300 ${240-minY}" role="img" aria-label="Plant growth stage ${stage}"><circle cx="150" cy="${108+minY/2}" r="85" fill="var(--soft)"/><path d="M111 182h78l-13 44h-52Z" fill="var(--primary)" opacity=".4"/><g class="new-growth">${stage?`<path d="M150 185V${top}" stroke="var(--green)" stroke-width="6" stroke-linecap="round"/>`:''}${Array.from({length:stage},(_,i)=>{const y=172-i*21,sign=i%2?-1:1;return `<path d="M150 ${y} C150 ${y-24} ${150+sign*20} ${y-35} ${150+sign*44} ${y-35} C${150+sign*44} ${y-12} ${150+sign*26} ${y} 150 ${y}Z" fill="var(--green)" opacity="${.62+(i%3)*.12}"/>`;}).join('')}${stage===0?'<ellipse cx="150" cy="176" rx="9" ry="6" fill="var(--green)"/>':''}</g><rect x="105" y="180" width="90" height="12" rx="6" fill="var(--primary)"/></svg>`;
}
function prepareJourney(id){
 const s=byId[id],a=activity();if(!s)return;
 if(id==='home')s.items[0]=rowItem(st.child+' · Child profile ⌄','children');
 if(id==='levels'){s.title=st.development+' development';s.sub='Choose any level. Each has three activities.';}
 if(id==='activities'){s.title=st.development+' · Level '+st.level;s.sub='Choose one of your three activities.';s.items=flow.activities.filter(x=>x.category===st.development&&x.level===st.level).map(actCard);}
 if(id==='activity'){s.title=a.title;s.sub=`${a.category} development · Level ${a.level} · ${a.seconds/60} minutes`;s.items=[{type:'activity-image',title:a.category},noteItem(a.description),{type:'card',title:'What you’ll need',sub:a.materials},noteItem('Stay with your child. Use age-appropriate materials and a clear play space.'),{type:'video',title:'Activity video',video:a.video},{type:'mode',title:'Choose your mode'}];}
 if(['steps','step-2','step-3'].includes(id)){const n=['steps','step-2','step-3'].indexOf(id);s.title=['Explore together','Try the next little step','Celebrate your discovery'][n];s.sub=`Step ${n+1} of 3 · ${a.title}`;s.items=[{type:'activity-image',title:a.category,variant:n},noteItem(a.steps[n])];}
 if(id==='individual'){s.title=a.title;s.sub=`Individual mode · Level ${a.level} · ${a.seconds/60} minutes`;s.items=[{type:'activity-image',title:a.category},noteItem('Explore at your child’s pace. Pause whenever you need to.'),{type:'timer',title:formatTime(st.timer)},rowItem(st.paused?'Resume timer':'Pause timer','@pause')];}
 if(id==='celebration')s.sub=`${a.title} complete · ${completed().length} growth ${completed().length===1?'stage':'stages'}`;
 if(id==='feedback')s.sub=`Overall, how satisfied were you with ${a.title}?`;
 if(id==='progress'){s.sub=st.child+'’s learning garden';s.items=[{type:'growth-chart',title:'Your activity growth'},{type:'card',title:'Your Level Garden',sub:`${completed().length} completed activities · ${completed().length} growth stages`},noteItem(`More to try · ${st.development} development · Level ${st.level}`),...flow.activities.filter(x=>x.category===st.development&&x.level===st.level).map(actCard),rowItem('View activity history','history')];}
 if(id==='history')s.items=completed().length?completed().slice().reverse().map(c=>({type:'card',title:c.title,sub:`${c.category} · Level ${c.level} · ${new Date(c.at).toLocaleDateString()}`,to:'@history-'+c.id,tag:c.mode+' MODE'})):[noteItem('Your first completed activity will appear here.')];
 if(id==='history-detail'){const c=saved.completions.find(c=>c.id===st.historyId)||completed().at(-1);s.title=c?.title||'Your activity history';s.items=c?[noteItem(`${c.category} development · Level ${c.level} · ${c.mode} mode`),noteItem('Completed '+new Date(c.at).toLocaleString()),{type:'card',title:'Your satisfaction',sub:c.feedback?.rating||'Feedback skipped'},{type:'card',title:'Your comment',sub:c.feedback?.comment||'No comment added.'}]:[noteItem('Complete an activity to start your history.')];}
 if(id==='product'){s.title=kit().title;s.sub='Playing kit · Demo price';s.items=[{type:'art',title:'product'},{type:'card',title:'Inside the kit',sub:kit().description},noteItem('₹'+kit().price+' · Demo price')];}
 if(id==='checkout'){s.items[1]={type:'card',title:kit().title,sub:'₹'+kit().price+' · Demo total'};s.actions[0].label='Simulate payment · ₹'+kit().price;}
 if(id==='notifications'){s.items=saved.community.filter(m=>m.status==='Approved').map(m=>({type:'card',title:'Your community post was approved',sub:'Demo notification · Your post is visible in the community.',to:'community',tag:'COMMUNITY UPDATE'}));if(!s.items.length)s.items=[noteItem('Community review updates will appear here.')];if(saved.community.some(m=>m.status==='Approved'))s.items.push({type:'card',title:'Email preview',sub:'Your community post has been approved and is now visible. Thank you for sharing! This is a preview; no email was sent.'});}
}
const oldItem=item;
item=function(it,i,s){
 if(it.type==='activity-image')return `<div class="activity-scene">${scene(it.title,it.variant||0)}</div>`;
 if(it.type==='video')return `<section class="video-block"><h2>${esc(it.title)}</h2><div class="embed-slot" data-video="${it.video}"><button class="video-start" data-load-video="${it.video}" aria-label="Play ${esc(it.title)}"><span class="play-circle">▶</span><span>Play on this page</span></button></div><a href="https://www.youtube.com/watch?v=${it.video}" target="_blank" rel="noopener noreferrer">Open video on YouTube ↗</a><small>Internet required. If playback is unavailable here, open YouTube.</small></section>`;
 if(it.type==='mode')return `<fieldset class="mode-picker"><legend>Choose your mode</legend>${['Guidance','Individual'].map(m=>`<button data-mode="${m}" aria-pressed="${st.mode===m}" class="${st.mode===m?'selected':''}"><strong>${m}</strong><span>${m==='Guidance'?'Three steps to follow together':'A timer to play at your own pace'}</span></button>`).join('')}</fieldset>`;
 if(it.type==='satisfaction')return `<fieldset class="satisfaction"><legend>Choose your satisfaction level</legend>${it.options.map((t,n)=>`<label><input type="radio" name="satisfaction" value="${esc(t)}" ${st.rating===t?'checked':''}><span>${esc(t)}</span></label>`).join('')}</fieldset>`;
 if(it.type==='growth-plant'){const n=completed().length;return `<div class="garden-art">${plantSvg(n)}</div><div class="growth-badge">${n} completed ${n===1?'activity':'activities'} · ${n} growth ${n===1?'stage':'stages'}</div><p class="note garden-note">One new leaf for every little discovery.</p>`;}
 if(it.type==='growth-chart'){const all=completed(),cs=all.slice(-8),n=cs.length,pts=cs.map((c,i)=>[25+i*(250/Math.max(1,n-1)),140-(i+1)*115/Math.max(n,1)]);return `<div class="graph"><h2>${esc(st.child)}’s activity growth</h2><div class="graph-label">${all.length} completed activities. Each completion adds one growth stage.<br>${all.length>8?'Showing the latest 8 completions.':'Tap a point to see the activity.'}</div><svg viewBox="0 0 300 170" role="img" aria-label="${all.length} activities completed"><path d="M25 25V145H285M25 85H285M25 25H285" fill="none" stroke="var(--border)"/><path class="line" d="M25 145 ${pts.map(([x,y])=>`L${x} ${y}`).join(' ')}" stroke="var(--primary)" stroke-width="3" fill="none"/>${pts.map(([x,y],i)=>`<circle class="point" cx="${x}" cy="${y}" r="5" fill="var(--primary)"/><circle tabindex="0" role="button" aria-label="${esc(cs[i].title)}" data-history-id="${cs[i].id}" cx="${x}" cy="${y}" r="20" fill="transparent"/><text x="${x}" y="163" text-anchor="middle" font-size="10" fill="var(--muted)">${all.length-n+i+1}</text>`).join('')}</svg>${n?'':'<p class="note">Complete your first activity to grow your garden.</p>'}</div>`;}
 if(it.type==='story-tools')return `<div class="story-tools"><button class="secondary" data-wishlist-filter aria-pressed="${st.wishlistOnly}">♡ Wishlist (${saved.wishlist.length})</button><button class="secondary" data-filter-toggle aria-expanded="${st.filtersOpen}">☷ Filter</button></div>`;
 if(it.type==='story-categories')return `<div ${st.filtersOpen?'':'hidden'} class="filter-panel">${oldItem(it,i,s)}</div>`;
 if(it.type==='book-grid'){const list=books.filter(b=>(st.storyCategory==='All'||b.category===st.storyCategory)&&(!st.wishlistOnly||saved.wishlist.includes(b.id)));return `<section class="story-shelf"><div class="shelf-heading"><h2>${st.wishlistOnly?'Your wishlist':'Our story shelf'}</h2><span id="book-count">${list.length} stories</span></div><div class="book-grid">${list.map(b=>`<article class="book-cell"><button class="book-tile" data-go="${b.detailId}" data-book="${b.id}" data-book-category="${esc(b.category)}" aria-label="Open ${esc(b.title)}"><span class="book-cover" data-cover="${b.id}">${b.cover}</span><span class="book-title">${esc(b.title)}</span></button><button class="wish-heart" data-wish="${b.id}" aria-label="${saved.wishlist.includes(b.id)?'Remove from':'Add to'} wishlist: ${esc(b.title)}" aria-pressed="${saved.wishlist.includes(b.id)}">${saved.wishlist.includes(b.id)?'♥':'♡'}</button></article>`).join('')}</div>${list.length?'':'<p class="note">No stories here yet. Save a story with its heart button or change the filter.</p>'}</section>`;}
 if(it.type==='book-intro'){const b=it.book;return oldItem(it,i,s)+`<button class="secondary" data-wish="${b.id}" aria-pressed="${saved.wishlist.includes(b.id)}">${saved.wishlist.includes(b.id)?'♥ Saved to wishlist':'♡ Add to wishlist'}</button>`;}
 if(it.type==='carousel'){const b=booksById[it.bookId],chapter=b.chapterRoutes.indexOf(s.id),page=st.pages[s.id]||0;return `<div class="reader-carousel" tabindex="0" aria-label="Story pages; swipe or use page buttons" data-reader="${s.id}">${[0,1,2].map(p=>`<article class="story-page">${storyPageImage(b,p,s.id)}<p>${esc([b.copy[chapter],'Together, they noticed something new. Every little discovery made the world feel a little bigger.','They paused to enjoy the moment. A small step, shared together, was something worth remembering.'][p])}</p><span class="page-mark">PAGE ${p+1} OF 3</span></article>`).join('')}<article class="chapter-end"><span class="end-spark">✧</span><h2>${chapter===2?'You finished the story!':'A little pause between chapters.'}</h2><p>${chapter===2?'A whole little world, explored together.':'Ready to discover what happens next?'}</p>${chapter<2?`<button class="primary" data-go="${b.chapterRoutes[chapter+1]}">Go to next chapter</button>`:''}<button class="secondary" data-go="${b.detailId}">Go back to chapters</button>${chapter===2?'<button class="secondary" data-go="stories">Back to stories</button>':''}</article></div><div class="reader-controls"><button class="secondary" data-page-delta="-1" ${page===0?'disabled':''} aria-label="Previous story page">←</button><span class="reader-position" aria-live="polite">${page<3?`Page ${page+1} of 3`:'Chapter complete'}</span><button class="secondary" data-page-delta="1" ${page===3?'disabled':''} aria-label="Next story page">→</button></div>`;}
 if(it.type==='community-feed')return `<div class="community-feed"><div class="day-label">Today</div><article class="message-bubble"><div class="message-media">${scene('Social')}</div><strong>Little Legacy team</strong><p>Small wins deserve a little celebration. What did your little one discover today?</p><time>9:15 AM</time></article><article class="message-bubble"><div class="message-media">${scene('Creative',1)}</div><strong>Little Legacy team</strong><p>A few crayons and a shared story can turn an ordinary afternoon into an adventure.</p><time>10:30 AM</time></article>${saved.community.map(m=>`<article class="message-bubble mine">${m.media?`<div class="attachment-label">▧ ${esc(m.media)}</div>`:''}<strong>You</strong><p>${esc(m.text)}</p><small>${m.status==='Approved'?'✓ Approved · Visible in the community':'◷ Waiting for admin review'}</small>${m.status==='Pending'?`<button class="demo-review" data-approve-post="${m.id}">Preview admin approval</button>`:''}</article>`).join('')}</div>`;
 if(it.type==='kit-list')return `<div class="kit-list">${flow.kits.map(k=>`<button class="card kit-card" data-go="@kit-${k.id}"><div class="kit-art">${arts.product}</div><span class="tag">PLAYING KIT</span><h2>${esc(k.title)}</h2><p>${esc(k.description)}</p><strong class="kit-price">₹${k.price} <small>Demo price</small></strong></button>`).join('')}</div>`;
 return oldItem(it,i,s);
};
const oldBuild=build;
build=function(s,asSheet=false){const el=oldBuild(s,asSheet);el.querySelectorAll('button').forEach(b=>b.type='button');
 if(s.id!=='home')el.querySelector('.right-icons')?.remove();
 if(s.id==='community'){const composer=document.createElement('div');composer.className='community-composer';composer.innerHTML=`${st.attachment?`<div class="attachment-label">${esc(st.attachment.name)} <button data-remove-attachment aria-label="Remove attachment">×</button></div>`:''}<div class="compose-row"><button class="icon-btn" data-community-media aria-label="Add community media">＋</button><textarea rows="1" placeholder="Message the community" aria-label="Message the community">${esc(st.communityText)}</textarea><button class="icon-btn send-message" data-community-send aria-label="Review community message">➤</button></div>`;el.insertBefore(composer,el.querySelector('.tabs'));}
 return el;};
const oldRender=render;
render=function(id,opts={}){
 prepareJourney(id);st.seenCelebration=true;oldRender(id,opts);
 const current=viewport.querySelector('.screen:last-of-type');
 if(id==='individual'){
  if(st.run?.done){current.querySelector('.actions').innerHTML='<button class="primary" data-go="progress">View completed activity growth</button>';return;}
  if(!st.run){st.run={id:uid(),activityId:activity().id,mode:'Individual',remaining:activity().seconds,done:false};st.timer=st.run.remaining;st.paused=false;}
  const timer=current?.querySelector('#timer-value');if(timer)timer.textContent=formatTime(st.timer);
  tick=setInterval(()=>{if(st.id!=='individual'||st.paused||!st.run||st.run.done)return;st.timer=Math.max(0,st.timer-1);st.run.remaining=st.timer;const t=current.querySelector('#timer-value');if(t)t.textContent=formatTime(st.timer);if(st.timer===0)completeActivity();},1000);
 }
 if(id==='celebration'&&st.run?.completionId&&st.shownGrowth!==st.run.completionId){st.shownGrowth=st.run.completionId;if(!reduced())animate(current.querySelector('.new-growth'),[{opacity:.1,transform:'scaleY(.3)'},{opacity:1,transform:'scaleY(1)'}],{duration:900,easing:'cubic-bezier(.2,.8,.2,1)'});}
 if(byId[id]?.kind==='reader'){
  const car=current.querySelector('.reader-carousel');const sync=()=>{const n=Math.max(0,Math.min(3,Math.round(car.scrollLeft/car.clientWidth)));st.pages[id]=n;car.querySelectorAll('.story-page,.chapter-end').forEach((slide,i)=>{slide.inert=i!==n;const stack=slide.querySelector('.perspective-stack');if(stack)stack.hidden=i!==n;});current.querySelector('.reader-position').textContent=n<3?`Page ${n+1} of 3`:'Chapter complete';current.querySelector('[data-page-delta="-1"]').disabled=n===0;current.querySelector('[data-page-delta="1"]').disabled=n===3;};
  car.scrollLeft=(st.pages[id]||0)*car.clientWidth;sync();car.addEventListener('scroll',sync,{passive:true});car.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();turnPage(e.key==='ArrowRight'?1:-1);}});
 }
 if(id==='celebration')$('#motion-note').textContent='Each completed activity adds one visible growth stage and a new leaf. Back does not award another stage.';
 if(byId[id]?.kind==='reader')$('#motion-note').textContent='Each image automatically shows its own alternate-view thumbnails at the bottom. Swiping changes the main image and its views. Swipe past image 3 for chapter navigation.';
};
function completeActivity(){
 if(!st.run||st.run.done)return;const a=activity();st.run.done=true;clearInterval(tick);const c={id:uid(),activityId:a.id,title:a.title,category:a.category,level:a.level,child:st.child,mode:st.run.mode,at:new Date().toISOString(),feedback:null};saved.completions.push(c);st.run.completionId=c.id;st.rating=null;st.drafts['feedback-1']='';persist();go('celebration');
}
function turnPage(delta){const car=viewport.querySelector('.screen:last-of-type .reader-carousel');if(car)car.scrollTo({left:Math.max(0,Math.min(3,(st.pages[st.id]||0)+delta))*car.clientWidth,behavior:reduced()?'instant':'smooth'});}
const oldGo=go;
go=function(to,opts={}){
 if(to.startsWith('@category-')){st.development=to.slice(10);st.level=1;return render('levels',opts);}
 if(to.startsWith('@level-')){st.level=Number(to.slice(7));return render('activities',opts);}
 if(to.startsWith('@activity-')){st.activityId=to.slice(10);st.development=activity().category;st.level=activity().level;st.run=null;st.mode='Guidance';return render('activity',opts);}
 if(to==='@start'){st.run={id:uid(),activityId:activity().id,mode:st.mode,remaining:activity().seconds,done:false};st.timer=activity().seconds;st.paused=false;return render(st.mode==='Individual'?'individual':'steps',opts);}
 if(to==='@complete'){if(!st.run)st.run={id:uid(),mode:'Guidance',done:false};return completeActivity();}
 if(to==='@pause'){st.paused=!st.paused;const b=viewport.querySelector('.screen:last-of-type [data-go="@pause"] span');if(b)b.textContent=st.paused?'Resume timer':'Pause timer';announce(st.paused?'Timer paused':'Timer resumed');return;}
 if(to==='@feedback-save'||to==='@feedback-skip'){const c=currentCompletion();if(to==='@feedback-save'&&!st.rating){announce('Choose your satisfaction level, or skip feedback.');return;}if(c){c.feedback=to==='@feedback-save'?{rating:st.rating,comment:st.drafts['feedback-1']||''}:null;persist();}return render('progress',opts);}
 if(to.startsWith('@auth-')){render('home',opts);announce((to.endsWith('google')?'Google':'Apple')+' sign-in simulated. No account was connected.');return;}
 if(to==='@child-save'){st.child=(st.drafts['child-setup-0']||'Maya').trim();saved.child=st.child;persist();return render('home',opts);}
 if(to.startsWith('@history-')){st.historyId=to.slice(9);return render('history-detail',opts);}
 if(to.startsWith('@kit-')){st.kitId=to.slice(5);return render('product',opts);}
 if(to==='@pay'){saved.orders.push({id:uid(),kit:kit().title,total:kit().price,at:new Date().toISOString(),demo:true});persist();return render('payment-complete',opts);}
 if(to==='@community-review')return render('community-review',opts);
 if(to==='@community-cancel'){st.communityIntent=null;return render('community',{back:true});}
 if(to==='@community-confirm'){
  if(st.communityIntent==='media'){render('community',{back:true});const input=document.createElement('input');input.type='file';input.accept='image/*,video/*';input.onchange=()=>{if(input.files[0]){st.attachment=input.files[0];render('community',{back:true});}};input.click();}
  else{const text=(st.communityText||st.drafts['message-0']||'').trim();if(!text&&!st.attachment){render('community',{back:true});announce('Add a message or media first.');return;}saved.community.push({id:uid(),text,media:st.attachment?.name||null,status:'Pending',at:new Date().toISOString()});st.communityText='';st.attachment=null;st.drafts['message-0']='';persist();render('community',{back:true});announce('Saved locally · Waiting for admin review.');}
  st.communityIntent=null;return;
 }
 return oldGo(to,opts);
};
document.addEventListener('input',e=>{if(e.target.name==='satisfaction')st.rating=e.target.value;if(e.target.matches('.community-composer textarea'))st.communityText=e.target.value;});
document.addEventListener('submit',e=>{e.preventDefault();e.target.querySelector('[data-submit]')?.click();});
document.addEventListener('click',e=>{
 const b=e.target.closest('button,[data-history-id]');if(!b)return;
 const handled=['mode','loadVideo','wish','wishlistFilter','filterToggle','category','pageDelta','perspective','communityMedia','communitySend','approvePost','removeAttachment','historyId'].some(k=>Object.hasOwn(b.dataset,k));if(!handled)return;
 e.preventDefault();e.stopImmediatePropagation();
 if(b.dataset.mode){st.mode=b.dataset.mode;b.closest('.mode-picker').querySelectorAll('button').forEach(x=>{x.classList.toggle('selected',x===b);x.setAttribute('aria-pressed',x===b)});}
 if(b.dataset.loadVideo){const slot=b.closest('.embed-slot');slot.innerHTML=`<iframe title="YouTube video player" src="https://www.youtube.com/embed/${b.dataset.loadVideo}?autoplay=1&rel=0" allow="autoplay; encrypted-media; picture-in-picture" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>`;}
 if(b.dataset.wish){const id=b.dataset.wish;saved.wishlist=saved.wishlist.includes(id)?saved.wishlist.filter(x=>x!==id):[...saved.wishlist,id];persist();render(st.id,{back:true});}
 if(Object.hasOwn(b.dataset,'wishlistFilter')){st.wishlistOnly=!st.wishlistOnly;render('stories',{back:true});}
 if(Object.hasOwn(b.dataset,'filterToggle')){st.filtersOpen=!st.filtersOpen;render('stories',{back:true});}
 if(b.dataset.category){st.storyCategory=b.dataset.category;render('stories',{back:true});}
 if(b.dataset.pageDelta)turnPage(Number(b.dataset.pageDelta));
 if(Object.hasOwn(b.dataset,'perspective')){const page=Number(b.dataset.perspectivePage),view=Number(b.dataset.perspective),frame=b.closest('.story-image-frame');st.perspectives[st.id+'-'+page]=view;frame.querySelector('.story-main-image').innerHTML=perspectiveSvg(booksById[b.dataset.perspectiveBook],page,view);frame.querySelectorAll('[data-perspective]').forEach(x=>x.setAttribute('aria-pressed',x===b));animate(frame.querySelector('.story-main-image'),[{opacity:.35},{opacity:1}],{duration:reduced()?120:220});}
 if(Object.hasOwn(b.dataset,'communityMedia')){st.communityIntent='media';go('community-review');}
 if(Object.hasOwn(b.dataset,'communitySend')){if(!st.communityText.trim()&&!st.attachment){announce('Add a message or media first.');return;}st.communityIntent='send';go('community-review');}
 if(b.dataset.approvePost){const post=saved.community.find(m=>m.id===b.dataset.approvePost);if(post){post.status='Approved';persist();render('community',{back:true});announce('Demo approval · App notification and email preview are ready.');}}
 if(Object.hasOwn(b.dataset,'removeAttachment')){st.attachment=null;render('community',{back:true});}
 if(b.dataset.historyId)go('@history-'+b.dataset.historyId);
},true);
document.addEventListener('keydown',e=>{if((e.key==='Enter'||e.key===' ')&&e.target.dataset.historyId){e.preventDefault();go('@history-'+e.target.dataset.historyId);}});
