import glob
import json

from sys import exit, argv
from example_blacklist import blacklist
from hifi.sentiment import classifier_for_training_set, \
                           positive_sentiment_for_sentences

positive_feedback = [
    'kudos on the app',
    'I love you guys',
    'Thank you for adding the podcasts!',
    'Thanks so much!',
    'Keep up the great work!',
    'Thanks for any help',
    'Thanks for the hard work that you put into the apps',
    'Love the layout',
    'Its much easier to navigate',
    'I really like the set up',
    'Awesome iPad app thank you',
    'This design is awesome',
    'this is an excellent app',
    'Love love love them',
    'Love the app!',
    'Nice app',
    'I love it that you guys are revamping your app',
    'The look is really refreshing',
    'Nice upgrade',
    'Great look for the app',
    'Thanks for all the awesome info you guys provide',
    'I religiously read up and follow your news',
    'You guys are amazing!!',
    'Thanks for updating this app!',
    'Hey I Love this new setup thanks',
    'great app and probably my most used app!',
    'Great app',
    'Nice overall',
    'app is king',
    'Great work',
    'Love this new app version!!!',
    'Great job with the new ipad update!',
    'Love the new layout',
    'Best regards',
    'Like the done, previous, next arrows',
]

negative_feedback = [
    'Im having crashing to desktop whenever I try to watch a video',
    'I am very confused by your latest update to this app',
    'I dont like that you cannot use the app in portrait viewing',
    'The layout is not as good as the one before and the Recent videos dont show any videos at all',
    'I cant get past the loading screen whenever I choose any option (news, game reviews, etc.)',
    'your app is pretty buggy',
    'I cant stand it',
    'Im about ready to give up',
    'Also, i dislike the format of four stories per row',
    'Big downgrade',
    'If this is not addressed you will be losing me as a reader',
    'Hate the layout of your site',
    'Boring app',
    'Um why is the resolution so horrible on the iPad version of your app?',
    'It is seriously horrible',
    'This app is junk nothing refreshes I cant forward things like I could in the old app',
    'Not the best update',
    'Looks muddy and just terrible to look at',
    'Also, forcing it into landscape view is really annoying',
    'Shits garbage fix it',
    'closes unexpectedly from time to time',
    'Search engine not working',
    'It then wont allow me to play any more videos',
    'an error that occurs',
    'cannot load movie',
    'It still crashes every time I scroll down the comment section too fast',
    'I think the comment system needs to be completely overhauled',
    'I have one problem!',
    'fail',
    'In fact, it makes it worse',
    'Reviews dont load to review section',
    'App is repeatedly crashing while viewing',
    'Slow when attempting to open up the news, upcoming etc',
    'So much space is wasted and makes it longer and harder to read!',
    'This sucks worse than the clumsy previous iteration of the actual website',
    'Fix the crashes',
    'Many videos dont load',
    'The app freezes a lot and crashes please fix this!',
    'Please fix the videos load!!',
    'This app is awful',
    'I dont know why but please fix',
    'Please hurry and fix the reviews',
    'The review section has a long loading time',
    'Make it 3G compatible!!',
    'It crashes',
    'It just keeps crashing!',
    'sucks man',
    'Please fix the resolution to hd',
    'Videos are constantly out of sync',
    'Videos just do not work properly',
    'I am very confused by your latest update to this app',
    'I really dont like the new update for the iPad',
    'This new app for ipad is way too sensitive',
    'It was much easier to browse stories when they were in a vertical list',
    'Hate the new layout of your site',
    'The new app format is frustrating',
    'it does not work good',
    'I can not access podcasts',
    'text is really bad',
    'looks bad',
    'terrible implementation',
]

if len(argv) < 2:
    print 'usage: python example_sentiment.py <preprocessor-files>' 
    exit(-1)

sentiment = 0

classifier = classifier_for_training_set(positive_feedback, negative_feedback,
                                         blacklist)

paths = argv[1:]
for path in paths:
    with open(path, 'r') as f:
        sentiment += positive_sentiment_for_sentences(classifier,
                                                      json.load(f)['sentences'])

print sentiment / len(paths)
