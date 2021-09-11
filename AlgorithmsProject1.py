
"""

Software solution for implementing RSA encryption and digital signature system
in Python.

Sedric, Khris, and Elijah.

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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~Sedric O'Donohue Start~~~~~~~~~~~~
def multpInverse(a, m):
    
   g, x, y = gcd(a,m)
   if g != 1:
       raise Exception('modular inverse does not exist')
   else:
       return x % m
 
 
def generate_keys(p = 7,q = 17):
    n = p * q
    
    fn = ((p-1) * (q-1))
    
    e = random.randrange(1, fn) 
    
    while gcd(e, fn) != 1: 
        e = random.randrange(1, fn)
       
    d = multpInverse(e, fn)
    
    pubk = open("public.key", "w+")
    pubk.write("%d\n" % e)
    pubk.write("%d\n" % n)
    pubk.close();
    pk = open("private.key", "w+")
    pk.write("%d\n" % d)
    pk.close();
    
    return (e, n, d)

def mainChoices():
    print("\n----Main Menu----")
    print("1) Encrypt or Decrypt a message.")
    print("2) Sign or verify a digital signature.")
    print("3) To exit the program")
    choice = input("Please enter 1, 2, or 3 to continue: ").upper()
    
    while choice != "1" and choice != "2" and choice != "3":
        choice = input("Please enter 1, 2, or 3 to continue: ").upper()
    return choice
    
def encryptChoices():
    print("\n---Encrypt a Message Choices---")
    print("4) Encrypt a message.")
    print("5) Decrypt a message.")
    print("6) Back to Main Menu.")
    choice = input("Pleaser enter 4, 5 or 6 to continue: ").upper()
    
    while choice != "4" and choice != "5" and choice != "6":
        choice = input("Please enter 4, 5 or 6 to continue: ").upper()
    
    return choice

def signChoices():
    print("\n---Document Signing Choices---")
    print("4) Sign a document.")
    print("5) Verify a signature.")
    print("6) Back to Main Menu.")
    choice = input("Pleaser enter 4, 5 or 6 to continue: ").upper()
    
    while choice != "4" and choice != "5" and choice != "6":
        choice = input("Please enter 4, 5 or 6 to continue: ").upper()
    
    return choice

def signDocument(d, n, e):
    print("\n---Sign a document")
    s = input("Enter your signature: ")
    sd = encrypt(d, n, s)
    
    print("Encypted Signature: ", ''.join(map(lambda x: str(x), sd)))
    
    with open('signature.crypt', 'w') as filehandle:
        filehandle.writelines("%d\n" % char for char in sd)
    
    print("\n\nFollow the menu choices to decrypt the signature. Returning to main menu.")
   
    
def verifySignature(e, n):
    if path.isfile("signature.crypt"):
        print("\n---Verify a signature")
        
        sd = []
        with open('signature.crypt', 'r') as filehandle:
            sd = [int(char.rstrip()) for char in filehandle.readlines()]
        os.remove("signature.crypt")
        
        sig = decrypt(e, n, sd)
        print("Decrypted Signature is: %s\n" % ''.join(sig))
    else:
        print("Sign a document first. Returning to main menu.")
        
def encryptMessage(e, n, d):
    print("\n---Encrypt a message---")
    m = input("Enter message to be encrypted: ")
    cm = encrypt(e, n, m)
    
    print("Encrypted Message is: ", ''.join(map(lambda x: str(x), cm)))
   
    
    with open('message.crypt', 'w') as filehandle:
        filehandle.writelines("%d\n" % char for char in cm)
    
    print("\n\nFollow the menu choices to decrypt the message. Returning to main menu.")
 
    
def decryptMessage(d, n):
    if path.isfile("message.crypt"):
        print("\n---Decrypt a message---")
        
        cm = []
        with open('message.crypt', 'r') as filehandle:
            cm = [int(char.rstrip()) for char in filehandle.readlines()]
        os.remove("message.crypt")
        
        message = decrypt(d, n, cm)
        print("Decrypted message: %s\n" % ''.join(message))
        
    else:
        print("Encrypt a message first. Returnig to main menu.")
        

def RSAmenu(e, n, d):
    choice = mainChoices()
    
    while choice != "3":
        
        if choice == "1":
            choice = encryptChoices()
            
            if choice == "4":
                encryptMessage(e, n, d)
            elif choice == "5":
                decryptMessage(d, n)  
        elif choice == "2":
            choice = signChoices()
            
            if choice == "4":
                signDocument(d, n, e)
            elif choice == "5":
                verifySignature(e, n)
        elif choice == "6":
            choice = mainChoices() 
         
        choice = mainChoices()  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Finish~~~~~~~~~~~~~~~            
