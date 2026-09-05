# Little Legacy — Connected wireframe package

Open **Little-Legacy-Prototype.html** in your browser. Its core screens work offline (YouTube needs internet), and it contains 82 connected screens. Use the left screen index on desktop, or navigate inside the phone on mobile. Theme, Wireframe, Tablet and Reduce motion controls sit outside the app.

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
