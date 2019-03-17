'''Module'''
import os,urllib2,time,sys
from time import sleep
'''COLOR'''
if sys.platform in ["linux","linux2"]:
	W = ("\033[0m")
	G = ("\033[32;1m")
	R = ("\033[31;1m")
'''Script'''
'''banner'''
banner = (G+" .d8888. d888888b \n 88'  YP `~~88~~' "+R+"Tools : Sudo-Termux\n"+G+" `8bo.      88    "+R+"Version : 1.0\n"+G+"   `Y8b.    88    "+R+"Author : Alee Martinezz\n"+G+" db   8D    88    "+R+"http://github.com/leemrtnzz\n"+G+" `8888Y'    YP    ")
def xnchan():
 try:
    print (R+"-----------------------------------------")
    print (banner)
    print (R+"-----------------------------------------")
    print (G+"[+] installing sudo-termux...\n")
    sleep(3)
    os.system("apt install ncurses-utils")
    sleep(3)
    u = urllib2
    site = ("https://gitlab.com/st42/termux-sudo/raw/master/sudo")
    u.Request(site)
    r = u.urlopen(site)
    c = r.read()
    file = open("sudo","a")
    file.write(c)
    sleep(3)
    os.system("cat sudo > /data/data/com.termux/files/usr/bin/sudo")
    os.system("chmod 700 /data/data/com.termux/files/usr/bin/sudo")
    print (G+"\n[+] Success install sudo-termux")
 except:
    print (R+"\n[!] Failed install sudo-termux")
if __name__ == "__main__":
	xnchan()