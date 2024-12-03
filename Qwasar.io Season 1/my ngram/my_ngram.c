#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char **argv) {
    int char_counter[256] = {0}; // assume ASCII characters only

    for (int i = 1; i < argc; i++) {
        char *string = argv[i];
        while (*string != '\0') {
            char_counter[(unsigned char)*string]++;
            string++;
        }
    }

    for (int i = 0; i < 256; i++) {
        if (char_counter[i] > 0) {
            printf("%c:%d\n", i, char_counter[i]);
        }
    }

    return 0;
}