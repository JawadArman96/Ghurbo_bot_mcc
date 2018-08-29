# encoding=utf-8
import random
import re
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')
flight_schedule=[]#["শিডিউল","টাইমটেবিল","সময়","টাইম","schedule","timetable","time","shomoy","somoy","date","ডেট"]
flight_package=[]
flight_fair=[]
flight_query=[]
flight_info="ধন্যবাদ, ghurbo.com থেকে আপনি আপনার ফ্লাইট শিডিউল,প্যাকেজ,টিকিট-ভাড়া ও অন্যান্য যাবতীয় তথ্য জানতে পারবেন\nনিচের লিংকে ক্লিক করে ghurbo flight serach option এ গিয়ে আপনার ফ্লাইট \nশিডিউল এন্ট্রি করে তথ্যগুলো সম্পর্কে জেনে নিন"
flight_search_link="\n\nhttps://mccltd.info//projects/ghurbo/messenger-bot/form.php"
ask_info="আপনি ফ্লাইট শিডিউল,ফ্লাইট প্যাকেজ,টিকিট-ভাড়া অথবা অন্য কোন বিষয় সম্পর্কে জানতে চান ?"

def find_if_there(list_name,message):
    for entry in list_name:
        m= re.search(entry,message)
        if m is not None:
            #print("yes.........")
            return True
    return False
def basic_flight_query(message):
    a=1
    # flight schdeule
    if find_if_there(flight_schedule,message)==True:
        print("basic flight query")

    # flight package

    # flight fair
def advanced_flight_query(message):
    a=1
    # Available flights

    #flight routes

    #shortest fair flights

    #shortest time

    #providing the nearest airport for any place

def customer_flight_query(message):          # detect what flight query customer asking
    a=1

def detect_flight_query(message):   # Checking query if it is flight related or not
    for query in flight_query:
        match=re.search(query,message)
        if match is not None:
            reply=flight_info+flight_search_link
            return reply
    return ""

def add_list_data(query_list,filename,):
    f= open(filename,"r")
    lines=f.readlines()
    for line in lines:
        a=""
        for c in line:
            if(c=='\n'):
                break;
            a+=c
        query_list.append(a)

def load_data():
    add_list_data(flight_schedule,"customer_query\\flight_query_domains\\flight_query_schedule.txt")
    add_list_data(flight_schedule,"customer_query\\flight_query_domains\\flight_query_package.txt")
    add_list_data(flight_schedule,"customer_query\\flight_query_domains\\flight_query_fair.txt")