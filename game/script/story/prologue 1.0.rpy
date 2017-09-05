# Prologue start : Scene 1
label pro1:

    scene bg_river with newscene

    elo "How is it now?"

    show durs longing1 normal with dissolve

    d "Better."

    elo "Yeah? That’s good."

    d disap "That was sarcasm. Can you SEE my face?"

    elo "Oh..."

    nar "I don’t know if he wants me to note the swelling from the poison or the sarcasm on his expression.{w} Or both?"

    elo "Sorry, Durs, I just need to know how much pain you’re feeling so I can -{w=.1}{nw}"

    d normal "So you can help or something?{w} Don’t worry. I’m not in pain yet, but I’m certainly not feeling better. Thanks for asking."

    nar "What does that even mean?"

    elo "Listen, I’m getting you inside those walls no matter what.{w} I’ll carry you if I have to."

    d disap ".{w=.1}.{w=.1}."

    elo "Er -{w=.25} drag you."

    d normal "Hmm that’s great."

    nar "At least I can tell that was sarcasm."

    elo "All I can ask is that you hang on."

    d "Can’t hang on if my arms explode."

    elo "Your arms won’t explode."

    d talk "Not first."
    show durs longing1 normal
    extend " My arms won’t explode first.{w} It’s the heart that goes first. Everyone knows that."

    elo "No, no one knows that. It’s a complete myth that anything will \“explode.\”"

    d "Don’t be stupid, Elorey.{w} Look, one touch and it would probably pop."

    nar "I love him too much to be offended by his words right now.{w} And I’m trying to understand what he’s going through." 
    nar "I place my hand on where his chest bulges and discolors.{w} I even give a little comforting rub."

    pause .8

    d disap "It’s not a baby, Elorey."

    elo "B-{w=.25}baby?"

    nar "Uh...now’s definitely not the time to bring up that news."

    d mad "Didn't I say not to touch it?{w} Get those hands off me."

    elo "You didn't really -{w=.1}{nw}"

    d ignore "And I’m sure this’ll hurt a whole lot more coming out."

    pause .8

    elo "Nothing’s coming out Durs!{w} You’re going to be alright."

    d disap "\“Alright,\” she says.{w} I’m growing a blue balloon in my chest and she says,{w=.1} \“Alright.\”"
    d "You can be a real airhead sometimes, you know?"
    show durs longing1 normal
    extend " But hey, I think I’m actually starting to feel better."
    d talk "The swelling’s gone down, and I’m feeling generally kinder than yesterday.{w} Maybe for once that awful intuition of yours will prove the world wrong."

    nar "Do I even try to interpret whether he really meant that?"

    show durs longing1 normal

    nar "His face is definitely getting worse.{w} And I’d say he’s lost sense of the word \“kindness...\”"

# 1st interlude
label pro2:
    scene bg_discourse with quickfade

    play music "heartofaffliction.mp3"

    dis "It’s called a longing heart, because not only does it cause the vessels to turn dark blue and swell up, but it also affects the victim emotionally by placing them in a chronic state of despair. That’s at least how he was when we first left. Everything he did felt dreadful and pointless, but this now... He’s turned into a real asshole. See, I didn’t marry a man who hated living. That’s why I chose to leave Carna and find the people who know the cure. But boy, I certainly didn’t marry an asshole. And that’s why I have to keep going and get there as fast as possible. I can’t imagine what’s next if this whole thing is not undone soon."
    
    stop music fadeout 3.0

    pause 3.0

#Scene 2
#label pro2:

    scene bg_river with quickfade #Temp. New BG should be risenian gates.

    show durs longing1 talk with dissolve

    d "Do you know why the leaders “take in” those who are diseased?{w} It’s not because we’re contagious, or you’d be affected now too."

    elo "Maybe I’m just stronger than you."

    d normal "That's real funny, Elorey."

    pause .8
    
    d talk "But seriously.{w} They're preventing people from exploding on their friends and family."

    pause .8

    d normal "Right?"

    nar "I'm just going to ignore that."

    elo "Hey look, do you see it?{w} The walls are just ahead of us."

    show bg_scene with quickfade #Temp. Use show and hide instead of scene.

    play music "riseniangates.mp3"

    elo "It really is huge."

    d talk "Ah, the fabled Kingdom of Risenia.{w} Land of uttermost gloriosity and powerfulness."
    d ignore "No way those starch-collared highlives would stop to hear our needs."

    nar "Starch?"

    elo "Look, there’s a man now coming from the gates.{w} I’m sure he’ll be willing to ride us in and prove you wrong."

    d "I hear that since they don't really have any needs, they make a sport out of doing good deeds.{w} Whoever receives the loudest praise is the winner."

    elo "He seems like a very nice and helpful man."

    d "And you're an extra winner if you can grab the King’s attention."

    elo "Here he comes."

    hide bg_scene with quickfade

    d talk "Hey, maybe he'll be more likely to receive us if we praise his horse."

    elo "Excuse me, sir. May we ask a favor of you?"

    show durs longing1 normal:
        xalign .25, yalign 1.0
    with move
    
    show leyna normal:
        xalign .75, yalign 1.0
    with dissolve

    Kris "Oh graces, what is this now? I’m being stopped by outsiders?"

    elo "You're from the Kingdom, right?{w} We’re villagers from Carna."

    Kris "What has given these tribal fools the idea -{w=.1}{nw}"

    show durs longing1 talk
    d "Good sir of Risenia, what a fine steed you have there."
    show durs longing1 normal
    extend "..much indeedily."

    Kris "Why thank -{w=.1}{nw}"
    Kris "Wait, do they further mock me or is this sincere adoration? I’ve never encountered this sort of person before."

    nar "He continues to think aloud to himself..."

    Kris "Best to move on before they decide to ask something of me."

    hide leyna normal with dissolve

    elo "Please wait, sir! We need to ask something of you."

    show leyna normal:
        xalign .75, yalign 1.0
    with dissolve

    Kris "*sigh* Alas it is too late."
    Kris "You there, travelers!{w=.25} What reason, if any, may I ask, do you have for stopping a knight of Risenia amidst his afternoon joyride?"

    elo "My name is Elorey, and this is my husband Durs.{w} As I think you can tell, he’s terribly ill."

    d mad "Woah, watch the language, woman."

    pause .8

    elo "Modestly infected...?"

    d disap ".{w=.1}.{w=.1}."

    pause .8

    elo "He’s just a little sick.{w=.1} And your people are said to be the only ones who can help.{w} I only ask that you give us a ride into the gates so he can get treated as soon as possible."

    Kris "Oh for goodness{w=.1}.{w=.1}.{w=.1}.{w} Oh for goodness graces{w=.1}.{w=.1}.{w=.1}.{w} People,{w=.25} can’t you see that there’s NO ONE around?"
    Kris "Why in the King’s name would you then ask me for assistance?"

    d mad "Well gosh, you high-horsed hooligan. Isn’t that EXACTLY the reason we need help from you?"

    Kris "Oh, well gosh, you blue-faced balloon-bottomed buffoon.{w} Isn’t that exactly why I shouldn’t?{w} Who else here would vouch for my actions?"
    Kris "Certainly not the{w=.1} \“fine steed\” I{w=.1} \“much indeedily\” have here."

    d normal "Vouch?"

    elo "Vouch?"

    d disap "Balloon?{w=.25}{nw}" #Longer interruption wait than usual.

    Kris "Alas, these foreigners really are as absent as they come."
    Kris "Now, listen you travelers, I have no more time for this empty form of chatter.{w} Go back to your land, and stay away from ours."

    elo "Is he being serious?"

    Kris "Off we go, my fine steed!"

    d ignore "He’s seriously leaving."

    hide leyna normal
    stop music

    pause .8

    elo "He left!"

    show durs longing1:
        center
    with move

    d normal "Wow. I should be happy to prove you wrong, but it really sucks in this sort of situation."
    show durs longing1 talk
    extend " You feel?"

    elo "He was just one person."

    d "Yep, and there’s a whole kingdom of them behind those walls just waiting for us."
    show durs longing1 ignore
    extend " Or -{w=.25} probably not waiting for us."

    elo "What do you think he meant by vouch for him?"

    d "...probably waiting for the chance to kick us out at least."

    elo "Hey."

    d disap "What?{w} What do you want, woman?{w} Still don’t get it?"

    elo "Well, I meant{w=.1}{nw}"

    d normal "It’s like I told you. The little game they play.{w} No one’s here to watch him pull a favor, so he decides it’s a waste of his time.{w} I thought that was obvious by now."

    elo "Durs...{w=.1}{nw}"

    d disap "Come on, Elorey, I don’t remember you ever being so ignorant.{w} I thought I at least married a little better."

    elo ".{w=.1}.{w=.1}."
    elo "Fine, you were right.{w} That what you want to hear?"

    d talk "Louder please."

    elo "Ugh. So what?!{w} Let's say they're all turds.{w=.1} They'll be dying to help once we’re inside and there’s an audience available, right?"

    nar "I can’t get mad too..."

    elo "It doesn’t end like this.{w} It can’t..."

    d normal "We’ll see about that. I’m sure they’ll have loads more excuses."

    nar "Does this guy even want to be cured?"

    d disap "And no more asking people for help before we get there.{w} Save us the embarrassment, please."

    elo "Ok..."

    pause .8

    d talk "Oh by the way.{w} About my balloon bottom."

    elo "Yeah...?"

    d ignore "Has it really gotten that bad?"

    show bg_scene with quickfade #Temp.

    nar "What sounded like a childish little insult in response to his own cheesy taunts, turns out to be pretty telling of his situation."
    nar "Not only have his heart and the vessels in his face engorged, but a lot of that stuff is pumping uncontrollably to his extremities."

    elo "Like I said.{w} I’ll drag you if I have to."

# Second interlude : Note there is no music this time.
    scene bg_discourse with quickfade

    dis "What is \“that stuff\” exactly though? Besides blue and thick and absolutely frustrating to deal with for the both of us? I don’t know much else. It’s obviously strong enough to change the man I love into a completely different person. How though? Why? I’m not sure anyone knows. But I don’t have to understand how it works. I just have to believe there’s a way to get it out. Without exploding. I can’t afford for him to prove me wrong again."

# FADE BACK TO CHARACTER VIEW
# CONTINUE AT 0.2