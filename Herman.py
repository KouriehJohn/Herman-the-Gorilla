
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def start(feed=0,workout=0,taunt=0,yell=0,name=""):
    # gets user's name
    name = describe_game(name)
    feed,workout,taunt,yell,name = big_herman(feed,workout,taunt,yell,name)



###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def describe_game(name):
    '''
        check if this is a new game or not.
        if it is a new game, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    '''


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
    if name != "":  # meaning, if we do not already have this user's name, then they are a new player and we need to get their name
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nPlease enter your name: ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be our new zookeeper!\nYou will be in charge of Herman the Gorilla.")
                    print("Herman's fate will be decided based off how well you care for him.")
                    print("We suggest you're nice to him, and are carful around him.")
                    print("We also suggest he gets plenty of exercise and banana\'s!.")
                    stop = False
    return name



###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def big_herman(feed,workout,taunt,yell,name):
    stop = True
    while stop:
        show_score(feed,workout,taunt,yell,name)
        pick = raw_input("\nYou appoach Herman\'s enclosure and start watching Herman.\nSoon after, Herman appoaches you and reaches out his hand...\nHow will you respond >>>> ??? \nFeed(f),  \nWorkout(w),  \nTaunt(t),  \nYell(y):").lower()
        if pick == "f":
            print("\n#>>> You hand Herman a Banana,\nHerman quickly grabs the banana and runs off.\nHe seems quite content! Cool!\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            feed = (feed + 1)
            stop = False
        if pick == "w":
            print("\n#>>> You decide its time to show everyone what Herman can do!\nYou direct Herman over to a barbell loaded with 500 lbs\nHerman tosses the bar up 15ft!\nThe bar then crashes down and Herman repeats this 10 times!\nThis is one crazy strong gorilla!\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            workout = (workout + 1)
            stop = False
        if pick == "t":
            print("\n#>>> You stand your ground and firmly glare at Herman.\nHerman doesn't seem too happy and stands up...\nFor some reason you decide to pound your chest several times.\nHerman doesn't like this, and charges at you!!...Forcefully slamming the enlosure wall\nOh oh. Bad move!\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            taunt = (taunt + 1)
            stop = False
        if pick == "y":
            print("\n#>>> You lose your cool and yell at Herman.\n Herman feels hurt by this and goes into the corner of his enclosure to hide.\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            yell = (yell + 1)
            stop = False
    score(feed,workout,taunt,yell,name) # pass the 5 variables to the score()


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def show_score(feed,workout,taunt,yell,name):
    print ("\n{}, you currently have: ({}, Feed) - ({}, Workout) - ({}, Taunt) - ({}, Yell) points.".format(name,feed,workout,taunt,yell))
 

###
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def score(feed,workout,taunt,yell,name):
     # score function is bein passed the values stored within the 3 variables
    if feed > 4: # # if condition is valid, call win function passing in the variables so it can use them
        chubby(feed,workout,taunt,yell,name)
        if feed < 1:
            print("Perhaps, Consider doing more activity with Herman? the poor guy ate too much.")           
    if workout > 4: # if condition is valid, call lose function passing in the variables so it can use them
        strong(feed,workout,taunt,yell,name)
    if taunt > 4: # # if condition is valid, call win function passing in the variables so it can use them
        angry(feed,workout,taunt,yell,name)
    if yell > 4: # if condition is valid, call lose function passing in the variables so it can use them
        emo(feed,workout,taunt,yell,name)
    else:        # else, call nice_mean function in the variables so it can use them
        big_herman(feed,workout,taunt,yell,name)

'''
Here is where I intend to add more functionality. Just not 100% sure how to go about it.
What I WANT to do, is add something along these lines, but of course that doesn't work : )


def rejected(feed,workout,taunt,yell,name):
    # checks if a certain input was entered more then a specified amount
    if count(feed) > 3: # # if condition is valid, call win function passing in the variables so it can use them
        print("Perhaps, Consider doing more activity with Herman? the poor guy ate too much.")
    if count(workout) > 3: # if condition is valid, call lose function passing in the variables so it can use them
        print("Nice job, consider a bit more rest for Herman next time?")
    if count(taunt) > 3: # # if condition is valid, call win function passing in the variables so it can use them
        print("Consider being a nicer person, life will be better!")
    if count(yell) > 3: # if condition is valid, call lose function passing in the variables so it can use them
        print("Therapy should help you.")     

'''
        


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def chubby(feed,workout,taunt,yell,name):
    print("\nNice job {}, sort of?!\nHerman loves you now, but the poor lad gained some weight!".format(name)) # Substitute the {} wildcards with our variables
    again(feed,workout,taunt,yell,name) # call again function and pass in our variables


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def strong(feed,workout,taunt,yell,name):
    print("\nNice job {}, you win!\nHerman\'s become  very fit and a HUGE attraction brining many new\n people to come visit our zoo!".format(name)) # Substitute the {} wildcards with our variables
    again(feed,workout,taunt,yell,name) # call again function and pass in our variables
    

###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def angry(feed,workout,taunt,yell,name):
    print("\nToo bad {},\nHerman does not like you at all!\nHe finds a barrel marked \"DK\" and breaks it over your head!!/nYou're FIRED!".format(name)) # Substitute the {} wildcards with our variables
    again(feed,workout,taunt,yell,name) # call again function and pass in our variables


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def emo(feed,workout,taunt,yell,name):
    print("\nToo bad {}, game over!\nHerman doesn\'t seem to want to do much.\nHe seems depressed and now needs a Gorilla shrink.\nYou're FIRED!".format(name)) # Substitute the {} wildcards with our variables
    again(feed,workout,taunt,yell,name) # call again function and pass in our variables


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def again(feed,workout,taunt,yell,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n").lower()
        if choice == "y":
            stop = False
            reset(feed,workout,taunt,yell,name)
        if choice == "n":
            print("\nSee you later Donkey Kong!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'... ")


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>###
def reset(feed,workout,taunt,yell,name):
    feed = 0
    workout = 0
    taunt = 0
    yell = 0
    # Notice, I do not reset the name variable as the same user has elected to play again.
    start(feed,workout,taunt,yell,name)




if __name__ == "__main__":
    start()
