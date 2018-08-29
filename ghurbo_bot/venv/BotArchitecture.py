# encoding=utf-8
import random
import re
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

##########################################################################################


bot_template = "BOT : {0}"
user_template = "USER : {0}"
customer_addressing=[]#["শুভ অপ্রাহ্ন", "শুভ সন্ধ্যা","শুভ স্কাল", "ধ্ন্যবাদ"];
wh_question=[]#["কোথায়", "কখন", "কিভাবে","কেন","কেমন","কি","কে","কিরকম","কিধরনের","কিজন্য","কিকারনে","কিকরে"]
responses = {
    "what is your name?": "my name is ghurbo bot",
    "hi": "hello",
    "আমি ঘুরতে যেতে চাই" : "আপনি কোথায় ঘুরতে যেতে চান?",
    "আমি ঘুরতে যাব" : "আপনি কোথায় ঘুরতে যেতে চান?",
    "কেমন আছ*" : [
                    "ভাল",
                    "মোটামুটি",
                    "খারাপ"
                 ]

}

query_type=["greetings","wh_question","other_question","information","other","yes_no_q"]
greeting_responses={
    "হ্যালো":customer_addressing,
    "হায়":customer_addressing,
    "hi":customer_addressing,
    "hello":customer_addressing
}
def load_data():
    f=open("wh_question.txt","r")
    lines=f.readlines()
    quws=[]
    for line in lines:
        a = ""
        for c in line:
            if(c=='\n'):
                break;
            a+=c
        wh_question.append(a)
    f=open("addressing.txt","r")
    lines=f.readlines()
    for line in lines:
        a=""
        for c in line:
            if(c=='\n'):
                break
            a+=c
        customer_addressing.append(a)

def respond(message):
    bot_message="I can hear you! You said: "+message
    return bot_message

def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message

def response(message):
   # message = message.decode('utf-8').lower();
    if message in greeting_responses:
        print(greeting_responses[message])
    return

def detect_date(message):
    a=""
    pattern = "^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$|^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{2}$"
    m = re.search(pattern, message)
    if m is not None:
        a=message.__getslice__(m.start(),m.end())
        #print(a)
        return a
    pattern = "^(0?[1-9]|1[012])[\/\-](0?[1-9]|[12][0-9]|3[01])[\/\-]\d{4}$"
    m = re.search(pattern, message)
    if m is not None:
        a = message.__getslice__(m.start(), m.end())
    return a

def categorize_query(message):
    print("message: "+message)
    if message in responses:
        print(responses[message])
    if message in greeting_responses:
        hour = datetime.datetime.now().hour
        if(hour>6 and hour<12):
            print(greeting_responses[message].__getitem__(0))
        elif (hour>12 and hour<18):
            print(greeting_responses[message].__getitem__(1))
        elif hour>18 and hour <20:
            print(greeting_responses[message].__getitem__(2))
        else:
            print(greeting_responses[message].__getitem__(3))
        return query_type[0]
    for greeting,ans in greeting_responses.items():
        pattern=greeting+"(.*)"
        match=re.search(pattern,message);
        if match is not None:
            #print("Greeting")
            if match.group(1)!="" :
               return categorize_query(match.group(1))

    if (message.endswith("কি?") or message.endswith("কি")):
        print("May be yes/no question");
        return query_type[5]
    m = re.search("কি ", message)
    if m is not None:
        return query_type[5]

    for pattern in wh_question:
        m=re.search("কে ",message)
        m = re.search(pattern,message)
        if m is not None:
            return query_type[1]
        if m is not None:
            return query_type[1]
    if (message.endswith("?")):
        print("Some type of Question Asked/ Yes no question");
        return query_type[2]
#    ([12]\d{3}-(0[1-9] | 1[0-2]) - (0[1 - 9] | [12]\d | 3[01]))

    detect_date(message)
    return query_type[4]
#categorize_query("হায়")

#message="হ্যালো"
#categorize_query(message)
load_data()





