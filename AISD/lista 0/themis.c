/*********************
 * Krzysztof Slawik  *
 * 307020            * 
 * PRZ               *
 *********************/
#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    long a, b;
    scanf("%d %d", &a, &b);
    long i = a - (a % 2021);
    if (i < a)
    {
        i += 2021;
    }
    char buffer[1000000];
    char *current_buffer_pos = buffer; 
    while (i <= b)
    {
        current_buffer_pos += snprintf(current_buffer_pos, 1000, "%d ", i);
        i += 2021;
        if(current_buffer_pos - buffer > 999985)
        {
            current_buffer_pos = buffer;
            printf("%s", buffer);
            buffer[0] = '\0';
        }
    }
    printf("%s", buffer);
    return 0;
}
