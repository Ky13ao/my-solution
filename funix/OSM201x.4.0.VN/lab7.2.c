#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
int main() { 
 /*Allocate 256MB memory*/ 
 size_t mem_size = 256 * 1024 * 1024; 
  
 char* based = malloc(mem_size); 

  
 if (based) { 
//  printf("Allocated %zu Bytes from %lx to %lx\n", mem_size,   based, based + mem_size);  } else { 
 printf("Allocated %lu Bytes from %p to %p\n", (unsigned long)mem_size, (void*)based, (void*)(based + mem_size));  } else { 
 printf("Allocation Error.\n"); 
 return 1; 
 } 
 /*Initialize the memory in batches*/ 
 size_t stage = 65536; 
 size_t initialized = 0; 
 while (initialized < mem_size) { 
 memset(based + initialized, '$', stage); 
 initialized += stage; 
 } 
  
 /*ReAllocate memory*/ 
 printf("\nEnter new size of array(MB): "); 
//  scanf("%d", &mem_size); 
 scanf("%zu", &mem_size); 
 mem_size = mem_size * 1024 * 1024; 
 based = realloc(based, mem_size); 

  
 if (based) { 
//  printf("Allocated %zu Bytes from %lx to %lx\n", mem_size, based, based + mem_size);  } else { 
 printf("Allocated %lu Bytes from %p to %p\n", (unsigned long)mem_size, (void*)based, (void*)(based + mem_size));  } else { 
 printf("Allocation Error.\n"); 
 return 1; 
 } 
 /*Free allocated memory and exit*/ 
 char exit = 'A'; 
 while(exit != 'q' && exit != 'Q'){ 
 printf("\n Enter any q/Q to quit: "); 
fflush(stdin); 
scanf("%c",&exit); 
if (exit == 'q' || exit == 'Q') break; 
 } 
 free(based); 
 return 0; 
}
