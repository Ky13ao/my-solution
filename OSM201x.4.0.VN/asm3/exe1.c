#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>

int mynum = 0; /* A global variable*/

// Câu hỏi: 

// Tại sao trong chương trình, giá trị của biến mynum có thay đổi nhưng các xâu PARENT0 được hiển thị liên tục mà không thay đổi giá trị số, trong khi xâu CHILDx được thay đổi giá trị số ?
// -> biến mynum là biến toàn cục trong chương trình vì vậy cả tiến trình cha và tiến trình con dều được sử dụng
// -> tại thời điểm thay đổi biến mynum ở tiến trình con, 
// -> biến mynum được thay đổi trong bộ nhớ của tiến trình con và sự thay đổi bị mất đi sau khi đến tiến trình cha in PARENT%d
// -> 
// Chụp ảnh màn hình chạy chương trình và lưu với tên exe1_1.jpg
// Mở cửa sổ Terminal khác và dùng lệnh kill để hủy tiến trình cha trong Terminal mới. Tại sao chương trình vẫn tiếp tục hiển thị nội dung trên Terminal cũ ? Chụp ảnh màn hình chạy chương trình và lưu với tên exe1_2.jpg.
// Hủy tiếp tiến trình con bằng lệnh kill để kết thúc.

int main(void) {
  pid_t childPID;
  int i;
  // TODO: create child process
  // tạo tiến trình con thông qua việc gán hàm fork()
  childPID = fork(); //[1]

  // is child process running?
  // kiểm tra xem có phải tiến trình con được thực thi hay không
  if (childPID==0) // Child process [2]
  {
    printf("Child process ID: %d\n", getpid());
    for (i = 0;; ++i) /*both processes do this*/ {
      mynum = i;
      sleep(1);
      printf("CHILD%d\n", mynum);
    }
  } 
  // is parent process running?
  // kiểm tra xem có phải tiến trình cha được thực thi hay không
  else if (childPID>0) //Parent process [3]
  {
    printf("Parent process ID: %d\n", getpid());
    for (i = 0;; ++i) /*both processes do this*/ {
      sleep(1);
      printf("PARENT%d\n", mynum);
    }
  } else // fork failed
  {
    printf("\n Fork failed, quitting!!!!!!\n");
    return 1;
  }
  return 0;
}