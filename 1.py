#!/bin/python

import os, sys

print ("\033[33;1mKalau Gak tau Username sama pass bisa sv aj whatsapp gw")

print ("\033[33;1m-=[085836465872]=-")

print ("\033[33;1mSEBELUM MASUK KITA LOGIN DULU")

username = 'Tools' 

password = 'Gabungan'


def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)


def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")


		if pwd == password:

			sys.exit()


		else:

			print "\033[31;1mUsername atau password yang anda masukan salah !!!\033[00m"


			restart()


	else:

		print "\033[31;1mUsername atau password yang anda masukan salah !!!\033[00m"


		restart()


try:

	main()

except KeyboardInterrupt:

	os.system('clear')

