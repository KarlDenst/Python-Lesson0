mail_attributes = ['.com', '.ru', '.net']


def is_contains(string):
    if '@' in string:
        for i in mail_attributes:
            if i in string:
                return True
    else:
        return False


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if is_contains(recipient) and is_contains(sender) is True:
        if sender =='university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        elif sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')






send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

