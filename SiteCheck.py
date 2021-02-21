# -*- Language: UTF-8 / Python 3.x.x -*- #

# Import all required dependencies
import urllib3
import urllib.request
import time
import requests
import socket

# Introduce the software
print("This is a tool to test if a website is suffering from outages")
print("and to look up the IP address of the requested site.")
print("The author of this software is R34p3r")
print("If you wish to see any improvements or changes, please contact me by email")
print("----------------------------------------------------------------------------------------")

# Take user inputs to find the site to test
name = input("Please enter your name: ")
site_to_check = input("Please enter the website you wish to check now: ")

# Convert the website URL into an IP address and store to variable
print("Below is the IP address of the site you searched, please press enter to continue")
IP = input(socket.gethostbyname(site_to_check))

# Test if the site is online and allow user to select between secure or non secure protocols
site_type = input("Is this site HTTPS(1) or HTTP(2)?")
if site_type == 2:
    request_response = requests.head("http://" + site_to_check)
else:
    request_response = requests.head("https://" + site_to_check)
status_code = request_response.status_code
website_is_up = status_code == 200

# Output to user
if (website_is_up == True):
    print("The website you selected is running!")
    retry = input("Would you like to run another test? y=1/n=0")
    if retry == 0:
        exit()
    else:
        exec(open("./SiteCheck.py").read())
    
if (website_is_up == False):
    retry = input("The site you searched is either down or doesn't exist, would you like to retry? y=1/n=0")
    if retry == 0:
        exit()
    else:
        exec(open("./SiteCheck.py").read())
        

