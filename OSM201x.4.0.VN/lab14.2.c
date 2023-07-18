#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

int sell = 0;
int product = 0;
sem_t sem;

void *sellThread(void *);
void *productThread(void *);

int main(){
    sem_init(&sem, 0, 0);
    pthread_t tid[2];
    pthread_create(&tid[0], NULL, sellThread, NULL);
    pthread_create(&tid[1], NULL, productThread, NULL);

    pthread_join(tid[0], NULL);
    pthread_join(tid[1], NULL);

    pthread_exit(NULL);
}

void *sellThread(void *arg){
    int count = 0;
    while(sell<10000){
        sem_wait(&sem);
        if (sell < product){
            sell++;
            printf("Sell num %d\n", sell);
        }
        count++;
        printf("Loop sell item: %d\n", count);
    }

    pthread_exit(NULL);
}

void *productThread(void * arg){
    while (product<10000){
        product++;
        printf("Product num: %d\n", product);
        sem_post(&sem);
    }

    pthread_exit(NULL);
}