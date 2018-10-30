############################
#jgn di recode om ,,
#cz codingan w ccad ea ,,
############################

import time,os,sys


B = '\003[34;1m'
G = '\033[32;1m'
P = '\033[35;1m'
C = '\033[31;1m'
R = '\033[31;1m'
W = '\033[1;37m'
Y = '\033[33;1m'


def main():

	os.system ('clear')
print W+       ("===================================").center(40)
print R+       ("MBF MULTI BRUTE FACEBOOK INSTALLER").center(40)
print W+       ("===================================").center(40)
print              (R+"[+]"+W+"Author :andrachocs"+R+"[+]").center(40)
print W+                     ("Github :https://github.com/clnx777").center(35)
print           ' '




print W+"LIST"+R+".."
print ' '
print R+"1"+R+")"+W+"Install MBF (by pirmansx)"
print R+"2"+R+")"+W+"Exit"
print ' '
pilih = input ("Choose Number..: ")

if pilih ==1:
   os.system ('clear')
   print R+  ('Installing...')
   os.system ('pkg install figlet')
   os.system ('figlet  "Wait.."')
   os.system ('apt upgrade && apt update')
   os.system ('pkg install figlet')
   os.system ('pkg install git')
   os.system ('pkg install python2')
   os.system ('pip2 install mechanize')
   os.system ('git clone https://github.com/tikuskecil/multi-bruteforce-facebook')
   os.chdir  ('multi-bruteforce-facebook')
   os.system ('python2 MBF.py')
   	
if pilih ==2:
   sys.exit ('Exiting.. Bye')
   
else:
		print "  [-] Input Salah !"
		raw_input('  [!] tkn enter untuk kmbali ke menu...')
		os.system('clear')
		
		main()
if __name__ == "__main__":
	main()

    
    
    
