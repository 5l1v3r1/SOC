import os
import json
import time
import requests
import urllib
import sys
import progressbar
import colorama
from colorama import Fore,Back,Style
from validate_email import validate_email
from os import system
import platform
import os
import time

colorama.init()
def info():
  Fore.RESET
  system('clear')
  print("1) Check mail")
  print("2) Verify phone number")
  print("3) Generate passwords")
  print("4) Get geolocation")
  print("5) Back")
  ask=input("<SOCIAL>")
  if ask == "1":
   system('clear')
   email=input("Enter your email:")
   bar = progressbar.ProgressBar(maxval=30, widgets=[Fore.RESET+'Checking email:',progressbar.Bar(left=Fore.RED+'[', marker=Fore.GREEN+'#', right=Fore.RED+']'),]).start()
   check=validate_email(email,verify=True)
   check=str(check)
   check=check.lower()
   for x in range(30):
    bar.update(x)
    time.sleep(0.01)
   bar.finish() 
   if check == "true":
    print(Fore.GREEN+"Email was found!("+email+")"+Fore.RESET)
    print("5) Back")
    y=input("<SOCIAL>")
    if y == "5":
     os.system('clear')
     info()
    else:
     print(Fore.GREEN+"Ok,Bye...")
     exit(0)
   else:
    print(Fore.RED+"Email wasn't found!("+email+")"+Fore.RESET)
    print("5) Back")
    y=input("<SOCIAL>")
    if y == "5":
     os.system('clear')
     info()
    else:
     print(Fore.GREEN+"Ok,Bye...")
     exit(0)
  elif ask == "2":
   key="6bc2663d231ea028c6e6c47debf9151d"
   num=input("Enter phone number(with '+'):")
   api="http://apilayer.net/api/validate?access_key="+key+"&number=" + num +"&country_code=&format=1"
   information=requests.get(api)
   output=information.text
   inf=output
   output=output.upper()
   output=output.replace("{","")
   output=output.replace("}","")
   output=output.replace(","," ")
   output=output.replace('"','')
   print(Fore.RED+"////////////////////////////////////////////")
   print(Fore.GREEN+output+Fore.RESET)
   print(Fore.RED+"////////////////////////////////////////////"+Fore.RESET)
   print("5) Back")
   y=input("<SOCIAL>")
   if y == "5":
    os.system('clear')
    info()
   else:
    print(Fore.GREEN+"Ok,Bye...")
    exit(0)
  elif ask == "3":
   Fore.RESET
   import pas
   pas.main()
  elif ask == "4":
   system('./track')
  elif ask == "5":
   start()
  else:
   system('clear')
   info()
def spam():
 system('clear')
 print("Start spamming to:")
 print("1) Mobile phone number")
 print("2) Email")
 print("3) Back")
 ask=input("<SOCIAL>")
 if ask == "1":
  c=""
  number=input("Enter phone-number (without '+7'):")
  th=input("Enter number of threads:")
  for v in number:
   print(v)
   if v == "+":
    c="+7"
    number=number.replace('+7',' ')
    break
   else:
    c="+7"
    break
  system('python3 bomber.py --sms '+th+' '+'--country '+c+' '+number) 
 elif ask == "2":
  import email_bomber
  email_bomber.main()
 elif ask == '3':
  system('clear')
  start()
 else:
  system('clear')
  spam()
def brute():
 system('clear')
 print("1) Facebook account")
 print("2) Instagram account")
 print("3) Back")
 ask=input("<SOCIAL>")
 if ask == "1":
  import brute_facebook as fb
  fb.main()
 elif ask == "2":
  system('./brute_instagram')
 elif ask == "3":
  start()
 else:
  brute()
def start():
 system('clear')
 print("1) Information gathering")
 print("2) Spamming")
 print("3) Cracking social accounts")
 ask=input("<SOCIAL>")
 if ask == "1":
  info()
 if ask == "2":
  spam()
 if ask == "3":
  brute() 
if __name__ == '__main__':
 start()
