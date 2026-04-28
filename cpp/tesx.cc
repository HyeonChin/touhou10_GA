#include <windows.h>
#include <iostream>

// z 15번 입력하는 코드

void pressZ() {
    INPUT input[2] = {};

    // 키 다운
    input[0].type = INPUT_KEYBOARD;
    input[0].ki.wVk = 'Z';

    // 키 업
    input[1].type = INPUT_KEYBOARD;
    input[1].ki.wVk = 'Z';
    input[1].ki.dwFlags = KEYEVENTF_KEYUP;

    SendInput(2, input, sizeof(INPUT));
}

int main() {
    std::cout << "3초 후 시작...\n";
    Sleep(3000);

    for (int i = 0; i < 15; i++) {
        pressZ();
        Sleep(1); // 입력 간격 (ms) - 줄이면 더 빠르게 입력됨
    }

    std::cout << "완료\n";
    return 0;
}