######################################################################
# Author: Shawn Villahermosa & Alex Meadors
# Username: villahermosa, meadors
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West]" )

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may NOT be coming right after the example above.

action = input("What do you want to do? [Put it on/Ignore it/Burn it]" )

print("You are in a room with strange symbols all over the walls.")
print("You see an amulet floating in the middle of the room.")

if action == "Put it on":
    # Bad choice
    print("Nothing happens... ")
    sleep(delay * 5)
    print("...")
    sleep(delay * 5)
    print("You feel strange, your hands starts twitching uncontrollably.")
    print("You start walking back into the darkness, not in control of your own actions.")
    print("Congratulations! You've been possessed!")
    print("Don't mess with cursed objects kids!")

    dead = True

elif action == "Burn it":
    # Good option
    print("As you cast the amulet into the lava, you feel watched by a giant eye.")
    print("As the amulet disintegrated, you feel a cursed being lifted from the Median-Earth.")


else:
    # Boring option
    print("So you ignore the floating mystical artifact in the middle of the room.")
    print("We went through all of the trouble in making a cool, floating item for you to use and you ignore it...")
    print("Way to go, you hurt our self-esteem.")
    print("We guess you can carry on, further deeper into the depths of the labyrinth.")

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
