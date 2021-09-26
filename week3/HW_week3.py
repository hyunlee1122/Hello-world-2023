# Pokemon World
# Now updated to Python 3

# At the top of the file are declarations and variables we need.
#
# Scroll to the bottom and look for the main() function, that is
# where the program logic starts.

# random numbers (https://docs.python.org/3.3/library/random.html)
import random
# system stuff for exiting (https://docs.python.org/3/library/sys.html)
import sys

# an object describing our player
player = {
    "name": "p1",
    "score": 0,
    "items": ["milk"],
    "friends": [],
    "location": "start"
}

rooms = {
    "room1": "Mt. Coronet mountain.",
    "room2": "a mountain path",
    "room3": "an alternate path"
}


def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum, maxNum)
    print("You roll a: " + str(result) + " out of " + str(maxNum))

    if (result <= difficulty):
        print("trying again....")

        input("press enter >")
        rollDice(minNum, maxNum, difficulty)  # this is a recursive call

    return result


def printGraphic(name):
    if (name == "meowth"):
        print('               .-. \_/ .-.')
        print('               \.-\/=\/.-/')
        print('            "-./___|=|___\.-"')
        print('           .--| \|/`"`\|/ |--.')
        print('          (((_)\  .---.  /(_)))')
        print('            `\ \_`-.   .-"_" "_')
        print('             ".__       __."(_))')
        print('                 /     \     //')
        print('                |       |__." /')
        print('                \       /--""')
        print('            .--,-" .--. "----.')
        print('           "----`--"  "--`----"')
        print('       Meowth (Pokemon)        ')

    if (name == "pokeball"):
        print('────────▄███████████▄────────')
        print('─────▄███▓▓▓▓▓▓▓▓▓▓▓███▄─────')
        print('────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────')
        print('───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───')
        print('──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──')
        print('─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─')
        print('██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██')
        print('██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██')
        print('██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██')
        print('███████████░░███░░███████████')
        print('██░░░░░░░██░░███░░██░░░░░░░██')
        print('██░░░░░░░░██░░░░░██░░░░░░░░██')
        print('██░░░░░░░░░███████░░░░░░░░░██')
        print('─██░░░░░░░░░░░░░░░░░░░░░░░██─')
        print('──██░░░░░░░░░░░░░░░░░░░░░██──')
        print('───██░░░░░░░░░░░░░░░░░░░██───')
        print('────███░░░░░░░░░░░░░░░███────')
        print('─────▀███░░░░░░░░░░░███▀─────')
        print('────────▀███████████▀────────')

    if (name == "pikachu"):
        print('░█▀▀▄░░░░░░░░░░░▄▀▀█')
        print('░█░░░▀▄░▄▄▄▄▄░▄▀░░░█')
        print('░░▀▄░░░▀░░░░░▀░░░▄▀')
        print('░░░░▌░▄▄░░░▄▄░▐▀▀')
        print('░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█')
        print('░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█')
        print('▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█')
        print('█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀')
        print('░▀▄░░▀░░▀▀▀░░▀░░░▄█▀')
        print('░░░█░░░░░░░░░░░▄▀▄░▀▄')
        print('░░░█░░░░░░░░░▄▀█░░█░░█')
        print('░░░█░░░░░░░░░░░█▄█░░▄▀')
        print('░░░█░░░░░░░░░░░████▀')
        print('░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀')
        print('  Picach!  Picach!      ')  # this one is escaped!

    if (name == "charizard"):
        print('                 ."-,.__')
        print('                 `.     `.  ,')
        print('              .--"  .._,""-"" `.')
        print('             .    ."         `"')
        print('             `.   /          ,"')
        print('               `  "--.   ,-""')
        print('                `"`   |  "')
        print('                   -. \, |')
        print('                    `--Y."      ___.')
        print('                         \     L._, \ ')
        print('             ,' '           `, `.   | \            ( `')
        print('          ../, `.            `  |    .\`.           \ \_')
        print('         ,", ..  .           _., "    ||\l            >  """.')
        print('        , ,"   \           ,".-.`-._,"  |           .  _._".')
        print('      ," /      \ \        `"" "" `--/   | \          / /   ../')
        print('    ."  /        \ .         |\__ - _ ,"` `        / /     `.`.')
        print('    |  "          ..         `-...-"  |  `-"      / /        . `.')
        print('    | /           |L__           |    |          / /          `. `.')
        print('   , /            .   .          |    |         / /             ` `')
        print('  / /          ,. ,`._ `-_       |    |  _   ,-" /               " |')
        print(' / .           /""_/. `-_ \_,.  ,"    +-"" `-""  _,        ..,-.    |"".')
        print('.  "         .-f    ,"   `    ".       \__.---"     _   ."   "     \ |')
        print('" /          `."    l     ." /          \..      ,_|/   `.  ,"`     L`')
        print('|"      _.-""` `.    \ _,"  `            \ `.___`.""`-.  , |   |    | |')
        print('||    ,"      `. `.   "       _,...._        `  |    `/ "  |   "     . |')
        print('||  ,"          `. ;.,.---" ,"       `.   `.. `-"  .-" /_ ."    ;_   ||')
        print('|| "              V      / /           `   | `   ,"   ,"" ".    !  `. ||')
        print('||/            _,-------7 "              . |  `-"    l         /    `||')
        print('. |          ," .-   ," ||               | .-.        `.      ."     ||')
        print(' `"        ,"    `"."    |               |    `.        ". -."       `"')
        print('          /      ,"      |               |,"    \-.._,."/"')
        print('          .     /        .               .       \    .""')
        print('        .`.    |         `.             /         :_,"."')
        print('          \ `...\   _     ,"-.        ."         /_.-"')
        print('           `-.__ `,  `"   .  _.>----"".  _  __  /')
        print('                ."        /""          |  ""   "_')
        print('               /_|.-"\ ,".             ""."`__"-( |')
        print('                 / ,"""\,"               `/  `-.|" mh')

    if (name == "title"):
        print(
            '                              `                  0')
        print(
            '  .:XHHHHk.              db.   .;;.     dH  MX   0')
        print(
            'oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN')
        print(
            'QMMMMMb  "MMX       MMMMMMP !MX" "M~   MMM MMM  .oo. XMMM "MMM')
        print(
            '  `MMMM.  )M> :X!Hk. MMMM   XMM.o"  .  MMMMMMM X?XMMM MMM>!MMP')
        print(
            '   "MMMb.dM! XM M":M MMMMMX."MMMMMMMM~ MM MMM XM "" MX MMXXMM')
        print(
            '    ~MMMMM~ XMM. .XM XM`"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP')
        print(
            '     ?MMM>  YMMMMMM! MM   `?MMRb.    `"""   !L"MMMMM XM IMMM')
        print(
            '      MMMX   "MMMM"  MM       ~%:           !Mh.""" dMI IMMP')
        print(
            '      "MMM.                                             IMX')
        print(
            '       ~M!M                                             IMP')
        print(
            '-----------------------------------------------------------------------------')


def gameOver():

    printGraphic("pokeball")

    print("-------------------------------")
    print("to be continued!")
    print("name: " + player["name"])  # customized with a name
    print("score: " + str(player["score"]))  # customized with a score
    return


def strangePath():
    print("You're on your way to the right. There are a lot of trees.")
    input("press enter >")

    print("You hear a cat crying somewhere.")
    input("press enter >")

    printGraphic("meowth")
    print("You found a pokemon!")
    print("You consider your options.")
    print(
        "options: [ capture, go back, run ]")

    pcmd = input(">")

    if (pcmd == "capture"):
        print("You are trying to capture...")
        print("Let's grab a pokeball and throw it!")

        # roll a dice from 0 to 20 to see what happens
        # if your number is higher than the difficulty, you win!
        difficulty = 10
        roll = rollDice(0, 20, difficulty)

        # you have to get lucky! this only happens to the player
        # if you roll the dice high enough
        if (roll >= difficulty):
            print("You caught it successfully!")
            printGraphic("pokeball")

            print("This Pokemon looks hurt")
            print("Let's take this to Dr. Oak")

            # we dive further into the logic
            pcmd = input("yes or no >")

            if (pcmd == "no"):
                print("You just left the Pokemon behind.")
                strangePath()

            elif (pcmd == "yes"):
                print("You are going to Dr. Oak.")
                # add an item to the array with append
                player["items"].append("pokeball")
                player["score"] += 100  # add to the score
                mountain()

            else:
                print("You just left the Pokemon behind.")
                mountain()

        else:
            print("Turns out you cannot capture this!... oh well.")
            strangePath()

    elif (pcmd == "go back"):
        print("You decide to go back.")
        pcmd = input(">")
        mountain()

    elif (pcmd == "run"):
        print("You run!")
        mountain()  # back to start

    else:
        print("You can't do that!")
        strangePath()


def mountainPath():
    print("The mountain path leads you down a narrow path of trees.")
    print("It is a very nice day.")
    input("press enter >")

    printGraphic("pikachu")
    print("Oh! You found such a cute pokemon!")
    input("press enter >")

    print("You consider your options.")

    # check the list for items
    # the 'in' keyword helps us do this easily
    if ("pokeball" in player["items"]):
        print("options: [ look around , capture, run ]")
    else:
        print("options: [ go back, capture, run ]")

    pcmd = input(">")

    # option 1: look at the fox
    if (pcmd == "go back"):
        print("You go back...")
        mountain()  # try again

    # option 2: talk to the fox
    elif (pcmd == "capture"):
        print("Let's capture pikachu!")
        print("Grab a pokeball!")
        input("press enter to throw it!")

        difficulty = 5
        # roll a dice between 0 and 20
        chanceRoll = rollDice(0, 20, difficulty)

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print("It's you're lucky day! Pikachu wants to be your friend.")
            player["score"] += 20
        else:
            print(
                "You are still trying to capture Pikachu, but... It doesn't seem easy.")
            mountainPath()  # try again

        # nested actions and ifs
        pcmd = input("be friends with Pikachu? yes or no >")

        # yes
        if (pcmd == "yes"):

            print("Pikachu becomes your friend!")

            player["friends"].append("pikachu")

            # string and int converstion!
            # we need to convert the score to a number to add to it
            # then convert it back to a string to display it to the player
            player["score"] = int(player["score"]) + 100  # conversion
            # we generate a custom string and add the score
            print("Your score increased to: " + str(player["score"]))
            gameOver()

        # no
        elif (pcmd == "no"):
            print("Pikachu runs away!")
            mountainPath()

        # try again
        else:
            mountainPath()

    elif (pcmd == "throw away pokeball"):
        print("You throw pokeball to Pikachu!")
        input("press enter>")
        printGraphic("pokeball")
        gameOver()

    # option 3: run
    elif (pcmd == "run"):
        print("You run!")
        mountain()  # back to start

    # try again
    else:
        print("I don't understand.")
        mountainPath()  # mountain path


def mountain():
    print("There are three crossroads.")
    print("Which direction are you going to go?")

    # this piece of game logic checks to see if the requirements are met to continue.
    # we can have some fun and change the options for the player
    # based on variables we stored

    # 1. check the list of items, to see if it is there
    # 2. check the list of friends, to see if you are in friends list

    if (("pokeball" in player["items"]) and not ("picachu" in player["friends"])):
        print(" Oh, you found a cave that looks like a shortcut.")
        print(" Do you want to go into? or go back? ")
        print(
            "Your options: [ go into, go back ]")

    elif ("pokeball" in player["items"]):
        print("Your options: [ left, straight, right ]")

    else:
        print("Your options: [ left, straight, right ]")

    pcmd = input(">")  # user input

    # player options
    if (pcmd == "left"):
        # its a trick!
        print("You look around... This is a dead end.")
        print("You have to go back.")

        input("press enter >")
        mountain()

    # path option
    elif (pcmd == "straight"):
        print("You keep moving forward..")
        input("press enter >")
        mountainPath()  # path 1

    # path2 option
    elif (pcmd == "right"):
        print("You take the other path.")
        input("press enter >")
        strangePath()  # path 2

    # exiting / catching errors and crazy inputs
    elif (pcmd == "go back"):
        print("I arrived at Dr. oak safe.")
        print("It was a memorable day.")
        return  # exit the application

    elif (pcmd == "go into"):
        printGraphic("charizard")

        print("Oh my god!!!!")  # escaped
        return  # exit the application, secret ending

    else:
        print("I don't understand that")
        mountain()  # the beginning


def introStory():
    # let's introduce them to our world
    print("Welcome to the Pokemon World! What should I call you?")
    player["name"] = input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print("Welcome to the Pokemon World!" + player["name"] + "!")
    print("You're new Pokemon trainer now.")
    print("You just received five pokeballs from Dr. Oak. Let's be friends with Pokemon!")
    print("Do you decide to go on an adventure?")

    pcmd = input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print("You're currently going up to the Mt. Coronet mountain...")
        input("press enter >")
        mountain()
    else:
        print("No? ... Tell me again if you change your mind.")
        pcmd = input("press enter >")
        introStory()  # repeat over and over until the player chooses yes!


# main! most programs start with this.
def main():
    printGraphic("title")  # call the function to print an image
    introStory()  # start the intro


main()  # this is the first thing that happens
