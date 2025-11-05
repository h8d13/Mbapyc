#include <stdio.h>
#include <stdlib.h>

int run() {
    const int MAX_BITS = 32;
    for (int bit = 0; bit < MAX_BITS; bit++)
        printf("BC: %d\n", bit);
    printf("Reached bit %d — exit delimiter triggered.\n", MAX_BITS);
    exit(0); // instead of return 0;
}