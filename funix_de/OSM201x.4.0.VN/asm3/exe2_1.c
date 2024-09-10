#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <pthread.h>

#define NUM_THREADS 4
void *hello(void * );

int main() {
  int j;
  pthread_t tid[NUM_THREADS];
  printf("My process ID %d\n", getpid());
  for (j = 0; j < NUM_THREADS; j++){
    // TODO: create child process with name = tid[j], run hello function with j parameter.
    pthread_create(&tid[j], NULL, hello, &j); //[1]
  }
  for (int i = 0; i < NUM_THREADS; i++){
    // TODO: main function is done if all child process is done.
    pthread_join(tid[i], NULL); //[2]
  }
  return 0;
}

void *hello(void * my_id) {
  printf("Hello World from branch thread %d\n", *(int * ) my_id);
  return NULL;
}

//Giải thích tại sao trên cửa sổ dòng lệnh có hiện tượng một hoặc nhiều luồng hiển thị giá trị my_id của nó giống với luồng khác ?
// -> Trong khi pthread_create chạy, nó chia sẻ con trỏ &j cho các luồng con mà nó tạo ra. 
// -> Điều này dẫn đến việc tất cả các luồng con tham chiếu cùng một địa chỉ trong bộ nhớ cho biến j.
// -> Khiến giá trị my_id trên các nhánh con đều mang giá trị 4