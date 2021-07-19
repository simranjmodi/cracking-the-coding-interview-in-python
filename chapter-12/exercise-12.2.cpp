/*
12.2 Reverse String

Implement a function void reverse(char* str) in C or C++ which reverses a null
terminated string.
*/

#include <string>

void reverse(char *str) {
    char* end = str;
    char tmp;
    if (str) {
        while (*end) {
            ++end;
        }
        --end;

        while (str < end) {
            tmp = *str;
            *str++ = *end
            *end-- = tmp;
        }
    }
}