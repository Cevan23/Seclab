#include <stdio.h>
void secret(){
    printf("Oops... secret!\n");
}
int main(){
    char buffer[30];
    printf("Input name: ");
    gets(buffer);
    printf(buffer);
    printf("\nInput bio: ");
    gets(buffer);
    return 0;
}
