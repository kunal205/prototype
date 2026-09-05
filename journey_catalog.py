"""Approved sample content and revised connected prototype screens."""
VIDEOS = ['r_kmNk3bcPQ', 'NDFqrbv6hkg']
SATISFACTION = ['Very Satisfied', 'Satisfied', 'Neutral', 'Unsatisfied', 'Very Unsatisfied']

# Each activity has its own instructions, materials and preset duration.
SEEDS = {
 'Cognitive': [
 ('Colour hunt','Safe household objects','Find an object in a colour you choose.|Find another match and compare their shapes.|Sort your finds by colour and name each group.'),
 ('Shape detectives','Large paper shapes','Choose a circle, square and triangle.|Look for those shapes around the room.|Put the shapes together to make a picture.'),
 ('Match my pair','Three pairs of everyday objects','Lay out one object from each pair.|Invite your child to find each matching object.|Mix them and try a new arrangement.'),
 ('Pattern parade','Large coloured blocks','Make a red-blue-red-blue pattern.|Invite your child to add the next block.|Create a new pattern together.'),
 ('What is missing?','Four familiar objects and a cloth','Name the objects together.|Cover them and remove one.|Uncover the objects and guess what is missing.'),
 ('Sort it your way','Large blocks in different shapes','Explore how the blocks are alike.|Sort them by shape or colour.|Try sorting the same blocks a different way.'),
 ('Build a bridge','Large building blocks and a toy','Place two blocks apart like riverbanks.|Try ways to bridge the gap.|Test the bridge with a lightweight toy and adjust it.'),
 ('Picture sequence','Three drawings of a daily routine','Talk about what each picture shows.|Place the pictures in the order things happen.|Tell the little story from beginning to end.'),
 ('Clue trail','Three familiar toys','Choose a toy and give a simple clue.|Let your child explore and find the match.|Swap roles and listen to your child’s clues.')],
 'Physical': [
 ('Animal moves','A clear soft play space','Stretch tall like a giraffe.|Walk slowly like a bear.|Choose an animal and invent its movement.'),
 ('Roll to me','A soft large ball','Sit facing each other.|Roll the ball gently between you.|Move a little farther apart and try again.'),
 ('Follow the footprints','Large paper footprints','Place footprints along a clear path.|Step slowly from one to the next.|Try a new path with gentle turns.'),
 ('Balance trail','Masking tape on a flat floor','Make a short tape line.|Walk along it with arms stretched out.|Try carrying a soft toy as you walk.'),
 ('Toss and land','Soft beanbags and a wide basket','Place the basket close by.|Toss a beanbag gently into it.|Adjust the distance to keep it comfortable.'),
 ('Stretch like a tree','A clear play space','Plant your feet comfortably.|Raise your arms like growing branches.|Sway gently and come back to the middle.'),
 ('Little obstacle path','Cushions and a clear floor','Arrange a low, stable cushion path.|Step around or over each cushion with support.|Let your child suggest the next route.'),
 ('Move and freeze','A clear play space','Choose a favourite movement.|Say freeze and balance in place.|Take turns calling move and freeze.'),
 ('Ribbon dance','A short wide fabric strip','Wave the fabric slowly from side to side.|Draw big circles in the air.|Make up a short dance together.')],
 'Emotional': [
 ('Feeling faces','A mirror','Make a happy face together.|Try a sad or surprised face.|Name a time you felt that way.'),
 ('My calm breath','A quiet place','Sit comfortably together.|Smell an imaginary flower slowly.|Blow an imaginary candle gently and repeat.'),
 ('Today feels like','Paper and crayons','Choose a colour for your feeling.|Draw marks that show that feeling.|Listen as your child tells you about the picture.'),
 ('Feelings weather','Paper and crayons','Imagine feelings as sunny, cloudy or rainy.|Draw today’s feelings weather.|Talk about what might help on a cloudy day.'),
 ('A cosy corner','A cushion and favourite toy','Find a comfortable quiet spot.|Choose something that feels comforting.|Practise asking for a little quiet time.'),
 ('Name that feeling','A favourite toy','Act out a toy losing something.|Ask how the toy might feel.|Find a kind way to help the toy.'),
 ('Brave little try','Paper and crayons','Talk about something new to try.|Draw one small first step.|Celebrate the effort of trying that step.'),
 ('My helpful words','Two soft toys','Let one toy feel frustrated.|Practise words such as I need help.|Use the words in a gentle pretend conversation.'),
 ('Feelings journey','Paper and crayons','Recall a small moment from today.|Draw how the feeling changed.|Talk about what helped along the way.')],
 'Social': [
 ('My turn, your turn','A soft ball','Say my turn before rolling the ball.|Invite your child to say your turn.|Keep taking turns at a comfortable pace.'),
 ('Hello little friend','A favourite toy','Say hello to the toy by name.|Ask the toy a friendly question.|Let your child answer and ask a question too.'),
 ('Build together','Large building blocks','Choose something to build together.|Add one block each in turn.|Give your creation a shared name.'),
 ('Kindness delivery','Paper and crayons','Think of someone to thank.|Draw a little picture for them.|Practise a kind sentence to go with it.'),
 ('Listen and draw','Paper and crayons','Describe a simple shape.|Listen as your child draws it.|Swap roles and follow their description.'),
 ('Our shared picnic','Toy cups and plates','Set a pretend place for each toy.|Share the pretend food fairly.|Ask each toy what it would like.'),
 ('Solve it together','Two toys and one toy car','Pretend both toys want the car.|Think of ways they could take turns.|Try one idea and talk about how it feels.'),
 ('Team treasure map','Paper and crayons','Draw a map to a familiar toy.|Choose one job for each person.|Follow the map together and celebrate teamwork.'),
 ('Little helpers','A few clean play items','Choose a small task together.|Let each person pick one part.|Finish together and thank each other.')],
 'Creative': [
 ('Scribble garden','Paper and washable crayons','Make a few playful marks.|Turn one mark into a leaf or flower.|Add an imaginary creature to your garden.'),
 ('Cloud stories','Paper and crayons','Draw a soft cloud shape.|Imagine what it could become.|Tell a little story about your cloud.'),
 ('Sound explorers','Hands and a clear space','Make a quiet clap or tap.|Copy each other’s sound.|Combine your sounds into a rhythm.'),
 ('Paper creatures','Large paper pieces and a glue stick','Arrange paper into a creature.|Choose its eyes, wings or feet.|Name it and describe where it lives.'),
 ('Paint a rhythm','Paper and washable crayons','Tap a gentle rhythm together.|Draw lines that follow the rhythm.|Change the rhythm and add new marks.'),
 ('My pretend shop','Safe everyday play objects','Arrange objects in a pretend shop.|Invent names for what you sell.|Take turns being shopkeeper and visitor.'),
 ('Invent a vehicle','Large blocks','Imagine a vehicle for a special journey.|Build it with blocks.|Explain its special features through pretend play.'),
 ('A story in three pictures','Paper and crayons','Draw a character and a place.|Draw something surprising that happens.|Draw an ending and tell the whole story.'),
 ('Our little show','Toys and a small clear stage','Choose characters for a short show.|Practise a beginning, middle and ending.|Perform together and celebrate every idea.')]
}
ACTIVITIES=[]
for category, entries in SEEDS.items():
 for n,(title,materials,steps) in enumerate(entries):
  ACTIVITIES.append(dict(id=category.lower()+'-'+str(n+1),category=category,level=n//3+1,title=title,materials=materials,steps=steps.split('|'),seconds=300 if n<6 else 420,video=VIDEOS[n%2],description=steps.split('|')[0]+' A playful moment to explore '+category.lower()+' development together.'))
KITS=[dict(id='discovery',title='Little discovery kit',price=499,description='Large sorting shapes, colour cards and playful discovery prompts.'),dict(id='creative',title='Little makers kit',price=649,description='Paper shapes, washable crayons and imaginative making prompts.'),dict(id='movement',title='Move & play kit',price=799,description='A soft ball, floor markers and movement activity cards.')]
FLOW=dict(activities=ACTIVITIES,kits=KITS,videos=VIDEOS,satisfaction=SATISFACTION)

def export_items(items):
 """Static equivalents for the editable SVG reference boards."""
 out=[]
 for it in items:
  typ=it['type'];title=it.get('title','')
  if typ in ['activity-image','growth-plant','carousel']:
   out += [dict(type='art',title='plant' if typ=='growth-plant' else 'story' if typ=='carousel' else 'activity')]
   if typ=='carousel':out += [dict(type='perspective-strip',title='Full view · Two alternate views'),dict(type='note',title='Each image automatically shows its own alternate views at the bottom. Swipe past image 3 for Go to next chapter / Go back.'),dict(type='row',title='Previous page     Page 1 of 3     Next page',to='')]
   if typ=='growth-plant':out += [dict(type='note',title='One completed activity = one growth stage, adding one new leaf.')]
  elif typ=='video':out += [dict(type='art',title='video'),dict(type='row',title=title+' · Play',sub='youtube.com/watch?v='+it['video'],to='')]
  elif typ=='mode':out += [dict(type='choice',title='Guidance · Three steps together',sub='Individual · Preset timer')]
  elif typ=='satisfaction':out += [dict(type='choice',title=SATISFACTION[0],sub='|'.join(SATISFACTION[1:]))]
  elif typ=='growth-chart':out += [dict(type='graph',title=title)]
  elif typ=='story-tools':out += [dict(type='row',title='♡ Wishlist                         ☷ Filter',to='')]
  elif typ=='community-feed':out += [dict(type='art',title='community'),dict(type='card',title='Little Legacy team',sub='Small wins deserve a little celebration. What did your little one discover today?'),dict(type='art',title='activity'),dict(type='card',title='A little creative moment',sub='A few crayons and a shared story can turn an ordinary afternoon into an adventure.'),dict(type='field',title='Message the community',sub='＋ Add media                                  Send',input='textarea')]
  elif typ=='kit-list':
   for k in KITS:out += [dict(type='art',title='product'),dict(type='card',title=k['title'],sub=k['description']+' · ₹'+str(k['price'])+' demo price',to='product')]
  else:out.append(it)
 return out

def revise(screens):
 def update(id,**changes):
  s=next(s for s in screens if s['id']==id);s.update(changes);return s
 def note(text):return dict(type='note',title=text)
 def row(title,to,sub=''):return dict(type='row',title=title,to=to,sub=sub)
 def card(title,sub='',to='',tag=''):return dict(type='card',title=title,sub=sub,to=to,tag=tag)
 def art(title):return dict(type='art',title=title)
 def action(label,to,secondary=False):return dict(label=label,to=to,secondary=secondary)
 def field(title,sub='',input='text'):return dict(type='field',title=title,sub=sub,input=input)
 def add(id,group,title,items,actions=[],kind='standard',sub='',tabs=False):screens.append(dict(id=id,group=group,title=title,sub=sub,items=items,actions=actions,kind=kind,tabs=tabs))
 for id in ['signin','signup']:
  s=next(s for s in screens if s['id']==id)
  s['items']=[it for it in s['items'] if 'I agree' not in it['title']]
  s['items'] += [row('Continue with Google','@auth-google'),row('Continue with Apple','@auth-apple'),note('Demo sign-in · No account is created or connected.')]
  s['actions']=[action('Sign in' if id=='signin' else 'Create account','child-setup'),action('Create an account' if id=='signin' else 'Already have an account?','signup' if id=='signin' else 'signin',True)]
 update('child-setup',items=[field('Child’s first name','First name'),field('Date of birth','','date')],actions=[action('Continue to Home','@child-save')])
 update('levels',items=[card(f'Level {i}', '3 activities · Available to try',f'@level-{i}','EXPLORE AT YOUR PACE') for i in range(1,4)])
 update('categories',title='Every way to grow',items=[row(c+' development','@category-'+c) for c in SEEDS])
 update('activities',items=[card(a['title'],a['description'],'@activity-'+a['id'],'5 MIN') for a in ACTIVITIES[:3]])
 update('activity',items=[art('activity'),note(ACTIVITIES[0]['description']),card('What you’ll need',ACTIVITIES[0]['materials']),dict(type='video',title='Activity video',video=VIDEOS[0]),dict(type='mode',title='Choose your mode')],actions=[action('Start activity','@start')])
 for n,id in enumerate(['steps','step-2','step-3']):
  update(id,kind='guided',title=ACTIVITIES[0]['steps'][n],items=[art('activity'),note(ACTIVITIES[0]['steps'][n])],actions=[action('Complete activity' if n==2 else 'Next step','@complete' if n==2 else ['step-2','step-3'][n])])
 add('individual','D','Play at your own pace',[art('activity'),dict(type='timer',title='05:00'),row('Pause timer','@pause')],[action('Finish early','@complete')],kind='individual',sub='Colour hunt · 5 minutes')
 update('celebration',items=[dict(type='growth-plant',title='Your growing garden'),note('One completed activity adds one growth stage.')],actions=[action('Continue to feedback','feedback')])
 update('feedback',title='How was this activity?',sub='Overall, how satisfied were you with the activity?',items=[dict(type='satisfaction',title='Satisfaction',options=SATISFACTION),field('Anything you’d like to remember?','Optional comment','textarea')],actions=[action('Save feedback','@feedback-save'),action('Skip feedback','@feedback-skip',True)],kind='feedback')
 update('progress',items=[dict(type='growth-chart',title='Your activity growth'),note('More activities from this level'),*[card(a['title'],a['description'],'@activity-'+a['id']) for a in ACTIVITIES[:3]]])
 update('history',items=[note('Completed activities will appear here.')])
 update('history-detail',items=[note('Your saved activity and feedback will appear here.')])
 update('stories',items=[dict(type='story-tools',title='Your story shelf'),*next(s for s in screens if s['id']=='stories')['items']])
 for s in screens:
  if s['kind']=='reader':
   s['items']=[dict(type='carousel',title=s['title'],bookId=s['bookId']),dict(type='video',title='Chapter background music',video=VIDEOS[1])]
   s['actions']=[]
 update('community',title='Little Legacy Community',sub='Little moments, shared together.',kind='community',items=[dict(type='community-feed',title='Community updates')])
 add('community-review','F','Share with the community?', [note('Everything you share will be verified by an admin before it appears in the community. You’ll receive an app notification and email when there is an update.'),note('This prototype previews the review process. It sends no messages or emails.')],[action('Okay','@community-confirm'),action('Cancel','@community-cancel',True)],kind='sheet')
 update('message',title='Share a little moment',items=[field('Message','Message the community','textarea')],actions=[action('Review message','@community-review')])
 update('post',actions=[action('Back to community','community')])
 update('shop',items=[dict(type='kit-list',title='Playing kits')],sub='Three little ways to play. Demo prices.')
 update('product',items=[art('product'),card('Inside the kit',KITS[0]['description']),note('₹499 · Demo price')],actions=[action('Continue to payment','checkout')])
 add('checkout','G','Payment',[art('product'),card('Little discovery kit','₹499 · Demo total'),note('Demo checkout · No card details needed. No money will be charged.')],[action('Simulate payment','@pay'),action('Cancel','product',True)],sub='Review your kit and payment total.')
 add('payment-complete','G','Demo payment complete',[art('product'),note('Your simulated order is confirmed. No money was charged.')],[action('Back to shop','shop')])
 # Retain old bookmarked routes as explanatory redirects, removing the obsolete request flow.
 for id in ['request','review','request-received']:
  update(id,title='Shop payment',sub='Playing kits now use the payment flow.',items=[row('Continue to payment','checkout')],actions=[])
 update('help-detail',items=[note('Choose a development category, level and activity. Guidance mode walks through three steps. Individual mode has a preset timer with Pause and Finish early. Completion grows your plant, followed by optional feedback and your growth chart.')])
 update('notifications',items=[note('Community review updates will appear here. No email is sent by this prototype.')])
 update('submitted',title='Waiting for admin review',sub='Your sample submission is saved on this device.',items=[note('The admin review and email are simulated in this prototype.')])
 # Remove the retired pages and consolidate the duplicate payment references.
 removed={'launch','welcome','recovery','child-setup','home-offline','categories','story-unavailable','story-empty','post','message','notification','help-detail','data-requests','data-form','data-received','review','request-received'}
 redirects={'review':'request','request-received':'request','message':'community','post':'community','notification':'notifications','welcome':'signin','launch':'signin','child-setup':'home'}
 screens=[s for s in screens if s['id'] not in removed]
 for s in screens:
  s['items']=[it for it in s['items'] if it.get('to') not in removed or it.get('to') in redirects]
  s['actions']=[a for a in s['actions'] if a.get('to') not in removed or a.get('to') in redirects]
  for item in [*s['items'],*s['actions']]:
   if item.get('to') in redirects:item['to']=redirects[item['to']]
 return screens
