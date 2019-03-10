# RainbowHash 
	RainbowHash is a Great Tool For Cracking or Recovering Hashed password.
	RainbowHash Supports multiple Hash Such as md5, sha1, sha223, sha3_384, blake2s, blake2b, sha384, sha3_224, sha512, sha256, sha3_256, ntlm.
	It Generates Rainbow Table and build a Sqlite3 Database in Current Directory and Match Hash With Rainbow Table Hashes.
	RainbowHash also Supports Prepend and Append Salt Value.
	RainbowHash can be used as Intractive Mode awa Single Lineer command
	RainbowHash directly recover Matched Hash from Rainbow Table Database whis is created inside Local Directory (easy to share)

	No need to Specify Hash Alogorithem type.
	No need to Make Rainbow table of same word or file anymore.

# Usage
# Intractive Mode Usage

	root@CK00:~/RainbowHash# python3.7 RainbowHash.py

	RainbowHash is a Great Tool For Cracking Hashes one at a time.
	It Supports Hash such as md5, sha1, sha223, sha3_384, sha384, sha3_224, sha512, sha256, sha3_256, blake2s, blake2b, ntlm 

	Rhash > help
	     help :    Show all Command
	     file :    Add Wordlist To Create Rainbow Table
	     hash :    Recover Hash
	     exit :    Exit CLI
	     clear:    Clear the Screen
	     word :    Single word to genrate Rainbow Table
	     Example : File /root/RainbowHash/pass

# To Creating rainbow table

	Rhash > file /root/RainbowHash/pass
	Rhash > file > run
	WORD:  10

# To Append Salt Value into ranbow table

	Rhash > file /mnt/SPORTS/VM/SF/Python-Kali/Projects/RH/pass00
	Rhash > file > app 123
	Rhash > file > run

# To Prepend Salt Value into ranbow table

	Rhash > file /mnt/SPORTS/VM/SF/Python-Kali/Projects/RH/pass00
	Rhash > file > pre 123
	Rhash > file > run

# To For Generating Hash Of A Particular Word
	Rhash > word RainbowMe

	md5     : f9defaa0ffd24ac8258f6abcf91ad8d9

	sha1    : ce0914d991231c490dd03e8cb076d719b7f221ac

	sha224  : eec37c3546ec44d7a0be451a5eae83b1f3418955e46765c9fc7f6f15

	blake2s : ac681534e4bf88895b3e35dfc18d4dc60f69b27ce4318061edbc76c76bcc428b

	blake2b : 3098dd77c584ca8a1c01490d6809c675e148d7001eff96db1410209bcba6edf5ba9246bd74344cf674c8f65345de5fdc98d21dcfce183c088f60aab62fb0d2a3

	sha3_384: 048d58fa0e49bd064e69751f02b29ffc3285bac5b8314b51cdffa98d99d074c23b27e75dfcbc774c2067c1af3d5d4695

	sha384  : 650b4e6b89a905b5bba2120c2046a114f2cb1723e75a655945f70969ce1ec8af75acbb417fcd63f0a048253dbd632e87

	sha3_512: a5b39419766ae05f3324213563b94d690af70a54c552d209ffda98a5e536769eaa51dbd6b36afb6831f67c6e71705a7601372cde7b1989cee177e252097a1fdc

	sha3_224: cf1cf714f3135708d25c4ec1e2ad50f5bf7f7cf7b367a096324a1017

	sha512  : 97a88c9afdf1333834678ed1ac755cec59011c1ffedfbb9d14ef42c5dd600ca2f16d949dc40629c5e02de877b9b21934476e8aab7e1699fabe68e6dc308fea2c

	sha256  : 11e1663b18e3a2868c5fc9392bd4a85845f41770aae6f5be03f8a4869e74a248

	sha3_256: cf1cf714f3135708d25c4ec1e2ad50f5bf7f7cf7b367a096324a1017

	ntlm	: 45044796f86c466f9309e683ede88f4c

	Enter y to store word in database : y
	word : RainbowMe

# To Cracking Hash

	Rhash > hash f9defaa0ffd24ac8258f6abcf91ad8d9
	Detected ALGORITHM (md5) :  f9defaa0ffd24ac8258f6abcf91ad8d9 
	word :  RainbowMe

# Command line / Non-Intractive Mode

# To Show Help options

	root@CK00:~/RainbowHash# python3.7 RainbowHash.py -h
	 
	usage: RainbowHash.py [-h] [-f FILE] [-p PRE] [-a APP] [-H HASH] [-v]
	                      [-w WORD]

	RainbowHash is Great Tool for recover Hashe.It Supports Hash such as md5,
	sha1, sha256, sha512, and many more. It is alsocapable of genrate Rainbow
	Table with Wordlist file as input.

	optional arguments:
	  -h, --help            show this help message and exit
	  -f FILE, --file FILE  File To Create Rainbow Table
	  -p PRE, --pre PRE     Prepend Salt Value
	  -a APP, --app APP     Append Salt Value
	  -H HASH, --hash HASH  Hash to recover
	  -v, --verbose         Verbose = True
	  -w WORD, --word WORD  Generate Hashe For A single string
	  -c, --check           Ignore repeated words in Wordlist, slow but effective


# To Creating rainbow table without repetation

	root@CK00:~/RainbowHash# python3.7 RainbowHash.py -v -f /root/RainbowHash/pass -c

# To Append Salt Value into ranbow table

	root@CK00:~/RainbowHash# python3.7 RainbowHash.py -a salt_value -v -f /root/RainbowHash/pass

# To Prepend Salt Value into ranbow table

	root@CK00:~/RainbowHash# python3.7 RainbowHash.py -p salt_value -v -f /root/RainbowHash/pass

# To For Generating Hash Of A Particular Word

	root@CK00:~/RainbowHash# python3.7 RainbowHash.py -w RainbowMe

	md5     : f9defaa0ffd24ac8258f6abcf91ad8d9

	sha1    : ce0914d991231c490dd03e8cb076d719b7f221ac

	sha224  : eec37c3546ec44d7a0be451a5eae83b1f3418955e46765c9fc7f6f15

	blake2s : ac681534e4bf88895b3e35dfc18d4dc60f69b27ce4318061edbc76c76bcc428b

	blake2b : 3098dd77c584ca8a1c01490d6809c675e148d7001eff96db1410209bcba6edf5ba9246bd74344cf674c8f65345de5fdc98d21dcfce183c088f60aab62fb0d2a3

	sha3_384: 048d58fa0e49bd064e69751f02b29ffc3285bac5b8314b51cdffa98d99d074c23b27e75dfcbc774c2067c1af3d5d4695

	sha384  : 650b4e6b89a905b5bba2120c2046a114f2cb1723e75a655945f70969ce1ec8af75acbb417fcd63f0a048253dbd632e87

	sha3_512: a5b39419766ae05f3324213563b94d690af70a54c552d209ffda98a5e536769eaa51dbd6b36afb6831f67c6e71705a7601372cde7b1989cee177e252097a1fdc

	sha3_224: cf1cf714f3135708d25c4ec1e2ad50f5bf7f7cf7b367a096324a1017

	sha512  : 97a88c9afdf1333834678ed1ac755cec59011c1ffedfbb9d14ef42c5dd600ca2f16d949dc40629c5e02de877b9b21934476e8aab7e1699fabe68e6dc308fea2c

	sha256  : 11e1663b18e3a2868c5fc9392bd4a85845f41770aae6f5be03f8a4869e74a248

	sha3_256: cf1cf714f3135708d25c4ec1e2ad50f5bf7f7cf7b367a096324a1017
	
	ntlm	: 45044796f86c466f9309e683ede88f4c

	Enter y to store word in database : y
	word : RainbowMe


# To Cracking Hash 

	root@CK00:~/RainbowHash# python3.7 RainbowHash.py -H f9defaa0ffd24ac8258f6abcf91ad8d9 

    Detected ALGORITHM (md5) :  f9defaa0ffd24ac8258f6abcf91ad8d9 
	word :  RainbowMe
