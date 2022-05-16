'''
Secure programming -course project: Password recovery tool
16.5.2022
'''

import hashlib
from time import sleep

'''MD5 password recovery'''
def md5_rec(wordlist, pass_hash):
    print('MD5')
    flag = 0
    try:
        pass_file = open(wordlist,'r')
    except:
        print('No file found')
        quit()

    '''Hashing and comparing. If there is matching hash gives word to printing 
        function flag = 1 and breaks loop'''
    for word in pass_file:
        enc_word = word.encode('utf-8')
        digest = hashlib.md5(enc_word.strip()).hexdigest()
        if digest == pass_hash:
            pass_print(word)
            flag = 1
            break
    if flag == 0:
        print('Password not in the password list')

'''SHA-256 password recovery'''
def sha256_rec(wordlist, pass_hash):
    print('SHA-256')
    flag = 0
    try:
        pass_file = open(wordlist,'r')
    except:
        print('No file found')
        quit()

    '''Hashing and comparing. If there is matching hash gives word to printing 
        function flag = 1 and breaks loop'''
    for word in pass_file:
        enc_word = word.encode('utf-8')
        digest = hashlib.sha256(enc_word.strip()).hexdigest()
        if digest == pass_hash:
            pass_print(word)
            flag = 1
            break
    if flag == 0:
        print('Password not in the password list')

'''SHA-512 password recovery'''
def sha512_rec(wordlist, pass_hash):
    print('SHA-512')
    flag = 0
    try:
        pass_file = open(wordlist,'r')
    except:
        print('No file found')
        quit()

    '''Hashing and comparing. If there is matching hash gives word to printing 
        function flag = 1 and breaks loop'''
    for word in pass_file:
        enc_word = word.encode('utf-8')
        digest = hashlib.sha512(enc_word.strip()).hexdigest()
        if digest == pass_hash:
            pass_print(word)
            flag = 1
            break
    if flag == 0:
        print('Password not in the password list')

'''Printing function'''
def pass_print(word):
    print('------------------------------')
    print('Password found')
    sleep(1)
    print('.')
    sleep(1)
    print('..')
    sleep(1)
    print('...')
    sleep(1)
    print(f'Password is {word}')
    print('------------------------------')


'''
------------------------------------------------------
START HERE!
'''
pass_hash = input('Enter hash: ')
hash_type = len(pass_hash)
wordlist = input('File name or just Enter: ')

'''
Default password list to test if program works although you can use any 
list like "passlist".
'''
if wordlist == "":
    wordlist = 'passlist'

'''Checking length of hash to identify hash type'''
if hash_type == 32:
    md5_rec(wordlist, pass_hash)
if hash_type == 64:
    sha256_rec(wordlist, pass_hash)
if hash_type == 128:
    sha512_rec(wordlist, pass_hash)