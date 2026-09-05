from pathlib import Path
import json, html, textwrap, base64, zipfile
from story_catalog import BOOKS, cover_svg, detail_id, chapter_ids

ROOT=Path(__file__).parent
VIDEO_FILE=ROOT/'youtube-videos.json'
HOME_VIDEOS=json.loads(VIDEO_FILE.read_text(encoding='utf-8')) if VIDEO_FILE.exists() else [dict(title='YouTube video',url=None),dict(title='YouTube video',url=None)]
SCREENS=[]
def add(id,group,title,sub='',items=None,actions=None,kind='standard',tabs=False):
    SCREENS.append(dict(id=id,group=group,title=title,sub=sub,items=items or [],actions=actions or [],kind=kind,tabs=tabs))
def card(title,sub='',to='',tag=''):
    return dict(type='card',title=title,sub=sub,to=to,tag=tag)
def row(title,to='',sub=''):
    return dict(type='row',title=title,sub=sub,to=to)
def field(title,placeholder='',input='text'):
    return dict(type='field',title=title,sub=placeholder,input=input)
def note(text): return dict(type='note',title=text)
def art(name): return dict(type='art',title=name)
def action(label,to,secondary=False):return dict(label=label,to=to,secondary=secondary)
DEVELOPMENTS=[
    dict(name='Cognitive',sub='Think, notice & discover',icon='brain'),
    dict(name='Physical',sub='Move, balance & explore',icon='move'),
    dict(name='Emotional',sub='Understand little feelings',icon='heart'),
    dict(name='Social',sub='Connect, share & belong',icon='people'),
    dict(name='Creative',sub='Imagine, make & express',icon='spark')]

add('launch','A','Little Legacy','Small moments. Lasting growth.',[art('brand')],[action('Begin','welcome')],kind='launch')
add('welcome','A','Big futures begin small.','Meaningful play for your 3–5 year old.',[art('plant'),note('A few minutes together. A new discovery every day.')],[action('Create an account','signup'),action('I already have an account','signin',True)],kind='welcome')
add('signin','A','Welcome back','Your next little adventure is waiting.',[field('Email address','you@example.com','email'),field('Password','Enter your password','password'),row('Forgot password?','recovery')],[action('Sign in','home'),action('Create an account','signup',True)],kind='form')
add('signup','A','Grow together','Create your parent account.',[field('Your name','Parent or caregiver'),field('Email address','you@example.com','email'),field('Password','Choose a password','password'),row('☐ I agree to the Terms and Privacy Policy','terms')],[action('Create account','verification')],kind='form')
add('verification','A','Check your inbox','Enter the code sent to your email.',[field('Verification code','6-digit code','text'),row('Send a new code','verification'),note('Check your spam folder if the email has not arrived.')],[action('Verify email','child-setup')],kind='form')
add('recovery','A','Let’s get you back in','We’ll send a password reset link.',[field('Email address','you@example.com','email')],[action('Send reset link','reset')],kind='form')
add('reset','A','Choose a new password','Use a password you haven’t used before.',[field('New password','New password','password'),field('Confirm password','Repeat password','password')],[action('Save password','signin')],kind='form')
add('session-expired','A','Please sign in again','Your session has ended.',[note('Your saved progress is still here.')],[action('Sign in','signin')])
add('child-setup','B','Who’s growing with us?','Create your first child profile.',[field('Child’s first name','First name'),field('Date of birth','','date'),row('Choose an avatar','children')],[action('Create child profile','home')],kind='form')
add('children','B','Your little learners','Choose a child to personalise the day.',[card('Maya · age 4','✓ Selected','home','CURRENT CHILD'),card('Leo · age 3','Switch child','home','CHILD PROFILE'),row('Add a child','add-child'),row('Edit Maya’s profile','edit-child')],[action('Done','home')],kind='sheet')
add('add-child','B','Add a little learner','Each child has their own progress.',[field('First name','First name'),field('Date of birth','','date')],[action('Add child','children')],kind='form')
add('edit-child','B','Maya’s profile','Update your child’s details.',[field('First name','Maya'),field('Date of birth','','date'),row('Remove Maya’s profile','remove-child')],[action('Save changes','children')],kind='form')
add('remove-child','B','Remove Maya’s profile?','This action applies to Maya.',[note('Review the effect on saved progress before confirming. Final retention wording requires approval.')],[action('Keep Maya’s profile','children'),action('Remove Maya’s profile','children',True)],kind='sheet')
add('home','C','A little play. A lot of possibility.','Hello, Maya’s grown-up.',[row('Maya · age 4   ⌄','children'),dict(type='bento',title='Every way to grow',areas=DEVELOPMENTS),dict(type='youtube',title='Watch together',videos=HOME_VIDEOS),card('Your garden is growing','See every little step forward.','progress','LEVEL GARDEN')],tabs=True,kind='home')
add('home-offline','C','You’re offline','Keep exploring what’s saved.',[note('Saved on device · Waiting to sync'),card('Resume colour hunt','Available on this device','steps','SAVED ACTIVITY'),row('Try connecting again','home')],tabs=True)
add('categories','D','What will you discover?','Choose a skill to grow together.',[card('Thinking & problem solving','Notice, sort and discover.','levels','01 · EXPLORE'),card('Movement & coordination','Big moves, little milestones.','levels','02 · MOVE'),card('Language & connection','Listen, share and express.','levels','03 · CONNECT')],tabs=True)
add('levels','D','One small step at a time','Thinking & problem solving',[card('Level 1 · Little explorer','✓ Current level','activities','YOUR NEXT STEP'),card('Level 2 · Curious thinker','Locked · Keep growing together','','NEXT CHAPTER'),row('View learning progress','progress')],tabs=True)
add('activities','D','Today’s activities','A few simple ways to connect.',[card('Colour hunt','Find everyday treasures in your home.','activity','5 MIN · INDOORS'),card('What comes next?','Make a pattern together.','activity','5 MIN · THINKING'),row('Refresh today’s activities','activities'),row('View completed activities','history')],tabs=True)
add('activity','D','A world of colour','Notice the colours hiding in plain sight.',[art('activity'),note('5 minutes · Thinking & problem solving'),card('What you’ll need','A few safe everyday objects. Stay with your child throughout.'),card('Make it your own','Name a colour and find matching objects together.')],[action('Start activity','steps')],kind='detail')
add('steps','D','Let’s find something red','Step 1 of 3 · Colour hunt',[art('activity'),note('Look around the room together. Let your child choose one safe red object.'),dict(type='timer',title='01:00'),row('Pause timer','@timer')],[action('Next step','step-2'),action('Skip timer','step-2',True)],kind='steps')
add('step-2','D','What else is the same?','Step 2 of 3 · Colour hunt',[art('activity'),note('Find another object in the same colour. Talk about what is different.'),dict(type='timer',title='01:00')],[action('Next step','step-3'),action('Skip timer','step-3',True)],kind='steps')
add('step-3','D','Celebrate the discovery','Step 3 of 3 · Colour hunt',[art('plant'),note('Name the colours you found. Thank your child for exploring with you.')],[action('Complete activity','feedback')],kind='steps')
add('feedback','D','How did it feel?','A quick reflection helps personalise tomorrow.',[dict(type='choice',title='Enjoyed it',sub='Needed a little help|Let’s try again'),field('Anything you’d like to remember?','Optional note','textarea')],[action('Save & celebrate','celebration'),action('Skip reflection','celebration',True)],kind='form')
add('celebration','D','A little growth, together.','Every moment you share makes a difference.',[art('plant'),note('✓ Activity complete · Saved on device')],[action('Continue','progress'),action('Skip celebration','progress',True)],kind='celebration')
add('progress','D','Look how far you’ve grown','Maya’s learning garden',[dict(type='graph',title='Small steps add up'),card('Your latest discovery','Colour hunt · Completed today','history-detail','ACTIVITY COMPLETE'),row('Explore activity history','history'),row('Find your next activity','activities')],tabs=True,kind='progress')
add('history','D','Your little milestones','Every activity has a story.',[card('Colour hunt','Completed today','history-detail','THINKING'),card('Sharing a story','Completed earlier','history-detail','LANGUAGE')],tabs=True)
add('history-detail','D','Colour hunt','Activity history',[note('✓ Completed · Maya'),card('Your reflection','Enjoyed it. Loved finding red objects.'),note('This is a saved record. Opening it does not replay the celebration.')],[action('Back to progress','progress')])
add('stories','E','A story to share','A quiet moment. A whole new world.',[dict(type='story-categories',title='Categories',categories=['All','Nature','Kindness','Feelings','Adventure','Bedtime']),dict(type='book-grid',title='Our story shelf',books=BOOKS)],tabs=True,kind='library')
for book in BOOKS:
    chapter_routes=chapter_ids(book)
    add(detail_id(book),'E',book['title'],book['category'],[dict(type='book-intro',title=book['title'],book=book),dict(type='chapters',title='Chapters',book=book,routes=chapter_routes)],[action('Start reading',chapter_routes[0])],kind='book-detail')
    for i,chapter in enumerate(book['chapters']):
        add(chapter_routes[i],'E',book['title'],f'Chapter {i+1} of 3 · {chapter}',[dict(type='chapter-art',title=book['title'],book=book),note(book['copy'][i])],[action('Next chapter' if i<2 else 'Finish story',chapter_routes[i+1] if i<2 else 'stories'),action('Back to chapters',detail_id(book),True)],kind='reader')
        SCREENS[-1]['bookId']=book['id'];SCREENS[-1]['chapterRoutes']=chapter_routes
add('story-video','E','Watch together','The little seed',[art('video'),note('Embedded YouTube region. An approved video and internet connection are required.'),row('Video unavailable example','story-unavailable')],[action('Read the story instead','reader')])
add('story-unavailable','E','This story is resting','We can’t open this content right now.',[note('Your place is saved. Please try again when you’re connected.')],[action('Try again','story'),action('Back to library','stories',True)])
add('story-empty','E','More stories are coming','Explore another category for now.',[],[action('Browse all stories','stories')])
add('community','F','You’re in good company','Little moments from our parent community.',[card('Making space for small wins','A reminder to notice everyday progress.','post','FROM LITTLE LEGACY'),card('Play can start anywhere','Simple ways to turn routines into connection.','post','PARENT NOTES'),row('Send a private message','message'),row('Share app or activity feedback','app-feedback')],tabs=True)
add('post','F','Making space for small wins','From Little Legacy',[art('community'),note('A new word. A shared smile. A moment of patience. Small wins deserve to be noticed.'),row('Send us a private message','message')],tabs=True)
add('message','F','A private conversation','Your message goes to the Little Legacy team.',[field('Subject','What’s on your mind?'),field('Message','Write your message','textarea'),row('Attach a photo or file','attachments')],[action('Review & send message','submitted')],kind='form')
add('app-feedback','F','Help us grow','Tell us about the app or an activity.',[field('Feedback about','App / activity'),field('Your feedback','What worked? What could be better?','textarea'),row('Attach a file','attachments')],[action('Send feedback','submitted')],kind='form')
add('attachments','F','Add an attachment','Choose what you’d like to share.',[row('Choose a photo','@file'),row('Choose a file','@file'),note('Review your selection before sending.')],[action('Done','message'),action('Cancel','message',True)],kind='sheet')
add('submitted','F','Thank you for sharing','Your message has been received.',[note('This prototype simulates submission. No message is sent.')],[action('Back to community','community')])
add('shop','G','Tools for together time','Thoughtful companions for everyday play.',[card('Little discovery kit','Hands-on activities for curious little minds.','product','LEARNING KIT'),card('Storytime collection','More stories to enjoy together.','product','STORYBOOKS')],tabs=True)
add('product','G','Little discovery kit','Make everyday moments a little more playful.',[art('product'),card('Inside the kit','Activity cards and simple prompts for parent-led play.'),note('Send a request for availability and details. No payment is taken here.')],[action('Request this product','request')],kind='detail')
add('request','G','Let’s hear from you','Request details for the Little discovery kit.',[field('Your name','Full name'),field('Email address','you@example.com','email'),field('Phone number','Optional phone number','tel'),field('Your request','Quantity or a question','textarea')],[action('Review request','review')],kind='form')
add('review','G','Check your request','Make sure everything looks right.',[card('Little discovery kit','Product information request'),card('Contact details','Your details appear here before submission.'),row('Edit your details','request'),note('This is a request, with no payment or confirmed order.')],[action('Submit request','request-received')])
add('request-received','G','Request Received','Thank you for your interest.',[art('plant'),note('The team will follow up using your contact details. This prototype does not send a real request.')],[action('Back to shop','shop')])
add('notifications','H','A little update','Stay close to what’s new.',[card('A new story is waiting','Discover your next shared adventure.','notification','NEW'),card('Your weekly little moments','Take a look at your progress.','notification','PROGRESS')],tabs=True)
add('notification','H','A new story is waiting','Notification detail',[note('Find a quiet moment and explore the latest story together.')],[action('Explore stories','stories')])
add('profile','H','Your little corner','Manage your family and preferences.',[row('Child profiles','children'),row('Account settings','account'),row('Notification preferences','notification-settings'),row('Sound & motion','appearance'),row('Help & support','help'),row('Terms & privacy','terms'),row('Data & account requests','data-requests')],tabs=True)
add('account','H','Account settings','Keep your details up to date.',[field('Your name','Parent name'),field('Email address','you@example.com','email'),row('Change password','reset')],[action('Save changes','profile')],kind='form')
add('notification-settings','H','Choose your updates','You’re in control of what reaches you.',[dict(type='toggle',title='Activity reminders',on=True),dict(type='toggle',title='New stories',on=True),dict(type='toggle',title='Community updates',on=False)],[action('Save preferences','profile')])
add('appearance','H','Make yourself comfortable','Choose how Little Legacy looks and feels.',[dict(type='themes',title='Appearance'),dict(type='toggle',title='Sound effects',on=False),dict(type='toggle',title='Reduced motion',on=False,key='reduced'),note('System follows your device and updates when it changes.')],[action('Done','profile')],kind='appearance')
add('help','H','A little help','Find answers or talk to our team.',[row('How do activities work?','help-detail'),row('Manage child profiles','children'),row('Send a private message','message')],tabs=True)
add('help-detail','H','Play at your child’s pace','A few minutes of connection is enough.',[note('Choose an activity, gather the materials, and follow the steps together. You can pause a timer, skip it, or leave and resume.'),row('Try an activity','activities')])
add('terms','H','Terms of use','Legal content layout',[note('Approved terms will appear here. Preserve the original wording, headings and version date. This wireframe does not supply legal terms.'),row('Privacy policy','privacy')],[action('Back','@back')])
add('privacy','H','Your family’s privacy','Privacy policy layout',[note('Approved privacy wording will appear here, including data use, retention, contact details and your rights. Final text is required.'),row('Data & account requests','data-requests')],[action('Back','@back')])
add('data-requests','H','Your data, your choices','Send a request to the team.',[row('Request a copy of my data','data-form'),row('Request account deletion','data-form'),note('We’ll explain the next steps before any permanent action.')])
add('data-form','H','Data & account request','Tell us what you need.',[field('Request type','Data export / account deletion'),field('Email address','you@example.com','email'),field('Details','Optional details','textarea')],[action('Send request','data-received')],kind='form')
add('data-received','H','Request received','Your account has not been deleted.',[note('The team will explain verification and next steps. Prototype only: no real request is sent.')],[action('Back to profile','profile')])

from journey_catalog import revise, FLOW, export_items
SCREENS=revise(SCREENS)

TOKENS={'Light':{'bg':'#FAF8F4','card':'#FFFFFF','text':'#282133','muted':'#6D6479','primary':'#7450AA','onPrimary':'#FFFFFF','border':'#E6E0EC','soft':'#EFE8F6','green':'#357551'},'Dark':{'bg':'#1D1926','card':'#292334','text':'#F6F1FC','muted':'#C1B5CD','primary':'#B99ADD','onPrimary':'#241730','border':'#44394F','soft':'#382E45','green':'#92C5A4'},'Wireframe':{'bg':'#F5F5F3','card':'#FFFFFF','text':'#232323','muted':'#646464','primary':'#333333','onPrimary':'#FFFFFF','border':'#DCDCD8','soft':'#EAEAE6','green':'#666666'}}
MOTION={'durationsMs':{'micro':150,'local':240,'navigation':360,'celebration':900,'theme':280,'reduced':120},'spring':{'navigation':{'stiffness':260,'damping':24,'mass':1},'reward':{'stiffness':180,'damping':20,'mass':1}},'listStagger':{'delayMs':40,'maxItems':6},'reducedMotion':'Crossfade only, 120ms. No movement, scale, shimmer or particle motion. OS preference always wins.'}

def illustration(name,color='currentColor'):
    if name in ['plant','brand']:
        return f'<svg viewBox="0 0 300 200" fill="none" aria-hidden="true"><circle cx="150" cy="94" r="77" fill="{color}" opacity=".06"/><path d="M118 145h64l-9 40h-46z" fill="{color}" opacity=".18"/><g class="grow"><path d="M150 147V65" stroke="{color}" stroke-width="5" stroke-linecap="round"/><path d="M149 113c-34 0-48-16-43-39 27 0 43 14 43 39Z" fill="{color}" opacity=".65"/><path d="M151 90c0-29 17-45 43-41 0 26-17 43-43 41Z" fill="{color}" opacity=".85"/><path d="M151 132c25 0 40-13 37-33-24 0-38 12-37 33Z" fill="{color}" opacity=".45"/></g><rect x="114" y="143" width="72" height="10" rx="5" fill="{color}" opacity=".75"/></svg>'
    if name in ['story','video']:
        return f'<svg viewBox="0 0 300 200" fill="none" aria-hidden="true"><rect x="83" y="20" width="134" height="160" rx="13" fill="{color}" opacity=".13"/><path d="M97 20v160" stroke="{color}" opacity=".35" stroke-width="2"/><circle cx="158" cy="81" r="31" fill="{color}" opacity=".16"/><path d="M158 111V75m0 20c-16 0-23-8-23-19 14 0 23 7 23 19Zm0-12c0-16 9-25 24-24 0 15-9 24-24 24Z" stroke="{color}" stroke-width="3"/><path d="M118 137h72m-59 13h46" stroke="{color}" stroke-width="4" stroke-linecap="round" opacity=".45"/></svg>'
    if name=='product':
        return f'<svg viewBox="0 0 300 200" fill="none" aria-hidden="true"><path d="m80 65 70-34 70 34-70 35Z" fill="{color}" opacity=".15"/><path d="m80 65 70 35v72l-70-36Z" fill="{color}" opacity=".3"/><path d="m150 100 70-35v71l-70 36Z" fill="{color}" opacity=".5"/><path d="m116 47 68 35v30" stroke="{color}" stroke-width="3"/></svg>'
    if name=='community':
        return f'<svg viewBox="0 0 300 200" fill="none" aria-hidden="true"><circle cx="115" cy="70" r="28" fill="{color}" opacity=".35"/><circle cx="185" cy="87" r="23" fill="{color}" opacity=".6"/><path d="M64 159c0-75 100-75 100 0m-10 0c0-52 75-52 75 0" stroke="{color}" stroke-width="8" stroke-linecap="round" opacity=".5"/></svg>'
    return f'<svg viewBox="0 0 300 200" fill="none" aria-hidden="true"><rect x="67" y="79" width="70" height="70" rx="14" fill="{color}" opacity=".22"/><circle cx="184" cy="66" r="35" fill="{color}" opacity=".48"/><path d="m182 114 36 61h-72Z" fill="{color}" opacity=".7"/><path d="m88 46 5-10m25 13 9-8m-69 17-8-6" stroke="{color}" stroke-width="3" stroke-linecap="round" opacity=".5"/></svg>'

def xml(v):return html.escape(str(v),quote=True)
def svg_text(text,x,y,w,size,color,bold=False):
    lines=[]
    for para in str(text).split('\n'):
        lines+=textwrap.wrap(para,width=max(8,int(w/(size*.55)))) or ['']
    out=f'<text x="{x}" y="{y}" fill="{color}" font-family="Plus Jakarta Sans, Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}">'
    for i,line in enumerate(lines):out+=f'<tspan x="{x}" dy="{0 if i==0 else size*1.4}">{xml(line)}</tspan>'
    return out+'</text>',len(lines)*size*1.4

def screen_svg(s,width=390,theme='Wireframe'):
    t=TOKENS[theme]; content=min(width-32,600);x=(width-content)/2; parts=[]
    def tx(text,yy,size=16,bold=False,color=None,xx=None,ww=None):
        a,h=svg_text(text,x if xx is None else xx,yy,content if ww is None else ww,size,color or t['text'],bold);parts.append(a);return h
    parts.append(f'<rect width="{width}" height="HEIGHT" rx="28" fill="{t["bg"]}"/>')
    tx('9:41',30,14,True);tx('●  ▰',30,14,True,xx=width-68,ww=55)
    tx('‹  Back',75,14,True,color=t['muted']); y=119
    if s['kind']!='book-detail':
        y+=tx(s['title'],y,26,True)+4
        y+=tx(s['sub'],y,14,color=t['muted'])+20
    for it in export_items(s['items']):
        typ=it['type'];title=it['title'];sub=it.get('sub','')
        if typ=='perspective-strip':
            start=x+(content-184)/2
            for n in range(3):
                xx=start+n*61
                parts.append(f'<rect x="{xx}" y="{y}" width="58" height="62" rx="10" fill="{t["soft"]}" stroke="{t["primary"] if n==0 else t["border"]}" stroke-width="{3 if n==0 else 1}"/>')
                parts.append(illustration('story',t['primary']).replace('<svg ',f'<svg x="{xx+2}" y="{y+2}" width="54" height="58" ',1))
            y+=84
            y+=tx(title,y,12,False,t['muted'])+20
        elif typ=='story-categories':
            y+=tx(title,y+17,18,True)+14
            xx=x
            for category in it['categories']:
                cw=max(68,len(category)*8+24)
                if xx+cw>x+content:xx=x;y+=54
                parts.append(f'<rect x="{xx}" y="{y}" width="{cw}" height="44" rx="22" fill="{t["primary"] if category=="All" else t["card"]}" stroke="{t["border"]}"/>')
                tx(category,y+28,14,category=='All',t['onPrimary'] if category=='All' else t['text'],xx+12,cw-20);xx+=cw+8
            y+=68
        elif typ=='book-grid':
            y+=tx(title,y+18,20,True)+18
            columns=3 if width>600 else 2;gap=16;bw=(content-gap*(columns-1))/columns;coverh=bw*4/3;rh=coverh+76
            for i,book in enumerate(it['books']):
                bx=x+(i%columns)*(bw+gap);by=y+(i//columns)*rh
                parts.append(cover_svg(book,theme=='Wireframe').replace('width="180" height="240"',f'x="{bx}" y="{by}" width="{bw}" height="{coverh}"',1))
                tx(book['title'],by+coverh+24,16,True,t['text'],bx,bw)
            y+=((len(it['books'])+columns-1)//columns)*rh+8
        elif typ=='book-intro':
            book=it['book'];bw=200;bh=bw*4/3;bx=x+(content-bw)/2
            parts.append(cover_svg(book,theme=='Wireframe').replace('width="180" height="240"',f'x="{bx}" y="{y}" width="{bw}" height="{bh}"',1));y+=bh+32
            y+=tx(book['title'],y,26,True)+10
            y+=tx(book['category']+' · 3 chapters',y,14,color=t['muted'])+14
            y+=tx(book['description'],y,16)+22
        elif typ=='chapters':
            y+=tx(title,y+18,20,True)+14
            for i,chapter in enumerate(it['book']['chapters']):
                parts.append(f'<rect x="{x}" y="{y}" width="{content}" height="64" rx="16" fill="{t["card"]}" stroke="{t["border"]}"/>')
                tx(str(i+1).zfill(2)+'   '+chapter,y+39,16,True,t['text'],x+16,content-32);y+=76
        elif typ=='chapter-art':
            bw=180;bh=240;bx=x+(content-bw)/2
            parts.append(cover_svg(it['book'],theme=='Wireframe').replace('width="180" height="240"',f'x="{bx}" y="{y}" width="{bw}" height="{bh}"',1));y+=bh+24
        elif typ=='bento':
            y+=tx(title,y+18,20,True)+16
            gap=12;tile=(content-gap)/2
            boxes=[(0,0,tile,300),(tile+gap,0,tile,144),(tile+gap,156,tile,144),(0,312,tile,164),(tile+gap,312,tile,164)]
            if width>600:
                tile=(content-2*gap)/3
                boxes=[(0,0,tile,344),(tile+gap,0,tile,166),(2*(tile+gap),0,tile,166),(tile+gap,178,tile,166),(2*(tile+gap),178,tile,166)]
            colors=['#EDE3F7','#E2EFE6','#F8E7D9','#F4E2EC','#ECEBDD'] if theme=='Light' else ['#3B2D4F','#263C34','#49362D','#452D40','#3B3B2D'] if theme=='Dark' else [t['soft']]*5
            for i,(area,box) in enumerate(zip(it['areas'],boxes)):
                bx,by,bw,bh=box;bx+=x;by+=y
                parts.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="22" fill="{colors[i]}"/>')
                tx(str(i+1).zfill(2),by+28,12,True,t['muted'],bx+16,bw-32)
                tx(area['name']+' development',by+62,16,True,t['text'],bx+16,bw-32)
                tx('→',by+bh-20,22,True,t['primary'],bx+bw-35,22)
                if i==0:
                    tx(area['sub'],by+137,14,False,t['muted'],bx+16,bw-32)
                    parts.append(f'<circle cx="{bx+bw/2}" cy="{by+225}" r="30" fill="none" stroke="{t["primary"]}" stroke-width="2"/><path d="M{bx+bw/2-16} {by+225}h32m-16-16v32" stroke="{t["primary"]}" stroke-width="2"/>')
            y+=362 if width>600 else 494
        elif typ=='youtube':
            y+=tx(title,y+18,20,True)+14
            for video in it['videos']:
                url=video.get('url')
                if url:parts.append(f'<a href="{xml(url)}" target="_blank">')
                parts.append(f'<rect x="{x}" y="{y}" width="{content}" height="154" rx="18" fill="{t["card"]}" stroke="{t["border"]}"/><rect x="{x+12}" y="{y+12}" width="{content-24}" height="87" rx="12" fill="{t["soft"]}"/><path d="m{x+content/2-7} {y+39} 22 14-22 14Z" fill="{t["primary"]}"/>')
                tx(video['title'],y+125,16,True,t['text'],x+16,content-32)
                if not url:tx('Video will appear here',y+144,12,False,t['muted'],x+16,content-32)
                if url:parts.append('</a>')
                y+=166
            y+=8
        elif typ=='art':
            svg=illustration(title,t['primary']).replace('<svg ',f'<svg x="{x}" y="{y-6}" width="{content}" height="170" ')
            parts.append(svg);y+=184
        elif typ in ['card','row','field']:
            fs=18 if typ=='card' else 16
            tw=content-56 if it.get('to') else content-32
            lines=max(1,len(textwrap.wrap(title,width=int(tw/(fs*.55)))))
            sublines=max(1,len(textwrap.wrap(sub,width=int((content-32)/(14*.55))))) if sub else 0
            h=max(58,26+lines*fs*1.4+sublines*19.6+(22 if it.get('tag') else 0))
            parts.append(f'<rect x="{x}" y="{y-7}" width="{content}" height="{h}" rx="16" fill="{t["card"]}" stroke="{t["border"]}"/>')
            yy=y+17
            if it.get('tag'):tx(it['tag'],yy,12,True,t['muted'],x+16,content-32);yy+=24
            if it.get('to'):tx('→',yy,16,True,t['muted'],x+content-30,20)
            yy+=tx(title,yy,fs,typ!='field',xx=x+16,ww=tw)
            if sub:tx(sub,yy+3,14,color=t['muted'],xx=x+16,ww=content-32)
            y+=h+9
        elif typ=='note':y+=tx(title,y+14,14,color=t['muted'])+24
        elif typ=='timer':
            y+=tx('01:00',y+40,42,True)+20
        elif typ=='graph':
            pts=[(x+25,y+126),(x+92,y+98),(x+170,y+106),(x+245,y+62),(x+content-25,y+26)]
            path='M'+' L'.join(f'{a} {b}' for a,b in pts)
            parts.append(f'<rect x="{x}" y="{y}" width="{content}" height="190" rx="20" fill="{t["card"]}"/><path d="{path}" fill="none" stroke="{t["primary"]}" stroke-width="3"/>')
            for a,b in pts:parts.append(f'<circle cx="{a}" cy="{b}" r="6" fill="{t["primary"]}"/>')
            tx('ILLUSTRATIVE PROGRESS · TAP A POINT',y+172,12,False,t['muted'],x+16,content-32);y+=214
        elif typ=='toggle':
            tx(title,y+24,16);parts.append(f'<rect x="{x+content-50}" y="{y+3}" width="48" height="28" rx="14" fill="{t["primary"] if it.get("on") else t["border"]}"/><circle cx="{x+content-(16 if it.get("on") else 36)}" cy="{y+17}" r="10" fill="{t["card"]}"/>');y+=68
        elif typ in ['themes','choice']:
            choices=['Light','Dark','System'] if typ=='themes' else [title]+sub.split('|')
            for i,label in enumerate(choices):y+=tx(('● ' if i==0 else '○ ')+label,y+20,16,True)+25
    for a in s['actions']:
        parts.append(f'<rect x="{x}" y="{y}" width="{content}" height="52" rx="16" fill="{t["card"] if a["secondary"] else t["primary"]}"/>')
        tx(a['label'],y+33,16,True,t['primary'] if a['secondary'] else t['onPrimary'],x+16,content-32);y+=64
    height=max(844 if width==390 else 1194,int(y+100))
    if s['tabs']:
        parts.append(f'<rect x="0" y="{height-76}" width="{width}" height="76" fill="{t["card"]}"/>')
        for i,label in enumerate(['Home','Stories','Community','Shop']):tx(label,height-33,12,True,t['muted'],i*width/4+14,width/4-16)
    annotation=f"{s['group']} / {s['id']} · Enter: {'sheet rise, 360ms spring' if s['kind']=='sheet' else 'shared layout, 360ms spring'} · Exit: reverse. Loading: shaped skeleton. Empty: explanatory copy + action. Error: inline retry. Reduced: 120ms dissolve."
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><title>{xml(s["id"]+" / "+theme)}</title>'+''.join(parts).replace('HEIGHT',str(height))+'</svg>',height,annotation

GROUPS={'A':'Entry & Account','B':'Children','C':'Home','D':'Learning flow','E':'Stories','F':'Community & Messaging','G':'Shop','H':'Utilities'}
def export_boards():
    paths=[]
    for theme,width,label in [('Wireframe',390,'01-phone-wireframes'),('Wireframe',834,'02-tablet-wireframes'),('Light',390,'03-light-screens'),('Dark',390,'04-dark-screens')]:
        folder=ROOT/'svg'/label;folder.mkdir(parents=True,exist_ok=True)
        current_ids={s['id'] for s in SCREENS}
        for retired in folder.glob('*.svg'):
            if retired.stem not in current_ids:retired.unlink()
        for g,name in GROUPS.items():
            screenlist=[s for s in SCREENS if s['group']==g]; rendered=[(s,*screen_svg(s,width,theme)) for s in screenlist];col=4;rowheight=max(r[2] for r in rendered)+220;bw=(width+80)*min(col,len(rendered))+80;bh=220+rowheight*((len(rendered)+col-1)//col)
            parts=[f'<rect width="{bw}" height="{bh}" fill="#EEEBE7"/>',svg_text(f'{g}. {name}',80,80,bw-160,36,'#282133',True)[0],svg_text(f'Little Legacy / {theme} / {width}px / connected screen inventory',80,127,bw-160,16,'#6D6479')[0]]
            for i,(s,svg,h,ann) in enumerate(rendered):
                sx=80+(i%col)*(width+80);sy=190+(i//col)*rowheight
                parts.append(svg_text(s['id'],sx,sy-24,width,14,'#282133',True)[0]);parts.append(svg.replace('<svg ',f'<svg x="{sx}" y="{sy}" ',1));parts.append(svg_text(ann,sx,sy+h+30,width,12,'#6D6479')[0]);
                (folder/(s['id']+'.svg')).write_text(svg,encoding='utf-8')
            board=ROOT/f'{label}-{g}.svg';board.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{bw}" height="{bh}" viewBox="0 0 {bw} {bh}">'+''.join(parts)+'</svg>',encoding='utf-8');paths.append(board)
    return paths

if __name__=='__main__':
    (ROOT/'screens.json').write_text(json.dumps(SCREENS,indent=2),encoding='utf-8')
    (ROOT/'design-tokens.json').write_text(json.dumps(dict(colors=TOKENS,motion=MOTION,themeStrategy='Separate Figma Light/Dark collections on Starter. System resolves live in prototype; no third static theme.'),indent=2),encoding='utf-8')
    boards=export_boards()
    shell=(ROOT/'prototype-template.html').read_text(encoding='utf-8')
    font=(ROOT/'embedded-font.css').read_text(encoding='utf-8') if (ROOT/'embedded-font.css').exists() else ''
    shell=shell.replace('<style>','<style>'+font,1)
    shell=shell.replace('__SCREEN_DATA__',json.dumps(SCREENS)).replace('__ART_DATA__',json.dumps({n:illustration(n) for n in ['plant','brand','story','video','activity','product','community']})).replace('__THEME_DATA__',json.dumps(TOKENS))
    book_data=[dict(**b,detailId=detail_id(b),chapterRoutes=chapter_ids(b),cover=cover_svg(b)) for b in BOOKS]
    shell=shell.replace('__BOOK_DATA__',json.dumps(book_data))
    shell=shell.replace('__JOURNEY_CSS__',(ROOT/'journey.css').read_text(encoding='utf-8')).replace('__JOURNEY_JS__',(ROOT/'journey.js').read_text(encoding='utf-8').replace('__FLOW_DATA__',json.dumps(FLOW)))
    (ROOT/'activity-catalog.json').write_text(json.dumps(FLOW,indent=2),encoding='utf-8')
    (ROOT/'story-catalog.json').write_text(json.dumps(book_data,indent=2),encoding='utf-8')
    (ROOT/'covers').mkdir(exist_ok=True)
    for book in BOOKS:(ROOT/'covers'/(book['id']+'.svg')).write_text(cover_svg(book),encoding='utf-8')
    (ROOT/'Little-Legacy-Prototype.html').write_text(shell,encoding='utf-8')
    print(json.dumps({'screens':len(SCREENS),'boards':len(boards),'svgScreens':len(SCREENS)*4,'prototype':str(ROOT/'Little-Legacy-Prototype.html')}))
