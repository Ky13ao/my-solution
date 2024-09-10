#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <pthread.h>

#define NUM_THREADS 4
void *hello(void * );

int main() {
  pthread_t tid[NUM_THREADS];
  printf("My process ID %d\n", getpid());
  for (int j = 0; j < NUM_THREADS; j++){
    // TODO: create child process with name = tid[j], run hello function with j parameter.
    pthread_create(&tid[j], NULL, hello, &j); //[1]
    // TODO: main function is done if all child process is done.
    // join thread ngay sau khi tạo thread để đảm bảo param ko được dùng chung
    pthread_join(tid[j], NULL); //[2]
  }
  return 0;
}

void *hello(void * my_id) {
  printf("Hello World from branch thread %d\n", *(int * ) my_id);
}