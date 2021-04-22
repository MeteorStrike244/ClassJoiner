import os
import os.path
from selenium import webdriver
import pyautogui
import cv2
import time
import sys
import pickle
from sys import exit

with open('C:/ClassJoiner/classnum.pckl', 'rb') as fclass: 
    class_amount = pickle.load(fclass)

if class_amount == ['1']:
    with open('C:/ClassJoiner/cfg.pckl', 'rb') as f: 
        g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link = pickle.load(f)

if class_amount == ['2']:
    with open('C:/ClassJoiner/cfg.pckl', 'rb') as f: 
        g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link = pickle.load(f)

if class_amount == ['3']:
    with open('C:/ClassJoiner/cfg.pckl', 'rb') as f: 
        g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link = pickle.load(f)

if class_amount == ['4']:
    with open('C:/ClassJoiner/cfg.pckl', 'rb') as f: 
        g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link = pickle.load(f)

if class_amount == ['5']:
    with open('C:/ClassJoiner/cfg.pckl', 'rb') as f: 
        g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link = pickle.load(f)

if class_amount == ['6']:
    with open('C:/ClassJoiner/cfg.pckl', 'rb') as f: 
        g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link, class_six_name, class_six_days, class_six_time, class_six_link = pickle.load(f)

if class_amount == ['7']:
    with open('C:/ClassJoiner/cfg.pckl', 'rb') as f: 
        g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link, class_six_name, class_six_days, class_six_time, class_six_link, class_seven_name, class_seven_days, class_seven_time, class_seven_link = pickle.load(f)

if class_amount == ['8']:
    with open('C:/ClassJoiner/cfg.pckl', 'rb') as f: 
        g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link, class_six_name, class_six_days, class_six_time, class_six_link, class_seven_name, class_seven_days, class_seven_time, class_seven_link, class_eight_name, class_eight_days, class_eight_time, class_eight_link = pickle.load(f)

if class_amount == ['9']:
    with open('C:/ClassJoiner/cfg.pckl', 'rb') as f: 
        g_user, g_pass, class_one_name, class_one_days, class_one_time, class_one_link, class_two_name, class_two_days, class_two_time, class_two_link, class_three_name, class_three_days, class_three_time, class_three_link, class_four_name, class_four_days, class_four_time, class_four_link, class_five_name, class_five_days, class_five_time, class_five_link, class_six_name, class_six_days, class_six_time, class_six_link, class_seven_name, class_seven_days, class_seven_time, class_seven_link, class_eight_name, class_eight_days, class_eight_time, class_eight_link, class_nine_name, class_nine_days, class_nine_time, class_nine_link = pickle.load(f)


print("Variables loaded. Wait for dev to add more to the program")
time.sleep(5)