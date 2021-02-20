#!/usr/bin/python
import subprocess
import time
from colorama import Fore, init
init()

print(Fore.RED)
banner = """
███╗   ██╗███╗   ███╗ █████╗ ██████╗        █████╗ ██╗   ██╗████████╗ ██████╗ 
████╗  ██║████╗ ████║██╔══██╗██╔══██╗      ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
██╔██╗ ██║██╔████╔██║███████║██████╔╝█████╗███████║██║   ██║   ██║   ██║   ██║
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ ╚════╝██╔══██║██║   ██║   ██║   ██║   ██║
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║           ██║  ██║╚██████╔╝   ██║   ╚██████╔╝
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝           ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ 
"""
print(banner)
print(Fore.CYAN)
print("Created by Blackster")
print("This is a tool of commands automatization for Nmap")
time.sleep(2)

menu = """
1- Scanning TCP mode.
2- Scanning TCP SYN mode.
3- Scanning without detection(to evitate firewalls)
4- Scanning with Ping.
5- Scanning UDP mode.(low, send packages)
6- No Ping mode (hidden mode).
7- Scanning Active Servers.
8- Scanning for detect operative system.
9- Scanning in information mode.
10- Scanning with Port Range.
"""
print(menu)

options = int(input("Choose an option: "))

if options==1:
	URL = str(input("Type here your Address/IP to scan: "))
	import subprocess
	subprocess.call(f'nmap -sT {URL}', shell = True)

elif options==2:
	URL = str(input("Type here your Address/IP to scan: "))
	import subprocess
	subprocess.call(f'nmap -sS {URL}', shell = True)

elif options==3:
	mode = """
	1- Stealth mode.
	2- Xmas tree.
	3- Nul Scan.
	"""
	print(mode)
	opt = int(input("choose an option: "))
	if opt==1:
		URL = str(input("Type here your Address/IP to scan: "))
		import subprocess
		subprocess.call(f'sudo nmap -sF {URL}', shell = True)

	elif opt==2:
		URL = str(input("Type here your Address/IP to scan: "))
		import subprocess
		subprocess.call(f'sudo nmap -sX {URL}', shell = True)

	elif opt==3:
		URL = str(input("Type here your Address/IP to scan: "))
		import subprocess
		subprocess.call(f'sudo nmap -sN {URL}', shell = True)

elif options==4:
	URL = str(input("Type here your Address/IP to scan: "))
	import subprocess
	subprocess.call(f'sudo nmap -sP {URL}', shell = True)

elif options==5:
	URL = str(input("Type here your Address/IP to scan: "))
	import subprocess
	subprocess.call(f'sudo nmap -sU {URL}', shell = True)

elif options==6:
	URL = str(input("Type here your Address/IP to scan: "))
	import subprocess
	subprocess.call(f'sudo nmap -pO {URL}', shell = True)

elif options==7:
	URL = str(input("Type here your Address/IP to scan: "))
	import subprocess
	subprocess.call(f'sudo nmap -PT {URL}', shell = True)

elif options==8:
	URL = str(input("Type here your Address/IP to scan: "))
	import subprocess
	subprocess.call(f'sudo nmap -o {URL}', shell = True)

elif options==9:
	URL = str(input("Type here your Address/IP to scan: "))
	import subprocess
	subprocess.call(f'sudo nmap -v {URL}', shell = True)

elif options==10:
	URL = str(input("Type here your Address/IP to scan: "))
	Port = str(input("Type here your Range to Scan (ex: 20-30): "))
	import subprocess
	subprocess.call(f'sudo nmap -p {Port} {URL}', shell = True)

else:
	print("Error XD")
