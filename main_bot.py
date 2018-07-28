# coding: utf8
import smtplib
from email.mime.text import MIMEText
from random import randint
from time import sleep

text = """
Здравстуйте, мы - команда веб-разработчиков "Chamber 47".
Мы готовы сделать сайт, который понравится Вам и Вашим пользователям.
Результат (будь то интернет-магазин, сайт-визитка и т.д.) полностью удовлетворит ваши запросы и будет достойным конкурентом в своей сфере.

Что входит в разработку:

- Полный функционал
- Уникальный адаптивный дизайн
- Оптимизация
- Заполнение контентом

Что вы получите в итоге:
- Быстро работающий сайт с привлекательным дизайном.
- Домен и хостинг
- Поддержка в течении месяца

Как с нами связаться:

Номера телефонов:

+ 38(094)-131-10-62
+ 38(098)-607-44-30

Telegram/Viber: 380662004294

E-mail: developerspython385@gmail.com

(Не стесняйтесь писать и звонить, мы всегда рады вам ответить)

За дополнительной информацией отправляйтесь на наш сайт - Chamber47.com

Надеемся на долгосрочное сотрудничество!' 

http://chamber47.com
"""

mail = open('mail.txt', 'r').readlines()
login = open('login.txt', 'r').read().split()
username = login[0]
password = login[1]


def start_server():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(username, password)
    return smtpObj


def send_mails(smtpObj):
    for email in mail:
        print(email)
        msg = MIMEText(text.encode('utf-8'), _charset='utf-8')
        msg['Subject'] = "Мы делаем дешевые качественые сайты. Chamber47"
        msg['From'] = username
        msg['To'] = email
        if email == 'Exit':
            smtpObj.quit()
            exit()
        else:
            smtpObj.sendmail(username, email, msg.as_string())


def main():
    while True:
        smtpObj = start_server()
        try:
            send_mails(smtpObj)
        except Exception:
            sleep(60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted program. Exitting...")