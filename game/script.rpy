define narrator = nvl_narrator
define sogakorou = Character(None, kind=nvl, what_xalign=0.37, what_color="#afaeae")
define shiina = Character(None, kind=nvl, what_xalign=0.37, what_color="#9b5f5f")
define cenNvl = Character(None, kind=nvl, what_font="fonts/Mukta-ExtraBold.ttf")
define cen = Character(None, xfill=True, what_xalign=0.5, what_text_align=0.5, what_font="fonts/Mukta-ExtraBold.ttf")

transform nighttime:
    matrixcolor TintMatrix("#7FA5F2")###or BrightnessMatrix (1.0)


# Start of the game
label start:

    # Display the background images
    scene classroom_day

    # Set up the story and introduce the murder mystery

    "It was just an ordinary day at Crestwood High School, where the monotony of textbooks and cafeteria mystery meat reigned supreme. 
    The halls echoed with the symphony of locker slams and the unmistakable scent of teenage angst."

    "But little did I know, destiny had brewed a concoction of chaos and intrigue, 
    ready to be served with a side of murder most unexpected! Until... wait for it... A shocking discovery burst through the mundane monotony like 
    a fire-breathing unicorn crashing a chemistry class!"

    "Picture this: as I was innocently minding my own business, contemplating the mysteries of quadratic equations, BAM! 
    The news hit me like a giant water balloon to the face—'A murder has taken place!'"
    "I tell you, my heart skipped more beats than a glitchy metronome on steroids!"

    nvl clear

    "Now, don't get me wrong. Murder is serious business. 
    But amidst the flurry of panic and bewildered expressions, 
    I couldn't help but feel a tiny spark of excitement." 
    
    "A chance to unleash my inner detective, clad in a tweed hat and carrying a magnifying glass that may or 
    may not have been a souvenir from a certain theme park. Oh, the thrilling possibilities!"

    "As rumors spread like wildfire through the grapevine, transforming the school into a buzzing beehive of 
    speculation, I knew I had stumbled upon an adventure that would rival the best Nancy Drew novels."

    "With each passing moment, the hallways became a stage for covert glances, hushed conversations, and suspicious sneezes 
    (who knows, maybe the culprit was allergic to algebra)."

    nvl clear

    "But I know that this murder mystery would be unlike anything Crestwood High had ever seen. Just like the manga I read."
    
    "There will be twists and turns that would make a roller coaster blush with envy."
    
    "Suspects emerged from the shadows like actors auditioning for the lead role in a dramatic play. 
    And all the while, I found myself caught up in a whirlwind of clues, alibis, and cafeteria food fights that took on a whole new meaning!"

    "However, as the gravity of the situation sank in, I couldn't help but feel a mixture of excitement and responsibility." 
    
    "Sure, solving a murder sounded thrilling in theory, but the weight of the truth and the impact it had on the lives of those 
    involved were not lost on me. The consequences were as real as the cafeteria meatloaf—questionable at best!"

    nvl clear

    "Well... I gulped down every last doubt in my mind and readied myself."

    "For a brief respite, I decided it would be wise to maintain a safe distance from the crime scene while engaging in conversation with potential witnesses."
    
    "I opted to observe the area from a discreet vantage point, allowing me to gather information without interfering with the ongoing 
    investigation."

    cenNvl "And so begun my investigation!"

    nvl clear

    # Show a transition effect and move to the investigation scene
    with ImageDissolve("investigation_phase.png", 1.0, ramplen=256)
    scene investigation_phase at nighttime
    cen "Investigation Phase I: The Art of Deceit"
    with Fade(0.1, 0.0, 0.5)

# Investigation scene
label investigation:

    # Display the investigation scene background
    scene school_hallway_day

    # Introduce the main character's investigation skills and curiosity
    "As a second-year student and an amateur detective, I couldn't resist getting involved."
    "With a watchful eye, I surveyed the surroundings, taking in the atmosphere and the hushed whispers that echoed through the air. 
    The scene before me was a mix of curious onlookers, concerned teachers, and bewildered students, all trying to comprehend the gravity of 
    the situation."
    shiina "Sensei... Why did you do this? Sniff... ugh, I didn't know she had something going on with her."
    "I approached an individual who seemed most likely to have witnessed the discovery of the lifeless body. 
    In engaging in a conversation, I adopted a tactful and empathetic approach, ensuring they felt comfortable sharing any pertinent 
    information without feeling overwhelmed by the somber ambiance."

    nvl clear

    sogakorou "Is that you Shiina Mufune?"
    shiina "...Who are you?"
    sogakorou "I was going to ask you about her... but judging from your look... I am... sorry."

    # Prompt the player to make a choice
    menu:
        "Examine the note":
            jump examine_note
        "Continue investigating":
            jump continue_investigating

# Examine the note scene
label examine_note:

    # Display the note image
    scene bg library

    # Present the details of the note
    sogakorou "The note contains a cryptic message."
    sogakorou "I need to decipher it to uncover more clues."

    # Prompt the player to make a choice
    menu:
        "Decipher the message":
            jump decipher_message
        "Continue investigating":
            jump continue_investigating

# Decipher the message scene
label decipher_message:

    # Display the code-breaking minigame or puzzle

    # Based on the player's success or failure in deciphering the message:
    if success:
        jump decipher_success
    else:
        jump decipher_failure

# Decipher success scene
label decipher_success:

    # Present the deciphered message and its significance
    sogakorou "I cracked the code!"
    sogakorou "The message reveals a hidden meeting place."

    # Show the second piece of evidence
    show evidence2

    sogakorou "I found a key at the meeting place."
    sogakorou "This could be a crucial clue."

    # Prompt the player to make a choice
    menu:
        "Continue investigating":
            jump continue_investigating

# Decipher failure scene
label decipher_failure:

    # Present the consequences of failing to decipher the message
    sogakorou "I couldn't crack the code..."
    sogakorou "I'll have to find another way to progress."

    # Prompt the player to make a choice
    menu:
        "Continue investigating":
            jump continue_investigating

# Continue investigating scene
label continue_investigating:

    # Continue the investigation and present more clues, puzzles, or interactions

    # Depending on the progress and choices made, present different paths, suspects, and revelations

    # Ultimately, lead to the climax and resolution of the murder mystery

    # End the game with different endings based on the player's choices and actions


