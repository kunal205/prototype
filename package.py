from build import *
import xml.etree.ElementTree as ET

def library():
    W=1640;H=3100;out=[f'<rect width="{W}" height="{H}" fill="#eeeae6"/>']
    def text(v,x,y,w=660,size=16,c='#282133',b=False):out.append(svg_text(v,x,y,w,size,c,b)[0])
    text('Little Legacy / Component & state library',60,75,1500,34,b=True)
    text('Editable SVG reference · Light and Dark · See motion-handoff.md for behavior',60,118,1500,16,c='#6D6479')
    for theme,x in [('Light',60),('Dark',850)]:
        t=TOKENS[theme];out.append(f'<rect x="{x-20}" y="160" width="750" height="2850" rx="24" fill="{t["bg"]}"/>');text(theme,x,206,650,25,t['text'],True);y=250
        text('01 / Buttons · 358 × 52',x,y,650,18,t['text'],True);y+=30
        for i,state in enumerate(['Default','Pressed · scale 0.97','Disabled','Submitting · width locked']):
            yy=y+i*70;out.append(f'<rect x="{x}" y="{yy}" width="358" height="52" rx="16" fill="{t["primary"]}" opacity="{.38 if i==2 else 1}"/>');text('◌ Saving…' if i==3 else 'Continue',x+20,yy+33,315,16,t['onPrimary'],True);text(state,x+390,yy+33,300,14,t['muted'])
        y+=325;text('02 / Inputs · floating labels',x,y,650,18,t['text'],True);y+=30
        for i,state in enumerate(['Default','Focused','Filled','Error · icon + message','Disabled']):
            yy=y+i*94;out.append(f'<rect x="{x}" y="{yy}" width="358" height="74" rx="14" fill="{t["card"]}" stroke="{t["primary"] if i in [1,3] else t["border"]}" stroke-width="{2 if i in [1,3] else 1}"/>');text('Email address',x+16,yy+23,325,14,t['muted']);text('! Check your email' if i==3 else 'parent@example.com' if i==2 else 'Enter email',x+16,yy+52,325,16,t['text']);text(state,x+390,yy+42,300,14,t['muted'])
        y+=505;text('03 / Cards · default / pressed / skeleton',x,y,650,18,t['text'],True);y+=28
        for i,title in enumerate(['Activity','Story','Product','Post','Level','Category']):
            yy=y+(i//2)*100;xx=x+(i%2)*345;out.append(f'<rect x="{xx}" y="{yy}" width="325" height="84" rx="18" fill="{t["card"]}" stroke="{t["border"]}"/>');text(title+' card   →',xx+16,yy+29,288,16,t['text'],True);out.append(f'<rect x="{xx+16}" y="{yy+47}" width="225" height="9" rx="4" fill="{t["border"]}"/><rect x="{xx+16}" y="{yy+63}" width="145" height="7" rx="3" fill="{t["border"]}"/>')
        y+=335;text('04 / Selection controls',x,y,650,18,t['text'],True);y+=30
        for i,title in enumerate(['☐ Checkbox → ☑ Checked','○ Radio → ● Selected','Switch OFF → ON','Dropdown → raised options sheet','Date picker → selected date + Done']):
            yy=y+i*62;out.append(f'<rect x="{x}" y="{yy}" width="670" height="50" rx="12" fill="{t["card"]}"/>');text(title,x+16,yy+31,638,16,t['text'])
        y+=345;text('05 / Sync & notification status',x,y,650,18,t['text'],True);y+=32
        for i,title in enumerate(['✓ Saved on device','◌ Syncing','✓ Synced','◷ Waiting to sync','! Failed · Retry','Notification badge: 1 / 12 / 99+']):text(title,x+16,y+i*36,630,15,t['muted'])
        y+=250;text('06 / Empty & failure states',x,y,650,18,t['text'],True);y+=35
        for title,action in [('No content yet','Explore activities'),('No results found','Clear search'),('You’re offline','Open saved content'),('Could not load','Try again')]:
            out.append(f'<rect x="{x}" y="{y}" width="670" height="87" rx="16" fill="{t["card"]}"/>');text(title,x+16,y+29,630,16,t['text'],True);text(action+' →',x+16,y+63,630,14,t['primary'],True);y+=102
        text('Motion: 150ms control / 240ms local / 360ms navigation.',x,y+20,665,14,t['muted']);text('Reduced motion: 120ms crossfade; no scale, travel or shimmer.',x,y+60,665,14,t['muted'])
    (ROOT/'05-component-state-library.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'+''.join(out)+'</svg>',encoding='utf-8')

library()
spec=[]
for s in SCREENS:
    spec.append(dict(id=s['id'],group=GROUPS[s['group']],entrance='Bottom sheet from triggering control; 360ms spring' if s['kind']=='sheet' else 'Shared card to detail, 360ms spring' if s['kind']=='detail' else 'Content enters over 360ms spring; tab routes 250ms fade and 8px settle',exit='Reverse entrance; back returns to previous screen',sharedElements=['card artwork','title'] if s['kind']=='detail' else ['plant'] if s['kind']=='celebration' else [],loading='Shaped card or field skeleton. Keep existing data during background refresh.',empty='Explain the missing content and offer a relevant next action.',error='Inline field message with icon and focus for forms; non-destructive retry for data.',reducedMotion='120ms crossfade only; all actions remain enabled.'))
(ROOT/'screen-specifications.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
motion='# Little Legacy — Connected journey handoff\n\nThe HTML prototype contains the working interactions. SVG boards are static editable references; imports do not create native Figma auto-layout, prototype connections or animation tracks.\n\n## Confirmed journey\n\n- Sign in / sign up with forms and simulated Google or Apple buttons → Home.\n- Bottom tabs: Home, Stories, Community, Shop. Profile and notification icons appear only in the Home header.\n- Home: five development categories in a bento layout, the two supplied individual YouTube links, and Level Garden.\n- Each development category has three available levels, with three distinct sample activities per level: 45 activities total.\n- Activity detail: illustration, description, materials, supplied YouTube video, Guidance / Individual choice and Start.\n- Guidance: three activity-specific steps. Individual: preset 5- or 7-minute timer, Pause / Resume and Finish early. Timer expiry also completes the activity.\n- Completion → plant growth → optional feedback → growth chart with the same level’s three activities below.\n- Feedback uses radio options: Very Satisfied, Satisfied, Neutral, Unsatisfied, Very Unsatisfied. Comment is optional; the whole page can be skipped.\n- Each completed activity adds one growth stage. Each new stage adds a leaf to the plant. Revisiting completion does not award another stage.\n- Stories: 10 illustrated sample books, wishlist, category filter, cover/title grid, detail/description and three chapters per book.\n- Each chapter has three sample main image pages. Each image automatically displays its own full-view thumbnail and two alternate-view thumbnails at the bottom, with no tap needed to reveal them. Selecting a thumbnail changes that image’s view; swiping to another main image shows only its own thumbnails. Swipe or use arrow controls; moving beyond the last page reveals next-chapter / go-back controls. The final chapter returns to the chapter list or library.\n- Chapter YouTube player is user initiated and stays visible for playback controls. Music/video selection uses the supplied links pending final chapter content.\n- Community: media/text feed, bottom message composer and attachment picker. Media or Send opens the admin-review notice with Cancel and Okay. Submission remains pending until the explicit demo admin-approval control is used. Approval creates a local notification and email preview; nothing is sent.\n- Shop: three sample playing kits with demo prices, product detail, payment-only demo checkout and confirmation. No contact-request form or sensitive payment details are collected.\n\n## Motion and accessibility\n\nNavigation enters over 360 ms using spring-like easing; tabs use a 250 ms fade. The first six cards stagger by 40 ms. Shared card / book cover transitions connect supported details. Plant growth runs once per completion for 900 ms; chart lines draw over 800 ms. Theme colors crossfade over 280 ms. The native story carousel uses scroll snapping and visible page controls.\n\nOS Reduce Motion always wins: navigation uses a 120 ms fade, plant growth stays static and page controls move instantly. System theme follows device changes live. Forms validate required fields. Feedback uses native labelled radio controls; all main actions have visible keyboard focus. Modal sheets trap keyboard focus and offer Cancel.\n\n## Persistence and boundaries\n\nProgress, feedback, wishlist, the child’s first name, demo community submissions and demo orders are saved in localStorage on this browser. Clearing browser data removes them. Passwords and form drafts are not persisted. The child date of birth is collected for the wireframe flow but not saved by this prototype. There is no real authentication, backend, payment, admin processing or email delivery.\n\nVideos: https://www.youtube.com/watch?v=r_kmNk3bcPQ and https://www.youtube.com/watch?v=NDFqrbv6hkg. YouTube playback requires internet and may depend on embedding permissions. Each player has an external YouTube link as fallback. The rest of the prototype is self-contained and includes its font and illustrations.\n\nThe growth algorithm is the user-approved temporary rule, not a developmental assessment. Illustrations, stories, activities and kit prices are sample content. Existing legal / account utility screens are layout references.\n\n## Verification\n\nSee validation-perspectives.json for the latest page-removal, navigation and automatic perspective-stack checks. validation-journey.json records the earlier complete activity journey checks. See preview-reader-perspectives*.png for current rendered reader examples. Static SVGs use simplified representations for videos, carousel, feed and progress; the HTML is the interaction reference. Cloud Figma remains partial due to the existing tool-call quota. This package does not imply the cloud file was updated.\n'
(ROOT/'motion-handoff.md').write_text(motion,encoding='utf-8')
readme=f'''# Little Legacy — Connected wireframe package

Open **Little-Legacy-Prototype.html** in your browser. Its core screens work offline (YouTube needs internet), and it contains {len(SCREENS)} connected screens. Use the left screen index on desktop, or navigate inside the phone on mobile. Theme, Wireframe, Tablet and Reduce motion controls sit outside the app.

## Import into Figma

1. Unzip this package.
2. Open your Figma file and drag in the desired SVG board. Each board is grouped exactly A–H from the brief.
3. For individual screens, use the `svg` folders; these are easier to rearrange.
4. SVGs contain editable vector shapes and text. They do **not** bring native auto-layout, component links, variable bindings or prototype connections. Use the HTML to review motion and `screen-specifications.json` plus `motion-handoff.md` for Figma wiring.

## Files

- 01-phone-wireframes-A…H.svg: all screens in grayscale at 390px.
- 02-tablet-wireframes-A…H.svg: all screens in grayscale at 834px; content capped at 600px.
- 03-light-screens-A…H.svg and 04-dark-screens-A…H.svg: all screens in both themes.
- 05-component-state-library.svg: button, input, card, selection, sync, notification and empty-state references.
- design-tokens.json: colors, spacing/motion references and physical spring constants.
- screen-specifications.json: per-screen entrance, exit, shared elements and state notes.
- motion-handoff.md: motion and accessibility matrix, implementation limits.

Long SVG screens show the complete scrolling content. The HTML uses a fixed viewport and scrolling, with persistent bottom navigation where appropriate. Example people, activity progress and story copy are illustrative. Progress, feedback, wishlist, child name, demo submissions and demo orders save locally in this browser. Authentication, payment and admin review are simulated. Passwords are never persisted. See motion-handoff.md for the complete revised flow and prototype boundaries.

## Figma file status

https://www.figma.com/design/ErNXt4S6SzvoLsYR80uiZI

Created: separate Light/Dark collections, grayscale and motion tokens, four type styles, and initial button/card/input/row/media components. The Starter plan limits collections to one mode and files to three pages. Its tool-call allowance was exhausted before screen creation and prototype wiring. The full screens and motion are delivered locally in this package; the cloud Figma file remains partial.
'''
(ROOT/'START-HERE.md').write_text(readme,encoding='utf-8')
for file in ROOT.rglob('*.svg'):ET.parse(file)
with zipfile.ZipFile(ROOT/'Little-Legacy-Figma-Import.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in ROOT.rglob('*'):
        if p.is_file() and p.suffix not in ['.zip','.py','.pyc','.cjs','.js','.css'] and 'prototype-template' not in p.name and '__pycache__' not in str(p) and p.name!='embedded-font.css':z.write(p,p.relative_to(ROOT))
print('Package complete; all SVG XML parsed.')

