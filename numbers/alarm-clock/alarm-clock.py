from time import localtime, mktime, sleep, strftime, strptime
import subprocess

def alert():
    sound = "/Users/jackieluo/Documents/code/projects/numbers/alarm-clock/alert.wav"
    h = int(raw_input("Hours: "))
    m = int(raw_input("Minutes: "))
    s = int(raw_input("Seconds: "))
    if h > 12 or m > 60 or s > 60:
        print "I'm sorry, we don't support that amount of time! Try again."
        alert()
    sleep(h * 60 * 60 + m * 60 + s)
    return_code = subprocess.call(["afplay", sound])

def alarm():
    sound = "/Users/jackieluo/Documents/code/projects/numbers/alarm-clock/alert.wav"
    t = raw_input("Please enter the desired time in HH:MM:SS format: ")
    try:
        now = localtime()
        then = strptime("%s %s" % (strftime("%Y %m %d"), t), "%Y %m %d  %H:%M:%S")
    except ValueError:
        print "The time you entered is incorrect. Try again."
        alarm()
    sleep(mktime(then) - mktime(now))
    return_code = subprocess.call(["afplay", sound])

c = raw_input("Would you like to be alerted after a length of time (A) or at a certain time (B)? ")
if c.upper() == "A":
    alert()
elif c.upper() == "B":
    alarm()
else:
    print "Sorry, that's not an option! Please choose A or B."