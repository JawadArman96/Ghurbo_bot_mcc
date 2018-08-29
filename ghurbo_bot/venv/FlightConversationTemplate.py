# encoding=utf-8
import random
import re
import sys
import datetime
import BotArchitecture
reload(sys)
sys.setdefaultencoding('utf-8')
#####################################################################################################

ask_info=[]
place_list=[]
flight_class=[]
qery_id=0;
first_place_flag=0
class flight_info:
    departure=""
    destination=""
    date=""
    passenger_class=""
    nAdult=0;
    nChild=0;
    nInfant=0;
    up_down=0;
    id=-1
    return_date=""
    def __init__(self):
        self.data=[]
    def show_all(self):
        print (self.departure+" "+self.destination+" "+self.date+" "+self.return_date+" "+self.passenger_class)
        print (str(self.nAdult)+" "+str(self.nChild)+" "+str(self.nInfant))
        print(self.up_down)
#fi=flight_info()
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
    add_list_data(ask_info,"customer_query\\flight_query_domains\\bot_ask_info_flight.txt")
    add_list_data(place_list,"customer_query\\flight_query_domains\\place_list.txt")
    add_list_data(flight_class,"customer_query\\flight_query_domains\\flight_class_list.txt")

def detect_place(string):
    for place in place_list:
        m=re.search(place,string)
        if m is not None:
            return m.group(0)
    return None

def detect_class(string):
    for item in flight_class:
        m=re.search(item,string)
        if m is not None:
            return m.group(0)
    return ""
def detect_adult_child_infant(string,fi):
    adult="[0-9]"+"(.*)"
    flag=0
    m=re.search(adult,string)
    if m is not None:
        a=string.__getslice__(m.start(),m.start()+1)
        string=m.group(1)
        fi.nAdult=int(a)
        flag=1
    child="[0-8]"+"(.*)"
    m = re.search(adult, string)
    if m is not None:
        a = string.__getslice__(m.start(), m.start() + 1)
        string = m.group(1)
        fi.nChild = int(a)
        flag=1
    infant="[0-1]"+"(.*)"
    m = re.search(adult, string)
    if m is not None:
        a = string.__getslice__(m.start(), m.start() + 1)
        string = m.group(1)
        fi.nInfant = int(a)
        flag=1
    if flag==1:
        return "ok"
    else:
        return ""
def detect_up_down(string):
    pattern="yes|y|ok|হ্যা।|আচ্ছা|হা|ha|up down|up_down|আপ ডাউন|round_trip|round trip|রাউন্ড ট্রিপ|রাউন্ড_ট্রিপ"
    m=re.search(pattern,string)
    if m is not None:
        return 1;
    pattern="one_way|1 way|one way|ওয়ান ওয়ে|ওয়ানওয়ে|ওয়ান_ওয়ে|no|na|না|not"
    m = re.search(pattern, string)
    if m is not None:
        return 0;
    return -1


def __preProcess():
    for i in range(0,100000000,1):
        a=1
def converstation(message,fi):
    message=message.lower()
    # res=detect_place(message)
    # if res is not None:
    #     string=ask_info.__getitem__(1)
    #     fi.departure=res
    #     return string
    res=BotArchitecture.detect_date(message)
    if res is not None:
        fi.date=res
        string = ask_info.__getitem__(2)
        return string
    res = detect_class(message)
    if res is not None:
        string = ask_info.__getitem__(3)
        fi.passenger_class=res
        return string
    #
    # if fi.id>6:
    #     return unicode("okay")
    # string=ask_info.__getitem__(fi.id);
    # if fi.id==1:
    #     res= detect_place(message)
    #     fi.departure=res
    #     fi.id=fi.id+1
    # elif fi.id==2:
    #     res = detect_place(message)
    #     fi.destination=res
    #     fi.id=fi.id+1
    # elif fi.id==3:
    #     res = BotArchitecture.detect_date(message)
    #     fi.date=res
    #     fi.id=fi.id+1
    # elif fi.id==4:
    #     res = detect_class(message)
    #     fi.passenger_class=res
    #     fi.id=fi.id+1
    # elif fi.id==5:
    #     res = detect_adult_child_infant(message,fi)
    #     fi.id=fi.id+1
    # elif fi.id==6:
    #     res = detect_up_down(message)
    #     fi.id=fi.id+1
    #     if res!=-1:
    #         fi.up_down=res
    return unicode(string)

load_data()
# a="abdshfgsdgfhsddsjf"
# b="shfg"
# m=re.search(b,a)
# a=a.__getslice__(m.start(),m.end())
# print(a)
# id=0
# user_input=""
# while(True):
#     if(id==7):
#         break;
#     user_input = raw_input()
#     string = converstation(user_input, id)
#     print string
#     id=id+1
#
# fi.show_all()