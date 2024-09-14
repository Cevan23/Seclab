#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[]) {
    char buf[8];
    memcpy(buf, argv[1], strlen(argv[1]));
    printf(buf);
}
