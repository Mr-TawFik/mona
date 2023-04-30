#Use With Python 3
import requests,re,sys,random,time,os
import os
from colorama import Fore, Back, init
from threading import Thread
init (autoreset = True)
from random import choice
init()
def logo():
    os.system('cls')
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
 
                
         ███    ███ ██████  ██   ██       ██████  ██   ██  ██████  ███    ██ ███████ 
         ████  ████ ██   ██  ██ ██        ██   ██ ██   ██ ██    ██ ████   ██ ██      
         ██ ████ ██ ██████    ███   █████ ██████  ███████ ██    ██ ██ ██  ██ █████   
         ██  ██  ██ ██   ██  ██ ██        ██      ██   ██ ██    ██ ██  ██ ██ ██      
         ██      ██ ██   ██ ██   ██       ██      ██   ██  ██████  ██   ████ ███████ 
                                                                            
                    Bulk Phone Number Generator  |  Coded by Mrx TawFik                          
                                [+]  My Telegram: @MrxTawFik  [+]
                                [+]  Channel: @Mrx_TawFik     [+]               
			                  """
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )        

logo()
print ("-"*52)
cc = input(str(' \033[1;31m1 : --> \033[1;33m Enter the Country Code \033[1;31m[ EX +1 For USA ] : \033[1;37m'))

sc = input(str(' \033[1;31m2 : -->  \033[2;32mEnter the Area Code \033[1;31m[ EX 910 ] : \033[1;37m'))

n = int(input(" \033[1;31m3 : -->  \033[2;36mEnter Amount of numbers \033[1;31m[ 50k ] : \033[1;37m"))

lent = int(input(' \033[1;31m4 : -->  \033[0mLength Remaining Digits \033[1;31m[ 7 FOR USA ] : \033[1;37m'))

mow = str('9'*lent)
print ('-'*52)
def random_phone_num_generator():
    first = str(random.randint(0,int(mow))).zfill(lent)
    return (first)

save = open('Mrx-TawFik/Phone.txt','a+')
for i in range(0,n):
    rez = cc+sc+random_phone_num_generator()
    save.write(rez + '\n')
print(' ✔️ \033[1;35mPhone Numbers Saved In  \033[2;32m[ Mrx-TawFik/Phone.txt ] ')
input(' ✔️ \033[1;36mEnter any Key to exit > ')


