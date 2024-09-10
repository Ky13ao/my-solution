// Lab 19-1 https://docs.google.com/document/d/1vGY_V922b6wePCVbFwn45IRnm-XTgSPrMb2yEuy8Dnk/edit

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    int childpid = fork();
    if (childpid < 0){
        printf("Fork error!!");
        exit(1);
    }
    else{
        if (childpid == 0){ // child process
            // TODO: add code to enter a string and print it
            printf("Child1 - Please enter string: ");
            char *strToPrint;
            scanf("%m[^\n]", &strToPrint);
            printf("Child1 - Your string is: %s\n", strToPrint);
            exit(0);
        } else { // parent process
            childpid = wait(&childpid);
            // TODO: add code to enter a positive number
            printf("\nChild2 - Please enter a positive number: ");
            int positiveNumber;
            scanf("%d", &positiveNumber);
            int childpid2 = fork();
            if (childpid2 < 0) {
                // TODO: print a message if the number is not posiitve and exit
                printf("Child2 - Number you entered: %d\n", positiveNumber);
            } else {
                if (childpid2 == 0) { // child 2 process
                  for(int i=0; i<positiveNumber; i++){
                    printf("Hello, How are you?\n");
                  }
                  exit(0);
                } else { // parent process
                    childpid2 = wait(&childpid2);
                    printf("\nParent: Good bye!\n");
                }
                exit(0);
            }
        }
    }
    return 0;
}