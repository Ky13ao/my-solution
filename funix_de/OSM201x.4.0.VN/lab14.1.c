#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

sem_t sem1, sem2;

void* T1(void* arg) {
    // do something
    printf("1");
    // T1 xử lý xong
    sem_post(&sem1); // tăng semaphore cho T2
    sem_post(&sem1); // tăng semaphore cho T3
}

void* T2(void* arg) {
    sem_wait(&sem1); // đợi cho T1 hoàn thành
    // do something
    printf("2");
    sem_post(&sem2); // tăng semaphore của T4 lên 1
}

void* T3(void* arg) {
    sem_wait(&sem1); // đợi cho T1 hoàn thành
    // do something
    printf("3");
    sem_post(&sem2); // tăng semaphore của T4 lên 1
}

void* T4(void* arg) {
    sem_wait(&sem2); // đợi cho T2 hoàn thành
    sem_wait(&sem2); // đợi cho T3 hoàn thành
    // do something
    printf("4");
}

// https://docs.google.com/document/d/1s9LCVfdNOvCkz-jOxQpa-Jjs3uL3GGwRBKerbSmX_Lk/edit


int main() {
    // khởi tạo semaphore
    sem_init(&sem1, 0, 0);
    sem_init(&sem2, 0, 0);

    // khởi tạo thread
    pthread_t thread[4];

    pthread_create(&thread[0], NULL, &T1, NULL);
    pthread_create(&thread[1], NULL, &T2, NULL);
    pthread_create(&thread[2], NULL, &T3, NULL);
    pthread_create(&thread[3], NULL, &T4, NULL);

    pthread_join(thread[0], NULL);
    pthread_join(thread[1], NULL);
    pthread_join(thread[2], NULL);
    pthread_join(thread[3], NULL);

    // giải phóng semaphore
    pthread_exit(NULL);
    sem_destroy(&sem1);
    sem_destroy(&sem2);
}