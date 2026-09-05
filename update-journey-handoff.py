from pathlib import Path
root=Path(__file__).parent
p=root/'package.py';s=p.read_text(encoding='utf-8')
start=s.index("motion='''");end=s.index("(ROOT/'motion-handoff.md')",start)
s=s[:start]+'''motion='''+repr('''# Little Legacy — Connected journey handoff

The HTML prototype contains the working interactions. SVG boards are static editable references; imports do not create native Figma auto-layout, prototype connections or animation tracks.

## Confirmed journey

- Sign in / sign up with forms and simulated Google or Apple buttons → child name and date of birth → Home.
- Bottom tabs: Home, Stories, Community, Shop. Profile remains in the header.
- Home: five development categories in a bento layout, the two supplied individual YouTube links, and Level Garden.
- Each development category has three available levels, with three distinct sample activities per level: 45 activities total.
- Activity detail: illustration, description, materials, supplied YouTube video, Guidance / Individual choice and Start.
- Guidance: three activity-specific steps. Individual: preset 5- or 7-minute timer, Pause / Resume and Finish early. Timer expiry also completes the activity.
- Completion → plant growth → optional feedback → growth chart with the same level’s three activities below.
- Feedback uses radio options: Very Satisfied, Satisfied, Neutral, Unsatisfied, Very Unsatisfied. Comment is optional; the whole page can be skipped.
- Each completed activity adds one growth stage. Five stages grow a plant; the next activity begins another plant. Revisiting completion does not award another stage.
- Stories: 10 illustrated sample books, wishlist, category filter, cover/title grid, detail/description and three chapters per book.
- Each chapter has three sample image pages. Swipe or use arrow controls; moving beyond the last page reveals next-chapter / go-back controls. The final chapter returns to the chapter list or library.
- Chapter YouTube player is user initiated and stays visible for playback controls. Music/video selection uses the supplied links pending final chapter content.
- Community: media/text feed, bottom message composer and attachment picker. Media or Send opens the admin-review notice with Cancel and Okay. Submission remains pending until the explicit demo admin-approval control is used. Approval creates a local notification and email preview; nothing is sent.
- Shop: three sample playing kits with demo prices, product detail, payment-only demo checkout and confirmation. No contact-request form or sensitive payment details are collected.

## Motion and accessibility

Navigation enters over 360 ms using spring-like easing; tabs use a 250 ms fade. The first six cards stagger by 40 ms. Shared card / book cover transitions connect supported details. Plant growth runs once per completion for 900 ms; chart lines draw over 800 ms. Theme colors crossfade over 280 ms. The native story carousel uses scroll snapping and visible page controls.

OS Reduce Motion always wins: navigation uses a 120 ms fade, plant growth stays static and page controls move instantly. System theme follows device changes live. Forms validate required fields. Feedback uses native labelled radio controls; all main actions have visible keyboard focus. Modal sheets trap keyboard focus and offer Cancel.

## Persistence and boundaries

Progress, feedback, wishlist, the child’s first name, demo community submissions and demo orders are saved in localStorage on this browser. Clearing browser data removes them. Passwords and form drafts are not persisted. The child date of birth is collected for the wireframe flow but not saved by this prototype. There is no real authentication, backend, payment, admin processing or email delivery.

Videos: https://www.youtube.com/watch?v=r_kmNk3bcPQ and https://www.youtube.com/watch?v=NDFqrbv6hkg. YouTube playback requires internet and may depend on embedding permissions. Each player has an external YouTube link as fallback. The rest of the prototype is self-contained and includes its font and illustrations.

The growth algorithm is the user-approved temporary rule, not a developmental assessment. Illustrations, stories, activities and kit prices are sample content. Existing legal / account utility screens are layout references.

## Verification

See validation-journey.json for the current interaction checks and preview-*-new.png for rendered examples. Static SVGs use simplified representations for videos, carousel, feed and progress; the HTML is the interaction reference. Cloud Figma remains partial due to the existing tool-call quota. This package does not imply the cloud file was updated.
''')+'\n'+s[end:]
s=s.replace('It works offline and contains','Its core screens work offline (YouTube needs internet), and it contains')
s=s.replace('Forms store draft text only in session memory, with no real sign-in, message, purchase or data request.','Progress, feedback, wishlist, child name, demo submissions and demo orders save locally in this browser. Authentication, payment and admin review are simulated. Passwords are never persisted. See motion-handoff.md for the complete revised flow and prototype boundaries.')
s=s.replace("p.suffix not in ['.zip','.py','.pyc','.cjs']","p.suffix not in ['.zip','.py','.pyc','.cjs','.js','.css']")
p.write_text(s,encoding='utf-8')
