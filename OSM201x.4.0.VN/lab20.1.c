// Lab 20-1 https://docs.google.com/document/d/10TzvOnE4ykR4iFDVcqwZ9ji8zBSj2Xkm_-YPyCsVUZw/edit

#include <stdio.h>
#include <pthread.h>
#include <string.h>
#include <stdlib.h>

pthread_t tid[3];
void *thread0(void *);
void *thread2(void *);
char *str;
int num;

typedef struct PARAM{
  int     order;
  char    name[30];
}param_t;

int main(){
  param_t param[2];

  param[0].order = 0;
  strcpy(param[0].name, "Thread0");
  param[1].order = 1;
  strcpy(param[1].name, "Thread1");

  for (int i=0; i <2; i++){
    pthread_create(&tid[i], NULL, thread0, &param[i]);
  }

  pthread_create(&tid[2], NULL, thread2, NULL);
  pthread_join(tid[0], NULL);

  exit(0);
}

void *thread0(void *arg){
    param_t *param = (param_t*)arg;
    // TODO: print a string "Hello, How are you?"
    // printf("Hello, How are you?\n");
    pthread_join(tid[param->order+1], NULL);
    switch (param->order) {
      case 0:
        // TODO: print "Hello, How are you" num times
        for(int i=0; i<num; i++){
          printf("Hello, How are you?\n");
        }
        break;
      case 1:
        // TODO: print a string has been entered from user
        printf("\nThe string has been entered: %s\n", str);
        break;
    }
    pthread_exit(NULL);
}

void *thread2(void *arg){
    // TODO: add code to enter a string
    
    // TODO: print a string has been entered from user
    printf("Enter a string: ");
    scanf("%m[^\n]", &str);
    printf("Please enter a number: ");
    scanf("%d", &num);
    pthread_exit(NULL);
}