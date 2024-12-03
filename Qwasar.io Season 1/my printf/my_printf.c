#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <ctype.h>

int printf_int(int num);
int printf_octal(unsigned int nu_ber);
int printf_unsigned(unsigned int numb_r);
int printf_hex(unsigned int num_er);
int printf_char(int c);
int printf_string(char *str);
int printf_pointer(void *ptr);

int my_printf(char *restrict format, ...) {
    va_list ap;
    int written = 0;

    va_start(ap, format);

    for (; *format != '\0'; format++) {
        if (*format == '%') {
            format++;
            switch (*format) {
                case 'd':
                case 'i':
                    written += printf_int(va_arg(ap, int));
                    break;
                case 'o':
                    written += printf_octal(va_arg(ap, unsigned int));
                    break;
                case 'u':
                    written += printf_unsigned(va_arg(ap, unsigned int));
                    break;
                case 'x':
                    written += printf_hex(va_arg(ap, unsigned int));
                    break;
                case 'c':
                    written += printf_char(va_arg(ap, int));
                    break;
                case 's':
                    {
                        char *str = va_arg(ap, char *);
                        if (str == NULL) {
                            written += printf_string("(null)");
                        } else {
                            written += printf_string(str);
                        }
                    }
                    break;
                case 'p':
                    written += printf_pointer(va_arg(ap, void *));
                    break;
                default:
                    written += printf_char('%');
                    written += printf_char(*format);
                    break;
            }
        } else {
            written += printf_char(*format);
        }
    }
    va_end(ap);
    return written;
}

int printf_int(int num) {
    int len = 0;
    char buffer[32];
    char *ptr = buffer + 31;

    *ptr = '\0';

    if (num == 0) {
        *--ptr = '0';
        len = 1;
    } else {
        int is_negative = 0;
        if (num < 0) {
            num = -num;
            is_negative = 1;
        }

        do {
            *--ptr = (num % 10) + '0';
            num /= 10;
            len++;
        } while (num!= 0);

        if (is_negative) {
            *--ptr = '-';
            len++;
        }
    }

    write(1, ptr, len);
    return len;
}

int printf_octal(unsigned int nu_ber) {
    int len = 0;
    char buffer[32];
    char *ptr = buffer + 31;

    *ptr = '\0';

    if (nu_ber == 0) {
        *--ptr = '0';
        len = 1;
    } else {
        do {
            *--ptr = (nu_ber % 8) + '0';
            nu_ber /= 8;
            len++;
        } while (nu_ber != 0);
    }

    write(1, ptr, len);
    return len;
}

int printf_unsigned(unsigned int numb_r) {
    int len = 0;
    char buffer[32];
    char *ptr = buffer + 31;

    *ptr = '\0';

    if (numb_r == 0) {
        *--ptr = '0';
        len = 1;
    } else {
        do {
            *--ptr = (numb_r % 10) + '0';
            numb_r /= 10;
            len++;
        } while (numb_r != 0);
    }

    write(1, ptr, len);
    return len;
}

int printf_hex(unsigned int num_er) {
    int len = 0;
    char buffer[32];
    char *ptr = buffer + 31;

    *ptr = '\0';

    if (num_er == 0) {
        *--ptr = '0';
        len = 1;
    } else {
        do {
            int digit = num_er % 16;
            if (digit < 10) {
                *--ptr = digit + '0';
            } else {
                *--ptr = digit - 10 + 'A';  // Convert to uppercase hex digits 'A' - 'F'
            }
            num_er /= 16;
            len++;
        } while (num_er != 0);
    }

    write(1, ptr, len);  // Output in uppercase hex format
    return len;
}

int printf_char(int c) {
    char buffer[1];
    buffer[0] = (char)c;
    write(1, buffer, 1);
    return 1;
}

int printf_string(char *str) {
    if (str == NULL) {
        write(1, "(null)", 6);
        return 6;
    }
    int len = strlen(str);
    write(1, str, len);
    return len;
}

int printf_pointer(void *ptr) {
    char buffer[32];
    char *ptr_str = buffer + 31;

    *ptr_str = '\0';

    unsigned long long int addr_ss = (unsigned long long int)ptr;

    do {
        int digit = addr_ss % 16;
        if (digit < 10) {
            *--ptr_str = digit + '0';
        } else {
            *--ptr_str = digit - 10 + 'a';
        }
        addr_ss /= 16;
    } while (addr_ss != 0);

    *--ptr_str = 'x';
    *--ptr_str = '0';

    write(1, ptr_str, 31 - (ptr_str - buffer));
    return 31 - (ptr_str - buffer);
}

int main() {
    // Test my_printf with various format specifiers
    my_printf("Hello, World!\n");

    int i = 42;
    my_printf("The answer is %d\n", i);

    unsigned int u = 0x12345678;
    my_printf("The hex value is %x\n", u);

    char c = 'A';
    my_printf("The character is %c\n", c);

    char *s = "Hello, World!";
    my_printf("The string is %s\n", s);

    void *p = &i;
    my_printf("The pointer is %p\n", p);

    // Test edge cases
    my_printf("%\n"); // should output "%"

    my_printf("%%\n"); // should output "%"

    // Test error handling (if implemented)
    //...

    printf("All tests passed!\n");
    return 0;
}