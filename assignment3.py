# Assignment3
# let the user know what's going on
print("Welcome to my house")
print("I will introduce my life in Cheongdo")
print("-----------------------------------")

# variables containing all of your story info
yourName = input("Enter your name: ")
location = input("Where is your house?: ")
surrounding = input("What's around your house?: ")
dogs = input("How many dogs?: ")
name1 = input("What's the name of a dog?: ")
name2 = input("What's the name of the other one?: ")
whoWith = input("Who are you with: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line.
# play close attention to the syntax!

story = "My name is " + yourName + ". My house is located in " + location + ", and is surrounded by " + surrounding + ". " \
        "There are " + dogs + "dogs there, and their name is " + name1 + " and " + name2 + ". " \
        "In the morning, I take a walk in the back mountain with them." \
        "In the evening, I have + myFavoriteFood with my" + \
        " " + whoWith + ", which is my favorite food."


# finally we print the story
print(story)
