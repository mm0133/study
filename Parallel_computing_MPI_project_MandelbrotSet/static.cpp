#include <stdio.h>
#include <SFML/Graphics.hpp>
#include <mpi.h>
#include <time.h>
using namespace sf;

int width = 400;
int height = 400;
int N_rectangle = 40;

struct complex {
	float real;
	float imag;
};


int cal_pixel(complex c) {
	int count = 0;
	int max = 256;
	complex z;
	z.real = 0;
	z.imag = 0;
	float temp, lengthsq;
	do {
		temp = z.real * z.real - z.imag * z.imag + c.real;
		z.imag = 2 * z.real * z.imag + c.imag;
		z.real = temp;
		lengthsq = z.real * z.real;
		count++;
	} while ((lengthsq < 4.0) && (count < max));
	return count;
}


int temblock[16001];
int data[400][400];
int block[16001];
int main(int argc, char** argv) {
	MPI_Init(&argc, &argv);
	int myid;
	int numprocs;
	MPI_Comm_rank(MPI_COMM_WORLD, &myid);
	MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
	MPI_Status status;

	float minR = -2;
	float minI = -2;
	float maxR = 2;
	float maxI = 2;
	float scale_real, scale_imag;
	scale_real = (maxR - minR) / width;
	scale_imag = (maxI - minI) / height;
	complex c;
	int color;


	if (myid == 0) {
		clock_t total_start_time, total_end_time;
		total_start_time = clock();
		int column = 0;
		int numblock = width / N_rectangle;
		int blocksize = N_rectangle * height;
		int R = numblock % numprocs;
		int Q = numblock / numprocs;
		int numSlaveBlock = 0;

		if (numprocs > 1) {

			int B;//각프로세스에 할당되는 블락수

			for (int i = 1; i < numprocs; i++) {
				if (i < R) {
					B = Q + 1;
				}
				else {
					B = Q;
				}
				numSlaveBlock += B;
				MPI_Send(&B, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
				MPI_Send(&column, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
				column = column + N_rectangle * B;
			}
		}

		int	s = column;
		int e;
		clock_t starttime, endtime;
		int index = 0;
		int start, end, cur;

		for (int i = 0; i < numblock; i++) {
			//본인블록을 처리하는 루틴 
			//프로세스 갯수만큼 처리할때마다 마스터는 본인도 하나의 블록을 처리함.
			if (index == 0) {
				starttime = clock();
				for (int y = 0; y < height; y++) {
					c.imag = minI + ((float)y * scale_imag);
					e = s + N_rectangle;
					for (int x = s; x < e; x++) {
						c.real = minR + ((float)x * scale_real);
						color = cal_pixel(c);
						data[y][x] = color;
					}

				}
				endtime = clock();
				printf("process %d complete a Block, time: %fs\n", myid, (double)(endtime - starttime) / CLOCKS_PER_SEC);
				s += N_rectangle;
			}
			// 다른 블록으로부터 데이터를 받아 저장하는 루틴
			else {
				MPI_Recv(&temblock, blocksize + 1, MPI_INT, MPI_ANY_SOURCE, 2, MPI_COMM_WORLD, &status);
				start = temblock[16000]; //0~15999는 데이터, 16000은 블락의 시작위치
				end = start + N_rectangle;
				cur = 0;
				for (int j = 0; j < height;j++)
					for (int k = start; k < end;k++) {
						data[j][k] = temblock[cur];
						cur += 1;
					}
			}
			// index는 마스터가 본인차례를 알기 위해 사용
			index = (index + 1) % numprocs;
		}


		total_end_time = clock();
		printf("\ntotal time in static allocation:%fs\n\n", (double)(total_end_time - total_start_time) / CLOCKS_PER_SEC);

		//마스터가 처리한 데이터를 display하는 과정
		RenderWindow window(VideoMode(width, height), "Mandlebrot set");
		Image image;
		image.create(width, height);
		Texture texture;
		Sprite sprite;
		while (window.isOpen()) {
			Event event;
			while (window.pollEvent(event))
			{
				if (event.type == Event::Closed) window.close();
			}
			for (int y = 0; y < height; y++)
				for (int x = 0; x < width; x++) {
					image.setPixel(x, y, Color(255 - data[y][x], 255 - data[y][x], 255 - data[y][x]));

				}

			window.clear();
			texture.loadFromImage(image);
			sprite.setTexture(texture);
			window.draw(sprite);
			window.display();
		}
	}

	//slave
	else {
		clock_t starttime, endtime;
		double term;
		starttime = clock();
		int BN;
		int start;
		MPI_Recv(&BN, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
		MPI_Recv(&start, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
		int cur;
		for (int k = 0; k < BN;k++)
		{
			cur = 0;
			block[16000] = start; //0~15999는 데이터, 16000은 블락의 시작위치
			for (int y = 0; y < height; y++) {
				c.imag = minI + ((float)y * scale_imag);
				for (int x = start; x < start + N_rectangle; x++) {
					c.real = minR + ((float)x * scale_real);

					color = cal_pixel(c);
					block[cur] = color;
					cur += 1;
				}
			}
			MPI_Send(&block, 16001, MPI_INT, 0, 2, MPI_COMM_WORLD);
			start = start + N_rectangle;
			endtime = clock();
			term = (double)(endtime - starttime) / CLOCKS_PER_SEC;
			printf("process %d complete a Block, time: %fs\n", myid, term);
			starttime = endtime;

		}

	}
	MPI_Finalize();
	return 0;
}