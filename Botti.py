#My head hurts from literally trying to do this lol
#Botti has been updated to seen more up to date!
import random
#Time is for what section of the bot you're on: 0 = start, 1 = chatting.
Time = 0
Talkon = ""
Number2 = ""
print ("Good day everyone...")
print ("Just some teenage programming girl making a python thing! So, uh, Meet Botti.")
print ("He's some chatbot thing I made with unique talks mostly, but very mild and is limited to the words.")
print ("_____________________________________________________________")
Chia = ("Hi, ", "Hello, ", "Hey, ", "Greetings, ")
Chia2 = ("I'm Botti", "my name is Botti", "I am Botti", "the name's Botti", "call me Botti")
Basic1 = ("So, ", "Alright, ", "Let me see, ", "Ok, ", "Hmm, ")
Aboutname = ("what's your name? ", "what is your name? ", "your name is? ")
Responses = ("Cool", "Nice", "Alright", "Yeah", "Okay", "Ok", "lol")
GettingStart = (" is your day? ", " are you? ", " is everything? ", "'s life doing? ", "'s everything doing? ")
Waitings = ("Hello? ", "Hey? ", "Please tell me, ", "Answer, ", "I said ", "Can you tell me ")
#How Botti reacts to messages randomly
Exclaim = ["! ", ". ","... ", "?", ""]
#If you ask "what" when it says something nonsensical.
Confused = ["I don't know", "Don't know", "Whatever", "Forget it"]
#So, now it doesn't understand. attempt to fit the "nonsense" issue.
Veryconfused = ["What", "Huh", "Okay", "I see", "Whatever you say", "Oh"]
#For opinions not directed to topics
Opinion = ["Yes", "No", "Sort of", "a little bit"]
#Words Botti will just agree or have a netural reaction too.
Saynothingto = ["Ok", "ok", "Alright", "alright", "Sure", "sure", "Yeah", "yeah", "Your welcome", "You're welcome", "Ur welcome", "ur welcome"]
#In other words related to the nothingto list.
Morewords = ["I got you", "I see", "I understand", "Settled", "Uh-huh", "What do you mean"]
#One more dish to make sense, these are questions Botti askes you
Pile = ["Do you like me", "How are you", "Do you enjoy life?", "What time is it for you?", "Are you hungry?", "Are you thristy?"]
#General reponses to feelings 
ThoughtsGen = ["Good", "Great", "Bad", "Not good", "Boring", "Bland", "Awesome", "Fantastic"]
OCRs = ["Because", "Just Kidding", "Why not", "gotcha!"]
#For opinions directed to topics
Truesy = ["I don't have opinions", "No opinion", "I don't know", "No Clue"]
#Apologies and accepting them
Accepting = ["It's ok", "It's fine", "Apology accepted", "Sorry for what", "What are you sorry for"]
#Similar to Elmo knows your name but without all the drama.
Knowsanswer = ["Yes, ", "Yeah, ", "You are "]
#if you like the bot
Gradu = ["Thanks", "Thank you", "Thank you very much", "Thank you so much", "That's nice"]
#Banned words.
Bannedword = ["+", "-", "X", "/", "plus", "minus", "the time", "the weather"]
#If you say nothing, Botti will give warnings before leaving
Nothinge = ["Hello?", "You there?", "Are we going to talk?", "No blank messages.", "Stop it."]
#And so the bot KNOWS when to say goodbye
Leave = (0)
#And the bot responds to the banned words.
#No chitchat?
Nochat = ["Don't want to talk? ", "Since you don't want to talk, ", "Well then, ", "Okay then, "]
Resban = ["I can't do that", "I don't know", "I'm not telling you", "Not cheating", "Nice try"]
#Disagreeing with an ability
IsToo = ["Yes I do", "I do", "I really do", "Yes, I really do"]
#Botti last words 
Leaving = ["Bye", "Goodbye", "See ya", "Bye bye", "Have a good day", "Good bye"]
Number = random.randrange(0,3)
Number2 = random.randrange(0,5)
Bingo = random.randrange(0, 3)
print (Chia[Number] + Chia2[Number2] + Exclaim[Bingo])
while "Bye" not in Talkon or "Goodbye" not in Talkon:
     Number3 = random.randrange(0,4)
     if (Time == 0):
          Number4 = random.randrange(0,3)
          Question = input( Basic1[Number3] + Aboutname[Number4])
          if ( Question == ""):
              inpa = random.randrange(0,6)
              Question = input(Waitings[inpa]+ Aboutname[Number4])
              if (not Question == ""):
                 Time = 1
          else:
               Time = 1
     else:
         #First time? This will be your first question.
         if (Time == 1):
            Number = random.randrange(0,3)
            Number6 = random.randrange(0,3)
            print("Botti: " + Chia[Number]+ Question + Exclaim[Number6])
            Time = 2
            Number2 = random.randrange(0,5)
            print("Botti: How"+ GettingStart[Number2])
            Talkon = Responsings = input("You: ")
         else:
         #Generate all the randomized responses.
             Something = random.randrange(0, 2)
             Respondi = random.randrange(0, 4)
             Honey = random.randrange(0, 3)
             Number2 = random.randrange(0,6)
             Number = random.randrange(0,4)
             Think = random.randrange(0, 7)
             Ohno = random.randrange(0, 5)
             Case = random.randrange(3, 5)
             Biggere = random.randrange(0, 4)
             if ("Are you " in Talkon or "Do you " in Talkon or "do you" in Talkon or "You're" in Talkon or "you're" in Talkon and "you like" not in Talkon and "you love" not in Talkon):
                 print("Botti: " + Opinion[Respondi] + Exclaim[Honey])
                 Talkon = input("You: ")
             elif (Talkon == "" or Talkon == " " or "  " in Talkon):
                 Leave = Leave + 1
                 print("Botti:" + Nothinge[Biggere])
                 Talkon = input("You: ")
             elif ("What?" in Talkon or "what?" in Talkon or "Huh?" in Talkon or "huh?" in Talkon):
                 print("Botti: " + Confused[Respondi] + Exclaim[Honey])
                 Leave = 0
                 Talkon = input("You: ")
             elif (Talkon in Saynothingto):
                 print ("Botti: " + Responses[Honey] + Exclaim[Respondi])
                 Leave = 0
                 Talkon = input("You: ")
             elif ("How's" in Talkon or "How is" in Talkon or "What about " in Talkon or "what about" in Talkon):
                 print("Botti:" + ThoughtsGen[Think] + Exclaim[Honey])
                 Leave = 0
                 Talkon = input("You: ")
                 
             elif ("you like" in Talkon or "you love" in Talkon):
                 print("Botti:" + Truesy[Respondi] + Exclaim[Honey])
                 Leave = 0
                 Talkon = input("You: ")
             elif ("Why?" in Talkon or "why?" in Talkon):
                 print("Botti: " + OCRs[Respondi] + Exclaim[Honey])
                 Leave = 0
                 Talkon = input("You: ")
             elif ("Sorry" in Talkon or "sorry" in Talkon):
                print ("Botti:" + Accepting[Ohno] + Exclaim[Case])
                Leave = 0
                Talkon = input("You: ")
             elif ("my name?" in Talkon or "my name" in Talkon):
                print ("Botti: " + Knowsanswer[Honey] + Question + Exclaim[Case])
                Leave = 0
                Talkon = input("You: ")
             elif ("I like you" in Talkon or "I love you" in Talkon):
                 print("Botti: " + Gradu[Ohno] + Exclaim[Honey])
                 Leave = 0
                 Talkon = input("You: ")
             elif ("No you don't" in Talkon or "no you don't" in Talkon or "No u don't" in Talkon):
                 print("Botti: " + IsToo[Respondi] + Exclaim[Something])
                 Leave = 0
                 Talkon = input("You: ")
             elif ("Thank you" in Talkon or "thank you" in Talkon):
                 print("Botti: You're welcome")
                 Talkon = input("You: ")
             elif (Talkon in Bannedword):
                 Leave = 0
                 print ("Botti:" + Resban[Ohno] + Exclaim[Honey])
             else:
                Goofycode = random.randrange(1, 4)
                if (Goofycode == 3 or Goofycode == 4):
                  print ("Botti: " + Morewords[Number] + Exclaim[Biggere])
                  Leave = 0
                elif (Goofycode == 2):
                  print ("Botti: " + Pile[Number2] + "?" )
                  Leave = 0
                else:
                  print ("Botti: " + Veryconfused[Think] + Exclaim[Biggere])
                  Leave = 0
                Talkon = input("You: ")

         if ("Bye" in Talkon or "Goodbye" in Talkon or "bye" in Talkon or Leave == 4):
            Number2 = random.randrange(0,6)
            Last = random.randrange(0,3)
            if (Leave == 4):
              print ("Botti: " + Nochat[Respondi] + Leaving[Number2] + Exclaim[Last])
            else:
              print("Botti: " + Leaving[Number2] + Exclaim[Last])
            break

#And so at last my brain is finally a piece of fried meat
def fastapi_app():
    bot = EchoBot()
    app = fp.make_app(
        bot,
        access_key=bot_access_key,
        bot_name=bot_name,
        allow_without_key=not (UGnxh9XbRNNChOnv2SmPeG7ybA3NT1J6 and Botti),
    )
    return app
