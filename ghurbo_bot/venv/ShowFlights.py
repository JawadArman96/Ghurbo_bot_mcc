import os
#os.system("php /C:/wamp64/www/ghurbo/test.php")
flight_type=" one_way_all_search"
dep=" DAC"
des=" SIN"
ddt=" 2018-09-06"
rdt=" 2018-09-10"
cl=" economy"
nad=1;
nc=0
ni=0


def show_results():
    f = open("description.txt", "r")
    lines = f.readlines()
    a = ""
    flag = 0
    for line in lines:
        for c in line:
            if c == "<":
                flag = 1
            if c == ">":
                a += "\n"
                flag = 0
            if flag == 0:
                a += c

    return a
def show_flights():
    f = open("description.txt", "r")
    lines = f.readlines()
    a = ""
    flag = 0
    for line in lines:
        for c in line:
            a+=c;
    return a

def search_flight():
    command_path = "C:/wamp64/bin/php/php5.6.35/php.exe C:/wamp64/www/bot/test2.php"  # one_way_all_search DAC CGP 2018-08-18 2018-09-26 economy 1 0 0"
    command_path = command_path + flight_type + dep + des + ddt + rdt + cl + " " + str(nad) + " " + str(nc) + " " + str(ni)
    print (command_path)
    os.system(command_path)
#search_flight()