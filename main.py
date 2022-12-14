import random, time, sys
from libraries import jokes, trivia, day

def type_out(string, t):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(t)
#chatbot code
message = ''
reply = ''
human = input('Bot: What is your name? ')
time.sleep(0.5)
type_out('Bot: Hello ' + human + '.', 0.05)
time.sleep(0.5)
print()
type_out("Bot: You may ask me to tell a joke, ", 0.04)
print()
type_out("random trivia, or how my day is.", 0.04)
print()
type_out('Try finding out some of my other', 0.04)
print()
type_out('features by saying different things!', 0.04)
print()
type_out('You may end our chat at any time', 0.04)
print()
type_out('by typing "bye".', 0.04)
print()
type_out("--------------------------------", 0.025)
time.sleep(0.5)
print()
def getReply(message):
    #All current responses programmed into the bot for different prompts
    if ('who' in message and 'you' in message) or (('what' in message or 'what\'s' in message) and 'name' in message):
        reply = "I'm Chat."
    elif 'joke' in message:
        reply = random.choice(jokes)
    elif 'trivia' in message:
        reply = random.choice(trivia)
    elif 'day' in message:
        reply = random.choice(day)
    elif 'love' in message and 'you' in message:
        reply = 'I\'m sorry, I don\'t feel love.'
    elif 'hello' in message:
        reply = 'Hello ' + human + '.'
    elif 'bye' in message:
        secondChance = ''
        while secondChance != 'y' and secondChance != 'n':
            secondChance = input('Are you sure you would like to end the chat? y/n: ')
            if secondChance == 'y':
                reply = 'bye'
                return True
            elif secondChance == 'n':
                reply = 'Okay, let\'s keep chatting.'
    else:
        reply = "I don't know how to respond to that."

    if reply != 'bye':
        type_out('Bot: ' + reply, 0.05)
        print()
while True:
    message = input('> ')
    if getReply(message):
        type_out('Bot: Goodbye.', 0.05)
        break