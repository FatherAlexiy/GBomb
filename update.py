import requests, sys
from termcolor import colored
def check_update(version):
    updat=requests.get('https://raw.githubusercontent.com/FatherAlexiy/GBomb/master/version.data')
    updat_vers = float(updat.text)
    if updat_vers > float(version):
        print(colored("\nНайдено обновление\nНачато обновление, пожалуйста подождите!", "cyan"))
        up_boom = requests.get('https://raw.githubusercontent.com/FatherAlexiy/GBomb/master/bomber.py')
        f = open("bomber.py", "wb")
        f.write(up_boom.content)
        f.close()
        print(colored("\nОбновление завершено, откройте бомбер заново командой", "cyan"), colored("'python bomber.py'", "magenta"))
        sys.exit()
    elif updat_vers == float(version):
    	print(colored("\nУстановлена последняя версия, спасибо!", "cyan"))
    else:
    	print(colored("Ошибка, файл обновлений не найден\nПопробуйте заново или проверьте подключение к интернету.", "red"))
