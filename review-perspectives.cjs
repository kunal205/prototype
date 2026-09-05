const {chromium}=require('C:/Users/KUNAL/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const assert=require('assert'),fs=require('fs');
(async()=>{
 const b=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const p=await b.newPage({viewport:{width:390,height:844},hasTouch:true,isMobile:true});const errors=[];p.on('pageerror',e=>errors.push(e.message));
 await p.goto('http://127.0.0.1:4191/Little-Legacy-Prototype.html#reader');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
 const active=()=>p.locator('.screen').last();const go=async id=>{await p.evaluate(id=>LL.go(id),id);await p.waitForTimeout(400)};
 const visibleStacks=()=>active().locator('.perspective-stack:not([hidden])');
 assert.equal(await visibleStacks().count(),1);assert.equal(await visibleStacks().locator('button').count(),3);assert.equal(await active().locator('.story-page').count(),3);
 assert.equal(await visibleStacks().locator('button').first().getAttribute('data-perspective-page'),'0');
 await p.screenshot({path:__dirname+'/preview-reader-perspectives.png'});
 await visibleStacks().locator('[data-perspective="1"]').click();assert.equal(await p.evaluate(()=>LL.st.pages.reader),0);assert.equal(await active().locator('.story-page').first().locator('.story-main-image svg').getAttribute('viewBox'),'80 80 210 193');
 await p.screenshot({path:__dirname+'/preview-reader-close-view.png'});
 // Exercise a real touch swipe on the main image, independent of its view buttons.
 const client=await p.context().newCDPSession(p);const box=await active().locator('.reader-carousel').boundingBox();const y=box.y+100;
 await client.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:box.x+box.width-25,y}]});
 for(let i=1;i<=8;i++){await client.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:box.x+box.width-25-(box.width-50)*i/8,y}]});await p.waitForTimeout(20);}
 await client.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});await p.waitForTimeout(600);
 assert.equal(await p.evaluate(()=>LL.st.pages.reader),1);assert.equal(await visibleStacks().count(),1);assert.equal(await visibleStacks().locator('button').first().getAttribute('data-perspective-page'),'1');
 assert.equal(await active().locator('.story-page').nth(0).locator('.perspective-stack').getAttribute('hidden'),'');
 assert.equal(await visibleStacks().locator('[aria-pressed="true"]').getAttribute('data-perspective'),'0');await p.screenshot({path:__dirname+'/preview-reader-next-image.png'});
 await active().locator('[data-page-delta="1"]').click();await p.waitForTimeout(500);await active().locator('[data-page-delta="1"]').click();await p.waitForTimeout(500);assert.equal(await visibleStacks().count(),0);assert.equal(await p.evaluate(()=>LL.st.pages.reader),3);
 await active().locator('[data-go="reader-2"]').click();await p.waitForTimeout(400);assert.equal(await visibleStacks().count(),1);assert.equal(await p.evaluate(()=>LL.st.pages['reader-2']),0);
 const removed=['launch','welcome','recovery','child-setup','home-offline','categories','story-unavailable','story-empty','post','message','notification','help-detail','data-requests','data-form','data-received','review','request-received'];
 const data=await p.evaluate(()=>({screens:LL.screens,activities:LL.flow.activities}));assert(removed.every(id=>!data.screens.some(s=>s.id===id)));assert.equal(data.screens.filter(s=>s.title==='Shop payment').length,1);assert(data.activities.some(a=>a.title==='Match my pair'));
 const ids=new Set(data.screens.map(s=>s.id)),broken=[];for(const s of data.screens)for(const item of [...s.items,...s.actions])if(item.to&&!item.to.startsWith('@')&&!ids.has(item.to))broken.push([s.id,item.to]);assert.deepEqual(broken,[]);
 await go('home');assert.equal(await active().locator('.right-icons button').count(),2);
 const overflows=[];for(const id of ids){await p.evaluate(id=>LL.render(id,{initial:true}),id);await p.waitForTimeout(125);if(id!=='home')assert.equal(await active().locator('.right-icons').count(),0);if(await active().locator('.scroll').evaluate(e=>e.scrollWidth>e.clientWidth+1))overflows.push(id);}
 await p.reload();await p.waitForTimeout(300);await go('signup');await active().locator('[data-go="@auth-apple"]').click();await p.waitForTimeout(400);assert.equal(await p.evaluate(()=>LL.st.id),'home');
 await go('signin');await active().locator('input[type=email]').fill('parent@example.com');await active().locator('input[type=password]').fill('demo-password');await active().locator('.actions .primary').click();await p.waitForTimeout(850);assert.equal(await p.evaluate(()=>LL.st.id),'home');
 await go('reader');await p.evaluate(()=>{LL.st.theme='Dark';LL.theme()});await p.waitForTimeout(300);await p.screenshot({path:__dirname+'/preview-reader-perspectives-dark.png'});
 await p.setViewportSize({width:1280,height:1200});await p.locator('#tablet').click();await p.waitForTimeout(300);await p.screenshot({path:__dirname+'/preview-reader-perspectives-tablet.png',fullPage:true});
 await p.emulateMedia({reducedMotion:'reduce'});await active().locator('[data-page-delta="1"]').click();await p.waitForTimeout(150);assert.equal(await visibleStacks().count(),1);
 assert.deepEqual(errors,[]);assert.deepEqual(overflows,[]);
 const report={passed:true,screens:ids.size,removedPages:removed,brokenLinks:broken,errors,overflows,checked:['Automatic per-image alternate thumbnails without a reveal tap','Selecting a perspective stays on the same main image','Real touch swipe switches the main image and its own stack','No previous-image stack on the next image','No perspective stack on the chapter-end panel','Next chapter opens with its own image views','Match my pair retained','Single Shop payment page','Notification/profile icons only on Home','Login and Apple sign-in directly to Home','Phone, dark, tablet and reduced motion']};fs.writeFileSync(__dirname+'/validation-perspectives.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report));await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
