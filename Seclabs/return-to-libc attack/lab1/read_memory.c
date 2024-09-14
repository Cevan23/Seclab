#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int main() {
    // Địa chỉ bộ nhớ giả định
    uintptr_t addr = 0xffffd700;
    
    // Đọc 4 byte từ địa chỉ
    uint8_t *ptr = (uint8_t *)addr;
    uint8_t data[4];
    
    memcpy(data, ptr, 4);
    
    // In giá trị dưới dạng hex
    printf("\\x%02x\\x%02x\\x%02x\\x%02x\n", data[0], data[1], data[2], data[3]);
    
    return 0;
}
