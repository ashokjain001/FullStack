# This is a project from a course in Udemy - "Website Blocker" where social netwroking websites are blocked from 8 AM to 5 PM
# This project makes use of the host file and updating it based on the time of the day, if the time is between 8 am to 5 pm
# then websites are redirected to 127.0.0.1 by writing 127.0.01 www.facebook.com to the host file. If the time is after 5 PM then
#these lines from host files are removed.


from datetime import datetime as dt
import time

#hosts_path = r"\etc\hosts"
hosts_path = "/Users/ashokjain/Desktop/Python/websiteblocker.txt"

redirect = "127.0.0.1"
websitelist = ["www.facebook.com", "www.twitter.com"]

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          17):

        print("Work Hours")

        with open(hosts_path, 'r+') as  hostfile:
            content = hostfile.read()

            for link in websitelist:
                if link in content:
                    pass
                else:
                    hostfile.write(redirect + " " + link + "\n")

    else:

        print("fun hours")

        with open(hosts_path, 'r+') as hostfile:
            content = hostfile.readlines()
            hostfile.seek(0)

            for line in content:
                if not any(link in line for link in websitelist):
                    hostfile.write(line)
            hostfile.truncate()

    time.sleep(5)

