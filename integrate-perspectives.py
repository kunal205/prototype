from pathlib import Path
root=Path(__file__).parent
p=root/'journey.js';s=p.read_text(encoding='utf-8')
old='<article class="story-page">${storyScene(b,p)}<p>'
new='<article class="story-page">${storyPageImage(b,p,s.id)}<p>'
assert old in s;s=s.replace(old,new)
old="st.pages[id]=n;current.querySelector('.reader-position')"
new="st.pages[id]=n;car.querySelectorAll('.story-page,.chapter-end').forEach((slide,i)=>{slide.inert=i!==n;const stack=slide.querySelector('.perspective-stack');if(stack)stack.hidden=i!==n;});current.querySelector('.reader-position')"
assert old in s;s=s.replace(old,new)
old="car.scrollLeft=(st.pages[id]||0)*car.clientWidth;car.addEventListener('scroll',sync"
new="car.scrollLeft=(st.pages[id]||0)*car.clientWidth;sync();car.addEventListener('scroll',sync"
assert old in s;s=s.replace(old,new)
s=s.replace('Swipe between three image pages. Swipe past the last image to reveal chapter navigation. Music starts only when you press Play.','Each image automatically shows its own alternate-view thumbnails at the bottom. Swiping changes the main image and its views. Swipe past image 3 for chapter navigation.')
p.write_text(s,encoding='utf-8')
p=root/'package.py';s=p.read_text(encoding='utf-8')
s=s.replace('Each chapter has three sample image pages. Swipe or use arrow controls;', 'Each chapter has three sample main image pages. Each image automatically displays its own full-view thumbnail and two alternate-view thumbnails at the bottom, with no tap needed to reveal them. Selecting a thumbnail changes that image’s view; swiping to another main image shows only its own thumbnails. Swipe or use arrow controls;')
p.write_text(s,encoding='utf-8')
