import os
import os.path
from selenium import webdriver
import pyautogui
import cv2
import time
import sys
import pickle
from sys import exit

if os.path.exists("C:/ClassJoiner"):
    print("Data directory exists, good job")
else:
    print("No data directory found, creating a new one.")
    cdrive = "C:/"
    newpathname = "ClassJoiner"
    path = os.path.join(cdrive, newpathname)
    os.mkdir(path)

class_amount = input("How many total unique Google Meet links do you have?:  ")

with open('C:/ClassJoiner/classnum.pckl', 'wb') as fclass:
    pickle.dump([class_amount], fclass)

def setup_class_one():
    global g_user
    global g_pass

    global class_one_name
    global class_one_days
    global class_one_time
    global class_one_link

    g_user = input("Pleae enter the username of your Google account:    ")
    g_pass = input("Pleae enter the password of your Google account:    ")
    class_one_name = input("What is the name of your first class:    ")
    class_one_days = input("What days of the week does your first class meet on?\nIf it meets Monday, Wednesday, and Thursday:MWR\nIf it meets every school day:MTWRF\nIf it meets all seven weekdays:SMTWRFU\nOr, if it meets every other school day on day ones:1\nOr every other schoold day on day twos:2\n Input Here:    ")
    class_one_time = input("What time does your first class meet at? Please specify time in 24h (A class at 2:30pm would be 14:30):    ")
    class_one_link = input("What is the Google Meet link for your first class:    ")
def setup_class_two():
    
    global class_two_name
    global class_two_days
    global class_two_time
    global class_two_link
    
    class_two_name = input("What is the name of your second class:    ")
    class_two_days = input("What days of the week does your second class meet on:    ")
    class_two_time = input("What time does your second class meet at? Please specify time in 24h (A class at 2:30pm would be 14:30):    ")
    class_two_link = input("What is the Google Meet link for your second class:    ")
def setup_class_three():
    
    global class_three_name
    global class_three_days
    global class_three_time
    global class_three_link
    
    class_three_name = input("What is the name of your third class:    ")
    class_three_days = input("What days of the week does your third class meet on:    ")
    class_three_time = input("What time does your third class meet at? Please specify time in 24h (A class at 2:30pm would be 14:30):    ")
    class_three_link = input("What is the Google Meet link for your third class:    ")
def setup_class_four():

    global class_four_name
    global class_four_days
    global class_four_time
    global class_four_link

    class_four_name = input("What is the name of your fourth class:    ")
    class_four_days = input("What days of the week does your fourth class meet on:    ")
    class_four_time = input("What time does your fourth class meet at? Please specify time in 24h (A class at 2:30pm would be 14:30):    ")
    class_four_link = input("What is the Google Meet link for your fourth class:    ")
def setup_class_five():

    global class_five_name
    global class_five_days
    global class_five_time
    global class_five_link

    class_five_name = input("What is the name of your fifth class:    ")
    class_five_days = input("What days of the week does your fifth class meet on:    ")
    class_five_time = input("What time does your fifth class meet at? Please specify time in 24h (A class at 2:30pm would be 14:30):    ")
    class_five_link = input("What is the Google Meet link for your fifth class:    ")
def setup_class_six():

    global class_six_name
    global class_six_days
    global class_six_time
    global class_six_link

    class_six_name = input("What is the name of your sixth class:    ")
    class_six_days = input("What days of the week does your sixth class meet on:    ")
    class_six_time = input("What time does your sixth class meet at? Please specify time in 24h (A class at 2:30pm would be 14:30):    ")
    class_six_link = input("What is the Google Meet link for your sixth class:    ")
def setup_class_seven():

    global class_seven_name
    global class_seven_days
    global class_seven_time
    global class_seven_link

    class_seven_name = input("What is the name of your seventh class:    ")
    class_seven_days = input("What days of the week does your seventh class meet on:    ")
    class_seven_time = input("What time does your seventh class meet at? Please specify time in 24h (A class at 2:30pm would be 14:30):    ")
    class_seven_link = input("What is the Google Meet link for your seventh class:    ")
def setup_class_eight():

    global class_eight_name
    global class_eight_days
    global class_eight_time
    global class_eight_link

    class_eight_name = input("What is the name of your eighth class:    ")
    class_eight_days = input("What days of the week does your eighth class meet on:    ")
    class_eight_time = input("What time does your eighth class meet at? Please specify time in 24h (A class at 2:30pm would be 14:30):    ")
    class_eight_link = input("What is the Google Meet link for your eighth class:    ")
def setup_class_nine():

    global class_nine_name
    global class_nine_days
    global class_nine_time
    global class_nine_link

    class_nine_name = input("What is the name of your ninth class:    ")
    class_nine_days = input("What days of the week does your ninth class meet on:    ")
    class_nine_time = input("What time does your ninth class meet at? Please specify time in 24h (A class at 2:30pm would be 14:30):    ")
    class_nine_link = input("What is the Google Meet link for your ninth class:    ")

if class_amount == "0":
    print("Then why are you using the program idiot?")
if class_amount == "1":
    setup_class_one()
    with open('C:/ClassJoiner/cfg.pckl', 'wb') as f:
        pickle.dump([g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link], f)
if class_amount == "2":
    setup_class_one()
    setup_class_two()
    with open('C:/ClassJoiner/cfg.pckl', 'wb') as f:
        pickle.dump([g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link], f)
if class_amount == "3":
    setup_class_one()
    setup_class_two()
    setup_class_three()
    with open('C:/ClassJoiner/cfg.pckl', 'wb') as f:
        pickle.dump([g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link], f)
if class_amount == "4":
    setup_class_one()
    setup_class_two()
    setup_class_three()
    setup_class_four()
    with open('C:/ClassJoiner/cfg.pckl', 'wb') as f:
        pickle.dump([g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link], f)   
if class_amount == "5":
    setup_class_one()
    setup_class_two()
    setup_class_three()
    setup_class_four()
    setup_class_five()
    with open('C:/ClassJoiner/cfg.pckl', 'wb') as f:
	    pickle.dump([g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link], f)
if class_amount == "6":
    setup_class_one()
    setup_class_two()
    setup_class_three()
    setup_class_four()
    setup_class_five()
    setup_class_six()
    with open('C:/ClassJoiner/cfg.pckl', 'wb') as f:
	    pickle.dump([g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link, class_six_name, class_six_days, class_six_time, class_six_link], f)
if class_amount == "7":
    setup_class_one()
    setup_class_two()
    setup_class_three()
    setup_class_four()
    setup_class_five()
    setup_class_six()
    setup_class_seven()
    with open('C:/ClassJoiner/cfg.pckl', 'wb') as f:
	    pickle.dump([g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link, class_six_name, class_six_days, class_six_time, class_six_link, class_seven_name, class_seven_days, class_seven_time, class_seven_link], f)
if class_amount == "8":
    setup_class_one()
    setup_class_two()
    setup_class_three()
    setup_class_four()
    setup_class_five()
    setup_class_six()
    setup_class_seven()
    setup_class_eight()
    with open('C:/ClassJoiner/cfg.pckl', 'wb') as f:
        pickle.dump([g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link, class_six_name, class_six_days, class_six_time, class_six_link, class_seven_name, class_seven_days, class_seven_time, class_seven_link, class_eight_name, class_eight_days, class_eight_time, class_eight_link], f)
if class_amount == "9":
    setup_class_one()
    setup_class_two()
    setup_class_three()
    setup_class_four()
    setup_class_five()
    setup_class_six()
    setup_class_seven()
    setup_class_eight()
    setup_class_nine()
    with open('C:/ClassJoiner/cfg.pckl', 'wb') as f:
	    pickle.dump([g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link, class_six_name, class_six_days, class_six_time, class_six_link, class_seven_name, class_seven_days, class_seven_time, class_seven_link, class_eight_name, class_eight_days, class_eight_time, class_eight_link, class_nine_name, class_nine_days, class_nine_time, class_nine_link], f)
    
if int(class_amount) > 9:
    print("At the moment, only 9 Google Meets are supported.")
    print("Closing program due to error in 5 seconds")
    time.sleep(5)
    sys.exit()

print("Class Setup Complete! Feel free to run ClassJoiner.exe now!")
time.sleep(3)