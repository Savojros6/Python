from random import randint

ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]
suits = ["Wands", "Cups", "Swords", "Pentacles"]
majorArcana = ["0 - The Fool", "I - The Magician", "II - The High Priestess", "III - The Empress", "IV - The Emperor", "V - The Hierophant",
               "VI - The Lovers", "VII - The Chariot", "VIII - Justice", "IX - The Hermit", "X - Wheel of Fortune", "XI - Strength",
               "XII - The Hanged Man", "XIII - Death", "XIV - Temperance", "XV - The Devil", "XVI - The Tower", "XVII - The Stars",
               "XVIII - The Moon", "XIX - The Sun", "XX - Judgement", "XXI - The World"]

pRanks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"] 
pSuits = ["Spades", "Diamonds", "Clubs", "Hearts"]
jokers = ["Joker", "Jester"]
empty = []

# Required for corrupt()
consonants	= ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
capsCons	= ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]            
vowels		= ["a", "e", "i", "o", "u", "y"]
capsVowels	= ["A", "E", "I", "O", "U", "Y"]

agree		= ["y", "yes", "okay", "ok", "sure", "alright", "agree", "accept", "do", "yeah", "ok fine", "okay fine", "fine"]
disagree	= ["n", "no", "nope", "nah", "never", "stop", "quit", "exit", "don't", "disagree", "object", "protest"]
nonspecific = ["card", "cards"]

easterEgg = ["Misspelled", "Censored", "Inconvienient", "Evil", "Fucked up", "Sinister",  "Spooky", "Dark", "Scary", "Ominous", "Mischievous",
             "Rude", "Kind of mean", "Villainous", "Monstrous", "Occult", "Ghostly", "Skeletal", "Frightening", "Unscrupulous", "Dastardly",
             "Killer", "Slightly bent", "Slightly torn", "Malicious", "Wicked", "Cruel", "Undead", "Spiteful", "Nefarious", "Heretical",
             "Fiendish", "Devilish", "Demonic", "Cursed", "Hexxed", "Spectral", "Phantom", "Haunted",  "Sinful", "Treacherous",
             "Deceitful", "Unholy", "Black", "Murderous", "Horror", "Bloody", "Hyper-realistic", "Satanic", "Terrifying", "Corrupted",
             '"Evil Ass" Rape', "Woke", "British", "John", "Political", "Unfunny", "Okay there's nothing actually wrong with this"]

# There's definitely a better way to do this, especially given how repetative the words for increasing numbers are
# tbh, can't be fucked right now. Maybe later.
johnSmartass = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20, "twenty-one": 21, "twenty one": 21, "twenty-two": 22,
    "twenty two": 22, "twenty-three": 23, "twenty three": 23, "twenty-four": 24, "twenty four": 24, "twenty-five": 25,
    "twenty five": 25, "twenty-six": 26, "twenty six": 26, "twenty-seven": 27, "twenty seven": 27, "twenty-eight": 28,
    "twenty eight": 28, "twenty-nine": 29, "twenty nine": 29, "thirty": 30, "thirty-one": 31, "thirty one": 31,
    "thirty-two": 32, "thirty two": 32, "thirty-three": 33, "thirty three": 33, "thirty-four": 34, "thirty four": 34,
    "thirty-five": 35, "thirty five": 35, "thirty-six": 36, "thirty six": 36, "thirty-seven": 37, "thirty seven": 37,
    "thirty-eight": 38, "thirty eight": 38, "thirty-nine": 39, "thirty nine": 39, "forty": 40, "forty-one": 41,
    "forty one": 41, "forty-two": 42, "forty two": 42, "forty-three": 43, "forty three": 43, "forty-four": 44,
    "forty four": 44, "forty-five": 45, "forty five": 45, "forty-six": 46, "forty six": 46, "forty-seven": 47,
    "forty seven": 47, "forty-eight": 48, "forty eight": 48, "forty-nine": 49, "forty nine": 49, "fifty": 50,
    "fifty-one": 51, "fifty one": 51, "fifty-two": 52, "fifty two": 52, "fifty-three": 53, "fifty three": 53,
    "fifty-four": 54, "fifty four": 54, "fifty-five": 55, "fifty five": 55, "fifty-six": 56, "fifty six": 56,
    "fifty-seven": 57, "fifty seven": 57, "fifty-eight": 58, "fifty eight": 58, "fifty-nine": 59, "fifty nine": 59,
    "sixty": 60, "sixty-one": 61, "sixty one": 61, "sixty-two": 62, "sixty two": 62, "sixty-three": 63,
    "sixty three": 63, "sixty-four": 64, "sixty four": 64, "sixty-five": 65, "sixty five": 65, "sixty-six": 66,
    "sixty six": 66, "sixty-seven": 67, "sixty seven": 67, "sixty-eight": 68, "sixty eight": 68, "sixty-nine": 69,
    "sixty nine": 69, "seventy": 70, "seventy-one": 71, "seventy one": 71, "seventy-two": 72, "seventy two": 72,
    "seventy-three": 73, "seventy three": 73, "seventy-four": 74, "seventy four": 74, "seventy-five": 75,
    "seventy five": 75, "seventy-six": 76, "seventy six": 76, "seventy-seven": 77, "seventy seven": 77,
    "seventy-eight": 78, "seventy eight": 78,
    
    "zero": 0, "playing": 1, "playing cards":1, "normal": 1, "normal cards": 1, "regular": 1, "regular cards": 1,
    "tarot": 2, "tarot cards":2, "w":1, "with":1, "with jokers":1, "without":2, "w/o": 2, "without jokers":2,
    "secret": 3, "evil": 3, "dark": 3, "sinister": 3, "fucked up": 3, "spooky": 3, "scary": 3, "scary cards": 3,
    "evil ass rape deck": 3, "evil ass rape cards":3, "evil ass rape": 3, "evil cards": 3, "dark cards": 3,
    "sinister cards": 3, "fucked up cards": 3,  "spooky cards": 3, "secret cards": 3
}

minorArcana 	= []
# suits + ranks
tarotDeck		= []
# the source deck
masterHand		= []
# temp ordered list
crazyHand		= []
# temp disordered list
coinflips		= []
# used to reverse cards
finishedDeck	= []
# the shuffled deck
discard			= []
# currently unused

first		= True
keepGoing	= True
teasing		= False
cursed		= False
silencer	= False
mean = 0

###############################################################
# Everything above here is initial data

# This puts the deck together. It stitches together the names of the
# Minor suits from rank and suit lists, then its merged with another
# list of any extra cards the deck might have.
#
# In theory, this could basically allow you to make new decks pretty much
# arbitrarily. As long as it has the 3 lists its asking for.
def makeDeck(x,y,z):
    global tarotDeck
    for i in range(len(x)):
        for j in range(len(y)):
            minorArcana.append(x[i] + ' of ' + y[j])
    for k in range(len(minorArcana)):
        tarotDeck.append(minorArcana[k])
    for l in range(len(z)):
        tarotDeck.append(z[l])

# This functions purpose is to insult the user for writing a
# nonsensical input, it was surprisingly annoying to make.
def scold():
    global mean, teasing, kind, tarotDeck, cursed
    
    if mean == 0:
        print("That's not one of the options.")
        mean = mean +1
    elif mean == 1:
        print("I was pretty clear the first time.")
        mean = mean +1
    elif mean == 2 and teasing == True:
        print("Seriously? We're doing this again?")
        mean = mean +1
    elif mean == 2:
        print("This program is not this hard to use!")
        mean = mean +1
    elif mean == 3:
        print("Incomphrehensible.")
        mean = mean +1
    elif mean == 4:
        print("You're just fucking with me now.")
        teasing = True
        mean = mean +1
    elif mean == 5:
        print("Why are you like this?")
        mean = mean +1
    elif mean == 6:
        print("Fundamentally broken human being.")
        mean = mean +1
    elif mean == 7 and cursed== True:
        print("Wtfug you're already cursed why are you even still doing this?!")
        mean = mean +1
    elif mean == 7:
        print("That's it, if your foolishness continues, I'll CURSE you with my wicked hex!")
        mean = mean +1
    elif mean == 8 and cursed == True:
        print("Man...")
        mean = mean +1
    elif mean == 8:
        print("Wtfug I warned you about my wicked hex and everything! >:(")
        print("You've forced my hand, I'm going to have to go all out, just this once...\n")
        mean = mean +1
        cursed = True
    elif mean == 9:
        print(":(")
        mean = mean +1
    elif mean == 10:
        print("Y'know what, if you're not going to take this seriously, I'm leaving!")
        print("No more unique error dialogue until you start taking this seriously again!")
        mean = mean +1
    else:
        print("Invalid input.")
        
def powerOfDarkness():
    global kind, silencer
    purge()
    b = pRanks
    c = pSuits
    d = jokers
    kind = "secret"
    makeDeck(b,c,d)
    silencer = True
    reset()
    
def forgive():
    global mean, cursed
    cursed = False
    mean = 0

# This is just rolling attempting to turn it into a numbered answer into one program.
# ideally, this only triggers if it can trigger and otherwise does nothing.
def speakAmerican(word):
    try:
        word = int(word)
    except ValueError:
        pass
    if isinstance (word, str) and word.lower() in johnSmartass:
        babble		= word.lower()
        evilBabble	= johnSmartass[babble]
        cardCounter	= int(evilBabble)
        word = cardCounter
    return word

# resets all values to empty
def purge():
    del minorArcana[:]
    del tarotDeck[:]
    del masterHand[:]
    del crazyHand[:]
    del coinflips[:]
    del finishedDeck[:]
    del discard[:]

def decide():    
    global kind, mean
    
    while True:
        a = input("Playing cards or tarot cards?\n").strip()
        a = speakAmerican(a)
        
        if isinstance (a, str) and a.lower() in agree:
            print("Okay, but which one?")
            continue
        
        if isinstance (a, str) and a.lower() in disagree:
            print("wtfug?? why're you even here?!")
            continue
            
        if isinstance (a, str) and a.lower() in nonspecific:
            print("That doesn't narrow it down!")
            print("Type 'playing' or 1 for playing cards,")
            print("Type 'tarot' or 2 for tarot cards.")
            continue

        try:
            if a == 1:
                print("Playing cards it is then.")
                b = pRanks
                c = pSuits
                while True:
                    d = input("With or without jokers?\n").strip()
                    d = speakAmerican(d)
                    if d in agree or d == 1:
                        print("Alright, with jokers it is.\n")
                        d = jokers
                        break
                    elif d in disagree or d == 2:
                        print("Alright, without jokers it is.\n")
                        d = empty
                        break
                    else:
                        scold(d)
                        continue
                kind = "Playing"
                makeDeck(b,c,d)
                break

            elif a == 2:
                print("Tarot cards it is then.\n")
                b = ranks
                c = suits
                d = majorArcana    
                kind = "tarot"
                makeDeck(b,c,d)
                break 
            
            elif a == 3 or a == 666:
                print("A secret, more sinister third thing...\n")
                b = pRanks
                c = pSuits
                d = jokers
                kind = "secret"
                makeDeck(b,c,d)
                break
            
            else:
                scold()
                continue
                
        except:
            continue
        
def corrupt(i):
    global masterHand, finishedDeck
    bad = randint (0, len(easterEgg)-1)
    
    # Add misspellings
    # this is designed to only fuck up one letter so you can still tell
    # what card its supposed to be, with an intentional preference for
    # lowercase consonants > capital consonants > vowels > capital vowels.
    # because I feel it keeps the words comphrehensible.
    if bad == 0:
        card		= masterHand[i]
        evilCard	= list(card)
        
        while True:
            x = randint (0, len(evilCard))
            a = randint (0, len(consonants))
            b = randint (0, len(capsCons))
            c = randint (0, len(vowels))
            d = randint (0, len(capsVowels))

            try:
                if evilCard[x] in consonants and evilCard[x] != consonants[a]:
                    evilCard[x] = consonants[a]
                    break
                elif evilCard[x] in capsCons and evilCard[x] != capsCons[b]:
                    evilCard[x] = capsCons[b]
                    break
                elif evilCard[x] in vowels and evilCard[x] != vowels[c]:
                    evilCard[x] = vowels[c]
                    break
                elif evilCard[x] in capsVowels and evilCard[x] != capsVowels[d]:
                    evilCard[x] = capsVowels[d]
                    break
                else:
                    continue
            except:
                continue
        moreEvilCard = "".join(evilCard)
        masterHand[i] = moreEvilCard
        finishedDeck.append(f"{easterEgg[bad]} {masterHand[i]}")
        
    # Censor card
    # this is designed not to censor the capitals, word 'of' or the second letters of the words
    # 'four', 'five', 'two' and 'ten' so that its always possible to determine the actual card
    elif bad == 1:
        card		= masterHand[i]
        evilCard	= list(card)
        for cycle in range(len(evilCard)):
            if evilCard[cycle-1] == "F" or evilCard[cycle-1] == "T" or evilCard[cycle-1] == " " and evilCard[cycle] == "o" or evilCard[cycle] == "f" and evilCard[cycle+1] == " ":
                continue
            elif evilCard[cycle] in consonants or evilCard[cycle] in vowels:
                evilCard[cycle] = "*"
                continue
            else:
                continue
        moreEvilCard = "".join(evilCard)
        masterHand[i] = moreEvilCard
        finishedDeck.append(f"{easterEgg[bad]} {masterHand[i]}")
        
    # Other evil
    else:
        finishedDeck.append(f"{easterEgg[bad]} {masterHand[i]}")

# This creates a list of the numbers 1 - 78 in a random order with no duplicates.
# it uses that list to randomly select cards from an orderly list
# to move them into a disorderly one. 
def reset():
    global masterHand, silencer
    if first == True and silencer == False:
        print("Shuffling cards.")
    elif silencer == False:
        print("Reshuffling cards.")
        
    # I only found out that random has a shuffle feature after I wrote this code
    # but also i think using it would make this less of an achievement compare
    # to me figuring out the logic required to do it this way.
    masterHand = [i + 1 for i in range (len(tarotDeck))]
    while len(crazyHand) != len(tarotDeck):  
        x = len(masterHand)
        c = randint (0, x)       
        if c not in crazyHand and c != x and x > 0:
            d = masterHand[c]
            crazyHand.append(d)
            del masterHand[c]
        else:
            continue

    if first == True and silencer == False:
        print("Shuffling cards..")
    elif silencer == False:
        print("Reshuffling cards..")

    for a in range (len(tarotDeck)):
        b = crazyHand[a]
        b = b - 1
        
        # this means this is the random card corresponding to the numbers randomized before
        # it has to be 1 lower because '78' exceeds the length of the array below.
        c = tarotDeck[b]
        # this is now actively selecting one random card                
        masterHand.append(c)
        # this is writing this random order to the masterHand list
            
    for i in range(len(tarotDeck)):
        x = randint (0, 1)
        coinflips.append(x)           
        if coinflips[i] == 1 and kind ==  "tarot":
            finishedDeck.append(f"{masterHand[i]} - (Reversed)")
        elif kind == "secret":
            corrupt(i)
        else:
            finishedDeck.append(masterHand[i])       
     
    if first == True and silencer == False:
        print("Shuffling cards...\n") 
    elif silencer == False:
        print("Reshuffling cards...\n")
    
    # These need to be purged before the next time the deck is shuffled.
    silencer = False
    del masterHand[:]
    del crazyHand[:]
    del coinflips[:]
    del discard[:]

# this is the check that asks if you want
# to reshuffle the deck
def again():
    global first, keepGoing, finishedDeck
    
    keepGoing = False
    yesAlready = False
    
    while len(finishedDeck) != len(tarotDeck) and len(finishedDeck) > 0:     
        answer = input ("Do you want to reshuffle?\n") 
        answer = speakAmerican(answer)
        
        if isinstance(answer, str) and answer.lower() in agree:
            keepGoing = True
            yesAlready = True
            del finishedDeck[:]
            print("Alright.")
            forgive()
            reset()
            break
        elif isinstance(answer, str) and answer.lower() in disagree:
            print("Alright.")
            forgive()
            break
        else:
            scold()
        
    while len(finishedDeck) != len(tarotDeck) and yesAlready == False:
        answer = input (f"Keep drawing {kind} cards?\n")
        answer = speakAmerican(answer)
        
        if isinstance (answer, str) and answer.lower() in agree:
            keepGoing = True
            yesAlready = True
            if len(finishedDeck) == 0:
                del finishedDeck[:]
                reset()
            print("Alright.")
            forgive()
            break
        elif isinstance (answer, str) and answer.lower() in disagree:
            forgive()
            print("Alright.")
            break
        else:
            scold()
    
    if keepGoing == False and yesAlready == False:
        while len(finishedDeck) != len(tarotDeck):
            answer = input("Do you want a different deck?\n")
            answer = speakAmerican(answer)
            
            if answer.lower() in agree:
                keepGoing = True
                print("Alright, same as before.")
                forgive()
                purge()
                decide()
                reset()
                break
            elif answer.lower() in disagree:
                keepGoing = False
                print("Alright, later then.")
                forgive()
                break
            else:
                scold()

# divine() is basically the actual point of the program.
# lets you pick how many cards you want to draw, and draw them (waow)
def divine():
    global first      

    if len(finishedDeck) != 0:
        while True:
            if first == True:
                a = input(f"How many {kind} cards would you like to draw? \n")
            else:
                a = input(f"How many {kind} cards? ")
                
            a = speakAmerican(a)         
        
            if isinstance(a, str) and a.lower() in disagree:
                print("wtfug?? mean!")
                first = False

            try:
                a = int(a)
                if a <= 0:
                    first = False
                    print("A positive number, smartass.")
                    continue      
                elif a > len(finishedDeck) and len(finishedDeck) == len(tarotDeck):
                    first = False
                    print(f"The {kind} card deck only has {len(tarotDeck)} cards!")
                    continue
                elif a > len(finishedDeck) and len(finishedDeck) == 1:
                    first = False
                    print(f"There's only one {kind} card left!")
                    continue
                elif a > len(finishedDeck) and len(finishedDeck) < len(tarotDeck):
                    first = False
                    print("There aren't that many cards left in the deck.")
                    again()
                    continue
                else:
                    break
            except ValueError:
                first = False
                if a.lower not in disagree:
                    print("That isn't a number.")
                continue
    
    g = a
    
    for g in range(g):
        print(f"Card {g+1}: {finishedDeck[g]}")
    
    # g has to be reset because the above 'for' loop changes it
    g = a
    
    for g in range(g):
        b = finishedDeck[0]
        discard.append(b)
        del finishedDeck[0]
    
    if kind == "secret" and first == True or kind == "secret" and cursed == True:
        print("\nWelcome to my dark and twisted reality...")
    
    print(f"\n{len(finishedDeck)} cards remaining.")
             
    if a == (len(tarotDeck)) and kind == "tarot":
        print("Good luck divining the entire deck, smartass.\n")
        
    elif a == (len(tarotDeck)) and kind == "playing":
        print(f"Y'know, {len(tarotDeck)} pickup isn't really playable on pc.\n")
        
    first = False
    forgive()
        
####################################################################################
# Everything above here is function definitions

def master():
    global keepGoing, mean
    decide()
    reset()
    if cursed == True:
        powerOfDarkness()
    while True:
        if cursed == True:
            powerOfDarkness()
        divine()
        again()
        if keepGoing == False:
            break   
master()