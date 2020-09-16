#This project is a bot that tells you what activities to perform based
#on how much energy you have

from random import choice

def get_activity_response(user_input):
    #These are the awnsers the bot will give when the user has a lot of energy
    bot_response_8_10 = ["Go for a swimm","Go to the gym","Go play your favorite sport","Go jogging","Go skateboarding",]
    if int(user_input) in range(8,11):
        return choice(bot_response_8_10)
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