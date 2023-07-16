import random
import string


def random_email():
    email = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    email += '@' + ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    email += '.' + random.choice(['com', 'net', 'org'])
    return email


def random_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return password


def random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

