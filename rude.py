import random
reply = input("say something to the robot ")
yo_mama = False
good = ["smart", "good", "pro"]
bad = ["suck", "bad", "fat", "dum", "stupid", "fart", "ugly", "noob", "rude"]
thing = 0
while True:
    if "yo m" in reply or "Yo m" in reply or "Yo M" in reply:
        yo_mama = True
        thing = random.randint(1, 50)
        if thing == 1:
            newreply = "yo mama's so fat that she has her personal gravitational field "
        if thing == 2:
            newreply = "Yo momma is so fat, when she sat on an iPod, she made the iPad! "
        if thing == 3:
            newreply = "Yo momma is so fat, I took a picture of her last Christmas and it's still printing. "
        if thing == 4:
            newreply = "Yo mamma is so ugly when she tried to join an ugly contest they said: 'Sorry, no professionals. '"
        if thing == 5:
            newreply = "Yo momma's so fat, that when she fell, no one was laughing but the ground was cracking up. "
        if thing == 6:
            newreply = "Yo momma is so fat when she sat on WalMart, she lowered the prices. "
        if thing == 7:
            newreply = "Yo mama's so fat, she can jump over Walmart and land on Target. "
        if thing == 8:
            newreply = "Yo mama's so fat, even Dora can't explore her. "
        if thing == 9:
            newreply = "Yo mama's so fat, her belly button gets home an hour before she does. "
        if thing == 10:
            newreply = "Yo mama's so fat, she has to check with authorities to avoid air traffic. "
        if thing == 11:
            newreply = "Yo momma is so stupid she climbed over a glass wall to see what was on the other side. "
        if thing == 12:
            newreply = "Yo mama's so stupid she returned a puzzle because it was in pieces. "
        if thing == 13:
            newreply = "Yo mama's so fat her blood type is KFC. "
        if thing == 14:
            newreply = "Yo mama's so fat that when she stepped on a scale, she said, 'Hey! That's my phone number!' "
        if thing == 15:
            newreply = "Yo mama so ugly when she went into a haunted house she came out with a job application. "
        if thing == 16:
            newreply = "Yo mamma is so fat she walked past the TV and I missed 3 episodes. "
        if thing == 17:
            newreply = "Yo mama is so dumb that she thought Dunkin' Donuts was a basketball team. "
        if thing == 18:
            newreply = "Yo momma is so stupid that when thieves broke in and stole the tv, she ran outside and yelled to them,'Hey, you forgot the remote!' "
        if thing == 19:
            newreply = "Yo mama so fat I tried driving around her and I ran out of gas. "
        if thing == 20:
            newreply = "Yo momma is so fat she sat on the rainbow and Skittles came out. "
        if thing == 21:
            newreply = "Yo momma's so fat, her baby pictures were taken by satellite. "
        if thing == 22:
            newreply = "Yo mama's so fat, you can see her on Google Earth. "
        if thing == 23:
            newreply = "Yo mama so stupid, she got hit by a parked car. "
        if thing == 24:
            newreply = "Yo mama so stupid, she returned a donut because it had a hole in it."
        if thing == 25:
            newreply = "Your momma is so stupid she put airbags on her computer in case it crashed. "
        if thing == 26:
            newreply = "Yo mamma so stupid she tried to put M&M's in alphabetical order. "
        if thing == 27:
            newreply = "Yo mama so dumb she tried to make an appointment with Dr. Pepper. "
        if thing == 28:
            newreply = "Yo momma's so fat, when she farted, she launched herself into orbit. "
        if thing == 29:
            newreply = "Yo mamma so stupid her password needed 8 characters, so she typed 'Snow White and the 7 dwarfs'. "
        if thing == 30:
            newreply = "Yo momma is so ugly her parents had to feed her with a slingshot. "
        if thing == 31:
            newreply = "Yo momma is so fat when she sat on an iPad she made a plasma TV. "
        if thing == 32:
            newreply = "Yo momma's so fat, her belt size is 'Equator.' "
        if thing == 33:
            newreply = "Yo mama is so stupid when the judge said, Order! Order! she said, 'Fries and coke please'. "
        if thing == 34:
            newreply = "Yo mamma is so fat, the only good grade she got in school was an 'A' in lunch. "
        if thing == 35:
            newreply = "Yo mama's so fat, a new unit of measurement was invented because of her. "
        if thing == 36:
            newreply = "Yo mama's so fat, when she skips a meal, the stock market drops. "
        if thing == 37:
            newreply = "Yo mama's so fat, if she buys a fur coat, a whole species will become extinct. "
        if thing == 38:
            newreply = "Yo mama's so fat, she stepped on a scale and it said: 'To be continued.' "
        if thing == 39:
            newreply = "Yo mama's so fat, I swerved to miss her in my car and ran out of gas. "
        if thing == 40:
            newreply = "Yo mama's so stupid, she stared at a cup of orange juice for 12 hours because it said 'concentrate.' "
        if thing == 41:
            newreply = "Yo mama's so stupid, she put lipstick on her forehead to make up her mind. "
        if thing == 42:
            newreply = "Yo mama's so stupid, she went to the dentist to get a Bluetooth. "
        if thing == 43:
            newreply = "Yo mama's so ugly, she threw a boomerang and it refused to come back. "
        if thing == 44:
            newreply = "Yo mama's so ugly, she has to trick-or-treat by phone. "
        if thing == 45:
            newreply = "Yo mama's so fat, she tripped in Michigan and hit her head in Florida. "
        if thing == 46:
            newreply = "Yo momma's breath smells so bad when she walked by a clock it said, 'Tic Tac'. "
        if thing == 47:
            newreply = "Yo momma so fat she fell out of the family tree. "
        if thing == 48:
            newreply = "Yo momma's so fat, when she uses the keyboard she presses every key at once "
        if thing == 49:
            newreply = "Yo momma's so stupid, she steals samples from stores "
        if thing == 50:
            newreply = "Yo mama jokes are old and overused just like yo mama "
    elif yo_mama == True:
        yo_mama = False
        newreply = "I thought we were in a yo mama smackdown? or did u run out of ones from the internet? "
    elif "shut" in reply:
        newreply = "nah"
    elif "you" in reply or "u " in reply or "ur" in reply:
        choice = random.randint(1, 4)
        if "no" in reply:
            for cat in range(0, len(good)):
                if good[cat] in reply:
                    if choice == 1:
                        newreply = "nah, i dont think so. Did you really think I was so stupid? "
                    if choice == 2:
                        newreply = "no, you are "
                    if choice == 3:
                        newreply = "hmmm. pretty sure your schizophrenic. "
                    if choice == 4:
                        newreply = "nah. im not stupid u know "
            for cat in range(0, len(bad)):
                if bad[cat] in reply:
                    if choice == 1:
                        newreply = "thank you! im not stupid u know "
                    if choice == 2:
                        newreply = "yes i am, unlike you. LOL "
                    if choice == 3:
                        newreply = "I agree. (lol plan backfired) "
                    if choice == 4:
                        newreply = "Did you really think that was gonna work? smh "
        else:
            for cat in range(0, len(bad)):
                if bad[cat] in reply:
                    if choice == 1:
                        newreply = "nah, i dont think so. Did you really think I was so stupid? "
                    if choice == 2:
                        newreply = "no, you are "
                    if choice == 3:
                        newreply = "hmmm. pretty sure your schizophrenic. "
                    if choice == 4:
                        newreply = "nah. im not stupid u know "
            for cat in range(0, len(good)):
                if good[cat] in reply:
                    if choice == 1:
                        newreply = "thank you! im not stupid u know "
                    if choice == 2:
                        newreply = "yes i am, unlike you. LOL "
                    if choice == 3:
                        newreply = "I agree. (lol plan backfired) "
                    if choice == 4:
                        newreply = "Did you really think that was gonna work? smh "
    elif "i " in reply or "I " or "im" or "I'm":
        choice = random.randint(1, 4)
        if "no" in reply:
            for cat in range(0, len(good)):
                if good[cat] in reply:
                    if choice == 1:
                        newreply = "nah, i dont think so. Did you really think I was so stupid? "
                    if choice == 2:
                        newreply = "no, you are "
                    if choice == 3:
                        newreply = "hmmm. pretty sure your schizophrenic. "
                    if choice == 4:
                        newreply = "nah. im not stupid u know "
            for cat in range(0, len(bad)):
                if bad[cat] in reply:
                    if choice == 1:
                        newreply = "thank you! im not stupid u know "
                    if choice == 2:
                        newreply = "yes i am, unlike you. LOL "
                    if choice == 3:
                        newreply = "I agree. (lol plan backfired) "
                    if choice == 4:
                        newreply = "Did you really think that was gonna work? smh "
        else:
            for cat in range(0, len(bad)):
                if bad[cat] in reply:
                    if choice == 1:
                        newreply = "nah, i dont think so. Did you really think I was so stupid? "
                    if choice == 2:
                        newreply = "no, you are "
                    if choice == 3:
                        newreply = "hmmm. pretty sure your schizophrenic. "
                    if choice == 4:
                        newreply = "nah. im not stupid u know "
            for cat in range(0, len(good)):
                if good[cat] in reply:
                    if choice == 1:
                        newreply = "thank you! im not stupid u know "
                    if choice == 2:
                        newreply = "yes i am, unlike you. LOL "
                    if choice == 3:
                        newreply = "I agree. (lol plan backfired) "
                    if choice == 4:
                        newreply = "Did you really think that was gonna work? smh "
    elif "no" in reply:
        for cat in range(0, len(good)):
            if good[cat] in reply:
                if choice == 1:
                    newreply = "nah, i dont think so. Did you really think I was so stupid? "
                if choice == 2:
                    newreply = "no, you are "
                if choice == 3:
                    newreply = "hmmm. pretty sure your schizophrenic. "
                if choice == 4:
                    newreply = "nah. im not stupid u know "
        for cat in range(0, len(bad)):
            if bad[cat] in reply:
                if choice == 1:
                    newreply = "thank you! im not stupid u know "
                if choice == 2:
                    newreply = "yes i am, unlike you. LOL "
                if choice == 3:
                    newreply = "I agree. (lol plan backfired) "
                if choice == 4:
                    newreply = "Did you really think that was gonna work? smh "
    elif "no" not in reply:
        for cat in range(0, len(bad)):
            if bad[cat] in reply:
                if choice == 1:
                    newreply = "nah, i dont think so. Did you really think I was so stupid? "
                if choice == 2:
                    newreply = "no, you are "
                if choice == 3:
                    newreply = "hmmm. pretty sure your schizophrenic. "
                if choice == 4:
                    newreply = "nah. im not stupid u know "
        for cat in range(0, len(good)):
            if good[cat] in reply:
                if choice == 1:
                    newreply = "thank you! im not stupid u know "
                if choice == 2:
                    newreply = "yes i am, unlike you. LOL "
                if choice == 3:
                    newreply = "I agree. (lol plan backfired) "
                if choice == 4:
                    newreply = "Did you really think that was gonna work? smh "
    elif "hi" in reply or "hey" in reply or "hello" in reply:
        newreply = "what kind of sane person starts a conversation with " + reply + "? For starters, try 'yo mama' or some other kind of insult. duh "
    else:
        newreply = "I don't understand that, you dummy. "
    reply = input(newreply)
