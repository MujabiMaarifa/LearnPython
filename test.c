# include <stdio.h>
#include <string.h>
void main(void) {
    char name[20];
    char names = name;

    printf("Enter your name: ");
    scanf("%c", name);

    printf("Your name is: %c\n", names);
    // Reverse the name

}