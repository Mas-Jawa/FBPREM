# HAI BANG GANTENG
# SC INI PREMIUM YA BANG GRATISAN
# JANGAN DI JUAL BELIKAN YA BANG
# FOLLOW IG GUA @fendipendol65
# JANGAN DI RECODE YA BANG
# KALO MAU RECODE BELI DULU

import requests, json, os, sys, time
from bs4 import BeautifulSoup as bs
 
 # MODULE
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE

try:
    import requests
except ImportError:
    os.system('pip install requests')
from requests import post

try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system('pip install bs4')
    os.system('pip install requests')
    os.system('clear')
    from bs4 import BeautifulSoup as bs

try:
    import json
except ImportError:
    os.system('pip install json')
    os.system('clear')
    import json

try:
    import os
except ImportError:
    os.system('pip install os')
    os.system('clear')

try:
    import sys
except ImportError:
    os.system('pip install sys')
    os.system('clear')

try:
    import time
except ImportError:
    os.system('pip install time')
    os.system('clear')

try:
    import Flask
except ImportError:
    os.system('pip install Flask')
    os.system('clear')

try:
    import tkinter
except ImportError:
    os.system('pip install tkinter')
    os.system('clear')

# IMPORT MODULE

import requests, bs4, json, os, sys, random, datetime, time, re, rich, base64, subprocess, uuid, calendar
from time import sleep
import shutil
import hashlib
from datetime import date
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.console import Console
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

#------[DATA SOUND/MODULE]------#
os.system("pkg install espeak")
os.system('clear')
time.sleep(2)
os.system('espeak -a 300 " CHECK!!"')
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mCHECK!!')
time.sleep(4)
os.system('espeak -a 300 " WELCOME"')
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mWELCOME')
time.sleep(2)
os.system('clear')

# GLOBAL NAME
sekarang = calendar.timegm(time.gmtime(time.time()))
pretty.install()
CON = sol()
wa = Console()
ugen = []
ugent = []
console = Console()
ses = requests.Session()
hapus  = '[/]'
lisensiku=[]
temanku = []
id, id2, loop, ok, cp, akun, tokenku, uid, method, pwpluss, pwnya, tokenmu = [], [], 0, 0, 0, [], [], [], [], [], []
dia, ualu, ualuh = [], [], []
sys.stdout.write("\x1b]2; fendi ganteng\x07")

#<----------[ WARNA ]---------->#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
mahal = random.choice([P,M,K,H,B,U])
#<----------[ BULAN ]---------->#
rb = {'1':'JANUARI','2':'FEBRUARI','3':'MARET','4':'APRIL','5':'MEI','6':'JUNI','7':'JULI','8':'AGUSTUS','9':'SEPTEMBER','10':'OKTOBER','11':'NOVEMBER','12':'DESEMBER'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
oke = 'FENN-LIVE-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cpe = 'FENN-CHECK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
#<----------[ UCAPAN MANIS ]---------->#
hour = datetime.datetime.now().hour
if 19 <= hour < 4:
  sall2 = f"SELAMAT MALAM"
elif 4 <= hour < 12:
  sall2 = f"SELAMAT PAGI"
elif 12 <= hour < 15:
  sall2 = "SELAMAT SIANG"
elif 15 <= hour < 18:
  sall2 = f"SELAMAT SORE"
elif 18 <= hour < 19:
  sall2 = f"SELAMAT MALAM"
else:
  sall2 = f"SELAMAT MALAM"  

#------[PRXY]------#
try:
    prox = requests.get(
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all"
    ).text
    open(".prox.txt", "w").write(prox)
except Exception as e:
    Console().print(
        f" {H2}•{P2} Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda"
    )
    exit()
prox = open(".prox.txt", "r").read().splitlines()

#<----------[ ANIMASI ]---------->#
def fenn(berjalan):
        for gasle in berjalan + "\n":sys.stdout.write(gasle);sys.stdout.flush();time.sleep(0.05)
def fenn(berjalan):
        for gasle in berjalan + "\n":sys.stdout.write(gasle);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	menu(id)
#------[PEMBUKAAAN]------#
def banner():
    os.system('clear')
    cetak(panel(f'''[blod yellow])
[bold yellow] ____  _   _ ____  _     _____ _____ ____  _   _ 
[blod yellow]|  _ \| \ | |  _ \| |   | ____| ____|  _ \| \ | |
[blod yellow]| | | |  \| | | | | |   |  _| |  _| | |_) |  \| |
[blod yellow]| |_| | |\  | |_| | |___| |___| |___|  _ <| |\  |
[bold yellow]|____/|_| \_|____/|_____|_____|_____|_| \_\_| \_|
[blue]AUTOR : FENDI 
[blue]VERSION : 1.0
[blue]STATUS : PREMIUM
[blue]INSTAGRAM : @fendipendol65                ''',width=68,title=f"[[green] FENDI GANTENG [/]]",padding=(0,2),style=f"bold green"))
