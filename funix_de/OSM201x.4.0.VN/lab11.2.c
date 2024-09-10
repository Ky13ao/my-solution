#include <stdio.h>
#include <string.h>
#define MAX_FRAME 4
int findLRU(int times[], int n){
	//Viết hàm tìm LRU
	//Viết code tại đây
    int minIndex = 0;
    for (int i = 1; i < n; i++) {
        if (times[i] < times[minIndex]) {
            minIndex = i;
        }
    }
    return minIndex;
}
int main(){
  int count = 0; // Đếm số lỗi trang
  // Các frame
  int frames[MAX_FRAME];
  int lru = 0; // Vị trí LRU
  int times[MAX_FRAME]; // Hỗ trợ tìm kiếm lru
  int flag = 0; // Vị trí được thay thế thực sự
  int available = 0; // Cho biết frame có nằm trong bộ nhớ chính hay không
  // Số frame trong bộ nhớ chính
  int frame = 4; //test case 1
  // int frame = 3; //test case 2
  // Số phần tử của chuỗi tham chiếu
  int n = 20;
  // Chuỗi tham chiếu
  int a[30] = {1, 0 , 1, 0, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1};
  
  printf("|Chuỗi\t|");
  for(int i = 0; i < frame; i++){
    frames[i] = -1; // Giả sử ban đầu các frame trống
    times[i] = 0;
    printf("Khung %d|", i);
  }
  printf("Lỗi trang?\n");
  for(int i = 0; i < n; i++){
    printf("| %d \t", a[i]);
    available = 0; // trang không có sẵn
    for(int k = 0; k < frame; k++)
      if(frames[k] == a[i]){ // kiểm tra trang có sẵn
        available = 1; // trang có sẵn
        times[k]++;
        flag = k;
      }
    if(available == 0) // thay thế trang nếu không có sẵn
    {
      lru = findLRU(times, frame);
      // Thực hiện thay thế frame theo vị trí LRU và đếm số lỗi trang
     // Viết code tại đây

      frames[lru] = a[i];
      times[lru]++;
      flag=lru;
      count++;

      // In ra màn hình – Không chỉnh sửa
      for(int k = 0; k < frame; k++){
        if(frames[k] >= 0)
          printf("|%d\t", frames[k]);
        else
          printf("|\t");
      }
      printf("| Có"); // Dấu hiệu nhận biết xảy ra lỗi trang
    }else{
      for(int k = 0; k < frame; k++){
        if(frames[k] >= 0)
          printf("|%d\t", frames[k]);
        else
          printf("|\t");
      }
      printf("| Không");
    }
    for(int temp = 0; temp < frame; temp++){
      if(temp == flag)
        continue;
      if(times[temp] >= times[flag]){
        times[flag] = times[temp]+1;
      }
    }
    printf("\n");
  }
  printf("Số lỗi trang là: %d\n", count);
  return 0;
}
