

int power(int n, int m)
{
	int i = 0;
	int prod = 1;
	for(i = 0; i < m; i++)
	{
		prod *= n;
	}

	return prod;
}
