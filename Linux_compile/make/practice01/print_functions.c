#include <stdio.h>

void print_cnt(int n)
{
	int i;
	for(i = 0; i < n; i++)
	{
		printf("hello world!\n");
	}
}

void print_cnt_v2(int n, int m)
{
	int i, j;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < m; j++)
		{
			printf("hello world!\t");
		}
		printf("\n");
	}
}
