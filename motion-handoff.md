# Little Legacy — Connected journey handoff

The HTML prototype contains the working interactions. SVG boards are static editable references; imports do not create native Figma auto-layout, prototype connections or animation tracks.

## Confirmed journey

- Sign in / sign up with forms and simulated Google or Apple buttons → Home.
- Bottom tabs: Home, Stories, Community, Shop. Profile and notification icons appear only in the Home header.
- Home: five development categories in a bento layout, the two supplied individual YouTube links, and Level Garden.
- Each development category has three available levels, with three distinct sample activities per level: 45 activities total.
- Activity detail: illustration, description, materials, supplied YouTube video, Guidance / Individual choice and Start.
- Guidance: three activity-specific steps. Individual: preset 5- or 7-minute timer, Pause / Resume and Finish early. Timer expiry also completes the activity.
- Completion → plant growth → optional feedback → growth chart with the same level’s three activities below.
- Feedback uses radio options: Very Satisfied, Satisfied, Neutral, Unsatisfied, Very Unsatisfied. Comment is optional; the whole page can be skipped.
- Each completed activity adds one growth stage. Each new stage adds a leaf to the plant. Revisiting completion does not award another stage.
- Stories: 10 illustrated sample books, wishlist, category filter, cover/title grid, detail/description and three chapters per book.
- Each chapter has three sample main image pages. Each image automatically displays its own full-view thumbnail and two alternate-view thumbnails at the bottom, with no tap needed to reveal them. Selecting a thumbnail changes that image’s view; swiping to another main image shows only its own thumbnails. Swipe or use arrow controls; moving beyond the last page reveals next-chapter / go-back controls. The final chapter returns to the chapter list or library.
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

See validation-perspectives.json for the latest page-removal, navigation and automatic perspective-stack checks. validation-journey.json records the earlier complete activity journey checks. See preview-reader-perspectives*.png for current rendered reader examples. Static SVGs use simplified representations for videos, carousel, feed and progress; the HTML is the interaction reference. Cloud Figma remains partial due to the existing tool-call quota. This package does not imply the cloud file was updated.
