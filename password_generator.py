#!/usr/bin/python
import random
import string
import re


def password_wifi(length):

    # string.ascii_letters+string.punctuation+string.digits
    password_wifi = "".join(random.choice(string.ascii_letters + string.punctuation + string.digits) for i in range(length))
    return password_wifi


def password_vpn(length):

    # string.ascii_letters+string.punctuation+string.digits
    password_vpn = "".join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    if (re.search(r"(\d)", password_vpn)) and (re.search(r"[A-Z]", password_vpn)) and (re.search(r"[a-z]", password_vpn)):
        return password_vpn


def password_pin(length):

    # string.ascii_letters+string.punctuation+string.digits
    password_pin = "".join(random.choice(string.digits) for i in range(length))
    return password_pin


print "---------PASSWORD-WIFI---------"
for i in range(6):
    print password_wifi(16)


print "----------PASSWORD-VPN--------"
for i in range(6):
    print password_vpn(8)

print "-----------PASSWORD-PIN---------"
for i in range(6):
    print password_pin(8)
