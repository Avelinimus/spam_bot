import smtplib
from email.mime.text import MIMEText
from random import randint
from time import sleep

to_mail = 'la52201519@gmail.com'
password = open('password.txt', 'r').read()
username = open('username.txt', 'r').read().split()
with open('username.txt') as f:
    username_count = sum(1 for _ in f)
text = [open('text_1.txt', encoding="utf8").read(),
        open('text_2.txt', encoding="utf8").read(),
        open('text_3.txt', encoding="utf8").read(),
        open('text_4.txt', encoding="utf8").read(),
        open('text_5.txt', encoding="utf8").read(),
        open('text_6.txt', encoding="utf8").read(),
        open('text_7.txt', encoding="utf8").read(),
        open('text_8.txt', encoding="utf8").read(),
        open('text_9.txt', encoding="utf8").read()]


def send_massage():
    count_cycle = int(input('Количество раз: '))
    print('-------------------------------')
    for z in range(count_cycle):
        login = username[randint(0, username_count - 1)]
        number_text = randint(0, 8)
        text_num = text[number_text]

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(login, password)
        msg = MIMEText(text_num.encode('utf-8'), _charset='utf-8')
        msg['Subject'] = str(randint(0, 9999)) + str(randint(0, 9999)) + str(666) + str(randint(0, 9999)) + str(randint(0, 9999))
        msg['To'] = to_mail
        smtpObj.sendmail(username, to_mail, msg.as_string())
        print(z+1, ')', login, '\n', number_text, '- text number')
        print('-------------------------------')
        smtpObj.close()


def main():
    while True:
        try:
            send_massage()
        except Exception:
            sleep(60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted program. Exitting...")
