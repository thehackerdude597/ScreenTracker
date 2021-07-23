from win10toast import ToastNotifier
import os
import time
import webbrowser

print("ScreenHelper, press A to see how it works")

user = input("")

if user == "A":
    print("ScreenHelper does not allow you to be on your computer for longer than two hours at time. After two hours your computer will shutdown. Are you sure you'd like to run this")

if user == "a":
    print("ScreenHelper does not allow you to be on your computer for longer than two hours at time. After two hours your computer will shutdown. Are you sure you'd like to run this")

name = input("What would you like me to call you")

print("Alright we can become best friends", name)


user_rem = ToastNotifier()

user_rem.show_toast("ScreenHelper", "ScreenHelper has started")

alert_0 = ToastNotifier() 

alert_1 = ToastNotifier()

alert_2 = ToastNotifier()

alert_3 = ToastNotifier()



user_start = input("Would you like to start a ScreenHelper session? yes/no")   

if user_start == "yes":
    print("Ok...Starting Now")
    time.sleep(3600)
    alert_0.show_toast("ScreenHelper", "You've now been on the following device for 1hr")
    time.sleep(5100)
    alert_1.show_toast("ScreenHelper", "You've now been on the following device for 1hr + 25min")
    time.sleep(7200)
    reminder_2 = alert_2.show_toast("ScreenHelper", "You've now been on the following device for 2hr, your device will now shutdown")
    os.system("shutdown /s /t 1")

if user_start == "no":
    print("Ending session")
    alert_3.show_toast("ScreenHelper", "The ScreenHelper session has now ended")
    exit()

print("Here are some of the great effects of limited screentime")


webbrowser.open("https://www.mayoclinichealthsystem.org/hometown-health/featured-topic/5-ways-slimming-screen-time-is-good-for-your-health")
