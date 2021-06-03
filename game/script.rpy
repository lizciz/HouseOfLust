# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n2 = Character("Narrator")

define m = Character("[p_nn_m!c]", color="#ffe169")
define b = Character("[p_nn_b!c]", color="#cf3723")
define l = Character("[p_nn_l!c]", color="#e072ce")
define p = Character(p_n, color="#5879cc")

transform centerleft:
    xalign .35 yalign 1.0

transform centerright:
    xalign .65 yalign 1.0

#define centerleft = Position(xpos=0.5, ypos=0.5)
#define centerright = Position(xpos=0.5, ypos=0.5)



# The game starts here.

label day01:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene house driveway car night nolights

    m "Look, there it is."
    b "Oh wow, looks pretty big."
    p "Yeah."
    m "There should be a garage. Drive a bit further up."
    p "Uhm..."
    extend "\nYep, I see it."
    "You pull up to the garage."
    m "Leave your bags for now, let's check it out first."

    scene black

    "You walk up to the front door together, and [p_nn_m] takes up the keys and open the door."
    m "Let's see if we can find a light switch."
    "..."
    m "Ah, here we go."

    scene house hallway first_entry

    show mom casual at right:
        zoom 0.5
    m "Well, the lights are working!"

    show bigsister casual at left:
        zoom 0.5
    b "Ooh, looks pretty fancy."

    show littlesister casual at centerleft:
        zoom 0.5
    l "Looks pretty old, if you ask me..."
    m "That's to be expected, it is quite old. But it certainly would have been fancy in its day."

    show player casual at centerright:
        zoom 0.5
    p "You said it had been renovated, right?"
    m "Oh yes, it should have full utilities, but also a lot of its original furnishing."
    m "Let's explore a bit. There should be enough bedrooms for all of us."

    b "Looks like a dining room in here."
    scene house dining_room night
    $ renpy.pause()

    show bigsister casual at right:
        zoom 0.5
    b "Hm, nice."
    show player casual at left:
        zoom 0.5
    p "If this is the dining room, I'd guess that the kitchen is close by."

    scene house kitchen night
    $ renpy.pause()
    
    show littlesister casual at left:
        zoom 0.5
    l "Ugh, I thought you said it was renovated?"
    show mom casual at right:
        zoom 0.5
    m "Well, yes, some of it should be. But as I said, a lot of the original furnishing was kept."
    m "I'm sure it will be fine."
    show player casual at centerright:
        zoom 0.5
    p "We should probably check that the fridge works."
    m "Ah, good idea!"

    scene black
    "You check out the fridge, which seem to be intact."
    "Theres a power switch that has been turned off. You turn it on and the fridge springs to life."

    scene house kitchen night
    show player casual at centerleft:
        zoom 0.5
    p "Seems to be working."
    show mom casual at centerright:
        zoom 0.5
    m "Let's give it some time get cold."

    show littlesister casual at left:
        zoom 0.5
    l "There's a room through here."

    scene house lounge night
    $ renpy.pause()

    show mom casual at right:
        zoom 0.5
    m "Ooh, a lounge. It has a fire place, and even an old TV."
    show bigsister casual at centerright:
        zoom 0.5
    b "Yeah, really old."
    show player casual at centerleft:
        zoom 0.5
    p "It's probably just for decoration at this point. I doupt it works."
    #m "Let's keep going."

    scene house kitchen night
    show bigsister casual at right:
        zoom 0.5
    b "There's another door here. Let's see where it leads."

    scene house lower_bathroom
    $ renpy.pause()
    show bigsister casual at left:
        zoom .5
    b "Ah, there's a bathroom here. Pretty small."
    extend "\nOh, and there's no lock on the door."
    m "Don't worry, we'll be fine."

    scene house garage night
    $ renpy.pause()
    show player casual at left:
        zoom 0.5
    p "There's a door to the garage here. That's pretty neat."
    show mom casual at centerright:
        zoom 0.5
    m "Oh, good. Then we don't need to run back and forth through the front door when we bring in our bags."
    m "I think that's everything on the first floor. Let's go and check the upstairs."

    scene house entrance night
    $ renpy.pause()

    scene house stairs
    $ renpy.pause()
    show player casual at centerright:
        zoom 0.5
    p "Ok, plenty of doors to choose from."
    p "Let's start here..."
    scene house main_upper_bathroom # door straight ahead from stairs (corner bathroom)
    $ renpy.pause()
    show player casual at centerright:
        zoom 0.5
    p "Another bathroom. A bit bigger, but still pretty sparse."
    show bigsister casual at right:
        zoom 0.5
    b "Does it have a lock?"
    p "Uhm, nope."
    b "Seriously, who doesn't have locks on their bathrooms?"
    p "I don't know. I guess that wasn't a thing back then?"

    l "There's a bedroom here."
    scene house spare_bedroom night # door to the rights from stairs
    show littlesister casual at left:
        zoom 0.5
    l "It doesn't look half bad, actually."
    show mom casual at center:
        zoom 0.5
    m "No, it looks nice."

    scene house master_bedroom night # left of stairs
    $ renpy.pause()
    show bigsister casual at right:
        zoom 0.5
    b "Another bedroom here!"
    b "A bit bigger, and theres two more doors."
    b "..."
    extend "\nThe first one is a closet. But there's no furniture in here, completely empty."

    scene house master_bathroom view1 # from master bedroom
    $ renpy.pause()
    show player casual at left:
        zoom 0.5
    p "The second one is a bathroom. This must have been part of the renovation, 'cause it looks pretty nice."
    show littlesister casual at right:
        zoom 0.5
    l "That's a relief. At least I can have a nice shower or a bath."

    scene house master_bedroom night
    show mom casual at right:
        zoom 0.5
    m "This must have been the master bedroom and bathroom."
    show littlesister casual at left:
        zoom 0.5
    l "I call dibs on this room!"
    show bigsister casual at centerleft:
        zoom 0.5
    b "You can't call dibs an the best room."
    l "I just did! [l_nn_m!cl], can I have this room?"
    b "Of course you can't!"
    m "Girls, don't start fighting. I think it's best if I take this room. Then there's no need for you to argue over it."
    l "Aww..."
    m "So far, this is the only bathroom we've found with an actual bath and a shower, so we might all have to share it any way."
    m "Let's keep going."

    scene house small_spare_bedroom night #next door on right side"
    $ renpy.pause()
    show player casual at left:
        zoom 0.5
    p "Another bedroom in here. A bit smaller than the first, and a single bed rather than double."
    show mom casual at centerright:
        zoom 0.5
    m "There's a nice wardrobe here, though. Plenty of space to hang clothes. I think the first room only had a dresser with drawers."
    m "Maybe you'd like this room, [l_n]?"
    show littlesister casual at centerleft:
        zoom 0.5
    l "I guess."
    p "Ok, next room."

    scene house child_bedroom night # next door on left side
    $ renpy.pause()
    show bigsister casual at left:
        zoom 0.5
    b "Great, another bedroom. That means we each get our own room!"
    show mom casual at right:
        zoom 0.5
    m "Yes, that's perfect."
    b "There's two beds in here. Not that it matters, though. And there's also a wardrobe."
    p "There should be one more room, I think. I'll go and check it out."

    scene house small_upper_bathroom #door straight ahead down the hall
    $ renpy.pause()
    show player casual at right:
        zoom 0.5
    p "Ah, another bathroom."
    p "Just a toilet here as well, and no shower. At least we won't have to fight for access to the toilets."
    "You go back to the others in the hallway."

    scene house stairs
    show player casual at left:
        zoom 0.5
    p "There's one more bathroom down the hall. Just another small one, no shower."
    show mom casual at right:
        zoom 0.5
    m "Ok, good. Then, let's decide on which bedrooms you all want."
    show littlesister casual at centerright:
        zoom 0.5
    l "I'd like the one with the big wardrobe."
    p "I don't mind either way, they all look fine to me."
    show bigsister casual at centerleft:
        zoom 0.5
    b "Well, I'd like the double bed, but I think I'd rather have some wardrobe space. So, I guess I'll take the one with two beds."
    p "I'll have the double bed then."
    m "Alright, perfect. Seems everyone is happy."
    m "Let's go and get all the luggage from the car and bring up to our rooms. It's getting pretty late already, so we can wait to unpack everything until tomorrow."

    scene black
    "You all help out bringing the luggage inside, and up to your rooms."
    "It requires a few trips up and down the stairs, but eventually you get everything inside."

    #[scene player_room]
    #[show player with luggage]
    scene house spare_bedroom night
    show player casual at centerright:
        zoom 0.5
    p "Phew. That's everything..."
    p "..."
    p "Alright, let's do some quick unpacking. I at least gotta find my toothbrush and stuff."

    scene black
    "You take a few minutes going through your bags to unpack the essentials."
    "Once you're done, you go to check up on the others."

    scene house kitchen night # (mom is packing the food they brought into the fridge)
    show mom casual backside bending at left:
        zoom 0.5
    "You find your [m_r_p] in the kitchen putting away the food you brought with you in the fridge."

    show player casual at centerright:
        zoom 0.5
    p "Hey [p_nn_m]. Is the fridge cold yet?"

    show mom casual at left:
        zoom 0.5
    m "Oh, hi [m_nn_p]. Well, not really but it's getting there."
    p "Need any help?"
    m "Uhm, no I'm nearly done already. Thanks any way."
    show mom casual backside bending at left:
        zoom 0.5
    p "Sure."
    m "Did you unpack your things?"
    p "Some of it. I'll do the rest tomorrow."
    m "Alright."

    "[p_nn_m!c] finishes putting the food away in the fridge."

    show mom casual at left:
        zoom 0.5
    m "There we go, all done."
    m "We should have enough food to last us the next two days. Although I think I might head out and pick up some additional things tomorrow."
    p "Oh yeah?"
    m "Yes. There should be a small town about a 40 minutes drive away, and I want to make sure I can find it and see what's there."
    p "Do you want us to come with you?"
    m "Hm, maybe. I might bring one of the girls. I was hoping you could help me set up my computer."
    p "Oh, sure. That's no problem."
    m "Thanks, honey."
    m "Now, I'm going to check in quickly with the girls, but you can go and get ready for bed."
    p "Alright. Good night, [p_nn_m], see you tomorrow."
    m "Good night."

    #(Bathroom, brushing teeth etc?)
    scene house spare_bedroom night
    "You change and brush your teeth, then get into bed."
    "You crawl under the covers in the unfamiliar bed, in which you will be spending the nights for the coming three months."

label day02:
    
    scene black
    centered "The next day" # day 2

    scene house spare_bedroom day
    "With the morning sun peeking in throough the windows, you slowly wake up, and stretch."
    "It feel weird waking up in this new room and bed, but at least you were able to get a good night of sleep."
    scene house main_upper_bathroom
    "You go to the bathroom to take a leak and wash the tiredness off your face."
    "Then you go downstairs."
    scene house kitchen day
    $ renpy.pause()
    show mom casual at centerleft:
        zoom 0.5
    "You find [p_nn_m] in the kitchen, making breakfast."
    show player casual at centerright:
        zoom .5
    p "Good morning."
    m "Oh, good morning, honey!"
    m "How was your night? Did you sleep well?"
    p "Yeah, pretty good actually, nothing to complain about."
    m "That's good to hear. I slept pretty well too."
    m "I was surprised over how utterly dark it got at night. With no street lights and other buildings around it was pitch black."
    p "Oh yeah, true. I didn't think of that."
    p "If you're going shopping later, you might want to pick up a flashlight."
    m "Good idea!"
    p "So, how's the kitchen?"
    m "Oh, it's fine. It's not as modern as we're used to, but it has everything we need."
    m "Would you mind waking up [p3_ref_bl]? Breakfast should be ready in 15 minutes or so."
    p "Ok, sure."

    scene house stairs
    "You head upstairs, and to [p_nn_bs] room."
    "You pull the handle and knock on the door as it swings upen."
    scene house child_bedroom day
    show player casual at centerright:
        zoom .5
    p "Hey [p_nn_b], you up?"
    show bigsister payama holding_underwear at left:
        zoom .5
    b "Oh, Jesus! You scared me, [b_nn_p]."
    p "Oh, sorry."
    show bigsister payama at left:
        zoom .5
    b "Yeah, I just got up. Watcha' want?"
    p "[p_nn_m!c] asked me to get you, she's making breakfast."
    b "Well, I was gonna take a shower."
    p "She said it'll be about 15 minutes, so it's probably fine if you hurry."
    b "Yeah, ok. I'll be quick."
    p "Ok, see ya' soon."

    scene house stairs
    "Next is [p_nn_l]."
    "You again open the door and knock as you enter."
    scene house small_spare_bedroom day
    show littlesister sleeping
    show player casual at left:
        zoom .5
    p "[p_nn_l], are you... up?"
    p "*sigh* I guess not."
    p "[p_nn_l], come on. Time to wake up."
    p "..."
    p "Hey, it's time to wake up."
    p "..."
    p "Still nothing."
    "You step closer as you wonder to yourself how she can sleep so deeply."
    "You give her a gentle nudge."
    p "[p_nn_l]?"
    p "..."
    "You raise your voice and give her another nudge."
    p "[p_nn_l]! Wakey-wakey."
    l "... Ughh..."
    p "Come on, sleepy-head. Time to get up."
    l "..."
    p "Are you awake?"
    l "No..."
    p "Yes you are. Get up."
    l "Ughmm... Why?"
    p "'Cause it's morning, and [p_nn_ms] making breakfast."
    "You pull off her covers and grab her arm to pull her up."
    l "Alright, alright. I'm getting up."

    show littlesister emptybed
    show littlesister payama sleepy as s1 at centerright:
        zoom .5
    l "*Yawn* ..."
    p "Tired as always, eh? Did you at least sleep ok?"
    l "Uh, yeah. I think so. Not really a fan of the pillow, but what ever."
    p "Good. Breakfast will be ready in like 10 minutes, so come down soon ok?"
    l "Ok. *yawn*"

    scene black
    "You leave your [l_r_ps] room and head downstairs."
    "After a short while, the whole family is gathered in the kitchen for breakfast."

    scene house kitchen_table day
    show kitchen_table nochairs empty
    show mom eating_in_kitchen
    show bigsister eating_in_kitchen
    show littlesister eating_in_kitchen
    show player eating_in_kitchen
    show kitchen_table_breakfast

    "... Small talk ..."

    
    # Morning, stretch, go to bath room. Knock, mom is in there, so you wait.
    # Your turn... Then, go to kitchen, mom is making breakfast (fully clothed), you say good morning.
    # Mom asks you to check if the girls are up, breakfast won't be long.
    # You check on big sister, knock at her door and enter at the same time. She's up, wearing pyamas and holding underwear. Breakfast... She's just gonna take a shower first. ok.
    # Check on little sister, knock and enter, she's awake but still in bed. come one, time to get up. yawns, ok fine... wearing pyamas (long sleeved shirt and trousers)

    # Breakfast. small talk. mom asks you to help her set up her computer later, so she can start working.
    # She also asks the girls to help her with some unpacking. We don't have to do it all, but please help me out a little.

    # After breakfast, you brush your teeth, then prepare to set up moms computer at work desk.
    # You see all girls unpacking stuff. Mom bends over to pick up something, and you see her cleavage and part of her bra, but think nothing of it.
    # You carry computer and stuff. Skip to having set it upp. Call for mom that its done.
    # Mom thanks you all, and suggests that you all check out the surrounding area.

    # You all leave together (you and sisters), finding and checking out:
    #     - lake, bridge, small boat
    #     - woods
    #     - field of grass
    #     - you find a jacuzzi close to the house, it have seen better days. needs cleaning.
        
    # Later, you come back, go to your room. Lay on bed with your phone for a while.

    # Later again, dinner everyone together.
    # Someone asks mom how the book is coming along. fairly well, she briefly describes the plot she's working on. looking to be a murder mystery (or something else?)
    # You mention the jacuzzi, and suggest you should get it cleaned up. Mom asks your sisters to help you. They agree but are not looking frward to it.

    # Evening, you sit on the couch (watching tv? only basic channels. or, a movie on DVD?)
    # Drinking coffee/tea. Playing on phone?
    # Then, going to bed...

    scene black
    centered "Sorry, that's it for now.\nThis is just a very early prototype where I test things out."

    return
