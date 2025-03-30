import time
from datetime import datetime as dt

# blocking the website by editing the hosts file which will redirect the Website to local domain
# path of the host file eill be different for mac and linux
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
# following is the lists of website i want to block... one is the domain of website and other is host part of the website
website_list=["www.facebook.com","facebook.com","google.com","www.google.com","www.youtube.com","youtube.com"]

while True:
# time is set between 8am and 4pm. Sites will be blocked only between these hours
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
# to pause the while loop execution every time by 5 seconds
    time.sleep(5)
