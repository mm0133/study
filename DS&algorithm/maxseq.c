#include <stdio.h>
#include <stdlib.h>

int MAXS1(const int A[], int N)
{
	int TS, MS, i, j, k,l;
	int X[30], Y[30];
	MS = 0;
	for (l = 0;l < N;l++)
		Y[l] = 81;
	for (i = 0; i < N;i++)
		for (j = i; j < N; j++)
		{
			TS = 0;
			for(l=0;l<N;l++)
			X[l] =81;
			for (k = i;k <= j;k++)
			{
				TS = TS + A[k];
				X[k] = A[k];
			}
			if (TS > MS)
			{
				MS = TS;
				for (l = 0;l < N;l++)
					Y[l] = X[l];
			}
		}
	printf("\n\n 알고리즘1 \nMAXSUM:%d   SEQUECE:",MS);
	for (i = 0;i < N;i++)
	{
		if(Y[i]!=81)
			printf("%d ", Y[i]);
	}
}

int MAXS2(const int A[], int N)
{
	int TS, MS, i, j, l;
	int X[30], Y[30];
	
	MS = 0;
	for (l = 0;l < N;l++)
		Y[l] = 81;
	for (i = 0;i < N;i++)
	{
		TS = 0;
		for (l = 0;l < N;l++)
			X[l] = 81;
		
		for (j = i; j < N; j++)
		{
			TS = TS + A[j];
			X[j] = A[j];
			if (TS > MS)
			{
				MS = TS;
				for (l = 0;l < N;l++)
					Y[l] = X[l];
			}

		}
	}
	printf("\n 알고리즘2 \nMAXSUM:%d   SEQUECE:", MS);
	for (i = 0;i < N;i++)
	{
		if (Y[i] != 81)
			printf("%d ", Y[i]);
	}
}

int same(int A[], int B[], int N)
{ 
	int i;
	for (i = 0;i < N;i++)
	{
		if(B[i]!=81)
		A[i] = B[i];
	}
}

int SUMSeq(int *A,int N)
{
	int i, MS=0;
	for (i = 0;i < N;i++)
	{
		if (A[i] != 81)
			MS = MS + A[i];
	}
	return MS;
}
int reset(int X[],int N)
{
	int i;
	for (i = 0;i < N; i++)
	{
		X[i] = 81;
	}
}

int MAXSUBSUM(const int A[], int L, int R)
{
	int MLS, MRS, MLBS, MRBS, LBS, RBS, Center, i, MS;
	if (L == R)
	{
		if (A[L] > 0)
			return A[L];
		else
			return 0;
	}

	Center = (L + R) / 2;
	MLS = MAXSUBSUM(A, L, Center);
	MRS = MAXSUBSUM(A, Center + 1, R);

	MLBS = 0, LBS = 0;
	for (i = Center;i >= L; i--)
	{
		LBS = LBS + A[i];
		if (LBS > MLBS)
			MLBS = LBS;
	}
	MRBS = 0; RBS = 0;
	for (i = Center + 1; i <= R;i++)
	{
		RBS = RBS + A[i];
		if (RBS > MRBS)
			MRBS = RBS;
	}
	MS = MLBS + MRBS;
	if (MLS > MS)
		MS = MLS;
	if (MRS > MS)
		MS = MRS;
	return MS;
}

int* MAXSEQ(int* A, int L, int R)
{
	int MLSeq[30], MRSeq[30], MLBSeq[30], MRBSeq[30], LBSeq[30], RBSeq[30];
	reset(MLSeq, 30);reset(MRSeq, 30);reset(MLBSeq, 30);reset(MRBSeq, 30);reset(LBSeq, 30);reset(RBSeq,30);
	int *tem;
	static int re[30];
	int MLS, MRS, MLBS, MRBS, LBS, RBS, Center, i, j,k, MS;
	if (L == R)
	{
		if (A[L] > 0)
			return A[L];
		else
			return 0;
	}


	Center = (L + R) / 2;
	
	tem = MAXSEQ(A, L, Center);
	for (k = 0;k < 30;k++)
		MLSeq[k] = tem[k];
	MLS = SUMSeq(MLSeq,30);


	
	tem = MAXSEQ(A, Center + 1, R);
	for (k = 0;k < 30;k++)
		MRSeq[k] = tem[k];
	MRS = SUMSeq(MRSeq,30);
	
	MLBS = 0, LBS = 0;
	for (i = Center;i >= L; i--)
	{
		LBS = LBS + A[i];
		LBSeq[i] = A[i];
		if (LBS > MLBS)
		{
			MLBS = LBS;
			same(MLBSeq, LBSeq, 30);
		}
	}
	
	MRBS = 0; RBS = 0;
	for (i = Center + 1; i <= R;i++)
	{
		RBS = RBS + A[i];
		RBSeq[i] = A[i];
		if (RBS > MRBS)
		{
			MRBS = RBS;
			same(MRBSeq, RBSeq, 30);
		}
		
	MS = MLBS + MRBS;
	same(re, MLBSeq, 30);same(re, MRBSeq,30);
	if (MLS > MS)
	{
		MS = MLS;
		reset(re, 30);
		same(re, MLSeq,30);
	}
	if (MRS > MS)
	{
		MS = MRS;
		reset(re, 30);
		same(re, MRSeq, 30);
	}
		return re;
	}
}


int MAXS3(const int A[], int N)
{
	int i;
	int* B;
	printf("\n 알고리즘3 \nMAXSUM:%d   SEQUECE:", MAXSUBSUM(A, 0, N - 1));
	/*
	B = MAXSEQ(A, 0, N - 1);
	for (i = 0;i < N; i++)
	{
		if (B[i] != 81)
			printf("%d ", B[i]);
	}*/
}



int MAXS4(const int A[], int N)
{
	int TS, MS, i, l;
	int X[30], Y[30];
		TS = MS = 0;
	for (l = 0;l < N;l++)
	{
		X[l] = 81;
		Y[l] = 81;
	}
	for (i = 0;i < N;i++)
	{
		TS = TS + A[i];
		X[i] = A[i];


		if (TS > MS)
		{
			MS = TS;
			for (l = 0;l < N;l++)
				Y[l] = X[l];
		}
		else if (TS < 0)
		{
			TS = 0;
			for (l = 0;l < N;l++)
				X[l] = 81;
		}
	}
	printf("\n 알고리즘4 \nMAXSUM:%d   SEQUECE:", MS);
	for (i = 0;i < N;i++)
	{
		if (Y[i] != 81)
			printf("%d ", Y[i]);
	}
}


int main(void)
{
	int i;
	int A[30], B[30], C[30], D[30], POSITIVE[30];
	
	
	for (i = 0;i < 30;i++)
		A[i] = (rand() % 81) - 20;
	for (i = 0;i < 30;i++)
		B[i] = (rand() % 81) - 20;
	for (i = 0;i < 30;i++)
		C[i] = (rand() % 81) - 20;
	for(i = 0;i < 30;i++)
		D[i] = (rand() % 81) - 20;
	for (i = 0;i < 30;i++)
		POSITIVE[i] = (rand() % 60) + 1;

	
	printf("input A: ");
	for (i = 0; i < 30; i++)
		printf("%d ", A[i]);
	MAXS1(A, 30);
	MAXS2(A, 30);
	MAXS3(A, 30);
	MAXS4(A, 30);

	
	printf("\n\n\ninput B: ");
	for (i = 0; i < 30; i++)
		printf("%d ", B[i]);
	MAXS1(B, 30);
	MAXS2(B, 30);
	MAXS3(B, 30);
	MAXS4(B, 30);
	
	printf("\n\n\ninput C: ");
	for (i = 0; i < 30; i++)
		printf("%d ", C[i]);
	MAXS1(C, 30);
	MAXS2(C, 30);
	MAXS3(C, 30);
	MAXS4(C, 30);

	printf("\n\n\ninput D: ");
	for (i = 0; i < 30; i++)
		printf("%d ", D[i]);
	MAXS1(D, 30);
	MAXS2(D, 30);
	MAXS3(D, 30);
	MAXS4(D, 30);

	printf("\n\n\ninput POSITIVE: ");
	for (i = 0; i < 30; i++)
		printf("%d ", POSITIVE[i]);
	MAXS1(POSITIVE, 30);
	MAXS2(POSITIVE, 30);
	MAXS3(POSITIVE, 30);
	MAXS4(POSITIVE, 30);

	
	
	
	return 0;
}