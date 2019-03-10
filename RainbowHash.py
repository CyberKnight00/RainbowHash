#!/usr/bin/python3
# importing required modules
import os
import hashlib
import sqlite3
import string
import argparse
import sys
import binascii

# used argparse module for creating help menu
parser = argparse.ArgumentParser(description="RainbowHash is Great Tool for recover Hashe.It Supports Hash such as md5, sha1, sha256, sha512, and many more. It is alsocapable of genrate Rainbow Table with Wordlist file as input.")
parser.add_argument('-f', '--file', help = 'File To Create Rainbow Table', nargs = 1)
parser.add_argument('-p', '--pre', help = 'Prepend Salt Value', nargs = 1)
parser.add_argument('-a', '--app', help = 'Append Salt Value', nargs = 1)
parser.add_argument('-H', '--hash', help = 'Hash to recover', nargs = 1)
parser.add_argument('-v', '--verbose', help = 'Verbose = True', action='store_true')
parser.add_argument('-w', '--word', help = 'Generate Hashe For A single string')
parser.add_argument('-c', '--check', help = 'Ignore repeated words in Wordlist, slow but effective', action='store_true')

# created argparse object to take command line argument
arg = parser.parse_args()

# used os module for checking directory exists or not, Create rainbow_Database directory if directory not exists
if os.path.isdir('.rainbow_Database'):
    os.chdir('.rainbow_Database/')
else:
    os.mkdir('.rainbow_Database')
    os.chdir('.rainbow_Database/')

# used sqlite3 module for creating database of Hashes
sql = sqlite3.connect('Database.db')
sql.execute('create table if not exists Hashes_Table(name text, md5 hash, sha1 hash, sha224 hash, blake2s hash, blake2b hash, sha3_384 hash, sha384 hash, sha3_512 hash, sha3_224 hash, sha512 hash, sha256 hash, sha3_256 hash, ntlm hash)')
sql.commit()

# Function fetch_from_database takes one argument 'ha_sh' to recover hash


def fetch_from_database(ha_sh):
    cursor = sql.execute('select * from Hashes_Table')
    sql.commit()
    for row in cursor:
        if ha_sh == row[1]:  # Is it in md5
            print('Detected ALGORITHM (md5) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[2]:  # Is it in sha1
            print('Detected ALGORITHM (sha1) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[3]:  # Is it in sha224
            print('Detected ALGORITHM (sha224) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[4]:  # Is it in blake2s
            print('Detected ALGORITHM (blake2s) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[5]:  # Is it in blake2b
            print('Detected ALGORITHM (blake2b) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[6]:  # Is it in sha3_384
            print('Detected ALGORITHM (sha3_384) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[7]:  # Is it in sha384
            print('Detected ALGORITHM (sha384) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[8]:  # Is it in sha3_512
            print('Detected ALGORITHM (sha3_512) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[9]:  # Is it in sha3_224
            print('Detected ALGORITHM (sha3_224) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[10]:  # Is it in sha512
            print('Detected ALGORITHM (sha512) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[11]:  # Is it in sha256
            print('Detected ALGORITHM( (sha256) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[12]:  # Is it in sha3_256
            print('Detected ALGORITHM (sha3_256) : ', ha_sh, '\nword : ', row[0], )
            return
        elif ha_sh == row[13]:	#Is it in ntlm
            print('Detected ALGORITHM ntlm : ', ha_sh, '\nword : ', row[0], )
            return
    else:
        print('Hash Not Found : Check your Hash String or update Database')


def check_me(ck_word):
    cursor = sql.execute('select name from Hashes_Table')
    sql.commit()
    
    for row in cursor:
        if ck_word == row[0]:  # Is it in Database
            return True

    else : return False


def add_data(word_file, salt_value=None, post_value=None, rep = 0):
    n = 0
    # it will create rainbow table with given file
    fp = open(word_file, 'r', encoding="Latin-1")
    for word in fp:
        try:
            n += 1
            word = word.strip(string.whitespace)
            if salt_value is not None:
                word = salt_value + word # Prepend the salt value
            if post_value is not None:
                word += post_value # append the salt value
            if arg.verbose:
                print(word)

            if rep == 1:
                chk = check_me(word)
            
            if rep == 0 : 
                chk = False
            
            if chk is False:
                # this function will create hashes
                md5 = hashlib.md5(word.encode()).hexdigest()
                sha1 = hashlib.sha1(word.encode()).hexdigest()
                sha224 = hashlib.sha224(word.encode()).hexdigest()
                blake2s = hashlib.blake2s(word.encode()).hexdigest()
                blake2b = hashlib.blake2b(word.encode()).hexdigest()
                sha3_384 = hashlib.sha3_384(word.encode()).hexdigest()
                sha384 = hashlib.sha384(word.encode()).hexdigest()
                sha3_512 = hashlib.sha3_512(word.encode()).hexdigest()
                sha3_224 = hashlib.sha3_224(word.encode()).hexdigest()
                sha512 = hashlib.sha512(word.encode()).hexdigest()
                sha256 = hashlib.sha256(word.encode()).hexdigest()
                sha3_256 = hashlib.sha3_224(word.encode()).hexdigest()
                ntlm = (binascii.hexlify(hashlib.new('md4', word.encode('utf-16le')).digest())).decode()

                sql.execute('insert into Hashes_Table(name, md5 , sha1, sha224 , blake2s , blake2b , sha3_384 , sha384 , sha3_512, '
                            'sha3_224, sha512, sha256, sha3_256, ntlm ) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (word, md5, sha1,
                                                                                                      sha224, blake2s,
                                                                                                      blake2b, sha3_384,
                                                                                                      sha384, sha3_512,
                                                                                                      sha3_224, sha512,
                                                                                                      sha256, sha3_256, ntlm))

        except Exception:  
            print(Exception)
    sql.commit()
    print('WORD: ', n)  


# stored user arguments to variable
if arg.file is not None:
    file_name = ''.join(arg.file)
    
    chk = 0
    if arg.check:
        chk = 1

    if os.path.isfile(file_name):
        if arg.pre is not None:
            salt = ''.join(arg.pre)
            add_data(file_name, salt_value = salt, rep = chk)
        elif arg.app is not None:
            post = ''.join(arg.ap)
            add_data(file_name, post_value = post, rep = chk)
        else:
            add_data(file_name, rep = chk)
    else:
        print("file doesn't exist")

# stored user arguments to variable
if arg.hash is not  None:
    hash1 = arg.hash
    hash1 = ''.join(hash1)
    fetch_from_database(hash1)


def word_hash(word):
# It takes one argument word and will create hash """
    md5 = hashlib.md5(word.encode()).hexdigest()
    sha1 = hashlib.sha1(word.encode()).hexdigest()
    sha224 = hashlib.sha224(word.encode()).hexdigest()
    blake2s = hashlib.blake2s(word.encode()).hexdigest()
    blake2b = hashlib.blake2b(word.encode()).hexdigest()
    sha3_384 = hashlib.sha3_384(word.encode()).hexdigest()
    sha384 = hashlib.sha384(word.encode()).hexdigest()
    sha3_512 = hashlib.sha3_512(word.encode()).hexdigest()
    sha3_224 = hashlib.sha3_224(word.encode()).hexdigest()
    sha512 = hashlib.sha512(word.encode()).hexdigest()
    sha256 = hashlib.sha256(word.encode()).hexdigest()
    sha3_256 = hashlib.sha3_224(word.encode()).hexdigest()
    ntlm = (binascii.hexlify(hashlib.new('md4', word.encode('utf-16le')).digest())).decode()
    
    print('md5     :' , md5)
    print()
    print('sha1    :' , sha1)
    print()
    print('sha224  :', sha224)
    print()
    print('blake2s :', blake2s)
    print()
    print('blake2b :', blake2b)
    print()
    print('sha3_384:', sha3_384)
    print()
    print('sha384  :', sha384)
    print()
    print('sha3_512:', sha3_512)
    print()
    print('sha3_224:', sha3_224)
    print()
    print('sha512  :', sha512)
    print()
    print('sha256  :', sha256)
    print()
    print('sha3_256:', sha3_256)
    print()
    print('ntlm    :', ntlm)
    print()

    # check if word alrady exists into database
    chk = check_me(word)
    
    if chk is False :
        # Store all hashes into database
        choice = input ("Enter y to store word in database : ")
        if choice == 'y':
            sql.execute('insert into Hashes_Table(name, md5 , sha1, sha224 , blake2s , blake2b , sha3_384 , sha384 , sha3_512, sha3_224, sha512, sha256, sha3_256, ntlm) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', ( word, md5, sha1, sha224, blake2s, blake2b, sha3_384, sha384, sha3_512, sha3_224, sha512, sha256, sha3_256, ntlm))
            sql.commit()
            print ("word : "+word)
        return

# will check word and strip word
if arg.word is not None:
    word = arg.word.strip()
    word = ''.join(word)
    word_hash(word)

# create lambda function for clear screen
clear = lambda: os.system('clear')  

# will check command line arguments if arguments are lessthan 2 then it will give user a CLI
if len(sys.argv) < 2:
    post = None
    salt = None
    file = None
    hash_opt = None
    print("RainbowHash is a Great Tool For Cracking Hashes one at a time.\nIt Supports Hash such as md5, sha1, sha223, sha3_384, sha384, sha3_224, sha512, sha256, sha3_256, blake2s, blake2b, ntlm \n")

    # wile loop condition always true
    while True:
        inp = input('Rhash > ')  
        inp = inp.strip(string.whitespace) 

        if (inp == 'help') or (inp == '?'):
            print('     help :    Show all Command')
            print('     file :    Add Wordlist To Create Rainbow Table')
            print('     hash :    Recover Hash')
            print('     exit :    Exit CLI')
            print('     clear:    Clear the Screen')
            print('     word :    Single word to genrate Rainbow Table')
            print('     Example : File /root/RainbowHash/pass')
            
            continue
        elif 'clear' == inp:
            clear()
            continue
        elif inp == 'exit':
            exit()
        elif inp == 'file':
            print('     file :  Add Wordlist To Create Rainbow Table')
            continue
        elif inp == 'hash':
            print('     Example : hash Hash_String')
            continue
        elif inp == 'word':
            print('     example : word RainbowMe')
            continue

        if inp is not '':
            inp = inp.split()

            if inp[0] == 'file':
                file = inp[1]

                # another while loop is true because of file option
                while True:
                    inp1 = input('Rhash > file > ')
                    inp1 = inp1.strip(string.whitespace)

                    if inp1 == 'show option':
                        print('     OPTION       VALUE')
                        print('     file        ', file)
                        print('     prepend     ', salt)
                        print('     append      ', post)
                        continue
                    elif inp1 == 'run':

                        # chk = 1 to avoide dublicity
                        chk = 1

                        if os.path.isfile(file):

                            if post is not None:
                                add_data(file, post_value=post, rep = chk)
                                continue
                            if salt is not None:
                                add_data(file, salt_value=salt, rep = chk)
                                continue
                            else:
                                add_data(file, rep = chk)
                                continue
                        else:
                            print(file, 'is not file')
                            continue

                    # help options of CLI
                    elif inp1 == 'help' or inp1 == '?':
                        print('     help  :  Show This Help Message And Exit')
                        print('     file  :  Add Wordlist To Create Rainbow Table')
                        print('     pre   :  Prepend Salt Value To Rainbow Table')
                        print('     app:  Append Salt Value To Rainbow Table')
                        print('     back  :  Back To Initial')
                        print('     run   :  Execute')
                        print('     clear :  Clear The Screen')
                        continue
                    elif inp1 == 'back':  # break this loop
                        break
                    elif inp1 == 'clear':  # clear screen
                        clear()
                        continue
                    elif inp1 == 'app':
                        print('     example : Append Hash Value')
                        continue
                    elif inp1 == 'pre':
                        print('     example : salt hash value')
                        continue
                    
                    if inp1 is not '':
                        inp1 = inp1.split()
                        if inp1[0] == 'app':
                            post = inp1[1]
                        elif inp1[0] == 'pre':
                            salt = inp1[1]
                        else:
                            print('Unknown Command')
                    elif inp1 is '':
                        continue
                    else:
                        print('Unknown Command')

            elif inp[0] == 'hash':
                fetch_from_database(inp[1])
                continue
            elif inp[0] == 'word':
                word_hash(inp[1])
                continue
            else:
                print('Unknown Command')

        elif inp == '':
            continue
        else:
            print('Unknown Command')
