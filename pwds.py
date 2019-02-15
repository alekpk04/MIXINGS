import os, sys

print ("\033[1;32mMasukin UserName&Password:)")

print ("\033[1;32mATAU HUBUNGI LANGSUNG Lee KPK")

username = 'Leekpk'      

password = '0404'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mGOOD BYE", 

			sys.exit()



		else:

			print "\033[1;32mSorry Passwordnya salah kuy!!!\033[00m"

			print "Back Login\n"

			restart()



	else:

		print "\033[1;32mSorry..WKWKWK !!!\033[00m"

		print "Back Login\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

