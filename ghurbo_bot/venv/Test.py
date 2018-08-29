import os
#os.system("php /C:/wamp64/www/ghurbo/test.php")
flight_type=" one_way_all_search"
dep=" DAC"
des=" CGP"
ddt=" 2018-08-18"
rdt=" 2018-08-20"
cl=" economy"
nad=1;
nc=0
ni=0




command_path="C:/wamp64/bin/php/php5.6.35/php.exe C:/wamp64/www/ghurbo/test2.php"# one_way_all_search DAC CGP 2018-08-18 2018-09-26 economy 1 0 0"
command_path=command_path+flight_type+dep+des+ddt+rdt+cl+" "+str(nad)+" "+str(nc)+" "+str(ni)
print (command_path)
os.system(command_path)

p="<br/>"
l=0
f=open("description.txt","r")
lines=f.readlines()
a=""
flag=0
for line in lines:
    for c in line:
        if c=="<":
            flag=1
        if c==">":
            a+="\n"
            flag=0
        if flag==0:
            a+=c




    print (a)








# import subprocess
# subprocess.call("php C:\\wamp64\\www\\ghurbo\\form.php")
# proc= subprocess.Popen("php C:\\wamp6\\www\\ghurbo\\form.php",shell=True,stdout=subprocess.PIPE)
# script_response= proc.stdout.read()
# # # if the script don't need output.
# # subprocess.call("php /path/to/your/script.php")
# #
# # # if you want output
# # proc = subprocess.Popen("php /path/to/your/script.php", shell=True, stdout=subprocess.PIPE)
# # script_response = proc.stdout.read()