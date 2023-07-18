#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>

#define BUF_SIZE 4096         /* use a buffer size of 4096 bytes */
#define OUTPUT_MODE 0700      /* protection bits for output file */
#define MAX_PATH_LENGTH 4096	/* maximum length of file path */
#define MAX_CMD_LENGTH 10240	/* maximum length of command */
#define MAX_CMD_ELEMENTS 3	  /* maximum number of elements in a command */

int copyFile(char *, char *);
int listDir(char *);
int makeDir(char *);
int mvFile(char *, char *);

int main (int argc, char **argv){
  // number of arguments: argc
  // vector of arguments: argv
  int ret = 0;


  if (argc >= 3){
    if(strcmp(argv[1],"ls") == 0){
      // print list at argv[2]
      ret = listDir(argv[2]);
    } else if(strcmp(argv[1],"mkdir") == 0){
      // create directory with name = argv[2]
      ret = makeDir(argv[2]);
    } else if(strcmp(argv[1],"cp") == 0){
      if(argc >= 4){
        // copy file from argv[2] to argv[3]
        ret = copyFile(argv[2], argv[3]);        
      } else {
        printf ("%s: missing destination file operand after %s\n", argv[1], argv[2]);
      }
    } else if(strcmp(argv[1],"mv") == 0){
      if(argc >= 4){
        // move or rename from argv[2] to argv[3]
        ret = mvFile(argv[2], argv[3]);
      } else {
        printf ("%s: missing destination file operand after %s\n", argv[1], argv[2]);
      }
    } else {
      printf("%s: command not found\n", argv[1]);
    }
  } else {
    printf("%s: missing arguments\n", argv[argc-1]);
  }
  if (ret > 0)
    printf("%s\n", strerror(errno));
    exit(ret);
  return 0;
}

/*
 * Copy file
 * [IN] source: Pointer to the string containing the path of source file
 * [IN] dest: Pointer to the string containing the path of destination file
 * Return: 0 if successful, otherwise return -1 
*/
int copyFile(char *source, char *dest){
  int in_fd, out_fd, rd_count, wt_count;
  char buffer[BUF_SIZE];
      
  in_fd=open(source, O_RDONLY);          /* open the source file */
  if (in_fd < 0) return errno;           /* if it cannot be opened, exit */
      
  out_fd=creat(dest, OUTPUT_MODE);       /* create the destination file */
  if (out_fd < 0) return errno;          /* if it cannot be created, exit */

  /* Copy loop */
  while (1) {
    rd_count=read(in_fd, buffer, BUF_SIZE);    /* read a block if data */
    if (rd_count <= 0) break;               /* if end of file or error, exit loop */

    wt_count = write(out_fd, buffer, rd_count);       /* write data */
    if (wt_count <= 0) return errno;                /* wt_count<=0 is an error */
  }

  /* Close the files */
  close(in_fd);
  close(out_fd);

  if (rd_count == 0)    /* no error on last read */
    return 0;
  else
    return errno;        /* error on last read */
}

/*
 * List the name of files and sub-directory in a directory
 * [IN] dirname: Pointer to the string containing the name of directory
 * Return: 0 if successful, otherwise return -1 
*/
int listDir(char *dirname){
  DIR *dir;
  struct dirent *subdir;

  dir = opendir(dirname);

  if(dir == NULL){
    return errno;
  } else {
    // hiển thị danh sách tệp tin theo tab và xuống dòng mỗi 10 tên
    int tabCount = 0;
    while ((subdir = readdir(dir)) != NULL){
      if(strcmp(subdir->d_name,".") != 0 && strcmp(subdir->d_name,"..") != 0){
        tabCount++;
        printf("%s", subdir->d_name);
        if(tabCount==10){
          printf("\n");
          tabCount=0;
        } else {
          if (sizeof(subdir->d_name)<=10) {
            printf("\t\t");
          } else {
            printf("\t");
          }
        }
      }
    }
    printf("\n");
    closedir(dir);
    return 0;
  }
}

/*
 * Make a directory
 * [IN] newDir: Pointer to the string containing the name of directory
 * Return: 0 if successful, otherwise return -1 
 */
int makeDir (char *newDir){
  // 1. Process mkdir
  if(mkdir(newDir, 0777) != 0) { 
    // 2. condition success or fail
    return errno;
  } else {
    printf("\"%s\" directory created.\n", newDir);
    return 0;
  }
}

/*
 * Move file
  *[IN] source: Pointer to the string containing the path of source file
 * [IN] dest: Pointer to the string containing the path of destination file
 * Return: 0 if successful, otherwise return -1 
 */
int mvFile (char *source, char *dest){
	
  // 1. Process rename
  if(rename(source, dest)!=0){
	// 2. Condition success or fail
    // printf("Failed to move \"%s\" to \"%s\"\n", source, dest);
    return errno;
  } else {
    printf("File \"%s\" has been moved to \"%s\"!\n", source, dest);
    return 0;
  }
}
