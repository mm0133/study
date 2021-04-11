#include <stdio.h>
#include "print_functions.h"
#include "math.h"

int main()
{
	int n = print_cnt(3);

	print_cnt_v2(2, 2);


	int p;
	p = power(3, 3);
	printf("power: %d\n", p);

	return 0;
}
