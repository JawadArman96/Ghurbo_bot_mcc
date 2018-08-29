# encoding=utf-8
import random
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def pr_new_line():
    print("\n")
responses = {
    "what is your name?": "my name is ghurbo bot",
    "hi": "hello",
    "হ্যালো আমি ঘুরতে যেতে চাই" : "আপনি কোথায় ঘুরতে যেতে চান?",
    "কেমন আছ*" : [
                    "ভাল",
                    "মোটামুটি",
                    "খারাপ"
                 ]

}
print (responses["হ্যালো আমি ঘুরতে যেতে চাই"])
print("Echo bot 1...")
bot_template = "BOT : {0}"
user_template = "USER : {0}"
def respond(message):
    bot_message="I can hear you! You said: "+message
    return bot_message
message="hi"
print ("You:"+message)
print("Bot:"+respond(message))
pr_new_line()
# Iterate over the rules dictionary
#Echo bot 2
print("Echo bot 2...")

def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

message="hello"
send_message(message)
pr_new_line()

print("Chit chat...")

name = "Greg"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}

# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message
print(respond("what's your name?"))
print(respond("what's today's weather?"))

pr_new_line()

def response(message):
   # message=message.decode('utf-8').lower();
    if(message.endswith("?")):
        print "yes\n"
    else:
        print ("no\n")
    if message in responses:
        return random.choice(responses[message])

    if re.search("hi.*",message):
        print("Yes")
    message = message.decode('utf-8').lower();
    if message in responses:
        return responses[message]


# m="aoa"
# print(m)
# m = response("hoppp")
# print(m)

# regular expression

message="okay go go if you do you will die"
pattern="if(.*)"
m=re.search(pattern,message).group(0)
#print(m)


#Eliza 2 wxtracting key phrases

rules={"do you remember (.*)": ["Did you think I would forget {0}",
                                "Why haven't you been able to forget {0}",
                                'What about {0}', 'Yes .. and?'],
       "I want (.*)":["What would it mean if you got {0}",
                      "Why do you want {0}",
                      "What's stopping you from getting {0}"],
       "do you think (.*)": ["if {0}? Absolutely.",
                             "No chance"],
       "if (.*)": ["Do you really think it's likely that {0}",
                   "Do you wish that {0}",
                   "What do you think about {0}",
                   "Really--if {0}"]
       }


# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None

    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase


# Test match_rule
print("Searching word with regular expression...")
print(match_rule(rules, "do you remember your last birthday"))
pr_new_line()

#Eliza 3
# Define replace_pronouns()
def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me','you',message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my','your',message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your','my',message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you','me',message)

    return message
print("Substituting Pronoun...")
print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))
pr_new_line()