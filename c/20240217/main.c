/*************************************************************************
        > File Name: main.c
        > Author: wutong
        > Mail: 2774326573@qq.com
        > Created Time: 2024年02月17日 星期六 20时49分26秒
 ************************************************************************/

#include <stdio.h>
int main(void) {
  int i, sum = 0;
  for (i = 1; i <= 100; i++) {
    sum = sum + i;
  }
  printf("sum=%d", sum);
  return 0;
}

