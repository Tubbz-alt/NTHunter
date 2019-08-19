# -*- coding: utf-8 -*-
# Author : ch1ngiz

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import sys
if len(sys.argv) <2:
        print bcolors.WARNING + bcolors.BOLD + "\nUsage: " + sys.argv[0] + " <ntds file location>\n"
        print "Example: python NTHunter.py /root/hashes\n" + bcolors.ENDC
        sys.exit()


def GetHashes():
	lc = sys.argv[1]
	f = open(lc,'r')
	hashes = f.readlines()

	global name
	global ntlm
	global surname
	global FullName
	global domainname
	
	domainname = []
	name = []
	ntlm = []
	FullName = []
	surname = []

	for h in hashes:
		
		hash = h.replace('\n','')

		F = hash.split(":")[0]
		FullName.append(F)

		nl = hash.split(":")[3]
		ntlm.append(nl)

		if "\\" in F:

	                hash2 = hash.split(":")[0].split("\\")[0].split(".")
                
			if len(hash2) > 2:
                        	dn = hash2[1]
				domainname.append(dn)
			else:
				dn = hash2[0]
				domainname.append(dn)

			n = F.split("\\")[1]

			if "." in n:
				n1 = n.split(".")[0]

        	                name.append(n1)

                	        s = n.split(".")[1]
                        	surname.append(s)
			else:
				name.append(n)

		else:
			print bcolors.FAIL + "[+] Incorrect syntax in ntds file! [+]" + bcolors.ENDC
			import os
			os._exit(0)

	return name
	return surname
	return ntlm
	return domainname
	return FullName

def Mix(nam):
	global mixNumber
	mixNumber = []

	for num in range(0,1000):
		mixNumber.append(str(num))

	for year in range(1900,2019):
		mixNumber.append(str(year))
	
	global characters
	characters = []
	for chars in('!','@','*'):
		characters.append(str(chars))

	global mixname
	mixname = []

	if 'i' in nam:
		mixed = nam.replace('i','1')
		mixname.append(mixed)

	if 'a' in nam:
		mixed = nam.replace('a','4')
		mixname.append(mixed)
		mixed = nam.replace('a','@')
		mixname.append(mixed)

	if 'o' in nam:
		mixed = nam.replace('o','0')
		mixname.append(mixed)
	
	if 'e' in nam:
		mixed = nam.replace('e','3')
		mixname.append(mixed)

	if 'A' in nam:
                mixed = nam.replace('A','4')
                mixname.append(mixed)

        if 'O' in nam:
                mixed = nam.replace('O','0')
                mixname.append(mixed)

        if 'E' in nam:
                mixed = nam.replace('E','3')
                mixname.append(mixed)

	global extension
	extension = []
	for i in ('0','00','000','0000','00000','000000'):
	        for x in range(0,10):
        	        p = i + str(x)
			extension.append(p)

	global commonExtensions
	commonExtensions = []
	for i in ('123','1234','12345','123456'):
		commonExtensions.append(i)

	return commonExtensions
	return extension
	return mixNumber
	return mixname
	return characters

def InvidualWordlist(*args,**kwargs):

	global list
	list = []
	
	if len(args) < 2:
		for i in mixNumber:
			
			list.append(dummy.title() + str(i))
			for c in characters:

				list.append(dummy.title() + str(c)) # for example, username + character
				list.append(dummy.title() + str(c) + str(c)) # username + character * 2

				list.append(str(c) + dummy + str(i)) # character + username + number
				list.append(dummy.title() + str(i) + str(c)) # username (with capital letter) + number + character

				list.append(dummy + str(i) + str(c)) # username + number + character

				for e in extension: # like 01, 001, 0001 etc.

				        list.append(dummy.title() + str(e) + str(c)) # username + 001 (or 0001 , 00001 etc.) + character
					list.append(dummy + str(e) + str(c)) # username (without capital letter) + 001 (or 0001 , 00001 etc.) + character


		for e in extension:
			list.append(dummy.title() + str(e)) # username + 001 (or 0001, 00001 etc.) 

		for s in mixname: # change i with 1 or a with 4 etc.

			list.append(s.title())
			for i in mixNumber:
	                	list.append(s + str(i))

	                for c in characters:
	                        list.append(s + str(c))
	                        list.append(str(c) + s)
	
		for ce in commonExtensions:
			list.append(dummy.title() + str(ce))
			list.append(dummy + str(ce) + '!')
			list.append(dummy.title() + str(ce) + '!')

	else:
		for ce in commonExtensions:
			list.append(dummy[:1].title() + sname[:1].title() + str(ce))
			list.append(dummy[:1].title() + sname[:1].title() + str(ce) + '!')

			list.append(dummy[:1].title() + sname[:1] + str(ce))
			list.append(dummy[:1].title() + sname[:1] + str(ce) + '!')

	return list
	
def main():

	print bcolors.HEADER + "\n[+] Getting Hashes... [+]\n" + bcolors.ENDC
	GetHashes()
	leng = len(name)

	print bcolors.WARNING +  "[+] ----------------------------------------------------- [+]\n" + bcolors.ENDC
        print bcolors.OKGREEN + "[+] Trying to crack the passwords by creating invidual wordlists for the related users... [+]\n" + bcolors.ENDC
	print bcolors.OKGREEN + "[+] Cracking in progress, please wait... [+]\n" + bcolors.ENDC
	c = 0 # for count of cracked passwords
	for d in range(leng):
			username = []
			username.append(name[int(d)-1])
			lastname = []

			if len(surname) != 0:
				lastname.append(surname[int(d)-1])

			ntl = ntlm[int(d)-1]
			dname = domainname[int(d)-1]

			plist = []
			global dummy
			global sname
			if len(lastname) > 0:
				for dummy in (username,lastname,dname):
					dummy = ''.join(dummy)
					Mix(dummy) # it returns some mixed extensions
					InvidualWordlist(dummy) # it returns final list with mixed extensions
		
					plist += list 

			
				for dummy in username:
					for sname in lastname:
						InvidualWordlist(dummy,sname)
						plist += list

			else:
				for dummy in (username,dname):
                                        Mix(dummy) # it returns some mixed extensions
                                        InvidualWordlist(dummy) # it returns final list with mixed extensions
                
                                        plist += list 
			
			nt = []
			for p in plist:

				import hashlib,binascii
		     
		        	hs = hashlib.new('md4', str(p).encode('utf-16le')).digest()
		        	nt.append(binascii.hexlify(hs))
				nt.append(p)
			
			for i in nt:
				if i == ntl:
					c = c + 1
					print bcolors.WARNING +  "[+] ----------------------------------------------------- [+]\n" + bcolors.ENDC
					print bcolors.FAIL + bcolors.BOLD + "[+] Password Cracked! [+]\n" + bcolors.ENDC
					print bcolors.FAIL + bcolors.BOLD + "[+] The ntlm hash of " + username[0] + " is: " + i + " [+]\n" + bcolors.ENDC
					print bcolors.FAIL + bcolors.BOLD + "[+] The password is beginning with: " + nt[nt.index(str(i)) + 1][:3] + "*** [+]\n" + bcolors.ENDC
					print bcolors.WARNING +  "[+] ----------------------------------------------------- [+]\n" + bcolors.ENDC
					break


	print bcolors.HEADER + "[+] Attack Done! Total cracked passwords: " + str(c) + " [+]\n" + bcolors.ENDC

if __name__=="__main__": main()
