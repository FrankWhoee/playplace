typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned long    ulong;
typedef unsigned char    undefined1;
typedef unsigned int    undefined4;
typedef unsigned long    cnode;
typedef unsigned short    word;
typedef struct eh_frame_hdr eh_frame_hdr, *Peh_frame_hdr;

struct eh_frame_hdr {
    byte eh_frame_hdr_version; // Exception Handler Frame Header Version
    dwfenc eh_frame_pointer_encoding; // Exception Handler Frame Pointer Encoding
    dwfenc eh_frame_desc_entry_count_encoding; // Encoding of # of Exception Handler FDEs
    dwfenc eh_frame_table_encoding; // Exception Handler Table Encoding
};

typedef struct fde_table_entry fde_table_entry, *Pfde_table_entry;

struct fde_table_entry {
    dword initial_loc; // Initial Location
    dword data_loc; // Data location
};

typedef struct Elf64_Shdr Elf64_Shdr, *PElf64_Shdr;

typedef enum Elf_SectionHeaderType {
    SHT_NULL=0,
    SHT_PROGBITS=1,
    SHT_SYMTAB=2,
    SHT_STRTAB=3,
    SHT_RELA=4,
    SHT_HASH=5,
    SHT_DYNAMIC=6,
    SHT_NOTE=7,
    SHT_NOBITS=8,
    SHT_REL=9,
    SHT_SHLIB=10,
    SHT_DYNSYM=11,
    SHT_INIT_ARRAY=14,
    SHT_FINI_ARRAY=15,
    SHT_PREINIT_ARRAY=16,
    SHT_GROUP=17,
    SHT_SYMTAB_SHNDX=18,
    SHT_ANDROID_REL=1610612737,
    SHT_ANDROID_RELA=1610612738,
    SHT_GNU_ATTRIBUTES=1879048181,
    SHT_GNU_HASH=1879048182,
    SHT_GNU_LIBLIST=1879048183,
    SHT_CHECKSUM=1879048184,
    SHT_SUNW_move=1879048186,
    SHT_SUNW_COMDAT=1879048187,
    SHT_SUNW_syminfo=1879048188,
    SHT_GNU_verdef=1879048189,
    SHT_GNU_verneed=1879048190,
    SHT_GNU_versym=1879048191
} Elf_SectionHeaderType;

struct Elf64_Shdr {
    dword sh_name;
    enum Elf_SectionHeaderType sh_type;
    qword sh_flags;
    qword sh_addr;
    qword sh_offset;
    qword sh_size;
    dword sh_link;
    dword sh_info;
    qword sh_addralign;
    qword sh_entsize;
};

typedef struct Elf64_Phdr Elf64_Phdr, *PElf64_Phdr;

typedef enum Elf_ProgramHeaderType {
    PT_NULL=0,
    PT_LOAD=1,
    PT_DYNAMIC=2,
    PT_INTERP=3,
    PT_NOTE=4,
    PT_SHLIB=5,
    PT_PHDR=6,
    PT_TLS=7,
    PT_GNU_EH_FRAME=1685382480,
    PT_GNU_STACK=1685382481,
    PT_GNU_RELRO=1685382482
} Elf_ProgramHeaderType;

struct Elf64_Phdr {
    enum Elf_ProgramHeaderType p_type;
    dword p_flags;
    qword p_offset;
    qword p_vaddr;
    qword p_paddr;
    qword p_filesz;
    qword p_memsz;
    qword p_align;
};

typedef struct Elf64_Dyn Elf64_Dyn, *PElf64_Dyn;

typedef enum Elf64_DynTag {
    DT_NULL=0,
    DT_NEEDED=1,
    DT_PLTRELSZ=2,
    DT_PLTGOT=3,
    DT_HASH=4,
    DT_STRTAB=5,
    DT_SYMTAB=6,
    DT_RELA=7,
    DT_RELASZ=8,
    DT_RELAENT=9,
    DT_STRSZ=10,
    DT_SYMENT=11,
    DT_INIT=12,
    DT_FINI=13,
    DT_SONAME=14,
    DT_RPATH=15,
    DT_SYMBOLIC=16,
    DT_REL=17,
    DT_RELSZ=18,
    DT_RELENT=19,
    DT_PLTREL=20,
    DT_DEBUG=21,
    DT_TEXTREL=22,
    DT_JMPREL=23,
    DT_BIND_NOW=24,
    DT_INIT_ARRAY=25,
    DT_FINI_ARRAY=26,
    DT_INIT_ARRAYSZ=27,
    DT_FINI_ARRAYSZ=28,
    DT_RUNPATH=29,
    DT_FLAGS=30,
    DT_PREINIT_ARRAY=32,
    DT_PREINIT_ARRAYSZ=33,
    DT_RELRSZ=35,
    DT_RELR=36,
    DT_RELRENT=37,
    DT_ANDROID_REL=1610612751,
    DT_ANDROID_RELSZ=1610612752,
    DT_ANDROID_RELA=1610612753,
    DT_ANDROID_RELASZ=1610612754,
    DT_ANDROID_RELR=1879040000,
    DT_ANDROID_RELRSZ=1879040001,
    DT_ANDROID_RELRENT=1879040003,
    DT_GNU_PRELINKED=1879047669,
    DT_GNU_CONFLICTSZ=1879047670,
    DT_GNU_LIBLISTSZ=1879047671,
    DT_CHECKSUM=1879047672,
    DT_PLTPADSZ=1879047673,
    DT_MOVEENT=1879047674,
    DT_MOVESZ=1879047675,
    DT_FEATURE_1=1879047676,
    DT_POSFLAG_1=1879047677,
    DT_SYMINSZ=1879047678,
    DT_SYMINENT=1879047679,
    DT_GNU_XHASH=1879047924,
    DT_GNU_HASH=1879047925,
    DT_TLSDESC_PLT=1879047926,
    DT_TLSDESC_GOT=1879047927,
    DT_GNU_CONFLICT=1879047928,
    DT_GNU_LIBLIST=1879047929,
    DT_CONFIG=1879047930,
    DT_DEPAUDIT=1879047931,
    DT_AUDIT=1879047932,
    DT_PLTPAD=1879047933,
    DT_MOVETAB=1879047934,
    DT_SYMINFO=1879047935,
    DT_VERSYM=1879048176,
    DT_RELACOUNT=1879048185,
    DT_RELCOUNT=1879048186,
    DT_FLAGS_1=1879048187,
    DT_VERDEF=1879048188,
    DT_VERDEFNUM=1879048189,
    DT_VERNEED=1879048190,
    DT_VERNEEDNUM=1879048191,
    DT_AUXILIARY=2147483645,
    DT_FILTER=2147483647
} Elf64_DynTag;

struct Elf64_Dyn {
    enum Elf64_DynTag d_tag;
    qword d_val;
};

typedef struct Gnu_BuildId Gnu_BuildId, *PGnu_BuildId;

struct Gnu_BuildId {
    dword namesz; // Length of name field
    dword descsz; // Length of description field
    dword type; // Vendor specific type
    char name[4]; // Build-id vendor name
    byte description[20]; // Build-id value
};

typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
    qword r_offset; // location to apply the relocation action
    qword r_info; // the symbol table index and the type of relocation
    qword r_addend; // a constant addend used to compute the relocatable field value
};

typedef struct Elf64_Ehdr Elf64_Ehdr, *PElf64_Ehdr;

struct Elf64_Ehdr {
    byte e_ident_magic_num;
    char e_ident_magic_str[3];
    byte e_ident_class;
    byte e_ident_data;
    byte e_ident_version;
    byte e_ident_osabi;
    byte e_ident_abiversion;
    byte e_ident_pad[7];
    word e_type;
    word e_machine;
    dword e_version;
    qword e_entry;
    qword e_phoff;
    qword e_shoff;
    dword e_flags;
    word e_ehsize;
    word e_phentsize;
    word e_phnum;
    word e_shentsize;
    word e_shnum;
    word e_shstrndx;
};

typedef struct Elf64_Sym Elf64_Sym, *PElf64_Sym;

struct Elf64_Sym {
    dword st_name;
    byte st_info;
    byte st_other;
    word st_shndx;
    qword st_value;
    qword st_size;
};

typedef ulong size_t;




void __DT_INIT(void)

{
  __gmon_start__();
  return;
}



void FUN_00100690(void)

{
                    // WARNING: Treating indirect jump as call
  (*(code *)(undefined *)0x0)();
  return;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

void free(void *__ptr)

{
  free(__ptr);
  return;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int putchar(int __c)

{
  int iVar1;
  
  iVar1 = putchar(__c);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int puts(char *__s)

{
  int iVar1;
  
  iVar1 = puts(__s);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

size_t strlen(char *__s)

{
  size_t sVar1;
  
  sVar1 = strlen(__s);
  return sVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int printf(char *__format,...)

{
  int iVar1;
  
  iVar1 = printf(__format);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

void * malloc(size_t __size)

{
  void *pvVar1;
  
  pvVar1 = malloc(__size);
  return pvVar1;
}



void __isoc99_scanf(void)

{
  __isoc99_scanf();
  return;
}



void __cxa_finalize(void)

{
  __cxa_finalize();
  return;
}



void FUN_00100720(cnode param_1,cnode param_2,cnode param_3)

{
  cnode unaff_retaddr;
  undefined auStack_8 [8];
  
  __libc_start_main(FUN_00100d15,unaff_retaddr,&stack0x00000008,FUN_00100e20,FUN_00100e90,param_3,
                    auStack_8);
  do {
                    // WARNING: Do nothing block with infinite loop
  } while( true );
}



// WARNING: Removing unreachable block (ram,0x00100767)
// WARNING: Removing unreachable block (ram,0x00100773)

void FUN_00100750(void)

{
  return;
}



// WARNING: Removing unreachable block (ram,0x001007b8)
// WARNING: Removing unreachable block (ram,0x001007c4)

void FUN_00100790(void)

{
  return;
}



void FUN_001007e0(void)

{
  if (DAT_00302020 != '\0') {
    return;
  }
  __cxa_finalize(&PTR_LOOP_00302008);
  FUN_00100750();
  DAT_00302020 = 1;
  return;
}



void FUN_00100820(void)

{
  FUN_00100790();
  return;
}



int rotate_char(char c,int n)

{
  return (c - 32 + n) % 95 + 32;
}



undefined * createCnode(undefined param_1)

{
  undefined *puVar1;
  
  puVar1 = (undefined *)malloc(0x10);
  *puVar1 = param_1;
  return puVar1;
}



void FUN_00100894(void *param_1)

{
  if (param_1 != (void *)0x0) {
    FUN_00100894(*(cnode *)((long)param_1 + 8));
    free(param_1);
  }
  return;
}



long join_cnode_2(long param_1,long param_2)

{
  cnode uVar1;
  
  if (param_1 != 0) {
    uVar1 = join_cnode_2(*(cnode *)(param_1 + 8),param_2);
    *(cnode *)(param_1 + 8) = uVar1;
    param_2 = param_1;
  }
  return param_2;
}


// center, left, right
void join_cnode_3(cnode center,cnode left,cnode right)

{
  join_cnode_2(center,join_cnode_2(left,right));
}



int compare_diff(char *param_1,char *param_2)

{
  char cVar1;
  char cVar2;
  int iVar3;
  
  if ((param_1 == (char *)0x0) && (param_2 == (char *)0x0)) {
    iVar3 = 0;
  }
  else if ((param_1 == (char *)0x0) || (param_2 == (char *)0x0)) {
    iVar3 = 1;
  }
  else {
    cVar1 = *param_1;
    cVar2 = *param_2;
    iVar3 = compare_diff(*(cnode *)(param_1 + 8),*(cnode *)(param_2 + 8));
    iVar3 = iVar3 + (uint)(cVar1 != cVar2);
  }
  return iVar3;
}



void print_cnode(char *param_1)

{
  char *local_10;
  
  for (local_10 = param_1; local_10 != (char *)0x0; local_10 = *(char **)(local_10 + 8)) {
    putchar((int)*local_10);
  }
  putchar(10);
  return;
}



long convertStringToCnode(char *input)

{
  long lVar1;
  cnode uVar2;
  
  if (*input == '\0') {
    lVar1 = 0;
  }
  else {
    lVar1 = createCnode((int)*input); // cnode->c = first character
    uVar2 = convertStringToCnode(input + 1); // create cnode from next character recursively

    *(cnode *)(lVar1 + 8) = uVar2; // cnode->next = uVar2
  }
  return lVar1;
}



char * populateTreenode(char* input,int level,cnode param_3,cnode param_4)

{
  char cVar1;
  char *pcVar2;
  
  pcVar2 = (char *)malloc(0x18);
  *pcVar2 = input;
  cVar1 = rotate_char((int)input,level);
  pcVar2[1] = cVar1;
  *(cnode *)(pcVar2 + 8) = param_3;
  *(cnode *)(pcVar2 + 0x10) = param_4;
  return pcVar2;
}



void FUN_00100abd(void *param_1)

{
  if (param_1 != (void *)0x0) {
    FUN_00100abd(*(cnode *)((long)param_1 + 8));
    FUN_00100abd(*(cnode *)((long)param_1 + 0x10));
    free(param_1);
  }
  return;
}



cnode FUN_00100aff(char *param_1)

{
  cnode uVar1;
  cnode uVar2;
  cnode uVar3;
  
  if (param_1 == (char *)0x0) {
    uVar1 = 0;
  }
  else {
    uVar1 = FUN_00100aff(*(cnode *)(param_1 + 0x10));
    uVar2 = createCnode((int)*param_1);
    uVar3 = FUN_00100aff(*(cnode *)(param_1 + 8));
    uVar1 = join_cnode_3(uVar3,uVar2,uVar1);
  }
  return uVar1;
}



cnode FUN_00100b6a(long param_1)

{
  cnode uVar1;
  cnode uVar2;
  cnode uVar3;
  
  if (param_1 == 0) {
    uVar1 = 0;
  }
  else {
    right = FUN_00100b6a(*(cnode *)(param_1 + 0x10));
    uVar2 = createCnode((int)*(char *)(param_1 + 1));
    uVar3 = FUN_00100b6a(*(cnode *)(param_1 + 8));
    right = join_cnode_3(uVar3,uVar2,right);
  }
  return right;
}



cnode traverse_tree(char *param_1,int param_2)

{
  cnode uVar1;
  cnode uVar2;
  cnode uVar3;
  
  if (param_1 == (char *)0x0) {
    return NULL
  }
  else {
    right = traverse_tree(*(cnode *)(param_1 + 0x10),param_2 == 0);
    left = traverse_tree(*(cnode *)(param_1 + 8),param_2 == 0);
    if (param_2 == 0) {
      mid = createCnode((int)*param_1);
    }
    else {
      mid = createCnode((int)param_1[1]);
    }
    uVar1 = join_cnode_3(mid,left,right);
  }
  return uVar1;
}



cnode str_to_tree(char* input,int len,int level)

{
  int mid;
  cnode right;
  cnode left;
  
  if (len < 1) {
    return NULL;
  }
  else {
    mid = param_2 / 2;
    right = str_to_tree(input + (long)mid + 1,(len - mid) + -1,level + 1);
    left = str_to_tree(input,mid,level + 1);
    right = populateTreenode((int)*(char *)(input + mid),level,left,right);
  }
  return right;
}



cnode FUN_00100d15(void)

{
  int iVar1;
  cnode uVar2;
  size_t len;
  cnode uVar4;
  cnode uVar5;
  
  uVar2 = convertStringToCnode("hglhhlbomrrw_nebedrcllpue");
  puts("Input flag: ");
  putchar(0x3e);
  putchar(0x20);
  __isoc99_scanf(&DAT_00100ecf,&DAT_00302040);
  len = strlen(&DAT_00302040);
  uVar4 = str_to_tree(&DAT_00302040,len,0);
  uVar5 = traverse_tree(uVar4,0);
  print_cnode(uVar5);
  iVar1 = compare_diff(uVar2,uVar5);
  if (iVar1 == 0) {
    printf("Correct! The flag is: maple{%s}\n",&DAT_00302040);
  }
  else {
    puts("Nope\n");
  }
  FUN_00100894(uVar2);
  FUN_00100894(uVar5);
  FUN_00100abd(uVar4);
  return 0;
}



void FUN_00100e20(undefined4 param_1,cnode param_2,cnode param_3)

{
  long lVar1;
  
  __DT_INIT();
  lVar1 = 0;
  do {
    (*(code *)(&__DT_INIT_ARRAY)[lVar1])(param_1,param_2,param_3);
    lVar1 = lVar1 + 1;
  } while (lVar1 != 1);
  return;
}



void FUN_00100e90(void)

{
  return;
}



void __DT_FINI(void)

{
  return;
}


