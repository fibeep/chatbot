#This project is a bot that tells you what activities to perform based
#on how much energy you have

from random import choice

def get_activity_response(user_input):

    #These are the awnsers the bot will give when the user has little to no energy
    bot_response_0_2 = ["Go sleep","Drink a coffe","Drink an energy drink","Splash some cold water in your face"]
    #These are the awnsers the bot will give when the user has barely any energy
    bot_response_3_4 = ["Read a book","Watch a movie","Play a board game","Play a card game"]
    #These are the awnsers the bot will give when the user has average energy
    bot_response_5_6 = ["Play video Games","Go for a joy ride", "Go for a walk", "walk the dogs",]
    #These are the awnsers the bot will give when the user has above average energy
    bot_response_7_8 = ["Clean your house", "Hang out with friends", "Go to a party"]
    #These are the awnsers the bot will give when the user has a lot of energy
    bot_response_9_10 = ["Go for a swimm","Go to the gym","Go play your favorite sport","Go jogging","Go skateboarding",]
   
   
    if int(user_input) in range(0,3):
        return choice (bot_response_0_2)
    elif int(user_input) in range(9,11):
        return choice(bot_response_9_10)
    else:
        return ("Please add an awnser within the parameters")

print("Welcome to activity planner")
print("On a scale of 0-10, how energetic are you feeling right now? Enter 100 if you dont want to participate in any activity")

user_input = None

while user_input != 100 :
    user_input = int(input("How energetic are you feeling? From 0 to 10 "))
    bot_response = get_activity_response(user_input)
    print(bot_response)
    

Bye = "Thank you for participating"
print(Bye)
