import os, platform, time, sys
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
 
print('\033[1;91m[◽\033[1;91m] \033[1;92mChecking For Update...')
os.system('git pull')
ranaxd = platform.architecture()[0]
if ranaxd == '64bit':
 print('\033[1;91m[◽\033[1;91m] \033[1;92mYour Device is 64bit')
 import MAHADI
elif ranaxd == '32bit':
 print('\033[1;91m[◽\033[1;91m] \033[1;92mYour Devive is 32bit')
 exit() 
 
 
