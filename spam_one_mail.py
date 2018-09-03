# coding: utf8
import smtplib
from email.mime.text import MIMEText
from random import randint
from time import sleep

to_mail = 'testuserfordev228@gmail.com'
password = open('password.txt', 'r').read()
username = open('username.txt', 'r').read().split()
with open('username.txt') as f:
    username_count = sum(1 for _ in f)

text = [open('text_1.txt').read(),
        open('text_2.txt').read(),
        open('text_3.txt').read(),
        open('text_4.txt').read()]


def send_massage():
    count_cycle = int(input('Количество раз: '))
    for z in range(count_cycle):
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(username[randint(0, username_count - 1)], password)
        msg = MIMEText(text[randint(0, 3)].encode('utf-8'), _charset='utf-8')
        msg['Subject'] = str(randint(0, 9999))
        msg['From'] = username[randint(0, username_count-1)]
        msg['To'] = to_mail
        smtpObj.sendmail(username, to_mail, msg.as_string())
        print(z+1, '- Хуйня')
        smtpObj.close()

def main():
    while True:
        try:
            send_massage()
        except Exception:
            sleep(200)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted program. Exitting...")