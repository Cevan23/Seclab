#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void target_func() {
    printf("Target function executed!\n");
    system("/bin/sh"); // Open a shell for the exploit
}

void vulnerable_function(char *input) {
    char buffer[24];
    // Vulnerable to buffer overflow
    strcpy(buffer, input);
}

int main() {
    char input[256];
    
    printf("Enter your input: ");
    fgets(input, sizeof(input), stdin);
    
    vulnerable_function(input);
    
    printf("Done.\n");
    return 0;
}
