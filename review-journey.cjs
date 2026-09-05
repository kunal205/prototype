const {chromium}=require('C:/Users/KUNAL/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');const assert=require('assert');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const p=await browser.newPage({viewport:{width:1440,height:1080}});const errors=[];p.on('pageerror',e=>errors.push(e.message));
 await p.goto('http://127.0.0.1:4191/Little-Legacy-Prototype.html?journey=complete');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(450);
 const screen=()=>p.locator('.screen').last();const click=async sel=>{await screen().locator(sel).click();await p.waitForTimeout(410)};
 const go=async id=>{await p.evaluate(id=>LL.go(id),id);await p.waitForTimeout(410)};
 const snap=async name=>{await p.screenshot({path:__dirname+'/preview-'+name+'.png',fullPage:true})};
 assert.equal(await p.evaluate(()=>LL.st.id),'welcome');
 await go('signup');await snap('signup-new');await click('[data-go="@auth-google"]');assert.equal(await p.evaluate(()=>LL.st.id),'child-setup');
 await screen().locator('input').nth(0).fill('Aria');await screen().locator('input').nth(1).fill('2022-05-12');await click('[data-go="@child-save"]');await p.waitForTimeout(420);
 assert.equal(await p.evaluate(()=>LL.st.child),'Aria');assert.equal(await p.evaluate(()=>LL.st.id),'home');
 assert.deepEqual(await screen().locator('.tabs .tab').allTextContents(),['Home','Stories','Community','Shop']);
 assert.equal(await screen().locator('.youtube-video[href]').count(),2);await snap('home-new');
 const counts=await p.evaluate(()=>Object.fromEntries(['Cognitive','Physical','Emotional','Social','Creative'].map(c=>[c,[1,2,3].map(l=>LL.flow.activities.filter(a=>a.category===c&&a.level===l).length)])));
 assert(Object.values(counts).every(v=>v.every(x=>x===3)));
 for(const c of Object.keys(counts)){await go('@category-'+c);assert.equal(await screen().locator('.card').count(),3);for(let l=1;l<=3;l++){await go('@level-'+l);assert.equal(await screen().locator('.card').count(),3);}}
 await go('@activity-cognitive-1');await snap('activity-new');await click('[data-go="@start"]');assert.equal(await p.evaluate(()=>LL.st.id),'steps');assert.equal(await screen().locator('.timer').count(),0);
 await click('[data-go="step-2"]');await click('[data-go="step-3"]');await click('[data-go="@complete"]');assert.equal(await p.evaluate(()=>LL.saved.completions.length),1);await p.waitForTimeout(550);await snap('plant-new');
 await go('@back');await go('@complete');assert.equal(await p.evaluate(()=>LL.saved.completions.length),1);await go('celebration');await click('[data-go="feedback"]');
 assert.deepEqual(await screen().locator('.satisfaction label').allTextContents(),['Very Satisfied','Satisfied','Neutral','Unsatisfied','Very Unsatisfied']);
 await click('[data-go="@feedback-save"]');assert.equal(await p.evaluate(()=>LL.st.id),'feedback');
 await screen().locator('input[value="Very Satisfied"]').check();await screen().locator('textarea').fill('Loved discovering red things.');await snap('feedback-new');await click('[data-go="@feedback-save"]');
 assert.equal(await p.evaluate(()=>LL.saved.completions[0].feedback.comment),'Loved discovering red things.');assert.equal(await screen().locator('[data-go^="@activity-"]').count(),3);await snap('growth-new');
 await go('@activity-physical-5');await click('[data-mode="Individual"]');await click('[data-go="@start"]');assert.equal(await p.evaluate(()=>LL.st.timer),300);
 await click('[data-go="@pause"]');const paused=await p.evaluate(()=>LL.st.timer);await p.waitForTimeout(1200);assert.equal(await p.evaluate(()=>LL.st.timer),paused);await snap('individual-new');
 await click('[data-go="@pause"]');await p.waitForTimeout(1200);assert((await p.evaluate(()=>LL.st.timer))<paused);
 await click('[data-go="@complete"]');assert.equal(await p.evaluate(()=>LL.saved.completions.length),2);await click('[data-go="feedback"]');await click('[data-go="@feedback-skip"]');assert.equal(await p.evaluate(()=>LL.saved.completions[1].feedback),null);
 await go('@activity-creative-9');await click('[data-mode="Individual"]');await click('[data-go="@start"]');await p.evaluate(()=>LL.st.timer=1);await p.waitForTimeout(1300);assert.equal(await p.evaluate(()=>LL.st.id),'celebration');assert.equal(await p.evaluate(()=>LL.saved.completions.length),3);
 await go('stories');assert.equal(await screen().locator('.book-tile').count(),10);await click('[data-wish="seed"]');await click('[data-wishlist-filter]');assert.equal(await screen().locator('.book-tile').count(),1);await click('[data-wishlist-filter]');await click('[data-category="Nature"]');assert.equal(await screen().locator('.book-tile').count(),2);await click('[data-category="All"]');await snap('stories-new');
 await click('[data-book="seed"]');assert.equal(await screen().locator('.chapter-row').count(),3);await click('.chapter-row:first-child');assert.equal(await screen().locator('.story-page').count(),3);
 await snap('reader-new');await click('[data-page-delta="1"]');await click('[data-page-delta="1"]');await click('[data-page-delta="1"]');assert.equal(await p.evaluate(()=>LL.st.pages.reader),3);await snap('chapter-end-new');await click('[data-go="reader-2"]');assert.equal(await p.evaluate(()=>LL.st.id),'reader-2');
 // Verify the provided source is used by the player; playback depends on YouTube.
 await click('[data-load-video]');assert((await screen().locator('iframe').getAttribute('src')).includes('NDFqrbv6hkg'));
 await go('community');await screen().locator('.community-composer textarea').fill('Aria loved her colour hunt!');await click('[data-community-send]');assert.equal(await p.evaluate(()=>LL.st.id),'community-review');await snap('community-review-new');
 await click('[data-go="@community-cancel"]');assert.equal(await p.evaluate(()=>LL.saved.community.length),0);await click('[data-community-send]');await click('[data-go="@community-confirm"]');assert.equal(await p.evaluate(()=>LL.saved.community[0].status),'Pending');await snap('community-new');
 await click('[data-approve-post]');await go('notifications');assert((await screen().textContent()).includes('Email preview'));
 await go('community');await click('[data-community-media]');const chooser=p.waitForEvent('filechooser');await click('[data-go="@community-confirm"]');await(await chooser).setFiles({name:'sample.svg',mimeType:'image/svg+xml',buffer:Buffer.from('<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"><rect width="20" height="20" fill="red"/></svg>')});await p.waitForTimeout(450);assert((await screen().textContent()).includes('sample.svg'));
 await go('shop');assert.equal(await screen().locator('.kit-card').count(),3);await snap('shop-new');await click('[data-go="@kit-creative"]');await click('[data-go="checkout"]');assert((await screen().textContent()).includes('₹649'));await snap('checkout-new');await click('[data-go="@pay"]');assert.equal(await p.evaluate(()=>LL.saved.orders.length),1);
 await p.reload();await p.waitForTimeout(450);assert.equal(await p.evaluate(()=>LL.saved.completions.length),3);assert.equal(await p.evaluate(()=>LL.saved.wishlist.length),1);assert.equal(await p.evaluate(()=>LL.saved.child),'Aria');
 const overflows=[];const ids=await p.evaluate(()=>LL.screens.map(s=>s.id));
 for(const id of ids){await p.evaluate(id=>LL.render(id,{initial:true}),id);await p.waitForTimeout(130);const o=await screen().locator('.scroll').evaluate(el=>el.scrollWidth>el.clientWidth+1);if(o)overflows.push(id);}
 await p.setViewportSize({width:390,height:844});await go('feedback');await snap('feedback-mobile-new');await go('stories');await p.evaluate(()=>{LL.st.theme='Dark';LL.theme()});await snap('stories-dark-new');await go('community');await snap('community-mobile-new');
 await p.setViewportSize({width:1280,height:1200});await p.locator('#tablet').click();await p.evaluate(()=>{LL.st.theme='Light';LL.theme()});await go('stories');await snap('stories-tablet-new');
 await p.emulateMedia({reducedMotion:'reduce',colorScheme:'dark'});await p.evaluate(()=>{LL.st.theme='System';LL.theme()});assert.equal(await p.locator('.device').getAttribute('data-palette'),'Dark');assert((await p.locator('.device').getAttribute('class')).includes('reduced'));
 assert.deepEqual(errors,[]);assert.deepEqual(overflows,[]);
 const report={passed:true,screens:ids.length,activities:counts,errors,overflows,checked:['Simulated Google login and child form','15 level activity lists','Guidance completion once only','Preset timer pause/resume, early finish and timer expiry','Feedback required selection, persistence and skip','Wishlist and category filter','3 image pages and chapter end navigation','YouTube iframe source','Community Cancel, Okay, media picker, admin preview and notifications','3 kits and demo payment','Persistence after reload','Phone, tablet, dark and reduced motion']};fs.writeFileSync(__dirname+'/validation-journey.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
