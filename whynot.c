#include <stdio.h>

__attribute__((naked)) int babyasm(int a, int b, int c) {
    __asm__ (
        ".intel_syntax noprefix;"
        "push   ebp;"
        "mov    ebp, esp;"
        "xor    eax, eax;"
        "mov    ah, BYTE PTR [ebp+0x9];"
        "shl    ax, 0x10;"
        "sub    al, BYTE PTR [ebp+0xe];"
        "add    ah, BYTE PTR [ebp+0xf];;"
        "xor    ax, WORD PTR [ebp+0x12];"
        "nop;"
        "pop    ebp;"
        "ret;"
        ".att_syntax;"
    );
}

int main() {
    int res = babyasm(0xabcd1456, 0xdfed7768, 0x68686868);
    printf("Result: 0x%X\n", res);
    return 0;
}