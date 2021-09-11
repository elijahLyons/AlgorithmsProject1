# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:01:22 2021

@author: Elijah
"""

import os.path
from os import path
import random


def encrypt(e, n, message):
    cryptmessage = [fastExpo(ord(char), e, n) for char in message]
    return cryptmessage

def decrypt(d, n, cmessage):
    message = [chr(fastExpo(char, d, n)) for char in cmessage]
    return ''.join(message)

def gcd(a = 1, b = 1):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def generate_prime_num():
    p = random.randint(100000, 10000001)
    while not prime_check(p, 100):
        p = random.randint(100000, 10000001)
    return p

def prime_check(n, s):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(s):
        a = random.randint(2, n - 1)
        if fastExpo(a, n - 1, n) != 1:
            return False
        return True
    
def fastExpo(a, p, n):
    t = 1
    while p > 0:
        if p % 2 == 0:
            a = (a * a) % n
            p = p/2
        else:
            t = (a * t) % n
            p = p - 1
    return t
