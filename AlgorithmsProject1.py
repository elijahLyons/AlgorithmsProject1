
"""

Software solution for implementing RSA encryption and digital signature system
in Python.

Sedric, Khris, and Elijah.

"""

#~~~~~~~~~~~~~~~~~~~~~~~~~Khristion Pace Start~~~~~~~~~~~~~~~
import os.path
from os import path
import random

# Encrypting algorithm
def encrypt(e, n, message):
    cryptmessage = [fastExp(ord(char), e, n) for char in message]
    return cryptmessage

# Decrypting algorithm
def decrypt(d, n, cmessage):
    message = [chr(fastExp(char, d, n)) for char in cmessage]
    return ''.join(message)

# GCD 
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Generating prime numbers between 100,000 and 1,000,000
def generatePrimeNumber():
    p = random.randint(100000, 10000001)
    while not checkPrime(p, 100):
        p = random.randint(100000, 10000001)
    return p

# Using Fermats Theory (little) to see if the number is prime
def checkPrime(n, s):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(s):
        a = random.randint(2, n - 1)
        if fastExp(a, n - 1, n) != 1:
            return False
        return True
    
def fastExp(a, p, n):
    t = 1
    while p > 0:
        if p % 2 == 0:
            a = (a * a) % n
            p = p/2
        else:
            t = (a * t) % n
            p = p - 1
    return t
#~~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~Sedric O'Donohue Start~~~~~~~~~~~~

#code found at https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#code found at https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def multiplicativeInverse(a, m):
    
   g, x, y = egcd(a,m)
   if g != 1:
       raise Exception('modular inverse does not exist')
   else:
       return x % m
 
 
def generateKeys(p, q):
    
    fn = ((p-1) * (q-1))
    
    e = random.randrange(1, fn) 
    
    while gcd(e, fn) != 1: 
        e = random.randrange(1, fn)
       
    d = multiplicativeInverse(e, fn)
    
    return (e, d)

def mainChoices():
    print("\n----Menu----")
    print("1) Encrypt or Decrypt a message.")
    print("2) Sign or verify a digital signature.")
    print("3) Exit program.")
    choice = input("Enter 1, 2, or 3: ").upper()
    
    while choice != "1" and choice != "2" and choice != "3":
        choice = input("Please enter 1, 2, or 3 to continue: ").upper()
    return choice
    
def encryptChoices():
    print("\n---Encrypt a Message Choices---")
    print("4) Encrypt a message.")
    print("5) Decrypt a message.")
    print("6) Back.")
    choice = input("Enter 4, 5 or 6: ").upper()
    
    while choice != "4" and choice != "5" and choice != "6":
        choice = input("Enter 4, 5 or 6 to continue: ").upper()
    
    return choice

def signChoices():
    print("\n---Digital Signature Choices---")
    print("4) Create digital signature.")
    print("5) Verify a signature.")
    print("6) Back to Main Menu.")
    choice = input("Enter 4, 5 or 6: ").upper()
    
    while choice != "4" and choice != "5" and choice != "6":
        choice = input("Enter 4, 5 or 6 to continue: ").upper()
    
    return choice

def createSignature(d, n, e):
    print("\n---Create a signature")
    s = input("Enter your signature: ")
    signature = encrypt(d, n, s)
    
    print("\nEncypted Signature: ", ''.join(map(lambda x: str(x), signature)))
    
    print("Your signature has been encrypted. Navigate to 'verify' to verify the signature.")
    return signature
   
    
def verifySignature(e, n, signature):
        print("\n---Verify a signature")
        
        if signature != 0:
            dsig = decrypt(e, n, signature)
            print("Decrypted Signature is: %s\n" % ''.join(dsig))
        else:
            print("\nNO DIGITAL SIGNATURES FOUND.")
        
def encryptMessage(e, n, d):
    print("\n---Encrypt a message---")
    m = input("Enter message: ")
    cmessage = encrypt(e, n, m)
    
    print("\nEncrypted Message is: ", ''.join(map(lambda x: str(x), cmessage)))
   
    
    print("Your message has been encrypted. Navigate to 'decrypt' to decrypt your message.")
    return cmessage
 
    
def decryptMessage(d, n, cmessage):

        if cmessage != 0:
            dmessage = decrypt(d, n, cmessage)
            print("Decrypted message: %s\n" % ''.join(dmessage))
        else:
            print("\nNO ENCRYPTED MESSAGES FOUND")
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Finish~~~~~~~~~~~~~~~ 
        
#~~~~~~~~~~~~~~~~~~~Elijah Lyons start~~~~~~~~~~~~~
def RSAdashboard(e, n, d):
    cmessage = 0
    signature = 0
    
    choice = mainChoices()
    
    while choice != "3":
        
        if choice == "1":
            choice = encryptChoices()
            
            if choice == "4":
                if cmessage == 0:
                    cmessage = encryptMessage(e, n, d)
                else:
                    print("\nDECRYPT YOUR MESSAGE BEFORE ENCRYPTING ANOTHER ONE")
            elif choice == "5":
                decryptMessage(d, n, cmessage) 
                cmessage = 0
        elif choice == "2":
            choice = signChoices()
            
            if choice == "4":
                if signature == 0:
                    signature = createSignature(d, n, e)
                else:
                    print("\nVERIFY YOUR SIGNATURE BEFORE CREATING ANOTHER ONE")
            elif choice == "5":
                verifySignature(e, n, signature)
                signature = 0
        elif choice == "6":
            choice = mainChoices() 
         
        choice = mainChoices()  
           


def driver():
    
    print("\n-------------------------------------------------")
    print("This program implements RSA encryption/decryption of text based messages,\nas well as signature creation and authentication.")
    print("-------------------------------------------------\n")
    
    #generate large prime numbers
    p = generatePrimeNumber()
    q = generatePrimeNumber()
    #calculate n
    n = p * q
    #generate public and private keys
    (e, d) = generateKeys(p, q)
    #RSAdashboard function responsible for front end of implementation.
    RSAdashboard(e, n, d)
    
    
    

driver()
    






