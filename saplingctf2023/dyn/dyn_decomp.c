#include <stdio.h>
#include <string.h>

int main(int argc,char * argv[])

{
  long lVar1;
  int iVar2;
  unsigned int uVar3;
  unsigned int uVar4;
  unsigned int uVar5;
  unsigned int uVar6;
  size_t sVar7;
  

  char* DAT_00301050;
  char* DAT_00301030;

  if (argc == 2) {
    sVar7 = strlen(*(char **)(argv + 8));
    if (((sVar7 == 25) && (iVar2 = memcmp(*(void **)(argv + 8),"maple{",6), iVar2 == 0)) &&
       (lVar1 = *(long *)(argv + 8), sVar7 = strlen(*(char **)(argv + 8)),
       *(char *)((sVar7 - 1) + lVar1) == '}')) {
      for (int i = 0; i < 18; i = i + 2) {
        uVar3 = (unsigned int)((char)(&DAT_00301030)[(int)((char)(&DAT_00301050)[i] - 65)] >> 4);
        uVar4 = (char)(&DAT_00301030)[(int)((char)(&DAT_00301050)[i] - 65)];
        uVar5 = (unsigned int)((char)(&DAT_00301030)[(int)((char)(&DAT_00301050)[i + 1] - 65)] >> 4);
        uVar6 = (char)(&DAT_00301030)[(int)((char)(&DAT_00301050)[i + 1] - 65)];
        if (uVar4 == uVar6) {
          (&DAT_00301050)[i] = "SAPLINGBCDEFHJKMOQRTUVWXY"[(long)(((int)(uVar3 - 1) % 5 + 5) % 5) * 5 + (long)(int)uVar4];
          (&DAT_00301050)[i + 1] = "SAPLINGBCDEFHJKMOQRTUVWXY"[(long)(((int)(uVar5 - 1) % 5 + 5) % 5) * 5 + (long)(int)uVar4];
        }
        else if (uVar3 == uVar5) {
          (&DAT_00301050)[i] =
               "SAPLINGBCDEFHJKMOQRTUVWXY"
               [(long)(int)uVar3 * 5 + (long)(((int)(uVar4 - 1) % 5 + 5) % 5)];
          (&DAT_00301050)[i + 1] =
               "SAPLINGBCDEFHJKMOQRTUVWXY"
               [(long)(int)uVar3 * 5 + (long)(((int)(uVar6 - 1) % 5 + 5) % 5)];
        }
        else {
          (&DAT_00301050)[i] =
               "SAPLINGBCDEFHJKMOQRTUVWXY"[(long)(int)uVar3 * 5 + (long)(int)uVar6];
          (&DAT_00301050)[i + 1] =
               "SAPLINGBCDEFHJKMOQRTUVWXY"[(long)(int)uVar5 * 5 + (long)(int)uVar4];
        }
      }
      iVar2 = memcmp((void *)(*(long *)(argv + 8) + 6),&DAT_00301050,0x12);
      if (iVar2 == 0) {
        puts("Correct!");
      }
      else {
        puts("Try again");
      }
    }
    else {
      puts("Try again!");
    }
  }
  else {
    puts("Usage: ./dyn FLAG");
  }
  return 0;
}

