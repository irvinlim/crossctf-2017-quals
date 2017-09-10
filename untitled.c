/*

|__64__|__56__|__48__|__40__|__32__|__24__|__16__|__8___|
|__________________________RAX__________________________|
|xxxxxxxxxxxxxxxxxxxxxxxxxxx|____________EAX____________|
|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|_____AX______|
|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|__AH__|__AL__|

*/

int main() {
    char local_20h = 0xffffffff;
    char local_1ch = 0;
    char local_18h = 0;
    int local_10h = 0;

    // 0x00400857
    eax = 0;                    // mov eax, 0
    menu();                     // call sym.menu
    local_20h = 0xffffffff;     // mov dword [local_20h], 0xffffffff
    rax = local_20h;            // lea rax, [local_20h]
    rsi = rax;                  // mov rsi, rax
    edi = "%d";                 // &edi = 0x400a34 where ps @ 0x400a34 : "%d" 
    eax = 0;                    // mov eax, 0
    scanf();                    // call sym.imp.__isoc99_scanf
    eax = *local_20h;           // mov eax, dword [local_20h]



    // 0x004008b7
    rax = *local_18h;
    rsi = rax;
    edi = "%d";
    eax = 0;
    scanf();
}