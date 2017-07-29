import datetime
import webbrowser
import time

def takeABreak():
    print "program started in ", time.ctime()
    for i in range(3):
        time.sleep(5)
        webbrowser.open("http://www.python.org")
    print "program ends on", time.ctime()
print takeABreak()


